#!/bin/bash

CURRENT_PATH=$(pwd)

if [[ -d "$CURRENT_PATH/venv" ]]; then
    echo "Virtual environment already exists. Activating it now."
    source venv/bin/activate
    echo "Virtual environment activated."
    echo "Updating dependencies..."
    pip install -r requirements.txt --quiet
else
    echo "No virtual environment found. Creating a new one now."
    python3 -m venv venv
    echo "Virtual environment created. Now sourcing..."
    source venv/bin/activate
    echo "Virtual environment activated. Installing dependencies..."
    pip install -r requirements.txt
fi

cat << EOF
 
Virtual environment created and dependencies installed.
To run demo enter the following:
python -m main
EOF

