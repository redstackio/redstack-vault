---
tags:
  - privilege-escalation
  - installation
  - macos
  - exploit
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/installer-run-pkg]]'
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:26.828Z'
sub_techniques: []
id: 8029f74f-fe3c-4175-83e2-a8681b9c74eb
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Achieve Privilege Escalation via Installer

## Summary

This procedure executes the Mozilla VPN installation on macOS, leveraging pre-placed symlinks to exploit a logic flaw and elevate privileges from unprivileged user to root.

## Description

The final stage of the attack runs the installer, which follows symlinks insecurely, allowing manipulation of root files. This bypasses protections and grants persistent root access. Requires symlinks in place and local access; outcomes include full system compromise.

## Requirements

1. Mozilla VPN .pkg file and symlinks prepared
2. Unprivileged user with ability to invoke sudo for installation
3. macOS target system

## Defense

Defensive measures and detection strategies:

- Validate installer integrity with hashes/signatures before running
- Use SIP (System Integrity Protection) to guard key paths
- Audit installation logs for symlink-related anomalies

## Objectives

1. Trigger symlink following during installation
2. Modify root files via redirection
3. Gain and verify root privileges

## Instructions

### Step 1: Initiate Installation

**Context**: Run the installer with logging to capture the exploitation process.

**Command** ([[commands/installer-run-pkg]]):
```bash
sudo installer -pkg MozillaVPN.pkg -target / -dumplog /tmp/vpn-install.log
```

> The sudo may prompt, but the flaw allows bypass. Expected output: Installation proceeds, log shows file operations redirected.

### Step 2: Verify Escalation

**Context**: Check for successful root modifications post-install.

**Command** ([[commands/cat-read-file]]):
```bash
cat /tmp/vpn-install.log | grep -i "symlink"
sudo -l
```

> Look for evidence of bypassed checks. If sudoers modified, passwordless sudo is available, indicating success.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/installer-run-pkg]]
- [[commands/cat-read-file]]

## Tools Used


## Tags

- [[privilege-escalation]]
- [[exploit]]
- [[installation]]
