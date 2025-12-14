---
data: dig +trace svcardproxydevus.starbucks.com
tags:
  - dns-tracing
type: command
output: Full DNS resolution trace
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.753Z'
id: f7471b1c-6209-410d-aee6-624475e4aa1a
verified: false
validated: true
submitted: true
---
# dig-trace-dns

## Command

```bash
dig +trace svcardproxydevus.starbucks.com
```

## Description

This command traces the complete DNS resolution path for a hostname, revealing CNAME chains and final endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `+trace` | Enable tracing | Yes |
| hostname | Target hostname | Yes |

## Examples

### Basic Usage

```bash
dig +trace svcardproxydevus.starbucks.com
```

### Advanced Usage

```bash
dig +trace @8.8.8.8 svcardproxydevus.starbucks.com
```

## Expected Output

Detailed trace showing root to leaf resolution, e.g., CNAME to trafficmanager.net then cloudapp.azure.com.

## Related

- [[procedures/Confirm-DNS-Record-Chain-to-Dead-Endpoint]]
