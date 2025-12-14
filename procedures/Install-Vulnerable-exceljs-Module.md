---
tags:
  - xss
  - node-js
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
  - '[[tools/exceljs]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-exceljs]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:46.855Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: bb479beb-2cec-47a6-9f4f-ad0bb0f721fb
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Install-Vulnerable-exceljs-Module

## Summary

This procedure installs the vulnerable version of the exceljs Node.js module, which fails to escape or validate cell values from XLSX files, enabling stored XSS when content is rendered in HTML.

## Description

In the context of demonstrating a stored XSS vulnerability, this step sets up the project by installing exceljs version 1.4.6 using npm. This module is used to parse XLSX files, but without proper sanitization, it allows HTML and JavaScript payloads to pass through unchanged. Prerequisites include a Node.js environment and npm. Expected outcome: The module is ready for use in a vulnerable application.

## Requirements

1. Node.js runtime installed (version 8.11.1 or later)
2. npm package manager available
3. Local project directory initialized (e.g., via `npm init`)

## Defense

Defensive measures and detection strategies:

- Use package vulnerability scanners like npm audit to detect outdated or vulnerable dependencies
- Enforce semantic versioning and update to patched versions (e.g., exceljs 1.6.0+ with .html property for safe rendering)
- Monitor npm install logs for installation of known vulnerable packages

## Objectives

1. Install exceljs to enable XLSX parsing in Node.js applications
2. Prepare environment for vulnerability demonstration
3. Verify installation for subsequent exploitation steps

## Instructions

### Step 1: Initialize Project and Install

**Context**: Set up a new Node.js project and install the vulnerable exceljs module.

**Command** ([[commands/npm-install-exceljs]]):
```bash
npm i exceljs
```

> This command installs exceljs version 1.4.6 (vulnerable to XSS). Expected output includes installation logs and package.json update confirming the dependency.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-exceljs]]

## Tools Used

- [[tools/npm]]
- [[tools/exceljs]]

## Tags

- xss
- node-js
- installation
