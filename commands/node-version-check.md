---
data: node --version
tags:
  - version
  - verify
type: command
output: v22.12.0
executor: bash
platforms:
  - Node.js
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.222Z'
id: bc700ef0-f8fe-4b29-a5df-eef168a207f3
verified: false
validated: true
submitted: true
---
# node-version-check

## Command

```bash
node --version
```

## Description

Checks the installed Node.js version to ensure compatibility with the V8 engine's Math.random() implementation for the undici vulnerability demo.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--version` | Outputs the version number | Yes |

## Examples

### Basic Usage

```bash
node --version
```

### Advanced Usage

Not applicable; simple version query.

## Expected Output

v22.12.0

## Related

- [[commands/node-server-start]]
- [[commands/node-exploit-run]]
