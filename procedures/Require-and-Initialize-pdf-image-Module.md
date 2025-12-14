---
tags:
  - rce
  - node.js
  - setup
type: procedure
tools:
  - '[[tools/pdf-image-exploit-script]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:32.581Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 38b63a59-7144-462d-adea-63c75ab581ae
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Require-and-Initialize-pdf-image-Module

## Summary

This procedure loads the vulnerable pdf-image Node.js module, preparing the environment for exploitation by importing the PDFImage class that handles PDF to image conversion via ImageMagick shell commands.

## Description

In a Node.js application using the pdf-image module for processing PDFs, the module relies on child_process.exec to run ImageMagick commands. This step sets up the module in a controlled script to demonstrate the vulnerability. It assumes the attacker has access to modify or inject into the application's code or input handling. Prerequisites include Node.js installed and npm access.

## Requirements

1. Node.js environment (v8+ recommended for pdf-image compatibility)
2. npm package manager
3. ImageMagick installed on the host system for shell command execution

## Defense

Defensive measures and detection strategies:

- Audit dependencies for known vulnerabilities using tools like npm audit or Snyk
- Restrict shell command execution in Node.js apps with libraries like safe-exec
- Monitor for unexpected module loads in application logs

## Objectives

1. Load pdf-image to access the vulnerable PDFImage class
2. Verify module availability without errors
3. Prepare for input injection in subsequent steps

## Instructions

### Step 1: Install the Module

**Context**: Use npm to install the pdf-image package, ensuring it's available for requiring.

**Command** (npm install):
```bash
npm install pdf-image
```

> This command fetches and installs the module from npm. Expected output: Installation logs showing success, with node_modules/pdf-image directory created.

### Step 2: Require in Script

**Context**: In a JavaScript file, require the module to import PDFImage.

**Command** (Node.js require):
```javascript
const PDFImage = require("pdf-image").PDFImage;
console.log("Module loaded successfully");
```

> Run with `node script.js`. Expected output: "Module loaded successfully" printed to console, confirming import.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/pdf-image-exploit-script]]

## Tags

- rce
- node.js
