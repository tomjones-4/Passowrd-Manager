Cryptographic Password Manager Tom Jones, David Lee, Henry Hilton

Implementation of basic command line version complete, along with stretch goal GUI.

Run from terminal with python master_password.py and follow prompts.

To clear data and start fresh, simply open infofile.txt and delete the saved encrypted data.

There is also a fully functional tktinker GUI version that can be run with python GUI.py. The GUI launches asynchronous subprocess threads that run master_password.py, and pipes back and forth the necessary data using stdin and stdout listeners.

Enjoy hacking the mainframe!
