#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Configuration ---
PYTHON_CMD="python3"
VENV_DIR="venv"
REQUIREMENTS_FILE="requirements.txt"
MAIN_SCRIPT="pass_cracker.py"
SAM_FILE="sam.save"
SYSTEM_FILE="system.save"

# --- Helper Functions ---
echo_info() {
    echo "[*] $1"
}

echo_success() {
    echo "[+] $1"
}

echo_error() {
    echo "[-] ERROR: $1" >&2
    exit 1
}

# --- Main Logic ---
echo_info "Starting the Linux setup and execution script..."

# 1. Check for required files
if [ ! -f "$SAM_FILE" ] || [ ! -f "$SYSTEM_FILE" ]; then
    echo_error "Missing required files. Please ensure '$SAM_FILE' and '$SYSTEM_FILE' are in this directory."
fi
echo_success "Found SAM and SYSTEM files."

# 2. Check for Python 3
if ! command -v $PYTHON_CMD &> /dev/null; then
    echo_error "$PYTHON_CMD could not be found. Please install Python 3."
fi
echo_success "Python 3 is available."

# 3. Create a virtual environment
if [ ! -d "$VENV_DIR" ]; then
    echo_info "Creating Python virtual environment in './$VENV_DIR'..."
    $PYTHON_CMD -m venv $VENV_DIR
    echo_success "Virtual environment created."
else
    echo_info "Virtual environment already exists."
fi

# 4. Install dependencies using the venv's pip
echo_info "Installing dependencies from '$REQUIREMENTS_FILE'..."
"$VENV_DIR/bin/pip" install -r "$REQUIREMENTS_FILE"
echo_success "Dependencies installed."

# 5. Run the main Python script using the venv's python
echo_info "Running the main script: '$MAIN_SCRIPT'..."
"$VENV_DIR/bin/python" "$MAIN_SCRIPT"

echo_success "Script finished execution. Check 'output.txt' for results."

