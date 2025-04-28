# CS4348.003-OS-Project-1
# CS4348 Project 1: Driver, Logger, and Encryption System

## Project Overview
This project consists of three separate programs working together:

- **Driver Program:** Main controller. Launches the logger and encryption programs, communicates with them, and interacts with the user.
- **Logger Program:** Receives logging messages from the driver and writes timestamped logs into a log file.
- **Encryption Program:** Provides Vigenère cipher encryption and decryption services.

Communication between the programs is done through **pipes**.  
This project is implemented in **Python** using the `subprocess` module.

---

## File Structure

- `driver.py`  
  The main entry point. Starts the logger and encryption processes, presents a user menu, and handles user interaction.
  
- `logger.py`  
  A program that receives log messages through standard input and writes them to a specified log file with timestamps.

- `encryption.py`  
  Provides Vigenère cipher encryption and decryption. Receives commands via standard input and returns results or errors via standard output.

- `devlog.md`  
  Development journal documenting session thoughts, plans, progress, and issues encountered.

- `README.md`  
  This file. Instructions and descriptions of project files and how to run the system.

---

## How to Compile and Run

### Prerequisites:
- Python 3.8 or higher installed
- No external libraries are needed (only standard libraries are used: `subprocess`, `sys`, etc.)

### Run the Project:
In the command line terminal, navigate to the project folder and run:

```bash
python driver.py log.txt