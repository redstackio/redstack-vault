---
id: ac-putty-pscp-rce-2016
tags:
  - putty
  - ssh
  - buffer-overflow
  - rce
  - dos
  - client-side
type: attack_chain
tools:
  - '[[tools/poc-py]]'
  - '[[tools/PuTTY-PSCP]]'
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Malicious-SSH-PoC-Server]]'
  - '[[procedures/Connect-Vulnerable-PuTTY-PSCP-Client]]'
  - '[[procedures/Trigger-Stack-Buffer-Overflow-for-RCE]]'
step_count: 3
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Process Injection]]'
updated_at: '2025-12-14T17:30:58.712Z'
description: >-
  Multi-stage client-side attack exploiting a stack buffer overflow in PuTTY
  PSCP during SSH file transfer to achieve remote code execution, with
  additional DoS vectors via malformed SSH packets.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Process Injection]]'
---
# PuTTY PSCP Client Stack Buffer Overflow for Remote Code Execution

Multi-stage attack chain demonstrating client-side exploitation of a stack buffer overflow in PuTTY's PSCP during post-authentication file size processing, leading to remote code execution on vulnerable Windows clients (PuTTY <= 0.66). The attack requires the victim to connect to a malicious SSH server, triggering memory corruption via crafted responses. Additional DoS conditions can be induced through malformed SSH string parsing and unrequested channel requests.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Up Malicious SSH Server] --> B[Victim Connects with Vulnerable PuTTY PSCP]
    B --> C[Trigger Buffer Overflow During File Transfer]
    C --> D[Remote Code Execution on Client]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/poc-py]]
- [[tools/PuTTY-PSCP]]

### Target Environment

- Target OS/Platform: Windows with PuTTY PSCP <= 0.66 installed
- Required services/ports: SSH on port 22 (malicious server side)
- Network access requirements: Attacker controls an SSH server; victim must initiate connection to it

### Initial Access Requirements

- Credential requirements: Valid SSH credentials for authentication (post-auth vuln)
- Network position: Attacker hosts malicious server; victim connects outbound
- Prior access needed: None, relies on social engineering or phishing to lure victim connection

## Detailed Attack Procedures

### Step 1: Set Up Malicious SSH Server
procedure: [[procedures/Set-Up-Malicious-SSH-PoC-Server]]

**Objective**: Deploy a Python-based SSH server that serves crafted responses to exploit PuTTY's file size parsing.

**Instructions**: Download and run the PoC script to start the malicious server listening on port 22.

Execute [[commands/run-poc-server]] to launch the server:

```bash
python poc.py
```

**Expected Output**: Server starts and listens for incoming SSH connections, ready to send malicious payloads.

**Success Indicators**:
- Server output confirms listening on port 22
- No errors in script execution

### Step 2: Connect Vulnerable PuTTY PSCP Client
procedure: [[procedures/Connect-Vulnerable-PuTTY-PSCP-Client]]

**Objective**: Authenticate and initiate file transfer from the victim's side using vulnerable PuTTY PSCP to reach post-auth processing.

**Instructions**: On the target Windows machine, use PSCP to connect to the attacker's server and start a file transfer session.

Execute [[commands/pscp-connect-transfer]]:

```bash
pscp -scp user:pass@attacker-ip:/remote/file localfile
```

Replace `user:pass` with valid credentials and `attacker-ip` with the server's IP.

**Expected Output**: Authentication succeeds, and file transfer begins, entering post-auth file size processing.

**Success Indicators**:
- Connection established without errors
- File transfer initiation logged

### Step 3: Trigger Stack Buffer Overflow for RCE
procedure: [[procedures/Trigger-Stack-Buffer-Overflow-for-RCE]]

**Objective**: Send crafted file size data from the server to overwrite the client's stack buffer, controlling EIP for code execution.

**Instructions**: The PoC server automatically responds with oversized file size values upon transfer request, causing the overflow.

Monitor the server logs during the transfer initiated in Step 2. The server sends a payload like a large string (e.g., 1000+ 'A's) in the file size field.

No additional client command needed; the vuln triggers automatically.

**Expected Output**: Client crashes or executes controlled code (EIP overwritten, e.g., to 0x41414141); server logs confirm payload sent and corruption.

**Success Indicators**:
- Client process memory corruption observed (e.g., via debugger)
- EIP overwrite confirmed in crash dump
- Potential shell or payload execution on client

## Attack Chain Summary

### Key Achievements

1. Established malicious SSH server to lure and exploit connecting clients
2. Achieved post-authentication stack buffer overwrite in PuTTY PSCP file handling
3. Demonstrated remote code execution via controlled EIP overwrite, with optional DoS extensions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Process Injection]] Process Injection (via buffer overflow leading to code exec)

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
