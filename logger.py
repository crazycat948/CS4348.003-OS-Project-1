import sys
import datetime

def write_log(log_file, message):
    """Writes a timestamped message to the log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    parts = message.split(" ", 1)
    action = parts[0] if len(parts) > 0 else "UNKNOWN"
    msg = parts[1] if len(parts) > 1 else ""
    
    with open(log_file, "a") as file: 
        file.write("{} [{}] {}\n".format(timestamp, action, msg))

def main():
    if len(sys.argv) != 2:
        print("Usage: python logger.py <logfile>")
        return

    log_file = sys.argv[1]

    while True:
        line = sys.stdin.readline().strip()
        if line == "QUIT":
            break
        write_log(log_file, line)

if __name__ == "__main__":
    main()
