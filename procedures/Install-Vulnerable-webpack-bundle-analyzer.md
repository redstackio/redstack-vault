---
tags:
  - xss
  - node.js
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-webpack-bundle-analyzer]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:36.981Z'
sub_techniques: []
id: 650d0977-7ebf-4037-bc0c-2a6bbf2a0561
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Install-Vulnerable-webpack-bundle-analyzer

## Summary

This procedure installs the vulnerable version (3.0.3) of the webpack-bundle-analyzer Node.js module, setting up the environment for XSS exploitation via unsanitized webpack stats input.

## Description

The webpack-bundle-analyzer is a tool for visualizing webpack bundle sizes. In version 3.0.3, it suffers from an XSS vulnerability due to lack of sanitization in the viewer.ejs template when rendering file and directory names from webpack stats JSON. This procedure uses npm to install the package, enabling subsequent steps to craft and analyze malicious stats files. The target environment is a Node.js developer setup, and the outcome is a local installation ready for analyzer execution, potentially leading to JavaScript execution in the browser.

## Requirements

1. Node.js and npm installed on the system
2. Write access to the current directory for node_modules
3. Internet access for package download

## Defense

Defensive measures and detection strategies:

- Pin package versions to fixed releases (e.g., >=3.3.2)
- Scan dependencies with tools like npm audit or Snyk for known vulnerabilities
- Monitor npm install logs for vulnerable package versions

## Objectives

1. Install webpack-bundle-analyzer@3.0.3 to replicate the vulnerable setup
2. Prepare environment for stats JSON analysis
3. Enable local server startup for XSS trigger

## Instructions

### Step 1: Execute npm Install

**Context**: Installs the vulnerable package globally or locally in the project.

**Command** ([[commands/npm-install-webpack-bundle-analyzer]]):
```bash
npm i webpack-bundle-analyzer
```

> This command fetches and installs webpack-bundle-analyzer version 3.0.3 (vulnerable) from the npm registry. Expected output includes installation progress and confirmation that the package is added to package.json and node_modules.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-webpack-bundle-analyzer]]

## Tools Used

- [[tools/npm]]

## Tags

- xss
- node.js
- installation
