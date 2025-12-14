---
data: ./node_modules/mcstatic/bin/mcstatic
tags:
  - server
  - execution
type: command
executor: bash
platforms:
  - Linux
  - Node.js
id: 110e0ef3-ec15-4b39-a6cf-afb828b73849
created_at: '2025-12-14T17:26:12.247Z'
updated_at: '2025-12-14T17:26:12.247Z'
verified: false
validated: true
submitted: true
---
# start-mcstatic-server

## Command

```bash
./node_modules/mcstatic/bin/mcstatic
```

## Description

This command executes the mcstatic binary to start a file server on port 8080, serving the current directory and exposing the path traversal vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
./node_modules/mcstatic/bin/mcstatic
```

### Advanced Usage

Run in background: ```bash
./node_modules/mcstatic/bin/mcstatic &
```

## Expected Output

"mcstatic serving ./ on port 8080" followed by the server awaiting connections.

## Related

- [[Related Procedure|procedures/Start-mcstatic-Server]]
