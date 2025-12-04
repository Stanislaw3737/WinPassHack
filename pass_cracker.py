import sys
import subprocess
import os

def main():
    """
    Main function to run the secretsdump.py script from impacket.
    """
    print("--- SAM/SYSTEM Hash Dumper (Educational Purposes Only) ---")

    sam_file = "sam.save"
    system_file = "system.save"
    output_file = "output.txt"

    # Get the absolute path to the secretsdump.py script in the venv's Scripts directory
    secretsdump_script = os.path.join(os.path.dirname(sys.executable), '..', 'Scripts', 'secretsdump.py')
    
    # Resolve the full path to handle '..'
    secretsdump_script = os.path.normpath(secretsdump_script)

    if not os.path.exists(secretsdump_script):
        print(f"\n[FAILURE] Could not find secretsdump.py at {secretsdump_script}")
        print("Please ensure impacket is correctly installed in the virtual environment and its scripts are in the 'venv/Scripts' directory.")
        return

    print(f"\n[+] Using SAM file: {sam_file}")
    print(f"[+] Using SYSTEM file: {system_file}")
    print(f"[+] Output will be saved to: {output_file}\n")

    command = [
        sys.executable, # Use the venv's python.exe
        secretsdump_script,
        '-sam', sam_file,
        '-system', system_file,
        'LOCAL'
    ]

    try:
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Write the successful output to the file
        with open(output_file, 'w') as f:
            f.write(result.stdout)
        
        print(f"\n[SUCCESS] Hash dump complete. Check the '{output_file}' for the results.")

    except FileNotFoundError:
        print(f"\n[FAILURE] Could not find one of the required files: {sam_file} or {system_file}")
    except subprocess.CalledProcessError as e:
        # If the command fails, write the error to the output file and check for common issues
        print("\n[FAILURE] The secretsdump.py script encountered an error.")
        error_output = "--- STDOUT ---\n"
        error_output += e.stdout
        error_output += "\n--- STDERR ---\n"
        error_output += e.stderr

        with open(output_file, 'w') as f:
            f.write(error_output)

        # Provide a more helpful message for the specific error
        if "[Errno 13] Permission denied" in e.stderr:
             print("\n[DIAGNOSIS] Permission denied. Please try running this script from a terminal with Administrator privileges.")
        elif "[Errno 22] Invalid argument" in e.stdout:
            print("\n[DIAGNOSIS] This error often means the SAM/SYSTEM files are corrupt or incomplete.")
            print(r"Please try exporting them again using 'reg save' in an Administrator Command Prompt.")
        
        print(f"Error details have been written to '{output_file}'.")
    except Exception as e:
        print(f"\n[FAILURE] An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()