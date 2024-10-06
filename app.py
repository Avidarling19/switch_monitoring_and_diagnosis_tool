from flask import Flask, render_template, jsonify # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
import serial # type: ignore
import time
from datetime import datetime
from flask_cors import CORS # type: ignore

app = Flask(__name__)

# Configuring the Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///device.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)  # Allow cross-origin requests

# Database Model
class DeviceConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(100), nullable=False)
    running_config = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Function to establish serial connection
def connect_to_switch(port, baudrate=9600, timeout=1):
    try:
        ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        return ser
    except serial.SerialException as e:
        raise Exception(f"Error connecting to serial port: {e}")

# Function to send commands to the switch
def send_command(ser, command):
    try:
        ser.write(command.encode('ascii') + b'\r\n')
        time.sleep(2)  # Give more time for the switch to respond
        
        output = ""
        while True:
            if ser.inWaiting() > 0:  # If there's data in the buffer
                data = ser.read(ser.inWaiting()).decode('ascii')
                output += data

                # Check if we encounter the --More-- prompt
                if '--More--' in data:
                    ser.write(b' ')  # Send space to continue
                    time.sleep(1)  # Wait before reading more data
                else:
                    break  # If no more data, exit loop

        return output.strip()
    except Exception as e:
        raise Exception(f"Error sending command: {e}")


# Function to save configuration
def save_config(ser):
    output = send_command(ser, 'write memory')
    return output

# Function to retrieve health parameters and determine device state
def get_health_parameters(ser):
    
    health_commands = [
        
        'show interfaces',
        'show processes cpu',
        'show memory',
        'show version',
    ]
    health_data = {}

    for command in health_commands:
        output = send_command(ser, command)

        health_data[command] = output

    # Basic check to determine device state
    device_state = 'Inactive'
    if 'Cisco' in health_data['show version']:
        device_state = 'Active'
    
    return health_data, device_state

@app.route('/get_device_data/<string:port>')
def get_device_data(port):
    try:
        ser = connect_to_switch(port)
        
        # Example commands to configure hostname and save config
        commands = [
            'enable',
            'configure terminal',
            'hostname inventa1',
            'end'
        ]
        
        # Sending configuration commands
        for command in commands:
            send_command(ser, command)
        
        # Save configuration
        running_config = save_config(ser)
        
        # Store the device configuration in the database
        device_name = "inventa1"
        new_entry = DeviceConfig(device_name=device_name, running_config=running_config)
        db.session.add(new_entry)
        db.session.commit()

        # Retrieve health parameters and determine device state
        health_parameters, device_state = get_health_parameters(ser)

        # Get the latest device entry from the database
        latest_device = DeviceConfig.query.order_by(DeviceConfig.timestamp.desc()).first()

        # Close the serial connection
        ser.close()

        # Return data as JSON for the frontend
        return jsonify({
            'device_id': latest_device.id,
            'device_name': latest_device.device_name,
            'device_state': device_state,
            'timestamp': latest_device.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'health_parameters': health_parameters
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    devices = DeviceConfig.query.all()
    return render_template('index.html', devices=devices)

if __name__ == '__main__':
    # Ensure database tables are created inside the application context
    with app.app_context():
        db.create_all()
    
    # Start the Flask application
    app.run(debug=True)
