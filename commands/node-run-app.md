---
data: node index.js
tags:
  - run
  - server
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.016Z'
id: 9f97009e-d3f7-4b32-830c-f7ceb53792d1
verified: false
validated: true
submitted: true
---
# node-run-app

## Command

```bash
node index.js
```

## Description

Executes the Node.js script index.js to start the Express server for the vulnerable app.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| index.js | Script file | Yes |

## Examples

### Basic Usage

```bash
node index.js
```

### Advanced Usage

```bash
node --inspect index.js
```

## Expected Output

"Example app listening on port 3000!"; server runs until stopped.

## Related

- [[commands/curl-send-jwt-token-jti1]]
