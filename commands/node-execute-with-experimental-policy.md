---
data: ../node-v19.6.1-linux-x64/bin/node --experimental-policy=policy.json proc.js
tags:
  - node.js
  - execution
type: command
output: |-
  v19.6.1
  #1 SMP PREEMPT Debian 5.16.18-1kali1 (2022-04-01)
  (node:2720) ExperimentalWarning: Policies are experimental.
  (Use `node --trace-warnings ...` to show where the warning was created)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.904Z'
id: 4fb8f22e-b2f1-43af-a7d7-5c113dc045f0
verified: false
validated: true
submitted: true
---
# node-execute-with-experimental-policy

## Command

```bash
../node-v19.6.1-linux-x64/bin/node --experimental-policy=policy.json proc.js
```

## Description

Executes a Node.js script (proc.js) under an experimental permission policy defined in policy.json, enforcing module loading restrictions while demonstrating a bypass vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--experimental-policy` | Path to the JSON policy file for module permissions | Yes |
| `proc.js` | The JavaScript file to execute | Yes |

## Examples

### Basic Usage

```bash
../node-v19.6.1-linux-x64/bin/node --experimental-policy=policy.json proc.js
```

### Advanced Usage

```bash
../node-v19.6.1-linux-x64/bin/node --experimental-policy=policy.json --trace-warnings proc.js
```

## Expected Output

Node.js version, OS version from loaded 'os' module, and experimental policy warning, indicating successful bypass of restrictions.

## Related

- [[Related Procedure: Execute-Node.js-Script-with-Policy]]
