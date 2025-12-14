---
data: 'export IPFS_GATEWAY="http://127.0.0.1:5001/"'
tags:
  - configuration
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.395Z'
id: a4c5bdca-6c2f-46c2-aa32-0a7ddd727b21
verified: false
validated: true
submitted: true
---
# set-ipfs-gateway-env

## Command

```bash
export IPFS_GATEWAY="http://127.0.0.1:5001/"
```

## Description

Sets the environment variable for the IPFS gateway URL used by the vulnerable proxy.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| IPFS_GATEWAY | URL of the simulated gateway | Yes |

## Examples

### Basic Usage

```bash
export IPFS_GATEWAY="http://127.0.0.1:5001/"
```

### Advanced Usage

Adjust URL for different gateways: export IPFS_GATEWAY="http://localhost:8080/"

## Expected Output

Shell echo of the variable; no output otherwise.

## Related

- [[Related Procedure: Configure-and-Start-Vulnerable-curl-IPFS-Proxy]]
