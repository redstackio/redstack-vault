---
id: cmd-nodejs-fs-open-readonly-001
data: >-
  const fs = require('fs'); const fd = fs.openSync('target-file.txt', 'r');
  console.log('File descriptor:', fd);
tags:
  - file-system
  - node.js
type: command
output: 'File descriptor: 3'
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.066Z'
verified: false
validated: true
submitted: true
---
# node-fs-open-read-only

## Command

```javascript
const fs = require('fs');
const fd = fs.openSync('target-file.txt', 'r');
console.log('File descriptor:', fd);
```

## Description

Opens a file in read-only mode using Node.js fs.openSync to obtain a file descriptor for use in permission bypass attacks. Use when targeting the experimental permission model to avoid write checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| path | Path to the target file (e.g., 'target-file.txt') | Yes |
| mode | File open mode ('r' for read-only) | Yes |

## Examples

### Basic Usage

```javascript
const fs = require('fs');
const fd = fs.openSync('/etc/passwd', 'r');
console.log(fd);
```

### Advanced Usage

```javascript
const fs = require('fs');
const fd = fs.openSync('sensitive.log', 'r', { encoding: 'utf8' });
// Use fd for further operations
fs.closeSync(fd);
```

## Expected Output

A positive integer representing the file descriptor (e.g., 'File descriptor: 3'), indicating successful opening. Errors like ENOENT occur if the file doesn't exist.

## Related

- [[Related Procedure: Open-Read-Only-File-Descriptor-in-Node.js]]
