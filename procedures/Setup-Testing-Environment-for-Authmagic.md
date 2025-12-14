---
id: proc-736522-setup-env
tags:
  - setup
  - environment
  - poc
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/create-poc-directory]]'
  - '[[commands/change-to-poc-directory]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:10.862Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Testing-Environment-for-Authmagic

## Summary

This procedure creates an isolated directory for testing the authmagic vulnerability, preventing conflicts with existing projects and ensuring a clean setup for reproducing the JWT forgery attack.

## Description

In a Node.js environment, setting up a dedicated proof-of-concept (PoC) directory is essential to install the vulnerable authmagic-timerange-stateless-core module without interfering with global or other local npm projects. This step simulates a development setup similar to a production deployment using the authmagic example app, allowing safe reproduction of the improper authentication vulnerability in core.js where JWT access tokens are not properly validated during reissuance.

## Requirements

1. Node.js and npm installed on the system
2. Bash-compatible shell (Linux/macOS or Git Bash on Windows)
3. Write permissions in the current working directory

## Defense

Defensive measures and detection strategies:

- Use containerization (e.g., Docker) to isolate PoC environments
- Monitor npm install logs for suspicious package versions like authmagic-timerange-stateless-core@0.0.9
- Enforce project naming conventions to avoid self-dependency issues

## Objectives

1. Create an isolated testing space
2. Prepare for dependency installation
3. Ensure reproducibility of the attack

## Instructions

### Step 1: Create PoC Directory

**Context**: Establishes a new directory to contain all test files and dependencies.

**Command** ([[commands/create-poc-directory]]):
```bash
mkdir poc
```

> This command creates a folder named 'poc'. Expected output: No output if successful; error if directory exists.

### Step 2: Navigate to Directory

**Context**: Changes the working directory to the new PoC folder for subsequent operations.

**Command** ([[commands/change-to-poc-directory]]):
```bash
cd poc/
```

> This switches to the 'poc' directory. Expected output: Shell prompt updates to reflect the new path.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/create-poc-directory]]
- [[commands/change-to-poc-directory]]

## Tools Used


## Tags

- setup
- environment
- poc
