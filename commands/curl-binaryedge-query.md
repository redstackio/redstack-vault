---
data: >-
  curl -H "X-Key: YOUR_API_KEY"
  "https://api.binaryedge.io/v2/query/search?query=product:kubernetes port:6443"
tags:
  - scanning
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 2065760a-ae25-4da6-b127-6c1049a27319
created_at: '2025-12-11T06:10:10.586Z'
updated_at: '2025-12-11T06:10:10.586Z'
verified: false
validated: true
submitted: true
---
# curl-binaryedge-query

## Command

```bash
curl -H "X-Key: YOUR_API_KEY" "https://api.binaryedge.io/v2/query/search?query=product:kubernetes port:6443"
```

## Description

This command queries the BinaryEdge API for exposed Kubernetes services on port 6443.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "X-Key: YOUR_API_KEY"` | API authentication | Yes |
| `query URL` | Search query | Yes |

## Examples

### Basic Usage

```bash
curl -H "X-Key: YOUR_API_KEY" "https://api.binaryedge.io/v2/query/search?query=product:kubernetes port:6443"
```

## Expected Output

JSON array of scan results, including IPs and service details.

## Related

- [[procedures/Scan-for-Exposed-Kubernetes-APIs]]
- [[tools/BinaryEdge]]
