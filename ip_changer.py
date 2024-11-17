from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import subprocess
import time
import threading
import requests

app = Flask(__name__)
socketio = SocketIO(app)

# Global variables
interval = 5  # Default interval in seconds
is_running = False
change_ip_thread = None

def get_current_ip():
    """Fetch the current public IP address."""
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json().get('ip')
    except Exception as e:
        return f"Error: {str(e)}"

def change_ip():
    """Change the IP using a VPN client command."""
    try:
        # Replace with your VPN client command. Example for NordVPN:
        result = subprocess.run(["nordvpn", "-c"], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"VPN Error: {result.stderr}")
        else:
            time.sleep(5)  # Give the VPN some time to change the IP
    except Exception as e:
        print(f"Error changing IP: {e}")

def auto_change_ip():
    """Automatically change IP every 'interval' seconds."""
    global is_running
    while is_running:
        change_ip()
        current_ip = get_current_ip()
        print(f"New IP: {current_ip}")
        socketio.emit('ip_update', {'ip': current_ip})
        time.sleep(interval)

@app.route('/')
def index():
    return render_template('index.html', current_ip=get_current_ip())

@socketio.on('change_ip')
def manual_change_ip():
    """Handle manual IP change request."""
    change_ip()
    current_ip = get_current_ip()
    emit('ip_update', {'ip': current_ip}, broadcast=True)

@socketio.on('set_interval')
def set_interval(data):
    """Set the interval for automatic IP change."""
    global interval
    interval = int(data['interval'])

@socketio.on('start_auto')
def start_auto_change():
    """Start automatic IP change."""
    global is_running, change_ip_thread
    if not is_running:
        is_running = True
        change_ip_thread = threading.Thread(target=auto_change_ip)
        change_ip_thread.start()

@socketio.on('stop_auto')
def stop_auto_change():
    """Stop automatic IP change."""
    global is_running
    is_running = False

if __name__ == '__main__':
    socketio.run(app, debug=True)
