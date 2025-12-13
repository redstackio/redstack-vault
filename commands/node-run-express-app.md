---
data: 'DEBUG=express:* node app.js'
tags:
  - run
type: command
executor: bash
platforms:
  - Linux
id: ca3e8e63-7ab2-4a35-a00a-c8ba6c7b5adf
created_at: '2025-12-13T09:01:22.075Z'
updated_at: '2025-12-13T09:01:22.075Z'
verified: false
validated: true
submitted: true
---
# node Run Express App

## Command

```bash
DEBUG=express:* node app.js
```

## Description

Runs a Node.js script (app.js) with debug logging enabled for Express modules.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `DEBUG` | Enables debug for Express modules | No |

## Examples

### Basic Usage

```bash
DEBUG=express:* node app.js
```

## Expected Output

Server listening on port 8080 with debug output.

## Related

- [[procedures/Setup-Node-js-Express-Backend-Server]]
- [[tools/Node-js]]
