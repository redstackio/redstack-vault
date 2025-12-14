---
id: cmd-uuid-2
data: sudo node index.js 51.75.74.52 80
tags:
  - setup
  - server
type: command
output: Server listening on port 80
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:19.866Z'
verified: false
validated: true
submitted: true
---
# sudo-node-dummy-server-example

## Command

```bash
sudo node index.js 51.75.74.52 80
```

## Description

Elevated execution of the dummy GitHub server on a specific IP and low port for production-like simulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 51.75.74.52 | Example public IP | Yes |
| 80 | Example port | Yes |

## Examples

### Basic Usage

```bash
sudo node index.js 51.75.74.52 80
```

### Advanced Usage

N/A (specific example)

## Expected Output

"Server bound to port 80 without errors."

## Related

- [[Related Procedure|procedures/Set-Up-Dummy-GitHub-Server-for-Malicious-Labels]]
