import subprocess
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python driver.py <logfile>")
        return

    log_file = sys.argv[1]
    

    logger_proc = subprocess.Popen(
        ["python3", "logger.py", log_file],
        stdin=subprocess.PIPE,
        universal_newlines=True
    )
    encrypt_proc = subprocess.Popen(
        ["python3", "encryption.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    history = []

    def log_message(action, message):

        logger_proc.stdin.write(f"{action} {message}\n")
        logger_proc.stdin.flush()

    log_message("START", "Driver started.")

    while True:
        print("\nCommands: password, encrypt, decrypt, history, quit")
        command = input("Enter command: ").strip().lower()

        if command == "password":
            key = input("Enter passkey: ").strip().upper()
            if not key.isalpha():
                print("ERROR: Only alphabetic passkeys allowed.")
                continue
            encrypt_proc.stdin.write(f"PASS {key}\n")
            encrypt_proc.stdin.flush()
            response = encrypt_proc.stdout.readline().strip()
            print(response)
       

        elif command == "encrypt":
            use_history = input("Use string from history? (Y/N): ").strip().lower()
            if use_history == 'y' and history:
                for i, entry in enumerate(history, 1):
                    print(f"{i}. {entry}")
                choice = input("Enter number or 0 to cancel: ").strip()
                if not choice.isdigit() or int(choice) < 0 or int(choice) > len(history):
                    print("Invalid choice.")
                    continue
                if int(choice) == 0:
                    continue
                text = history[int(choice) - 1]
            else:
                text = input("Enter text to encrypt: ").strip().upper()
                if not text.isalpha():
                    print("ERROR: Only alphabetic input allowed.")
                    continue
                history.append(text)

            encrypt_proc.stdin.write(f"ENCRYPT {text}\n")
            encrypt_proc.stdin.flush()
            response = encrypt_proc.stdout.readline().strip()
            print(response)

            if response.startswith("RESULT"):
                result = response.split(" ", 1)[1]
                history.append(result)
            log_message("ENCRYPT", text)

        elif command == "decrypt":
            use_history = input("Use string from history? (Y/N): ").strip().lower()
            if use_history == 'y' and history:
                for i, entry in enumerate(history, 1):
                    print(f"{i}. {entry}")
                choice = input("Enter number or 0 to cancel: ").strip()
                if not choice.isdigit() or int(choice) < 0 or int(choice) > len(history):
                    print("Invalid choice.")
                    continue
                if int(choice) == 0:
                    continue
                text = history[int(choice) - 1]
            else:
                text = input("Enter text to decrypt: ").strip().upper()
                if not text.isalpha():
                    print("ERROR: Only alphabetic input allowed.")
                    continue
                history.append(text)

            encrypt_proc.stdin.write(f"DECRYPT {text}\n")
            encrypt_proc.stdin.flush()
            response = encrypt_proc.stdout.readline().strip()
            print(response)

            if response.startswith("RESULT"):
                result = response.split(" ", 1)[1]
                history.append(result)
            log_message("DECRYPT", text)

        elif command == "history":
            print("\nHistory:")
            if not history:
                print("(empty)")
            else:
                for i, entry in enumerate(history, 1):
                    print(f"{i}. {entry}")

        elif command == "quit":
            log_message("QUIT", "Driver shutting down.")
            encrypt_proc.stdin.write("QUIT\n")
            encrypt_proc.stdin.flush()
            logger_proc.stdin.write("QUIT\n")
            logger_proc.stdin.flush()
            break

        else:
            print("ERROR: Invalid command.")

    encrypt_proc.wait()
    logger_proc.wait()
    print("Driver exited.")

if __name__ == "__main__":
    main()