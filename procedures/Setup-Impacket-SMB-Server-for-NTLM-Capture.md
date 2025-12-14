---
tags:
  - smb
  - ntlm-capture
  - listener
type: procedure
tools:
  - '[[tools/Impacket]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/impacket-smbserver-setup]]'
verified: false
platforms:
  - Linux
  - Windows
submitted: true
created_at: '2024-10-04'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.755Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2c5c51af-ade1-4325-a26a-ef6952717b01
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup Impacket SMB Server for NTLM Capture

## Summary

This procedure sets up an SMB server using Impacket to listen for authentication attempts from vulnerable servers, capturing NTLM hashes during connection attempts triggered by SSRF exploits like CVE-2024-38472.

## Description

In the context of SSRF vulnerabilities involving UNC paths, the target server attempts to access a remote share (\\attacker\share), initiating an SMB connection to the attacker's IP on port 445. The Impacket smbserver.py script acts as a fake SMB server, forcing NTLM authentication and logging the challenge-response hashes from the target's machine account. This is useful for credential leakage without prior access. Prerequisites include Python 3 and network reachability on port 445.

## Requirements

1. Python 3.6+ installed
2. Git for cloning Impacket repository
3. Open TCP port 445 on attacker's firewall/NAT
4. A share directory (e.g., /tmp/share) with read permissions

## Defense

Defensive measures and detection strategies:

- Block outbound SMB (port 445) from web servers using firewalls
- Monitor for unexpected SMB connections from internal servers
- Use NTLM auditing and restrict NTLMv1 usage

## Objectives

1. Establish a listener for SMB authentication attempts
2. Log NTLM hashes for offline cracking or relay attacks
3. Validate SSRF exploit success via captured credentials

## Instructions

### Step 1: Install Impacket

**Context**: Clone and install the Impacket toolkit, which includes the smbserver module for SMB simulation.

**Command** ([[commands/impacket-smbserver-setup]]):
```bash
pip install impacket
git clone https://github.com/SecureAuthCorp/impacket.git
cd impacket/examples
```

> This installs dependencies and navigates to the examples directory. Expected output: Successful clone and no errors in pip install.

### Step 2: Start SMB Server

**Context**: Launch the SMB server with debug logging to capture authentication details, including NTLM hashes.

**Command** ([[commands/impacket-smbserver-setup]]):
```bash
python3 smbserver.py SHARE /tmp/share -debug
```

> The server binds to port 445 and logs all connections. Expected output: "Impacket v0.x.x - Copyright 202x SecureAuth Corporation" followed by listening confirmation. Hashes appear in logs as base64-encoded NTLMSSP responses during auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/impacket-smbserver-setup]]

## Tools Used

- [[tools/Impacket]]

## Tags

- [[smb]]
- [[ntlm]]
- [[listener]]
