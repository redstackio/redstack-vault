---
id: uuid-bash-run
data: bash run.sh
tags:
  - setup
type: command
output: 'Server running on http://localhost:3000'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.784Z'
verified: false
validated: true
submitted: true
---
# bash-run-sh

## Command

```bash
bash run.sh
```

## Description

Executes the setup script to start a vulnerable Fastify server with fastify-static, installing dependencies and binding to localhost:3000.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| run.sh | The script file in the extracted fastify-dos directory | Yes |

## Examples

### Basic Usage

```bash
bash run.sh
```

### Advanced Usage

```bash
# If in subdirectory
cd fastify-dos && bash run.sh
```

## Expected Output

Server logs showing successful startup: "Server running on http://localhost:3000". No errors if environment is set up correctly.

## Related

- [[Related Procedure: Set-Up-Vulnerable-Fastify-Server]]
