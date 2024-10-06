

# Network Switch Monitoring and Diagnosis Dashboard

## Project Description

This project is a full-stack Python application that monitors the health of a network switch by extracting memory and interface data via serial communication which is ueful for diagnosis of problems which may arise in future . It stores this data in a database and presents it through a web-based dashboard built using HTML, CSS, and JavaScript. The dashboard automatically refreshes every 15 minutes, ensuring real-time monitoring of key parameters such as memory usage and interface status.

The project is designed for network administrators who need to track the performance of their network switches and monitor crucial metrics in a clean and simple interface.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used

### Backend:

- **Python**: Main language for backend logic.
- **Flask**: Lightweight web framework for building the API.
- **PySerial**: Library for serial communication with network switches.
- **SQLAlchemy**: ORM for interacting with the SQLite database.
- **Flask-CORS**: Enabling cross-origin requests from the frontend.

### Frontend:

- **HTML5**: For building the structure of the dashboard.
- **CSS3**: For styling and designing the layout.
- **JavaScript**: For making dynamic requests to the backend and updating the data on the dashboard.

### Database:

- **SQLite**: Embedded database for storing memory and interface status data.

## Features

- **Real-time Monitoring**: The dashboard fetches data from the backend every 15 minutes, displaying up-to-date memory and interface status.
- **Serial Communication**: Communicates with the network switch via serial connection to retrieve health parameters.
- **Data Storage**: Memory and interface data are stored with timestamps for tracking historical performance.
- **Interactive Dashboard**: Users can view and monitor memory and interface data through a clean, intuitive web dashboard.
  
## Installation

### Prerequisites

1. Python 3.x
2. A network switch with a serial connection
3. A serial-to-USB cable (or equivalent)

### Backend Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/network-monitor-dashboard.git
   cd network-monitor-dashboard/backend
   ```

2. **Create a Virtual Environment and Install Dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Database Initialization**
   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

4. **Run the Backend Server**
   ```bash
   python app.py
   ```

### Frontend Setup

1. **Navigate to the Frontend Directory**
   ```bash
   cd ../frontend
   ```

2. **Open the `index.html` File**
   You can open the `index.html` file in any modern web browser. The dashboard will automatically connect to the Flask backend to fetch the data.

### API Endpoints

- `/memory-data`: Returns memory utilization details.
- `/interface-data`: Returns interface status details.

## Usage

1. **Connect to the Switch:**
   - Ensure the network switch is connected to your computer via a serial connection.
   - The backend is configured to communicate with the switch over the specified serial port (e.g., `COM5` or `/dev/ttyUSB0`). Modify the serial port in the `app.py` file if needed.

2. **View the Dashboard:**
   - Open the `index.html` file in a browser to view the network monitoring dashboard.
   - The dashboard will automatically refresh every 15 minutes to fetch the latest data from the switch.

3. **Database Monitoring:**
   - All the fetched data (memory and interface details) is stored in a SQLite database (`network_data.db`). You can query this data to view historical metrics.

## Project Structure

```bash
network-monitor-dashboard/
│
├── backend/                 # Flask app folder
│   ├── app.py               # Flask app with routes for fetching switch data
│   ├── models.py            # SQLAlchemy models for memory and interface data
│   ├── utils.py             # Utility functions for serial communication and data parsing
│   ├── requirements.txt     # Backend dependencies
│   └── network_data.db      # SQLite database (created after running the app)
│
├── frontend/                # Frontend folder
│   ├── index.html           # HTML file for the dashboard
│   ├── style.css            # CSS file for dashboard styling
│   └── script.js            # JavaScript file for dynamic data fetching and display
│
├── README.md                # Project documentation
└── .gitignore               # Files and folders to ignore in Git
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please ensure all changes are tested before submission.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

Feel free to customize this README further with any additional project-specific details.
