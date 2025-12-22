---
data: python3 vulnerable_proxy.py
tags:
  - setup
  - vulnerable
type: command
output: >-
  Vulnerable proxy listening on 0.0.0.0:9000 and logs like '[vulnerable_proxy]
  Rewritten gateway URL: http://127.0.0.1:5001/api/v0/shutdown'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.392Z'
id: 15a9e5e5-9ff1-4541-9659-5daae1e289f2
verified: false
validated: true
submitted: true
---
# start-vulnerable-proxy

## Command

```bash
python3 vulnerable_proxy.py
```

## Description

Launches the Python proxy using vulnerable curl IPFS rewriting on port 9000.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Relies on IPFS_GATEWAY env | Yes |

## Examples

### Basic Usage

```bash
python3 vulnerable_proxy.py
```

### Advanced Usage

Run with env: IPFS_GATEWAY=... python3 vulnerable_proxy.py

## Expected Output

Listening confirmation and URL rewrite logs upon requests.

## Related

- [[Related Procedure: Configure-and-Start-Vulnerable-curl-IPFS-Proxy]]
