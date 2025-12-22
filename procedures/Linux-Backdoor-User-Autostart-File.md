---
id: 1353162b-cac5-41c1-905c-ba938d0802e2
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.070727+00:00'
updated_at: '2023-04-10T20:34:18.923868+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Boot-or-Logon-Autostart-Execution|T1547 - Boot or Logon
    Autostart Execution]]
sub_techniques: []
tags:
  - '[[tags/Linux-Persistence]]'
  - '[[tags/Autostart-Backdoor]]'
commands:
  - '[[commands/mkdir-create-autostart-directory]]'
  - '[[commands/create-backdoor-autostart-desktop-file]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Backdoor-User-Autostart-File

## Summary

This procedure demonstrates how to achieve persistence on a Linux system with a graphical desktop environment (such as GNOME) by creating or modifying a user autostart file. A malicious script or program is added to the ~/.config/autostart directory via a .desktop file, which executes automatically upon user login, allowing attackers to maintain access, exfiltrate data, or perform other post-exploitation activities without detection.

## Description

Backdooring user startup files targets the autostart mechanism in desktop environments like GNOME, where .desktop files in ~/.config/autostart are executed at login. This technique is stealthy because it masquerades as a legitimate startup application, blending with normal system processes. It requires local user-level access but can be combined with privilege escalation for root persistence. The approach involves creating a .desktop file with an Exec entry pointing to a backdoor payload, such as a reverse shell script. Upon successful execution, the backdoor runs in the user's session, providing ongoing access even after reboots. This is particularly effective in environments where users log in graphically and defenders overlook home directory changes.

## Requirements

1. Local access to the target user's account (shell access via SSH or console).
2. Write permissions to the user's home directory (~/.config).
3. A pre-placed backdoor script or binary on the target (e.g., a reverse shell in a hidden location like ~/.hidden/backdoor.sh).
4. GNOME or compatible desktop environment on the target Linux system.

## Defense

- Monitor file system changes in user home directories, especially ~/.config/autostart, using tools like auditd or inotify.
- Implement application whitelisting or integrity checks on startup files to prevent unauthorized modifications.
- Review autostart entries regularly via ls ~/.config/autostart and validate Exec paths against known legitimate applications.
- Enable logging for desktop environment startups and correlate with unexpected process spawns.

## Objectives

1. Establish persistence by automatically executing a backdoor on user login.
2. Maintain stealthy access to the compromised account post-reboot.
3. Enable further post-exploitation, such as keylogging or data exfiltration, within the user session.

## Instructions

### Step 1: Create Autostart Directory

**Context**: The ~/.config/autostart directory may not exist; create it to hold the backdoor .desktop file. This ensures the file is placed in the correct location for execution at login.

**Command** ([[commands/mkdir-create-autostart-directory]]):
```bash
mkdir -p ~/.config/autostart
```

> This command creates the directory recursively if it does not exist. It performs no action if the directory already exists.

**Expected Output**: No output on success (silent operation). Verify with `ls ~/.config` to see the 'autostart' directory.

### Step 2: Create Backdoor Desktop File

**Context**: Generate a .desktop file that defines the autostart application. The file uses a benign name and comment to avoid suspicion, but the Exec field points to the attacker's backdoor script. This file will trigger the payload every time the user logs into the graphical session.

**Command** ([[commands/create-backdoor-autostart-desktop-file]]):
```bash
cat > ~/.config/autostart/backdoor.desktop << 'EOF'
[Desktop Entry]
Type=Application
Exec=$_BACKDOOR_SCRIPT_PATH
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=System Service
Comment=Background system service
EOF
```

> Substitute $_BACKDOOR_SCRIPT_PATH with the full path to your backdoor script (e.g., /home/user/.ssh/backdoor.sh). The heredoc (<< 'EOF') preserves literal content without expansion. Ensure the backdoor script is executable (chmod +x $_BACKDOOR_SCRIPT_PATH) before running this.

**Expected Output**: No stdout output; the file is written silently. Verify creation and content with `cat ~/.config/autostart/backdoor.desktop` to confirm the Exec path is set correctly.

### Step 3: Verify and Test Persistence

**Context**: Confirm the backdoor file is in place and will execute. Log out and back in to the graphical session to test; monitor for backdoor execution (e.g., via a listener on the attacker side if it's a reverse shell).

**Instructions**: Run `ls -la ~/.config/autostart` to list files. The backdoor.desktop should appear with recent modification time. For decision point: If the desktop environment is not GNOME, adapt for KDE (~/.config/autostart-scripts/) or other DEs; otherwise, proceed to testing.

**Expected Output**: Output shows backdoor.desktop file. Upon login test, the backdoor script executes (e.g., connection to attacker listener).

**Success Indicators**:
- .desktop file exists and contains correct Exec path.
- No permission errors during file creation.
- Backdoor activates on graphical login without user notification.
