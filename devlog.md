 # 3/10/2025
 this is my second time work on this project, i didnt remember how to write delog last time so this is my first note here
 it is midterm week, i finished midterm for this class last week but i have other two for this week, and this project, sorry for been late to work on it.

 #3/10/2025 11:53
 I am Still trying to write delog correctly

# 3/10/2025 11:59
Last moment of today, I just uploaded three empty files to the dir, i am going to coding on VScode and upload to here, it is hard to coding on vim

#3/11/2025 12:21 
first moment of today,I finished implementing the logger for our OS project. The logger continuously reads messages from stdin and writes them to a log file with a timestamp. It only stops when it receives "QUIT"
I had some issue with this phase.
first the python version problem: During testing, I ran into an issue where the logger script wouldn’t run because of a syntax error on the f-string line
I found out f-strings didn’t work on some versions, so I switched to .format().

#3/11/2025 9/28
Today I am going to code the encryption part and make some changes in logger

#3/11/2025 11:59am
Last moment of this morning
Got the encryption program up and running today! It uses the Vigenère cipher to encrypt and decrypt messages based on a passkey. The program reads commands from stdin, processes them, and prints structured output (RESULT or ERROR).
Commands work as expected:
PASS SECRET : sets the encryption keyy
ENCRYPT HELLO : outputs RESULT ZINWW
DECRYPT ZINWW : outputs RESULT HELLO
Proper error handling when no passkey is set or input contains non-alphabetic characters..

#3/23/2025 3/23/2025
I back to Dallas when 3/22/2025 but the cs1 crushed yestertoday so I am going to keep work on it 
today I am going to develop the driver.py
The driver program controls the system by starting the logger and encryption programs, handling communication between them, and managing all input, output, and logging. It keeps a temporary history of messages and coordinates all actions without logging passwords.

#3/23/2025 00:07
the last day before the project due



 I started working on the driver program. According to the specs, it needs to launch two subprocesses: logger.py and encryption.py, and communicate with them using pipes. I’ve used subprocess.Popen before, but never with both stdin and stdout piped at once, so this was new territory.

 I wrote the basic structure of the program: it takes in a logfile name as a command-line argument, starts the logger and encryption processes, and shows a simple menu (password, encrypt, decrypt, etc.). It felt good to get the initial setup running without errors.

#3/23/2025 6:14
I worked on this project like whole day
I focused on adding the interactive menu and the actual command logic today. Each command has a purpose:
password sets the key for the encryption.
encrypt and decrypt let the user input text or choose from history.
history shows previous strings and results.
quit exits cleanly.
I added a history list to store the strings used during the session. For each command, I made sure to log actions using the logger subprocess — except for the password, of course.
So I tried running the whole thing, and… it got stuck. After entering encrypt and typing a string, the program just froze. I had no clue what was going on at first. I started printing debug messages before and after reading from encrypt_proc.stdout, and that’s when it clicked:

The encryption program wasn’t flushing its output!

In encryption.py, I was using print() to send results back, but I forgot to call sys.stdout.flush(). That’s why the driver was waiting forever — it never got the response.

Once I added sys.stdout.flush() after each print(), everything started working beautifully. Lesson learned: flush your output when using pipes!

I also added proper error messages in encryption.py for things like "password not set" or "non-alphabetic input". That made debugging way easier.

and I made sure:
Only alphabetic inputs are accepted for encryption, decryption, and password.
The driver doesn’t crash if the user types something weird.
The history menu lets users cancel and go back.
All commands and results (except the password) are logged with timestamps.
I even added helpful error messages if someone tries to encrypt “Hello World!” — we don’t allow spaces or punctuation here


