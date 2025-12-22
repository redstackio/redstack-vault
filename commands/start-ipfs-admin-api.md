---
data: python3 admin_api.py
tags:
  - setup
type: command
output: >-
  Admin API listening on 127.0.0.1:5001 and logs like '[admin_api]
  127.0.0.1:62081 -> /api/v0/shutdown'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.405Z'
id: c3fdd719-3c14-40c1-b80b-c69b99f5e288
verified: false
validated: true
submitted: true
---
# start-ipfs-admin-api

## Command

```bash
python3 admin_api.py
```

## Description

Starts a Python HTTP server simulating IPFS admin API on localhost:5001 to log incoming requests for SSRF testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs the script directly | Yes |

## Examples

### Basic Usage

```bash
python3 admin_api.py
```

### Advanced Usage

No advanced options; script handles server setup.

## Expected Output

Server startup message and request logs upon hits, e.g., listening confirmation followed by path logs.

## Related

- [[Related Procedure: Setup-Simulated-IPFS-Admin-API-Server]]
