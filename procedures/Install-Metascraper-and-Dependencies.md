---
id: proc-install-metascraper
tags:
  - npm
  - dependency-install
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/npm-install-metascraper-deps]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Time Discovery]]'
updated_at: '2025-12-14T03:16:20.507Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[System Time Discovery]]'
---
# Install-Metascraper-and-Dependencies

## Summary

This procedure installs the vulnerable metascraper library along with got (HTTP client) and express (web framework) in a Node.js project to set up the exploitation environment.

## Description

As the legitimate developer, install packages via npm to demonstrate how metascraper is integrated. This creates a vulnerable app that scrapes without sanitization. Prerequisites: Node.js and npm installed; run in an empty directory with package.json initialized (npm init -y).

## Requirements

1. Node.js (v12+) and npm installed
2. Empty project directory
3. Internet access for package download

## Defense

Defensive measures and detection strategies:

- Audit third-party dependencies for XSS vulnerabilities using tools like npm audit
- Pin versions and review changelogs for security fixes
- Implement input validation wrappers around library outputs

## Objectives

1. Add metascraper for metadata extraction
2. Include got for HTTP requests and express for serving
3. Confirm installation without errors

## Instructions

### Step 1: Initialize Project and Install Packages

**Context**: Set up the Node.js project and install dependencies.

**Command** ([[commands/npm-install-metascraper-deps]]):
```bash
npm init -y
npm install metascraper got express
```

> Initializes package.json and downloads packages to node_modules. Expected output: Installation logs ending with 'added X packages'.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[System Time Discovery]] System Binary Proxy Execution (adapted for npm install)

### Sub-Techniques


## Commands Used

- [[commands/npm-install-metascraper-deps]]

## Tools Used

- [[tools/npm]]

## Tags

- [[tools/npm]]
- [[dependency-install]]
