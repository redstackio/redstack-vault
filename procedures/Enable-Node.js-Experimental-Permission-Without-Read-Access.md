---
id: proc-nodejs-enable-permission-no-read
tags:
  - nodejs
  - setup
  - permissions
type: procedure
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/run-node-with-experimental-permission]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:51.840Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Enable-Node.js-Experimental-Permission-Without-Read-Access

## Summary

This procedure sets up a Node.js environment with the experimental permission system enabled but intentionally omits read access to a target file, creating conditions for demonstrating permission bypass vulnerabilities.

## Description

The experimental permission system in Node.js (--experimental-permission flag) is designed to restrict file system operations, but certain functions like fs.openAsBlob() fail to enforce these checks. This procedure launches Node.js in restricted mode without granting read permissions to 'file.txt', allowing subsequent steps to exploit the bypass. It targets local Node.js runtimes and requires shell access to execute the startup command. Expected outcome: Node.js runs with permissions active but vulnerable to bypass attempts.

## Requirements

1. Node.js installed (version supporting --experimental-permission, e.g., v20+ experimental)
2. A target file (e.g., file.txt) present in the script directory
3. Shell access to run Node.js commands

## Defense

Defensive measures and detection strategies:

- Patch Node.js to the latest version to fix permission check gaps
- Monitor Node.js process flags for --experimental-permission usage in production
- Implement file system auditing to detect unauthorized reads

## Objectives

1. Establish a permission-restricted Node.js runtime
2. Ensure no explicit read access is granted to target files
3. Prepare environment for vulnerability exploitation

## Instructions

### Step 1: Prepare the Script and File

**Context**: Create a basic script.js and a target file.txt to test against.

No command needed; manually create:
- file.txt with sample content (e.g., "secret data")
- script.js containing the exploit code (detailed in next procedure)

### Step 2: Launch Node.js in Restricted Mode

**Context**: Start Node.js with the experimental permission flag, omitting any --allow-fs-read permissions for the target file.

**Command** ([[commands/run-node-with-experimental-permission]]):
```bash
node --experimental-permission script.js
```

> This command enables the permission system without read grants. Expected output: Script runs without immediate permission errors, proceeding to file operations.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/run-node-with-experimental-permission]]

## Tools Used

- [[tools/Node.js]]

## Tags

- nodejs
- permissions
- setup
