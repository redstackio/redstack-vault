---
data: node start.js
tags:
  - server
  - node
  - start
type: command
output: 'Server starts, similar to atlasboard start'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.326Z'
id: 77e9c812-bdfd-4a24-84cb-031d517f9065
verified: false
validated: true
submitted: true
---
# node-start-js

## Command

```bash
node start.js
```

## Description

Executes the Atlasboard server script directly using the Node.js runtime.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `start.js` | Entry point script file | Yes |

## Examples

### Basic Usage

```bash
node start.js
```

### Advanced Usage

```bash
node start.js --port=8080
```

## Expected Output

Server startup logs on port 3000.

## Related

- [[commands/atlasboard-start]]
- [[procedures/Launch-Dashboard-and-Trigger-XSS]]
