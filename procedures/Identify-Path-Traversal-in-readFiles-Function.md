---
tags:
  - path-traversal
  - vulnerability-identification
  - node-js
type: procedure
tools:
  - '[[tools/fs-Node.js-Module]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:12.553Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 19192f02-8f8a-49f2-a50b-c48897812ccf
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Identify-Path-Traversal-in-readFiles-Function

## Summary

This procedure details the analysis of the readFiles function in saveContracts.js to confirm a path traversal vulnerability arising from unsanitized filename concatenation in Node.js fs operations.

## Description

The readFiles function uses fs.readdir to list files from 'build/contracts/' and then fs.readFile with a path constructed as dirname + '/' + filename, without validating or sanitizing the filename. This allows attackers to use traversal sequences like '../../../../etc/passwd' to access files outside the intended directory, such as sensitive OS files. In a code review context, this identification highlights the risk of arbitrary file disclosure on the server running the script. Prerequisites include the cloned repository; expected outcomes are a clear understanding of the root cause and potential impact on server security.

## Requirements

1. Cloned Sifnode repository
2. Knowledge of Node.js path resolution
3. Ability to simulate path joining mentally or with a Node.js REPL

## Defense

Defensive measures and detection strategies:

- Sanitize filenames using path.basename or path.resolve with allowlists
- Use chroot or containerization to limit file system access

## Objectives

1. Confirm lack of sanitization in filename handling
2. Map traversal impact to arbitrary file reads
3. Recommend fixes like path validation

## Instructions

### Step 1: Analyze fs.readdir Usage

**Context**: Understand how files are listed from the target directory.

Review the code:

```javascript
const fs = require('fs');
// ...
readFiles('build/contracts/', (err, files) => { ... });
```

> fs.readdir reads all filenames in 'build/contracts/'. Expected output: List of filenames passed to callback without filtering.

### Step 2: Examine fs.readFile Concatenation

**Context**: Identify the insecure path construction.

Look for:

```javascript
fs.readFile(dirname + '/' + filename, 'utf8', (err, data) => { ... });
```

> No sanitization allows '../' sequences to traverse up directories. Expected output: Path resolves to arbitrary locations like '/etc/passwd'.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/fs-Node.js-Module]]

## Tags

- path-traversal
- vulnerability-identification
