# IPChangerX
IPChangerX is a web application designed to automatically change your public IP address using a VPN client (e.g., NordVPN) at a specified interval. The IP can also be manually changed via the web interface. This project uses Flask and Socket.IO to provide real-time updates of your IP address.


Features
Automatically change your IP address at a customizable interval (default: every 5 seconds).
Manually change your IP address with a button click.
Real-time display of the current public IP.
Modern, responsive user interface with adjustable fonts and styles.
Easy-to-use controls for setting the interval and starting/stopping automatic IP changes.
Table of Contents
Requirements
Installation
Usage
Project Structure
Troubleshooting
Contributing
License
Requirements
Before you begin, ensure you have the following software installed on your system:

Python 3.8+
pip (Python package installer)
A VPN client (tested with NordVPN)
Visual Studio Code (VS Code) (recommended IDE)
Python Packages
The following Python packages are required:

Flask
Flask-SocketIO
requests
Installation
Step 1: Clone the Repository
To get started, clone this project using the following command:

bash
Copy code
git clone https://github.com/yourusername/IPChangerX.git
cd IPChangerX
Step 2: Set Up a Virtual Environment (Optional)
It's recommended to use a virtual environment to manage dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Step 3: Install the Required Dependencies
Run the following command to install all the dependencies listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
Step 4: Verify Your VPN Client Setup
Make sure your VPN client (e.g., NordVPN) is installed and configured correctly. Ensure it works using the command line:

bash
Copy code
nordvpn -c
Step 5: Run the Application
To start the Flask server, use:

bash
Copy code
python ip_changer.py
The application should be accessible at:

arduino
Copy code
http://127.0.0.1:5000
Usage
Accessing the Web Application
Open your web browser and navigate to:
arduino
Copy code
http://127.0.0.1:5000
Use the buttons on the interface to:
Change IP Now: Manually change your IP.
Set Interval: Set a custom interval (in seconds) for automatic IP change.
Start Automatic IP Change: Begin changing your IP at the specified interval.
Stop Automatic IP Change: Stop the automatic IP changing process.
Testing IP Change
To verify that your IP address is changing:

Visit https://www.whatismyip.com or similar sites.
Observe the change in IP after triggering the change from the web app.
Project Structure
Here's an overview of the project structure:

php
Copy code
IPChangerX/
├── static/
│   └── background.jpg         # Background image
├── templates/
│   └── index.html             # HTML template for the web UI
├── ip_changer.py              # Main Flask application
├── requirements.txt           # Python package dependencies
└── README.md                  # Documentation
Explanation of Files
static/: Contains static assets like images.
templates/: HTML templates for rendering the web pages.
ip_changer.py: Core Flask application that handles IP changing and socket communication.
requirements.txt: List of required Python packages.
Troubleshooting
If you run into any issues, consider the following:

VPN Client Issues:

Ensure that your VPN client is installed correctly and that the command nordvpn -c works in your terminal.
If using a different VPN, adjust the command in the change_ip() function within ip_changer.py.
Permissions:

On Linux, you may need to run the Flask server with elevated privileges to change the IP:
bash
Copy code
sudo python ip_changer.py
Real-time Updates:

If the IP is not updating in real-time, ensure that the Flask-SocketIO library is properly installed and accessible.
Contributing
Contributions are welcome! If you have suggestions for improvements or want to report a bug, please open an issue or create a pull request on the GitHub repository.

To Do:
Add support for additional VPN clients.
Add a Dockerfile for containerized deployment.
Implement user authentication for more secure access.
License
This project is licensed under the MIT License. Feel free to use, modify, and distribute as needed.

![Screenshot 2024-11-17 230627](https://github.com/user-attachments/assets/6782cbf2-71b5-4c04-8f31-f92847cd3d9f)

