# BlackUnzipper

BlackUnzipper is a Python application designed to crack the password of a zip file using a provided wordlist. The script reads passwords from the wordlist and tries each one until it finds the correct password or exhausts the list.

## Features

- Cracks password-protected zip files using a dictionary attack.
- Provides feedback on whether the correct password was found.
- Handles common errors gracefully.

## Requirements

- Python 3
- A zip file to crack
- A wordlist file containing potential passwords

## Installation

1. Ensure you have Python 3 installed on your machine.
2. Clone this repository or download the `blackunzipper.py` script.
3. Make sure you have the required wordlist file.

## Usage

```sh
python3 blackunzipper.py <target_file> <wordlist>
```
- <target_file>: The path to the zip file you want to crack.
- <wordlist>: The path to the wordlist file containing potential passwords.

## Example
```sh
python3 blackunzipper.py secret.zip passwords.txt
```

## How It Works

1. The script checks if the provided wordlist path is valid.
2. It reads passwords from the wordlist file and attempts to use each one to unzip the target file.
3. If the correct password is found, it prints [+] Password Cracked = <password>.
4. If the correct password is not found in the wordlist, it prints [-] Could not find password in wordlist.

## Error Handling

- The script checks if the provided wordlist path is valid and exits with a message if it's not.
- If any other error occurs during the password checking process, it is handled gracefully and the script continues to the next password.

## Author

This script was created by BlackMagic.

## License

This project is licensed under the MIT License.

## Disclaimer

This tool is for educational purposes only. Use it at your own risk. Ensure you have permission to attempt to crack the zip file. The author is not responsible for any misuse or damage caused by this tool.
