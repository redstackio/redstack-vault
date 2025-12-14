---
id: proc-003
tags:
  - setup
  - webpack
  - degit
type: procedure
tools:
  - '[[tools/npx]]'
  - '[[tools/degit]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npx-degit-webpack-example]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:11.574Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Obtain-Webpack-Sapper-Example

## Summary

This procedure uses degit to shallow clone the Webpack-specific branch of the Sapper template, setting up the exact stack vulnerable to path traversal in static file serving.

## Description

The Webpack integration in Sapper builds static assets in a directory that lacks path validation, enabling '../' traversal. This step targets the #webpack branch for precise reproduction.

## Requirements

1. Installed dependencies from previous steps
2. npx and degit available via NPM
3. Current directory with write access

## Defense

Defensive measures and detection strategies:

- Restrict shallow clones in build scripts
- Audit template sources for vulnerabilities

## Objectives

1. Acquire Webpack-integrated Sapper files
2. Create isolated 'my-app' directory
3. Align environment with vulnerable configuration

## Instructions

### Step 1: Shallow Clone Webpack Branch

**Context**: Use degit for efficient cloning of the specific example.

**Command** ([[commands/npx-degit-webpack-example]]):
```bash
npx degit "sveltejs/sapper-template#webpack" my-app
```

> This creates 'my-app' with Webpack files. Expected output: Cloning progress and directory creation confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/npx-degit-webpack-example]]

## Tools Used

- [[tools/npx]]
- [[tools/degit]]

## Tags

- [[setup]]
- [[webpack]]
- [[tools/degit]]

---
