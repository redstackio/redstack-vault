---
id: 5f7397df-8b1a-4451-8052-5265fe6e2acd
name: Set-Up-NTLM-Capture-Server
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:54.919Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Adversary-in-the-Middle]]'
sub_techniques: []
tags:
  - ntlm
  - capture
  - responder
commands:
  - '[[commands/responder-capture]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Responder]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---

# Set-Up-NTLM-Capture-Server

## Summary

This procedure sets up a malicious server using Responder to capture NTLM authentication attempts, commonly used in SSRF attacks where a vulnerable server is forced to authenticate to the attacker's endpoint, leaking Windows credentials.

## Description

In the context of CVE-2024-40898, the SSRF in Apache mod_rewrite on Windows can be directed to an attacker-controlled server. When the target server attempts to access resources on the attacker's server (e.g., via HTTP or SMB), it may use NTLM authentication, allowing the attacker to capture the challenge-response hash. This hash can then be cracked offline or relayed to other services for unauthorized access to internal network resources. Prerequisites include a network interface accessible to the target and tools like Responder installed on the attacker's machine.

## Requirements

1. Attacker machine with network access (e.g., public IP or VPN to target's internal network).
2. Responder tool installed (Python-based, runs on Linux/Windows).
3. Knowledge of protocols that trigger NTLM (HTTP, SMB, etc.).
4. Firewall rules allowing inbound traffic on ports 80, 139, 445.

## Defense

Defensive measures and detection strategies:

- Disable NTLM authentication where possible; enforce Kerberos or modern auth.
- Monitor for unexpected outbound connections from web servers to external IPs.
- Use network segmentation to prevent web servers from accessing internal auth services.
- Deploy IDS/IPS rules to detect Responder-like traffic patterns (e.g., LLMNR poisoning).

## Objectives

1. Establish a listener to intercept NTLM auth attempts from the SSRF exploit.
2. Capture and log NTLMv2 hashes for post-exploitation.
3. Enable potential relay to internal SMB shares or services.

## Instructions

### Step 1: Install and Configure Responder

**Context**: Ensure Responder is ready to poison and capture NTLM traffic. This step prepares the tool for multi-protocol listening.

**Command** ([[commands/responder-capture]]):
```bash
python Responder.py -I eth0 -w -r -f -v
```

> This command starts Responder on interface eth0, enabling WPAD poisoning (-w), NBT-NS (-r), LLMNR (-f), and verbose output (-v). Replace eth0 with your interface (e.g., wlan0). Expected output includes logs like "[WPAD] Listening for WPAD requests" and port bindings.

### Step 2: Verify Listener and Wait for Traffic

**Context**: Confirm the server is listening and monitor for incoming connections from the target.

**Command** (No specific command; monitor logs):

> Tail the Responder logs in real-time using `tail -f Responder-Session.log`. Successful setup shows no binding errors. When SSRF triggers, expect entries like "[SMB] NTLMv2-SSP Client   : ::ffff:TARGET_IP" followed by the captured hash.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used

- [[commands/responder-capture]]

## Tools Used

- [[tools/Responder]]

## Tags

- ntlm
- capture
- responder
