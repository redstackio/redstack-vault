---
tags:
  - node-js
  - setup
  - cve-2025-27210
type: procedure
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/node-version-check]]'
verified: false
platforms:
  - Windows
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:22.272Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 4512a2df-0ec0-41a1-9836-fb3b14d22de0
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Setup-Node.js-Environment-with-Fix

## Summary

This procedure sets up a Node.js environment on Windows with version v24.4.1 or later, which includes the CVE-2025-27210 patch for path traversal in local paths, to test the remaining vulnerability in UNC paths.

## Description

The CVE-2025-27210 fix normalizes paths by prefixing device names (e.g., CON) with '.\\' to prevent traversal in regular Windows paths. However, this procedure prepares the environment to demonstrate that UNC paths (starting with '\\\\') handle device names differently, stripping them without the prefix and allowing traversal sequences like '../' to escape the share root. This is critical for testing file access in network shares used by Node.js applications like file upload handlers.

## Requirements

1. Windows operating system with administrative access for Node.js installation
2. Internet access to download Node.js if not pre-installed
3. Basic command-line proficiency

## Defense

Defensive measures and detection strategies:

- Use input validation to reject device names (CON, PRN, AUX) in user-supplied paths
- Implement allowlisting for permitted path segments in UNC joins
- Monitor Node.js logs for suspicious path resolutions involving UNC shares

## Objectives

1. Confirm Node.js version includes the partial fix
2. Ensure path module is functional for Windows (win32)
3. Prepare for vulnerability reproduction without local path interference

## Instructions

### Step 1: Install or Verify Node.js Version

**Context**: Check if Node.js v24.4.1+ is installed; if not, download and install from official sources to include the CVE fix.

**Command** ([[commands/node-version-check]]):
```bash
node --version
```

> This command outputs the Node.js version. If below v24.4.1, install via https://nodejs.org. Expected output: v24.4.1 or higher.

### Step 2: Test Path Module Access

**Context**: Verify the path module loads correctly on Windows, using win32 variant for UNC handling.

**Command** ([[commands/node-require-path]]):
```javascript
const path = require('path'); console.log(path.win32 ? 'Win32 path ready' : 'Non-Windows');
```

> Run with `node -e` or in a script. Expected output: 'Win32 path ready', confirming environment setup.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/node-version-check]]
- [[commands/node-require-path]]

## Tools Used

- [[tools/Node.js]]

## Tags

- node-js
- setup
- windows
