---
tags:
  - setup
  - undici
  - vulnerable-install
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/npm-install-undici-vulnerable]]'
platforms:
  - Node.js
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f4c02973-d1a9-4da5-bf59-289581c96de8
created_at: '2025-12-14T17:26:36.608Z'
updated_at: '2025-12-14T17:26:36.608Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Install-Vulnerable-Undici-Version

## Summary

This procedure installs the vulnerable version (5.13) of the undici library using npm, setting up a Node.js environment to reproduce the ReDoS vulnerability in the Headers class.

## Description

Undici is an HTTP/1.1 client for Node.js, and version 5.13 contains an inefficient regex in headerValueNormalize() that enables ReDoS. This step prepares the environment by installing the specific vulnerable package, allowing subsequent exploitation of header processing. It targets local Node.js projects where undici might be used for fetch operations with untrusted inputs.

## Requirements

1. Node.js installed (version 14+ recommended for undici compatibility)
2. npm package manager available
3. Local project directory initialized with package.json (run `npm init -y` if needed)

## Defense

Defensive measures and detection strategies:

- Use dependency scanners like npm audit or Snyk to detect vulnerable undici versions
- Pin undici to patched versions (e.g., >=5.14.0) in package.json
- Monitor for unexpected package installations in CI/CD pipelines

## Objectives

1. Establish a reproducible environment with the flawed library
2. Enable testing of Headers.set() and append() methods
3. Prepare for DoS impact demonstration

## Instructions

### Step 1: Initialize Project if Needed

**Context**: Ensure a Node.js project exists to install packages.

**Command** ([[commands/npm-init]]):
```bash
npm init -y
```

> Creates package.json. Expected output: Basic package.json file generated.

### Step 2: Install Vulnerable Undici

**Context**: Install undici@5.13 to include the ReDoS-vulnerable Headers implementation.

**Command** ([[commands/npm-install-undici-vulnerable]]):
```bash
npm install undici@5.13
```

> Installs the package. Expected output: Logs showing download and addition to node_modules/package.json.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-undici-vulnerable]]

## Tools Used

- [[tools/npm]]

## Tags

- setup
- undici
