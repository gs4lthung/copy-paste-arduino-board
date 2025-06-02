import serial
import time
import pyautogui
import subprocess
import sys
import platform
from datetime import datetime

# Configurable Settings
SERIAL_PORT = "/dev/ttyUSB1"
BAUD_RATE = 9600
NOTIFY_TIME = "2000"  # in milliseconds
COPY_COMMAND = "CTRL + C"
PASTE_COMMAND = "CTRL + V"

# Hotkey bindings
COPY_HOTKEY = ("ctrl", "c")
PASTE_HOTKEY = ("ctrl", "v")

def log(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

def notify(message):
    os_type = platform.system()
    if os_type == "Linux":
        subprocess.run(['notify-send', '-t', NOTIFY_TIME, message])
    elif os_type == "Darwin":  # macOS
        subprocess.run(['osascript', '-e', f'display notification "{message}" with title "Arduino Copy/Paste"'])
    elif os_type == "Windows":
        try:
            from plyer import notification
            notification.notify(
                title='Arduino Copy/Paste',
                message=message,
                timeout=int(NOTIFY_TIME) // 1000
            )
        except ImportError:
            log("Install 'plyer' for Windows notifications: pip install plyer")
    else:
        log(f"Notification: {message}")

def wait_for_device():
    while True:
        try:
            log(f"Trying to connect to {SERIAL_PORT}...")
            arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
            time.sleep(2)  # Wait for Arduino to reset
            log("Connected to Arduino!")
            notify("🟢 Copy/Paste Keyboard Connected")
            return arduino
        except serial.SerialException:
            log("⚠️ Arduino not found. Retrying in 2s...")
            time.sleep(2)

def handle_command(command):
    if command == COPY_COMMAND:
        pyautogui.hotkey(*COPY_HOTKEY)
        log("Executed: Ctrl+C")
    elif command == PASTE_COMMAND:
        pyautogui.hotkey(*PASTE_HOTKEY)
        log("Executed: Ctrl+V")
    elif command:
        log(f"Unknown command received: '{command}'")

def main():
    arduino = wait_for_device()
    log("Listening for commands (COPY/PASTE)...")

    try:
        while True:
            try:
                if arduino.in_waiting:
                    command = arduino.readline().decode(errors='ignore').strip().upper()
                    handle_command(command)
            except (serial.SerialException, OSError):
                log("🔌 Lost connection. Reconnecting...")
                notify("🔌 Arduino Disconnected. Reconnecting...")
                arduino = wait_for_device()
    except KeyboardInterrupt:
        log("Program interrupted by user.")
        notify("❌ Copy/Paste Listener Stopped")
        sys.exit(0)

if __name__ == "__main__":
    main()
