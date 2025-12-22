---
tags:
  - installation
  - node.js
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-takeapeek]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Execution through Module Load]]'
updated_at: '2025-12-14T00:11:16.256Z'
sub_techniques: []
id: ec4049fd-3695-4e45-9872-50c2589c5987
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Execution through Module Load]]'
---
# Install-takeapeek-Module

## Summary

This procedure installs the vulnerable takeapeek Node.js module globally using npm, enabling the use of its static web server for demonstrating the XSS vulnerability in directory listings.

## Description

The takeapeek module (version 0.2.2) is a simple Node.js static file server that includes directory listing functionality. Installing it globally allows execution as a command-line tool. This step is the prerequisite for setting up the environment to exploit the unsanitized filename handling that leads to stored XSS. The attack scenario involves local simulation of a server that could be accessed by multiple users, where an attacker uploads or creates files with malicious names.

## Requirements

1. Node.js and npm installed on a Linux system
2. Internet access for downloading the package
3. Administrative privileges for global installation

## Defense

Defensive measures and detection strategies:

- Monitor npm installations for known vulnerable packages using tools like npm audit
- Restrict global installations in production environments
- Use vulnerability scanners like Snyk to detect outdated modules

## Objectives

1. Prepare the vulnerable server component
2. Enable directory listing exploitation
3. Set up for payload injection

## Instructions

### Step 1: Install Globally

**Context**: Use npm to fetch and install takeapeek from the registry, making it available system-wide.

**Command** ([[commands/npm-install-takeapeek]]):
```bash
npm install -g takeapeek
```

> This command downloads and installs version 0.2.2 (vulnerable) globally. Expected output includes progress bars and confirmation messages from npm.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Execution through Module Load]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-takeapeek]]

## Tools Used

- [[tools/npm]]

## Tags

- installation
- node.js
