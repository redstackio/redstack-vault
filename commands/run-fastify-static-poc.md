---
id: cmd-run-poc-001
data: bash run.sh
tags:
  - poc
  - server-start
type: command
output: 'Server listening on http://localhost:3000'
executor: bash
platforms:
  - Node.js
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:23.259Z'
verified: false
validated: true
submitted: true
---
# run-fastify-static-poc

## Command

```bash
bash run.sh
```

## Description

Executes the shell script to set up and start a local Fastify server with the vulnerable fastify-static configuration, including npm install for dependencies and server launch on port 3000.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `run.sh` | The PoC startup script | Yes |

## Examples

### Basic Usage

```bash
bash run.sh
```

### Advanced Usage

Run in background:
```bash
bash run.sh &
```

## Expected Output

Initial npm install output, followed by "Server listening at http://localhost:3000" indicating successful startup with redirect: true enabled.

## Related

- [[procedures/Run-Fastify-Static-Vulnerable-Server]]
