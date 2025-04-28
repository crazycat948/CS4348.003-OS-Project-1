import sys

class VigenereCipher:
    def __init__(self):
        self.key = None

    def set_key(self, key):
        self.key = key.upper()

    def encrypt(self, text):
        if not self.key:
            return "ERROR Password not set"
        return f"RESULT {self.vigenere_cipher(text, encrypt=True)}"

    def decrypt(self, text):
        if not self.key:
            return "ERROR Password not set"
        return f"RESULT {self.vigenere_cipher(text, encrypt=False)}"

    def vigenere_cipher(self, text, encrypt=True):
        text = text.upper()
        key = self.key
        key_len = len(key)
        result = []

        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(key[i % key_len]) - ord('A')
                base = ord('A')
                if encrypt:
                    new_char = chr((ord(char) - base + shift) % 26 + base)
                else:
                    new_char = chr((ord(char) - base - shift) % 26 + base)
                result.append(new_char)
            else:
                return "ERROR Input must be alphabetic only"
        return "".join(result)

def main():
    cipher = VigenereCipher()

    while True:
        line = sys.stdin.readline().strip()
        if not line:
            continue
        parts = line.split(" ", 1)
        command = parts[0].upper()
        argument = parts[1] if len(parts) > 1 else ""

        if command == "PASS":
            cipher.set_key(argument)
            print("RESULT")
            sys.stdout.flush()
        elif command == "ENCRYPT":
            print(cipher.encrypt(argument))
            sys.stdout.flush()
        elif command == "DECRYPT":
            print(cipher.decrypt(argument))
            sys.stdout.flush()
        elif command == "QUIT":
            break
        else:
            print("ERROR Unknown command")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
