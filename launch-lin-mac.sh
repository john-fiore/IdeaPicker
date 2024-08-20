#!/bin/bash

if ! command -v python &> /dev/null
then
    echo "ERROR: Python is not installed."
    read -p "Do you want to open the Python website? (y/n): " openWebsite
    if [[ "$openWebsite" == "y" || "$openWebsite" == "Y" ]]; then
        xdg-open https://www.python.org 2> /dev/null || open https://www.python.org
    fi
    exit 1
fi

python your_script.py
