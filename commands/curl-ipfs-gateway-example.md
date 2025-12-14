---
id: b4bcde30-21e6-4e80-9955-640ad88e2db7
name: curl-ipfs-gateway-example
type: command
executor: bash
data: 'curl --ipfs-gateway https://trusted-gateway.com ipfs://QmPDF'
output: File fetch or error with leak
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.932Z'
platforms:
  - Linux
tags:
  - ipfs
  - curl
verified: false
validated: true
submitted: true
---

# curl-ipfs-gateway-example

## Command

```bash
curl --ipfs-gateway https://trusted-gateway.com ipfs://QmPDF
```

## Description

Fetches an IPFS file via a gateway; with malicious IPFS_PATH, leaks content in error.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --ipfs-gateway | Specify gateway URL | Yes |
| ipfs://QmPDF | IPFS CID | Yes |

## Examples

### Basic Usage

```bash
curl --ipfs-gateway https://example.com ipfs://QmPDF
```

## Expected Output

File content or error with leak if vuln triggered.

## Related

- [[commands/curl-trigger-ipfs-vuln]]
- [[tools/curl]]
