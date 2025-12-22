---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:16.364916+00:00'
updated_at: '2023-04-10T20:36:20.000747+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Access Tools|T1219 - Remote Access Tools]]'
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques:
  - '[[sub-techniques/SSH|T1021.004 - SSH]]'
tags:
  - '[[tags/Cobalt Strike]]'
  - '[[tags/Payloads]]'
  - '[[tags/SSH Beacon]]'
  - lateral-movement
  - persistence
commands:
  - '[[commands/cobalt-strike-beacon-ssh-password-auth]]'
  - '[[commands/cobalt-strike-beacon-ssh-key-auth]]'
platforms:
  - Windows
  - Linux
tools:
  - '[[tools/Cobalt-Strike]]'
validated: true
---

# Deploy-SSH-Beacon-via-Cobalt-Strike

## Summary

This procedure uses Cobalt Strike to deploy an SSH Beacon payload on a compromised system, enabling persistent remote access via SSH for command execution, file transfer, and lateral movement to other systems. It leverages the beacon's built-in SSH client capabilities to establish connections using either password or key-based authentication, allowing attackers to maintain control without relying on native SSH binaries that might trigger alerts.

## Description

The SSH Beacon payload in Cobalt Strike is a specialized implant that spawns an SSH client from within an existing beacon session on a compromised host. Once deployed, it connects outbound to an attacker-controlled SSH server or pivots to internal targets, providing a stealthy channel for post-exploitation activities. This technique is particularly useful in environments with SSH services enabled, as it blends with legitimate traffic and supports encrypted command and control. The procedure assumes an initial beacon is already running on the target and focuses on using the beacon console to initiate SSH sessions for persistence or lateral movement. It maps to MITRE ATT&CK for remote services exploitation and is effective against Linux/Unix systems but adaptable to Windows with SSH enabled.

## Requirements

1. An active Cobalt Strike beacon session on the compromised target system (initial access via exploit or phishing).
2. Valid credentials (username/password) or SSH private key for the target SSH service.
3. Cobalt Strike client with team server configured for C2 communication.
4. Network access from the compromised host to the target SSH server (port 22 open).
5. Attacker-controlled SSH server for reverse connections if needed.

## Defense

- Enforce multi-factor authentication (MFA) for all SSH access and monitor for brute-force attempts.
- Use host-based firewalls to restrict outbound SSH connections to trusted endpoints and log all SSH activity.
- Implement endpoint detection and response (EDR) tools to monitor for anomalous processes spawning SSH clients, such as unexpected PowerShell or beacon-like behaviors.
- Segment networks to limit lateral movement and deploy SSH honeypots to detect scanning.

## Objectives

1. Establish persistent SSH-based access from the compromised system to maintain control.
2. Enable lateral movement to additional internal systems via SSH pivoting.
3. Facilitate data exfiltration and arbitrary command execution over encrypted channels.

## Instructions

### Step 1: Verify Beacon Session and Target SSH Service

**Context**: Confirm the beacon is active and identify the target SSH host for connection. This ensures the environment is ready for SSH deployment without alerting defenses.

Use reconnaissance commands within the beacon to probe the target, such as pinging or port scanning if needed, but assume port 22 is open.

**Expected Output**: Confirmation of beacon stability and target reachability.

### Step 2: Initiate SSH Connection with Password Authentication

**Context**: From the beacon console, spawn an SSH client using password credentials to authenticate and establish a session. This step creates the beacon's SSH tunnel for remote access.

**Command** ([[commands/cobalt-strike-beacon-ssh-password-auth]]):

```cobalt-strike-beacon
ssh $_TARGET_PORT $_USERNAME $_PASSWORD
```

> This command launches the SSH client targeting the specified host and port (default 22), authenticating with the provided username and password. Success grants an interactive SSH shell within the beacon, allowing uploads/downloads and command execution. If authentication fails, it returns an error; monitor for connection logs.

**Expected Output**: Successful login prompt or shell access, e.g., "Connected to target. Escape character is '^]'". Failure shows "Permission denied".

### Step 3: Initiate SSH Connection with Key-Based Authentication

**Context**: For more secure or key-only environments, use a private key file uploaded to the beacon to authenticate. This avoids password exposure in logs.

First, upload the private key to the beacon using the built-in upload command, then execute the SSH key auth.

**Command** ([[commands/cobalt-strike-beacon-ssh-key-auth]]):

```cobalt-strike-beacon
ssh-key $_TARGET_PORT $_USERNAME $_KEY_PATH
```

> Upload the key via "upload /local/path/to/key.pem" before running. The command uses the key for authentication, providing the same shell access as password auth but with stronger credential handling. Verify key permissions (600) on the target side if needed.

**Expected Output**: Authenticated shell session, similar to password auth. Errors include "Key not found" or permission issues.

### Step 4: Utilize SSH Session for Post-Exploitation

**Context**: Once connected, leverage the SSH session for persistence, exfiltration, or movement. Common beacon-integrated actions include file transfer and port forwarding.

Within the SSH shell, execute beacon commands like upload, download, or socks for proxying.

**Expected Output**: Successful file operations or forwarded ports, e.g., "File uploaded successfully".

**Success Indicators**:
- Interactive shell access without errors.
- Ability to run commands like 'ls' or 'whoami' on the remote host.
- No immediate disconnection or alert triggers.
