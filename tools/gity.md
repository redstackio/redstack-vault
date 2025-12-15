---
url: 'https://www.npmjs.com/package/gity'
tags:
  - git-wrapper
  - vulnerable
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.666Z'
configuration: version 1.0.5
id: 72dab265-6760-4e0f-a293-19780539bb5d
validated: true
submitted: true
---
# gity

**Status**: Unverified

## Overview

gity is a Node.js wrapper for Git commands, vulnerable to RCE in version 1.0.5 due to unsanitized shell command formatting.

## Description

gity simplifies Git operations in JS apps but insecurely interpolates inputs into shell strings, enabling command injection. Used in exploitation to demonstrate supply chain risks in npm dependencies.

## Features

- Feature 1: Git init, add, commit, and run methods
- Feature 2: Promise-based async operations
- Feature 3: Direct shell command execution

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm i gity@1.0.5
```

## Basic Usage

```bash
# In JS: const gity = require('gity');
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Methods like .commit(message) |

## Examples

### Example 1: Basic Usage

```javascript
const git = require('gity')();
git.init();
```

### Example 2: Advanced Usage (Vulnerable)

```javascript
git.commit('-m "msg"; malicious command; #');
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- gity module loaded in Node.js processes
- Anomalous Git shell spawns with injected payloads
- Unexpected file artifacts from injections

## Related Procedures

- [[procedures/Exploit-gity-RCE-with-Injected-Commands]]

## Related Tools

- [[tools/Node-js]]

## References

- npm page: https://www.npmjs.com/package/gity
- HackerOne report: https://hackerone.com/reports/730111
