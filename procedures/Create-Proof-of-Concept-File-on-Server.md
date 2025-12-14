---
tags:
  - persistence
  - file-write
  - poc
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:23:54.955Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 9c992a7f-7a7c-4bf1-920f-b99fc9b48279
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[Hijack Execution Flow]]'
---
# Create-Proof-of-Concept-File-on-Server

## Summary

This procedure writes a simple file to the server's public directory via the reverse shell, demonstrating file system write access and serving as evidence of compromise.

## Description

Using the shell, echo content to a file in /public/, making it web-accessible. In the report, 'hackerone.txt' with 'PoC by michiel' was created, intermittently visible due to load balancing. This proves RCE impact.

## Requirements

1. Active shell with write permissions
2. Knowledge of web root (e.g., /var/www/app/public)

## Defense

Defensive measures and detection strategies:

- File integrity monitoring (e.g., Tripwire) on web directories
- Log file creations in /public/ and alert on anomalies
- Use containerization to limit file system access

## Objectives

1. Demonstrate write capability
2. Create verifiable PoC
3. Highlight persistence potential

## Instructions

### Step 1: Navigate to Public Directory

**Context**: Change to writable web dir.

```bash
cd /path/to/app/public
```

### Step 2: Write the PoC File

**Context**: Create and populate the file.

```bash
echo "PoC by michiel" > hackerone.txt
```

> Expected output: File created, size 12 bytes.

### Step 3: Verify Accessibility

**Context**: Check via HTTP.

From browser: http://facebooksearch.algolia.com/hackerone.txt

> Expected output: File content displayed (may vary by server in cluster).

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation (or TA0005 Defense Evasion for PoC)

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Hijack Execution Flow]] Hijack Execution Flow (file write for persistence)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- poc
- file-write
- rails
