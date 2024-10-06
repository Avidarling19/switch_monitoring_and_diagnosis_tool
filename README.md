Apologies for the confusion! Here's the revised version of the README file, keeping the API endpoints section and just modifying how the application is run, as per your request:

---

# Switch Configuration and Monitoring System

This project is a Flask-based web application that allows users to connect to a network switch via a serial port, send configuration commands, retrieve the running configuration, and display device health parameters on a frontend. The configuration is stored in a SQLite database.

## Project Structure

```
project/
│
├── env/                     # Virtual environment directory (auto-created)
│   ├── Include/              # Virtual environment includes
│   ├── Lib/                  # Python libraries used in the project
│   └── Scripts/              # Scripts for the virtual environment
│
├── instance/                 # Directory for instance-specific files
│   └── device.db             # SQLite database to store device configurations
│
├── templates/                # Directory for HTML templates
│   └── index.html            # Frontend for displaying device data
│
├── app.py                    # Main application file for Flask
├── init.py                   # Empty init file (optional, to mark this as a module)
├── .venv/                    # Python virtual environment configuration
└── .pycache__/               # Auto-generated cache files
```

## Features

- **Serial Communication**: Establishes a connection to the network switch via a serial port using the `pyserial` library.
- **Database Integration**: Stores the running configuration of the switch in a SQLite database using `Flask-SQLAlchemy`.
- **Health Monitoring**: Retrieves and displays health parameters from the switch such as interfaces, CPU usage, memory, and version.
- **Web Interface**: A simple web page (`index.html`) displays the retrieved device data, including its state and health parameters.
- **REST API**: The application exposes an endpoint (`/get_device_data/<string:port>`) to fetch the device data and configurations.
- **Cross-Origin Requests**: Enabled with `Flask-CORS` for allowing requests from different origins.

## Prerequisites

1. Python 3.x
2. Virtualenv (recommended for managing project dependencies)

## Installation

1. Clone the repository.
2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Initialize the SQLite database:
    ```bash
    python app.py
    ```

## Running the Application

1. Ensure the virtual environment is activated.
2. Run the Flask application using the following command:
    ```bash
    flask --app app run
    ```
    This will start the Flask development server on `http://127.0.0.1:5000/`.

## API Endpoints

- **`/get_device_data/<port>`**: Fetches the switch data connected to the specified serial port (e.g., `COM3` on Windows).
- **`/`**: Displays the stored device configurations and health parameters on the web interface.

## Database

The application uses SQLite as its database (`device.db`), which is located inside the `instance/` folder. The database stores the following information:

- **Device ID**: Unique identifier for each device configuration.
- **Device Name**: Name of the configured device.
- **Running Configuration**: Saved configuration of the switch.
- **Timestamp**: Date and time when the configuration was stored.

## License

This project is licensed under the MIT License.

---

This version keeps your API endpoints the same while updating how to run the application using the `flask --app app run` command instead of running `app.py` directly. Let me know if this is what you needed!
