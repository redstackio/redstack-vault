---
id: cmd-006
data: dig +short www.██████████
tags:
  - dns
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.642Z'
verified: false
validated: true
submitted: true
---
# dig-www-related

## Command

```bash
dig +short www.██████████
```

## Description

Resolves the IP of a related domain to check for shared hosting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| +short | Short output (IP only) | Yes |
| domain | Domain to query (www.██████████) | Yes |

## Examples

### Basic Usage

```bash
dig +short related.com
```

## Expected Output

Matching IP address.

## Related

- [[Related Procedure: Verify-Related-Domains-with-DNS-Lookup]]
