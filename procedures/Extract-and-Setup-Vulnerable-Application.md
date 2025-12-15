---
tags:
  - setup
  - node.js
  - undici
type: procedure
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-version-check]]'
  - '[[commands/npm-install]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.235Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d4dcb813-85eb-457f-a2b5-e772210066a8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-and-Setup-Vulnerable-Application

## Summary

This procedure extracts the provided report archive and sets up the vulnerable Node.js application environment, including dependency installation, to prepare for demonstrating the undici multipart boundary predictability vulnerability.

## Description

The setup involves unpacking report.tar.xz, which contains server.js (Express app using undici for multipart requests), order.php (PHP backend for processing orders), and exp.js (exploit script). Verifying Node.js version ensures compatibility with V8's Math.random() implementation. Installing dependencies like express and undici replicates the environment where boundaries are generated predictably. This is a prerequisite for observing and exploiting the LCG-based randomness in multipart/form-data requests sent to the backend API.

## Requirements

1. Access to report.tar.xz archive
2. Node.js v22.12.0 installed
3. Local file system permissions for extraction and installation

## Defense

Defensive measures and detection strategies:

- Use containerized environments to isolate setup
- Monitor for unexpected archive extractions or npm installs in production logs
- Enforce dependency scanning for known vulnerabilities in libraries like undici

## Objectives

1. Prepare the vulnerable application code and dependencies
2. Verify runtime compatibility for the exploit
3. Establish baseline environment for boundary observation

## Instructions

### Step 1: Extract Archive

**Context**: Unpack the report archive to access the vulnerable files.

**Command** ([[commands/tar-extract]]):
```bash
tar -xf report.tar.xz
```

> Extracts server.js, order.php, and exp.js. Expected output: Files created in current directory without errors.

### Step 2: Verify Node.js Version

**Context**: Confirm Node.js version to ensure V8 Math.random() predictability.

**Command** ([[commands/node-version-check]]):
```bash
node --version
```

> Checks version. Expected output: v22.12.0.

### Step 3: Install Dependencies

**Context**: Install Node.js packages required for the server.

**Command** ([[commands/npm-install]]):
```bash
npm install
```

> Installs express and undici. Expected output: Installation logs showing packages added to node_modules.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/node-version-check]]
- [[commands/npm-install]]

## Tools Used

- [[tools/npm]]
- [[tools/node]]

## Tags

- setup
- extraction
- dependencies
