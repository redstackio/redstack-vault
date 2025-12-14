---
data: >-
  node -e "const cp = require('child_process'); cp.exec(Object.prototype.command
  || 'echo safe', (err, out) => console.log(out))"
tags:
  - rce
  - nodejs
type: command
executor: bash
platforms:
  - Linux
  - Node.js
id: 35283304-3adc-4913-90fc-c0f0fd557d47
created_at: '2025-12-14T17:23:36.768Z'
updated_at: '2025-12-14T17:23:36.768Z'
verified: false
validated: true
submitted: true
---
# node-command-injection-test

## Command

```bash
node -e "const cp = require('child_process'); cp.exec(Object.prototype.command || 'echo safe', (err, out) => console.log(out))"
```

## Description

This Node.js one-liner tests for command injection via prototype pollution by executing a child_process.exec with a fallback to a polluted Object.prototype.command property, simulating RCE in Rocket.Chat's runtime.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `node` | Node.js interpreter | Yes |
| `-e` | Execute string as JS code | Yes |
| `"const cp..."` | JS code importing child_process and exec | Yes |

## Examples

### Basic Usage

```bash
node -e "console.log(Object.prototype.polluted || 'clean')"
```

### Advanced Usage

```bash
node -e "Object.prototype.command = 'whoami'; require('child_process').exec(Object.prototype.command, (err, stdout) => console.log(stdout))"
```

## Expected Output

If polluted: Output of injected command, e.g., "uid=0(root)\n". If clean: "safe\n".

## Related

- [[Related Procedure|procedures/Trigger-RCE-via-Command-Injection]]
