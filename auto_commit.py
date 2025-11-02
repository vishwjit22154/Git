#!/usr/bin/env python3
"""
Automated GitHub Commit Script
Keeps your GitHub contribution graph active by making daily commits
"""

import os
import sys
from datetime import datetime
import subprocess


def run_command(command, cwd=None):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error: {e.stderr}")
        return None


def main():
    # Get the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Log file path
    log_file = os.path.join(script_dir, "activity_log.txt")
    
    # Current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Append to log file
    with open(log_file, "a") as f:
        f.write(f"Automated commit at {timestamp}\n")
    
    print(f"✓ Updated activity log at {timestamp}")
    
    # Git operations
    os.chdir(script_dir)
    
    # Check if git repo is initialized
    if not os.path.exists(os.path.join(script_dir, ".git")):
        print("Initializing git repository...")
        run_command("git init", script_dir)
        run_command("git branch -M main", script_dir)
    
    # Configure git if not already configured
    git_user = run_command("git config user.name", script_dir)
    if not git_user:
        print("Please configure git:")
        print("  git config user.name 'Your Name'")
        print("  git config user.email 'your.email@example.com'")
        sys.exit(1)
    
    # Stage changes
    run_command("git add activity_log.txt", script_dir)
    
    # Commit
    commit_msg = f"Auto-commit: {timestamp}"
    run_command(f'git commit -m "{commit_msg}"', script_dir)
    
    print(f"✓ Created commit: {commit_msg}")
    
    # Push to remote (if configured)
    remote = run_command("git remote", script_dir)
    if remote:
        print("Pushing to remote...")
        push_result = run_command("git push origin main", script_dir)
        if push_result is not None:
            print("✓ Successfully pushed to GitHub")
        else:
            print("⚠ Push failed - please check your remote configuration")
    else:
        print("⚠ No remote configured. Add one with:")
        print("  git remote add origin <your-repo-url>")
        print("  git push -u origin main")
    
    print("\n✅ Automation complete!")


if __name__ == "__main__":
    main()

