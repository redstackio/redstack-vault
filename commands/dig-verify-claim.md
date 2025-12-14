---
id: cmd-dig-verify
data: dig +short $SUBDOMAIN
tags:
  - dns
  - verify
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.569Z'
verified: false
validated: true
submitted: true
---
# dig-verify-claim

## Command

```bash
dig +short $SUBDOMAIN
```

## Description

Verifies DNS resolution after claiming a subdomain to confirm control.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `+short` | Compact output | Yes |
| `$SUBDOMAIN` | Claimed subdomain | Yes |

## Examples

### Basic Usage

```bash
dig +short vulnerable-subdomain.mozgcp.net
```

## Expected Output

Resolves to attacker's service IP or CNAME.

## Related

- [[Related Procedure: Claim Dangling Subdomain]]
