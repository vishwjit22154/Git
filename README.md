# GitHub Activity Automation

Automatically maintain your GitHub contribution graph with daily commits! 🌱

## 🎯 What This Does

- Makes automated commits to your repository daily
- Updates an activity log file with timestamps
- Pushes changes to GitHub to keep your contribution graph active
- Runs automatically in the background on your Mac

## 📋 Setup Instructions

### 1. Initialize Git Repository

```bash
cd /Users/hvishwajit/GitHubHacks

# Initialize git (if not already done)
git init
git branch -M main

# Configure git with your details
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### 2. Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository (e.g., `github-activity`)
3. Don't initialize with README (we already have files)

### 3. Connect to GitHub

```bash
# Add your remote repository
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Make initial commit
git add .
git commit -m "Initial commit: Set up automation"
git push -u origin main
```

### 4. Set Up Automation

```bash
# Make scripts executable
chmod +x run_daily.sh
chmod +x auto_commit.py

# Test the script manually first
./auto_commit.py
```

### 5. Schedule Daily Automation (macOS)

```bash
# Copy the plist file to LaunchAgents
cp com.githubhacks.autocommit.plist ~/Library/LaunchAgents/

# Load the automation (runs daily at 2 PM)
launchctl load ~/Library/LaunchAgents/com.githubhacks.autocommit.plist

# Verify it's loaded
launchctl list | grep githubhacks
```

## ⚙️ Customization

### Change the Schedule

Edit `com.githubhacks.autocommit.plist` and modify the `StartCalendarInterval`:

```xml
<key>StartCalendarInterval</key>
<dict>
    <key>Hour</key>
    <integer>14</integer>  <!-- Change hour (0-23) -->
    <key>Minute</key>
    <integer>0</integer>   <!-- Change minute (0-59) -->
</dict>
```

Then reload:
```bash
launchctl unload ~/Library/LaunchAgents/com.githubhacks.autocommit.plist
cp com.githubhacks.autocommit.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.githubhacks.autocommit.plist
```

### Run Multiple Times Per Day

You can add multiple `StartCalendarInterval` dictionaries:

```xml
<key>StartCalendarInterval</key>
<array>
    <dict>
        <key>Hour</key>
        <integer>10</integer>
    </dict>
    <dict>
        <key>Hour</key>
        <integer>16</integer>
    </dict>
</array>
```

## 🧪 Testing

### Test Manually
```bash
# Run the script manually to test
python3 auto_commit.py

# Or use the shell wrapper
./run_daily.sh
```

### Check Logs
```bash
# View automation logs
tail -f automation.log

# View launchd logs
tail -f launchd.log
tail -f launchd.error.log
```

## 🛑 Stop/Remove Automation

```bash
# Unload the automation
launchctl unload ~/Library/LaunchAgents/com.githubhacks.autocommit.plist

# Remove the plist file
rm ~/Library/LaunchAgents/com.githubhacks.autocommit.plist
```

## 📝 Files Overview

- `auto_commit.py` - Main Python script that creates commits
- `run_daily.sh` - Shell wrapper for logging
- `com.githubhacks.autocommit.plist` - macOS scheduler configuration
- `activity_log.txt` - Log file that gets updated with each commit
- `automation.log` - Script execution logs
- `launchd.log` / `launchd.error.log` - System scheduler logs

## ⚠️ Important Notes

1. **Authentication**: Make sure you have Git authentication set up:
   - Use SSH keys (recommended): https://docs.github.com/en/authentication/connecting-to-github-with-ssh
   - Or use a Personal Access Token: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

2. **Privacy**: This creates public commits. Make sure you're comfortable with this activity on your profile.

3. **GitHub Terms**: Automated commits for the sole purpose of increasing your contribution count may be against GitHub's terms of service. Use responsibly.

## 🚀 Quick Start (All-in-One)

```bash
cd /Users/hvishwajit/GitHubHacks

# 1. Make scripts executable
chmod +x run_daily.sh auto_commit.py

# 2. Configure git
git init
git branch -M main
git config user.name "Your Name"
git config user.email "your@email.com"

# 3. Add remote (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/github-activity.git

# 4. Initial commit
git add .
git commit -m "Initial commit"
git push -u origin main

# 5. Set up automation
cp com.githubhacks.autocommit.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.githubhacks.autocommit.plist

# 6. Test it
python3 auto_commit.py
```

## 🎉 Success!

Your automation is now set up! Check your GitHub profile tomorrow to see your contribution graph updating automatically.

---

**Made with ❤️ for maintaining coding streaks**

