# PassCracker: SAM/SYSTEM Hash Extractor (Educational Purposes Only)

## Disclaimer
This tool is for **educational and ethical security research purposes only**. Unauthorized access to computer systems, including password hash extraction, is illegal and unethical. Use this tool only on systems you own or have explicit, written permission to test. The author is not responsible for any misuse of this software.

## Introduction
PassCracker is a Python-based utility designed to extract NTLM password hashes from the Windows Security Account Manager (SAM) and SYSTEM registry hives. It leverages the powerful `impacket` library to parse these files, allowing you to recover user hashes for security auditing or penetration testing practice in controlled environments.

This tool is specifically designed for **Linux environments** to process Windows `sam.save` and `system.save` files.

## Features
*   Extracts NTLM hashes from `sam.save` and `system.save` files.
*   Automated setup and execution script for Linux systems.
*   Outputs extracted hashes to a clear text file (`output.txt`).

## Prerequisites
*   A **Windows machine** from which to retrieve the `sam.save` and `system.save` files.
*   A **Linux system** (or Windows Subsystem for Linux - WSL) to run this script.
*   **Python 3** installed on your Linux system (`python3` command should be available).

## How to Obtain `sam.save` and `system.save` Files (from Windows)
The `SAM` and `SYSTEM` registry hives contain the encrypted password hashes and the cryptographic key (Boot Key or SysKey) needed to decrypt them, respectively. **These files are locked by Windows while the OS is running, so direct copying will result in corrupt files.**

To obtain valid copies, you **must** use the `reg save` command from an Administrator command prompt:

1.  Open **Command Prompt (cmd)** or **PowerShell** as an **Administrator**.
2.  Execute the following commands, one after the other:
    ```cmd
    reg save hklm\sam C:\sam.save
    reg save hklm\system C:\system.save
    ```
    This will save clean copies of `sam.save` and `system.save` to the root of your `C:\` drive.
3.  Copy these two files (`C:\sam.save` and `C:\system.save`) to the directory where you will run PassCracker on your Linux system.

## Setup and Usage (on Linux/WSL)

1.  **Transfer Files:**
    Ensure all project files (`pass_cracker.py`, `requirements.txt`, `setup_and_run.sh`, `sam.save`, `system.save`) are in the same directory on your Linux machine.

2.  **Make the Setup Script Executable:**
    Open your Linux terminal, navigate to the project directory, and make the `setup_and_run.sh` script executable:
    ```bash
    chmod +x setup_and_run.sh
    ```

3.  **Run the Setup and Execution Script:**
    Execute the shell script. It will automatically:
    *   Check for `sam.save` and `system.save`.
    *   Create a Python virtual environment (`venv`).
    *   Install the `impacket` library (and its dependencies) into the virtual environment.
    *   Run the `pass_cracker.py` script using the virtual environment's Python.

    ```bash
    ./setup_and_run.sh
    ```

## Output
The extracted hashes will be saved in a file named `output.txt` in the same directory. The format typically looks like:
`username:RID:LMhash:NThash`

## Important Notes & Troubleshooting

*   **`[Errno 22] Invalid argument`:** This error almost always means your `sam.save` or `system.save` files are corrupt or incomplete. Please re-read the "How to Obtain..." section above and ensure you use the `reg save` command from an Administrator prompt.
*   **Permissions on Linux:** If you encounter permission errors on Linux, ensure the `sam.save` and `system.save` files are readable by your user. You might need to change their permissions using `chmod` if they were copied with restrictive permissions (e.g., `chmod 644 sam.save system.save`).
*   **Virtual Environments:** The `setup_and_run.sh` script automatically creates and uses a Python virtual environment. This is crucial for isolating dependencies and preventing conflicts with your system's Python installation.
*   **Ethical Hacking:** Always stay within legal and ethical boundaries. This tool is intended for educational purposes on systems you have explicit permission to audit.
