# Linux User Management Demonstration

## Step 1: Creating a User
Command: 'sudo useradd -m yahiko
Explanation: This creates a new user called 'yahiko' with a home directory

## Step 2: Setting password
Command: sudo passwd yahiko
Explanation: Adds password to user 'yahiko'

## Step 3: Create a directory and Change its ownership
Command: mkdir 'test_dir' & sudo chown yahiko ~/test_dir path
Explanation: mkdir creates a new directory and chown assigns the directory to user yahiko

## Step 4: Modify file permissions
Command: touch test1 test2 test3 & sudo chmod u+x test1 test2 test3
Explanation: touch creates empty file, while u+x assigns excute permission to the user

# Step 5: Lock and Unlock a user account
Command: sudo usermod -L yahkiko & sudo usermod -U yahiko
Explanation: -L locks the user yahiko and -U unlocks the user yahiko

