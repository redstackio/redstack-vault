---
id: proc-uuid-1
tags:
  - setup
  - node-js
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-html-pages]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T03:16:02.826Z'
skill_level: beginner
impact_level: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Install-html-pages-Module

## Summary

This procedure installs the vulnerable html-pages Node.js module using npm, setting up the environment for exploiting the stored XSS vulnerability in directory listings.

## Description

The html-pages module is a simple HTTP server for development, but version 2.1.1 fails to sanitize directory names when generating HTML listings. Installing it locally allows creation of malicious directories that inject JavaScript payloads. This step is prerequisite for server startup and payload injection, targeting local Node.js environments.

## Requirements

1. Node.js and npm installed on the system
2. Internet access for package download
3. Write permissions in the working directory

## Defense

Defensive measures and detection strategies:

- Use package vulnerability scanners like npm audit before installation
- Avoid using unmaintained modules like html-pages in production
- Monitor npm install logs for suspicious packages

## Objectives

1. Prepare the vulnerable module for exploitation
2. Establish a local server environment
3. Enable subsequent steps for XSS injection

## Instructions

### Step 1: Install the Module

**Context**: Download and install html-pages from npm registry to the current directory.

**Command** ([[commands/npm-install-html-pages]]):
```bash
npm install html-pages
```

> This command fetches html-pages v2.1.1 (vulnerable version) and creates node_modules. Expected output includes installation progress and confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used

- [[commands/npm-install-html-pages]]

## Tools Used

- [[tools/npm]]

## Tags

- setup
- node-js
