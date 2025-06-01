# Copy-Paste Keyboard (Arduino Uno + Python)

A simple hardware/software combo that allows you to trigger **Ctrl+C** (Copy) and **Ctrl+V** (Paste) using two physical buttons connected to an Arduino Uno.

Since the Arduino Uno can't act as a USB keyboard natively, this project uses a Python script to listen over USB (serial) and simulate the key presses on your computer.

---

## 🧠 How It Works

- The Arduino sketch detects button presses and sends `"COPY"` or `"PASTE"` over the serial port.
- The Python script listens to the serial messages and simulates pressing `Ctrl+C` or `Ctrl+V` using `pyautogui`.

---

## 📁 Project Structure

| File                      | Description                                 |
|---------------------------|---------------------------------------------|
| `copy_paste_keyboard.ino` | Arduino sketch to read buttons and send commands |
| `copy_paste_listener.py`  | Python script that listens and sends keypresses |

---

## 🛠 Requirements

### 🔧 Software (Ubuntu/Linux)

Install required Python libraries:

```bash
sudo apt install python3-serial
python3 -m pip install --user pyautogui
