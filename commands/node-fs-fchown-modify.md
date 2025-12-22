---
id: cmd-nodejs-fs-fchown-001
data: >-
  const fs = require('fs'); const fd = fs.openSync('target-file.txt', 'r');
  fs.fchownSync(fd, 0, 0); console.log('Ownership modified to root');
  fs.closeSync(fd);
tags:
  - file-system
  - ownership-change
  - node.js
type: command
output: Ownership modified to root
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.061Z'
verified: false
validated: true
submitted: true
---
# node-fs-fchown-modify

## Command

```javascript
const fs = require('fs');
const fd = fs.openSync('target-file.txt', 'r');
fs.fchownSync(fd, 0, 0);
console.log('Ownership modified to root');
fs.closeSync(fd);
```

## Description

Changes the ownership (uid and gid) of a file using a file descriptor via fs.fchownSync, bypassing Node.js permission model write restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| fd | File descriptor from fs.open | Yes |
| uid | New user ID (e.g., 0 for root) | Yes |
| gid | New group ID (e.g., 0 for root) | Yes |

## Examples

### Basic Usage

```javascript
const fs = require('fs');
const fd = fs.openSync('file.txt', 'r');
fs.fchownSync(fd, 1000, 1000);
fs.closeSync(fd);
```

### Advanced Usage

```javascript
const fs = require('fs');
const fd = fs.openSync('/var/log/app.log', 'r');
fs.fchownSync(fd, 0, 0); // Escalate to root
fs.closeSync(fd);
```

## Expected Output

Confirmation message like 'Ownership modified to root' with no errors. Verify changes externally with ls -l.

## Related

- [[Related Procedure: Modify-File-Ownership-Permissions-via-File-Descriptor]]
