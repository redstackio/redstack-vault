---
data: >-
  const fs = require('fs'); fs.writeFileSync('/tmp/escalated.txt', 'bypassed');
  console.log('Escalation successful');
tags:
  - test
  - escalation
  - fs
type: command
output: null
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.828Z'
id: 12b10f9e-e35e-45e9-8061-af0daa171324
verified: false
validated: true
submitted: true
---
# node-test-escalated-access

## Command

```javascript
const fs = require('fs');
fs.writeFileSync('/tmp/escalated.txt', 'bypassed');
console.log('Escalation successful');
```

## Description

Tests file system write access post-bypass to confirm privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `path` | File path to write | Yes |
| `content` | Data to write | Yes |

## Examples

### Basic Usage

```javascript
fs.writeFileSync('/tmp/test.txt', 'success');
```

## Expected Output

File created successfully; 'Escalation successful' logged.

## Related

- [[Related Procedure: Achieve-Arbitrary-Code-Execution-Bypassing-Permissions]]
