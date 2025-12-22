---
tags:
  - setup
  - file-creation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/echo-create-index-html]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:11.738Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3adbc677-fa8a-4c25-b012-ec859dc81ca1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Index-HTML-File

## Summary

This procedure creates a basic index.html file necessary for the angular-http-server to start without errors, simulating a minimal Angular app directory.

## Description

The server expects an index.html in the root directory to serve content. This step uses a simple echo command to generate it on a Linux system. The procedure is part of setting up the vulnerable environment and has no direct security impact but is required for reproduction.

## Requirements

1. Shell access with write permissions
2. Basic text editor or echo command available

## Defense

Defensive measures and detection strategies:

- Ensure web servers validate required files before startup
- Monitor for unexpected file creations in server directories

## Objectives

1. Provide the minimal file structure for server initialization
2. Avoid startup errors due to missing index
3. Prepare for serving and exploitation testing

## Instructions

### Step 1: Generate the File

**Context**: Echo simple content to create index.html.

**Command** ([[commands/echo-create-index-html]]):
```bash
echo "hi" > index.html
```

> This redirects the string "hi" to index.html. Expected output is silent success; verify with ls or cat index.html.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/echo-create-index-html]]

## Tools Used


## Tags

- setup
- file-creation
