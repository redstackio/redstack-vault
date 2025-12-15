---
tags:
  - setup
  - node-js
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-serve-here]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:11.900Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 021b760e-8a28-4f25-890a-3f988ef30b0c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-and-Setup-serve-here

## Summary

This procedure installs the vulnerable serve-here Node.js package version 3.2.0 and navigates to a test directory like /root, preparing the environment for demonstrating the directory traversal vulnerability in a controlled setup.

## Description

In an attack scenario, an adversary with local access to a Node.js environment installs the serve-here package to set up a static web server. The package's failure to sanitize URL paths allows traversal attacks. This step assumes a Linux host with Node.js and npm pre-installed. Expected outcome is a ready-to-use server environment from which files can be served, enabling subsequent exploitation.

## Requirements

1. Node.js and npm installed on the target Linux host
2. Shell access (e.g., root or sudo privileges for /root directory)
3. Internet access for package download from npm registry

## Defense

Defensive measures and detection strategies:

- Monitor npm installations for suspicious packages like serve-here in production environments
- Use application whitelisting to restrict Node.js package installations
- Log and alert on directory changes to sensitive paths like /root

## Objectives

1. Install serve-here@3.2.0 to enable vulnerable server setup
2. Position in a test directory to control the web root
3. Verify environment readiness without triggering alerts

## Instructions

### Step 1: Install serve-here Package

**Context**: Download and install the specific vulnerable version globally to make the 'here' command available.

**Command** ([[commands/npm-install-serve-here]]):
```bash
npm install -g serve-here@3.2.0
```

> This command fetches and installs serve-here version 3.2.0 from the npm registry. Expected output includes confirmation messages like "+ serve-here@3.2.0" and no errors.

### Step 2: Navigate to Test Directory

**Context**: Change to the /root directory to serve files from a known location, simulating a misconfigured server root.

**Command** ([[commands/cd-root]]):
```bash
cd /root
```

> This positions the shell in /root. Expected output is a prompt change to indicate the new directory, e.g., "root@host:/root#".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/npm-install-serve-here]]
- [[commands/cd-root]]

## Tools Used

- [[tools/npm]]

## Tags

- setup
- node-js
- installation
