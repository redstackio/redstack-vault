---
id: 3494e79c-4daf-4af4-b682-fb5d13818648
name: featurebook-serve
type: command
executor: bash
data: featurebook serve --port 8081
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.826Z'
platforms:
  - Linux
  - Node.js
tags:
  - server
  - node-js
verified: false
validated: true
submitted: true
---

# featurebook-serve

## Command

```bash
featurebook serve --port 8081
```

## Description

This command starts the featurebook server, serving content from the current directory on the specified port, exposing the vulnerable viewer endpoint for directory traversal attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--port` | Port to listen on (default may vary, but 8081 used here) | No |
| `8081` | Specific port value | Yes for custom |

## Examples

### Basic Usage

```bash
featurebook serve --port 8081
```

### Advanced Usage

```bash
featurebook serve --port 8081 --host 0.0.0.0
```

## Expected Output

Server logs: "Server started successfully. Listening on port 8081" or similar, with the process idling to accept requests.

## Related

- [[commands/npm-install-global]]
