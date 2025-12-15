---
tags:
  - privilege-escalation
  - symlink-attack
  - homebrew
  - root
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - macOS
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Homebrew-Symlink-for-Root-Access]]'
step_count: 1
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:10.109Z'
description: >-
  A privilege escalation attack exploiting improper symlink handling in
  Homebrew's brew services command, allowing replacement of the opt prefix link
  to gain root access on macOS or Linux systems with Homebrew installed.
skill_level: intermediate
impact_level: high
id: 36272ce5-a665-48fd-b2c2-efcf2bb53333
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Homebrew Privilege Escalation via Symlink Replacement in Brew Services

Multi-stage attack chain demonstrating a complete attack workflow exploiting a vulnerability in Homebrew's brew services command.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Local Access] --> B[Privilege Escalation]
    B --> C[Root Access Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Homebrew (installed on target system)

### Target Environment

- macOS or Linux with Homebrew package manager
- Local user access to the system
- brew services command available

### Initial Access Requirements

- Valid local user account (non-root)
- Ability to create symlinks in Homebrew directories
- No prior root access needed

## Detailed Attack Procedures

### Step 1: Exploit Symlink Vulnerability
procedure: [[procedures/Exploit-Homebrew-Symlink-for-Root-Access]]

**Objective**: Replace the Homebrew opt prefix symlink by exploiting missing chown operations in brew services, leading to root privilege escalation.

**Instructions**: Identify writable paths in Homebrew's opt prefix, create a malicious symlink pointing to a controlled location, and trigger brew services to follow and chown it as root, allowing arbitrary code execution or file overwrite with elevated privileges.

First, locate the Homebrew prefix (typically /opt/homebrew on macOS or /home/linuxbrew/.linuxbrew on Linux) and check for unprotected symlinks:

```bash
brew --prefix
ls -la $(brew --prefix)
```

Then, create a symlink in a directory not properly chowned by brew services, pointing to a sensitive root-owned file or script:

```bash
ln -s /path/to/root/controlled/file /opt/homebrew/unprotected/symlink
brew services restart some-service
```

Monitor for the chown operation to elevate the symlink's ownership, then execute the linked payload.

**Expected Output**: Symlink ownership changed to root, allowing access to root resources or execution of malicious code.

**Success Indicators**:
- Symlink ownership updated to root:chown
- Ability to read/write root-owned files via the symlink
- Root shell or elevated command execution confirmed

## Attack Chain Summary

### Key Achievements

1. Successful replacement of Homebrew opt prefix symlink
2. Privilege escalation from local user to root
3. Potential for persistent root access via modified services

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
