---
data: node poc.js
tags:
  - run
  - server
type: command
output: Server listening on port 3000
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.573Z'
id: 980f58f6-0d4e-45ea-a66a-f46654faf5de
verified: false
validated: true
submitted: true
---
# node-run-poc

## Command

```bash
node poc.js
```

## Description

Executes the proof-of-concept JavaScript file to start the vulnerable Express server. Used after creating poc.js to launch the application for testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `poc.js` | Path to the POC script file | Yes |

## Examples

### Basic Usage

```bash
node poc.js
```

### Advanced Usage

```bash
node --inspect poc.js
```

## Expected Output

Server on 3000 (or similar), with the process running in the foreground.

## Related

- [[procedures/Start-POC-Server]]
- [[commands/curl-test-without-header]]
