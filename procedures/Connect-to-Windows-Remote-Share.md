---
type: procedure
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques:
  - >-
    [[sub-techniques/SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin
    Shares]]
tags:
  - '[[tags/Mount a remote share]]'
  - '[[tags/Other methods]]'
  - '[[tags/Windows - Using credentials]]'
commands:
  - '[[commands/net-use-connect-remote-share]]'
platforms:
  - Windows
skill_level: beginner
impact_level: medium
detection_risk: high
verified: true
validated: true
---

# Connect-to-Windows-Remote-Share

## Summary

This procedure demonstrates how to mount a remote Windows administrative share using valid credentials, enabling access to files and directories on a target system for lateral movement within a network. It leverages the built-in 'net use' command to establish a connection to hidden shares like C$, allowing attackers to read or write data as if accessing a local drive.

## Description

In lateral movement scenarios, attackers often use remote share access to pivot between compromised systems. This technique targets SMB/Windows Admin Shares (T1021.002), which are enabled by default on many Windows servers for administrative purposes. By providing domain credentials, the attacker can connect to shares on remote hosts without needing interactive logon rights. The procedure assumes the attacker has obtained credentials through prior enumeration or phishing and has network connectivity to the target. Success grants file system access, facilitating data staging, tool deployment, or further reconnaissance. Note that this method generates detectable network traffic and may trigger credential auditing if monitored.

## Requirements

1. Valid domain or local credentials (username and password) with read/write access to the target share.
2. Network connectivity to the target host via SMB (port 445 open).
3. Local execution privileges on a Windows system (e.g., command prompt or PowerShell access).
4. Knowledge of the target hostname or IP and the share name (e.g., C$ for system drive root).

## Defense

- Disable administrative shares (Admin Shares) via registry or Group Policy to prevent unauthorized access.
- Implement network segmentation and firewall rules to restrict SMB traffic between segments.
- Enable multi-factor authentication (MFA) for accounts and monitor for anomalous credential usage via tools like Windows Event Logs (Event ID 4624 for logons).
- Use endpoint detection and response (EDR) solutions to alert on 'net use' executions or unexpected SMB connections.

## Objectives

1. Establish a persistent connection to a remote Windows share using provided credentials.
2. Enable file access on the target system for lateral movement or data exfiltration.
3. Verify successful mount without triggering immediate alerts.

## Instructions

### Step 1: Prepare Connection Details

**Context**: Gather the necessary details for the connection, including the target UNC path (e.g., \\hostname\share), domain-qualified username, and password. Ensure SMB is accessible by pinging the target or using tools like [[commands/nmap-smb-enumeration]] to confirm port 445 availability. This step prevents execution errors due to misconfiguration.

If the share is an admin share like C$, confirm the credentials have administrative privileges on the target.

### Step 2: Execute the Share Connection

**Context**: Use the 'net use' command to authenticate and mount the remote share. This creates a mapped connection that can be accessed via Windows Explorer or subsequent commands like 'dir' for listing contents. The connection persists until manually disconnected or the session ends, but avoid persistent mapping to reduce detection risk.

**Command** ([[commands/net-use-connect-remote-share]]):
```cmd
net use \\srv01.domain.local\C$ /user:DOMAIN\username password
```

> This command connects to the C$ admin share on srv01.domain.local using the specified credentials. Replace placeholders with actual values: hostname/IP, share name, domain/username, and password. If successful, the share mounts without errors, allowing commands like `dir \\srv01.domain.local\C$` to list files. For persistent mapping to a drive letter (e.g., Z:), add `/persistent:yes`.

**Expected Output**:
```
The command completed successfully.
```

If credentials are invalid, expect: `System error 5 has occurred. Access is denied.` or `System error 1326 has occurred. The user name or password is incorrect.`

### Step 3: Verify and Use the Connection

**Context**: Confirm the mount by accessing the share and performing basic operations. This validates access and allows immediate use for objectives like copying files.

Run a directory listing on the mounted share:
```cmd
dir \\srv01.domain.local\C$
```

> Expected output includes a list of root directory contents (e.g., Windows, Program Files). If accessible, proceed to copy tools or exfiltrate data using commands like `copy localfile.exe \\srv01.domain.local\C$\temp\`.

**Expected Output**:
```
 Volume in drive C is Windows
 Directory of \\srv01.domain.local\C$

04/10/2023  10:00 AM    <DIR>          PerfLogs
04/10/2023  10:00 AM    <DIR>          Program Files
... (file listing)
```

### Step 4: Clean Up Connection

**Context**: Disconnect the share to minimize footprint and avoid persistent artifacts. This reduces the window for detection.

**Command**:
```cmd
net use \\srv01.domain.local\C$ /delete
```

> Expected output: `The command completed successfully.` Use `net use` without arguments to list active connections before deletion.
