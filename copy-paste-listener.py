import serial
import time
import pyautogui
import subprocess
import sys

SERIAL_PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600
NOTIFY_TIME="1"

def notify(message):
    subprocess.run(['notify-send', '-t', NOTIFY_TIME, message])

def wait_for_device():
    while True:
        try:
            print(f"Trying to connect to {SERIAL_PORT}...")
            arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
            time.sleep(2)  # Wait for Arduino to reboot
            print("Connected!")
            notify("Copy/Paste Keyboard Connected")
            return arduino
        except serial.SerialException:
            print("Waiting for Arduino... (unplugged?)")
            time.sleep(2)

def main():
    arduino = wait_for_device()

    print("Listening for COPY/PASTE...")

    try:
        while True:
            try:
                if arduino.in_waiting:
                    command = arduino.readline().decode().strip()
                    if command == "COPY":
                        pyautogui.hotkey("ctrl", "c")
                        print("Ctrl+C")
                    elif command == "PASTE":
                        pyautogui.hotkey("ctrl", "v")
                        print("Ctrl+V")
            except (serial.SerialException, OSError):
                print("Lost connection to Arduino.")
                notify("🔌 Disconnected. Reconnecting...")
                arduino = wait_for_device()

    except KeyboardInterrupt:
        print("\nStopped by user.")
        notify("❌ Copy/Paste Listener Stopped")
        sys.exit()

if __name__ == "__main__":
    main()
