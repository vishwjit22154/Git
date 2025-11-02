#!/bin/bash

# Navigate to the script directory
cd "$(dirname "$0")"

# Log the execution
echo "===========================================" >> automation.log
echo "Running at: $(date)" >> automation.log

# Run the Python script
python3 auto_commit.py >> automation.log 2>&1

echo "Completed at: $(date)" >> automation.log
echo "" >> automation.log

