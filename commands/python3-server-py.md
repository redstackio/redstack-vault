---
data: python3 server.py
tags:
  - server
  - python
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.015Z'
id: 74565f98-bff5-4d09-ba04-e136b91faf20
verified: false
validated: true
submitted: true
---
# python3-server-py

## Command

```bash
python3 server.py
```

## Description

Runs Python script to start HTTPS and HTTP servers for cookie vuln setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| server.py | Script file | Yes |

## Examples

### Basic Usage

```bash
python3 server.py
```

## Expected Output

Serving HTTPS on 9443, HTTP on 9080.

## Related

- [[procedures/Launch-HTTPS-and-HTTP-Servers-for-Cookie-Reproduction]]
- [[commands/curl-trigger-vuln]]
