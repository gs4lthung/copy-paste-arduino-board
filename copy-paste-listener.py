import serial
import pyautogui

# Replace with your Arduino serial port (check with `ls /dev/tty*`)
arduino = serial.Serial('/dev/ttyUSB0', 9600)

print("Listening for COPY/PASTE...")

while True:
    if arduino.in_waiting:
        command = arduino.readline().decode().strip()
        if command == "COPY":
            pyautogui.hotkey("ctrl", "c")
            print("Ctrl+C")
        elif command == "PASTE":
            pyautogui.hotkey("ctrl", "v")
            print("Ctrl+V")
