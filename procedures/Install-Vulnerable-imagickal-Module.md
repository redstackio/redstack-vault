---
id: proc-uuid-1
tags:
  - rce
  - nodejs
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-imagickal]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:19.203Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Install-Vulnerable-imagickal-Module

## Summary

This procedure installs the vulnerable imagickal Node.js module (version 4.2.0) from the npm registry, setting up the environment to exploit a command injection vulnerability in its ImageMagick wrapper functions.

## Description

The imagickal module is a Node.js wrapper for ImageMagick commands. Version 4.2.0 contains a vulnerability where user-supplied filenames in functions like im.identify() are passed unsanitized to ImageMagick, allowing shell metacharacters to inject arbitrary commands. This procedure uses npm to install the specific vulnerable version, enabling subsequent exploitation for remote code execution on the host system running the Node.js application.

## Requirements

1. Node.js and npm installed on the target environment
2. Internet access to the npm registry
3. Local write permissions in the project directory

## Defense

Defensive measures and detection strategies:

- Pin package versions to secure releases and audit dependencies with tools like npm audit
- Use containerization (e.g., Docker) to isolate Node.js applications and limit shell access
- Monitor npm installations for known vulnerable packages using vulnerability scanners like Snyk

## Objectives

1. Install the imagickal module to gain access to the vulnerable im.identify() function
2. Prepare the runtime environment for command injection testing
3. Enable arbitrary command execution via ImageMagick integration

## Instructions

### Step 1: Install the Package

**Context**: Fetch and install imagickal version 4.2.0 using npm to introduce the vulnerability into the Node.js project.

**Command** ([[commands/npm-install-imagickal]]):
```bash
npm i imagickal@4.2.0
```

> This command downloads the package and its dependencies, logging the installation process. Expected output includes confirmation messages like "added 1 package" and updates to package.json.

### Step 2: Verify Installation

**Context**: Confirm the module is available for require() in JavaScript code.

**Command** (node -e "console.log(require('imagickal'))"):
```bash
node -e "console.log(require('imagickal'))"
```

> Outputs the module object if successfully installed, indicating readiness for exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- None

## Commands Used

- [[commands/npm-install-imagickal]]

## Tools Used

- [[tools/npm]]

## Tags

- rce
- nodejs
- installation
