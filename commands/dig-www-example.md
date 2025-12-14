---
id: cmd-005
data: dig +short www.█████
tags:
  - dns
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.653Z'
verified: false
validated: true
submitted: true
---
# dig-www-example

## Command

```bash
dig +short www.█████
```

## Description

Performs a DNS lookup to resolve the IP of the primary domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| +short | Short output (IP only) | Yes |
| domain | Domain to query (www.█████) | Yes |

## Examples

### Basic Usage

```bash
dig +short example.com
```

## Expected Output

IP address, e.g., 192.0.2.1.

## Related

- [[Related Procedure: Verify-Related-Domains-with-DNS-Lookup]]
