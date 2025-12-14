---
id: tool-child-process-exec
url: >-
  https://nodejs.org/api/child_process.html#child_process_child_process_exec_command_options_callback
tags:
  - node-js
  - execution
  - rce
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.621Z'
validated: true
submitted: true
---
# child_process-exec

**Status**: Unverified

## Overview

child_process.exec() is a built-in Node.js function for executing shell commands asynchronously, returning output via a callback. Its insecure usage in modules like create-git allows command injection, making it a vector for RCE in offensive security testing.

## Description

This API spawns a shell to run the provided command string, interpreting shell metacharacters. Without sanitization, concatenated user inputs enable injection attacks. Node.js documentation recommends safer alternatives like execFile() for file-based execution without shell parsing. Commonly exploited in supply chain attacks on NPM dependencies.

## Features

- Feature 1: Asynchronous command execution with stdin/stdout/stderr streams
- Feature 2: Callback for handling output and errors
- Feature 3: Options for shell customization and encoding

## Installation

### Requirements

- Node.js 8+ (built-in, no install needed)

### Install Commands

```bash
# No installation required; use require('child_process')
```

## Basic Usage

```javascript
const { exec } = require('child_process');
exec('ls', (error, stdout, stderr) => {
  console.log(stdout);
});
```

### Common Options

| Option | Description |
|--------|-------------|
| cwd | Working directory |
| env | Environment variables |
| shell | Custom shell (default: /bin/sh on Unix) |
| timeout | Execution timeout in ms |

## Examples

### Example 1: Basic Usage

```javascript
const { exec } = require('child_process');
exec('git init', (err, stdout) => {
  if (err) throw err;
  console.log(stdout);
});
```

### Example 2: Advanced Usage

```javascript
const { exec } = require('child_process');
exec('git remote add origin ' + userInput, { timeout: 5000 }, (err, stdout) => {
  // Vulnerable to injection if userInput is unsanitized
});
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Hook Node.js runtime to log exec() calls with dynamic strings
- Use application security tools like Snyk to scan for unsafe child_process usage
- Monitor process trees for unexpected shell spawns from Node.js

## Related Procedures

- [[procedures/Exploit-Command-Injection-in-create-git]]

## Related Tools

- [[tools/create-git]]

## References

- Official documentation: https://nodejs.org/api/child_process.html#child_process_child_process_exec_command_options_callback
