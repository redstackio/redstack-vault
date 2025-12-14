---
id: 123e4567-e89b-12d3-a456-426614174003
name: Install-Vulnerable-meta-git-Module
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.204Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploitation for Client Execution]]'
sub_techniques: []
tags:
  - installation
  - vulnerable-module
  - npm
commands:
  - '[[commands/install-meta-git-global]]'
platforms:
  - Linux
  - Node.js
tools:
  - '[[tools/npm]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---

# Install-Vulnerable-meta-git-Module

## Summary

This procedure installs the vulnerable meta-git module version 1.1.2 globally using npm, preparing the environment for RCE exploitation through the insecure git clone command.

## Description

The meta-git module, a Node.js plugin for git operations in the meta framework, contains an RCE flaw in its clone functionality. Installing it globally allows execution of the vulnerable 'meta-git clone' command, where user input is unsanitized and interpolated into shell commands.

## Requirements

1. Node.js and npm installed on the system
2. Internet connectivity for package download
3. Global installation permissions (sudo if needed)

## Defense

Defensive measures and detection strategies:

- Pin package versions to secure releases and audit dependencies with tools like npm audit
- Monitor npm installations for known vulnerable packages using vulnerability scanners

## Objectives

1. Deploy the vulnerable module for testing
2. Ensure version 1.1.2 is used to replicate the flaw
3. Prepare for command injection exploitation

## Instructions

### Step 1: Global Installation

**Context**: Installs meta-git globally to make the clone command available system-wide.

**Command** ([[commands/install-meta-git-global]]):
```bash
npm i meta-git -g
```

> Installs the latest available version (1.1.2 at time of vulnerability). Expected output: Installation logs ending with 'added X packages'.

### Step 2: Verify Installation

**Context**: Confirm the module is installed and accessible.

**Command** (npm list):
```bash
npm list -g meta-git
```

> Lists installed version; expected output: meta-git@1.1.2.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/install-meta-git-global]]

## Tools Used

- [[tools/npm]]

## Tags

- [[installation]]
- [[vulnerable-module]]
- [[tools/npm]]
