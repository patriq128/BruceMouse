# BruceMouse

BruceMouse is an educational Python project created to demonstrate how keyboard-based brute force attacks can work in a controlled, learning-focused environment.

This project was written entirely by a human as a learning experience.  
It is not perfect, contains bugs and unnecessary code, and that is intentional — it reflects real learning and experimentation.

---

## Disclaimer

This project is for educational purposes only.

- Do not use this project to attack real systems
- Do not use it on accounts, websites, or devices you do not own
- The author takes no responsibility for misuse

The goal of this project is to understand how attacks work so they can be better prevented.

---

## Features

- Keyboard-based brute force simulation (desktop only)
- Visualization-only mode (no keyboard input)
- Password strength calculation
- Configurable speed via a config file
- Terminal-based user interface with ANSI colors
- Device detection (Desktop / Termux)
- Built-in help menu

---

## How It Works (High-Level)

BruceMouse generates combinations of characters using Python's itertools.product.

Depending on the selected mode:
- The program prints combinations to the terminal (visualization mode)
- Or simulates keyboard input (desktop only)

The password calculator estimates how many possible combinations a password has based on the character sets it contains.

No real passwords are cracked.  
No real targets are included.

---

## Requirements

- Python 3.x
- Desktop operating system (Linux or Windows) for keyboard simulation
- pyautogui (optional, desktop only)

Visualization mode works without pyautogui.

---

## Usage

```bash
python brucemouse.py

## License
This project is licensed under the MIT License — see the LICENSE file for details.
