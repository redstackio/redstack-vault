---
tags:
  - reverse-shell
  - reconnaissance
  - file-system-access
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/whoami-shell]]'
  - '[[commands/ls-directory]]'
  - '[[commands/cat-readme-md]]'
verified: false
platforms:
  - Linux
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:24:15.394Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: 59941d2f-1b80-49c4-b594-8edc7b6d538f
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Interact-with-Reverse-Shell

## Summary

Interact with the established reverse shell to perform reconnaissance on the compromised EC2 instance, exploring the file system and confirming internal infrastructure.

## Description

Once the shell connects via netcat, execute commands to identify the user, list directories, and read key files like README.md, revealing Shopify's Kit CRM repository details. This confirms control over the 'deploy' user on the Rails app server.

## Requirements

1. Active reverse shell from previous steps
2. Netcat session open
3. Basic Linux command knowledge

## Defense

Defensive measures and detection strategies:

- Monitor for outbound connections on non-standard ports (e.g., 8080)
- Implement host-based IDS for shell activity
- Restrict metadata access from app processes
- Audit file access logs

## Objectives

1. Verify shell access and user context
2. Explore file system for sensitive data
3. Confirm target infrastructure

## Instructions

### Step 1: Identify Current User

**Context**: Determine the running user for privilege assessment.

**Command** ([[commands/whoami-shell]]):
```bash
whoami
```

> Returns 'deploy', indicating app deployment user.

### Step 2: List Directory Contents

**Context**: Scan for application files.

**Command** ([[commands/ls-directory]]):
```bash
ls
```

> Lists Rails structure: app, bin, config, etc.

### Step 3: Read README File

**Context**: Confirm internal repo.

**Command** ([[commands/cat-readme-md]]):
```bash
cat README.md
```

> Displays Shopify Kit CRM details, CI info, deployment notes.

**Expected Output**: Infrastructure confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/whoami-shell]]
- [[commands/ls-directory]]
- [[commands/cat-readme-md]]

## Tools Used

- [[tools/netcat]]

## Tags

- reverse-shell
- reconnaissance
- file-system-access
