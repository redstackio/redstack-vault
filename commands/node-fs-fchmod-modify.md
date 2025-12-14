---
id: cmd-nodejs-fs-fchmod-001
data: >-
  const fs = require('fs'); const fd = fs.openSync('target-file.txt', 'r');
  fs.fchmodSync(fd, 0o777); console.log('Permissions set to 777');
  fs.closeSync(fd);
tags:
  - file-system
  - permissions-change
  - node.js
type: command
output: Permissions set to 777
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.058Z'
verified: false
validated: true
submitted: true
---
# node-fs-fchmod-modify

## Command

```javascript
const fs = require('fs');
const fd = fs.openSync('target-file.txt', 'r');
fs.fchmodSync(fd, 0o777);
console.log('Permissions set to 777');
fs.closeSync(fd);
```

## Description

Modifies file permissions using a file descriptor with fs.fchmodSync, evading write permission checks in Node.js experimental model.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| fd | File descriptor from fs.open | Yes |
| mode | New permission mode (octal, e.g., 0o777 for full access) | Yes |

## Examples

### Basic Usage

```javascript
const fs = require('fs');
const fd = fs.openSync('file.txt', 'r');
fs.fchmodSync(fd, 0o644);
fs.closeSync(fd);
```

### Advanced Usage

```javascript
const fs = require('fs');
const fd = fs.openSync('config.ini', 'r');
fs.fchmodSync(fd, 0o777); // Grant full access
fs.closeSync(fd);
```

## Expected Output

Message like 'Permissions set to 777' without exceptions. Confirm with ls -l showing updated modes.

## Related

- [[Related Procedure: Modify-File-Ownership-Permissions-via-File-Descriptor]]
