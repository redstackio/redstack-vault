---
id: b38b9020-b51a-4d42-956a-ba374edb4ab4
name: dig-resolve-subdomain
type: command
executor: bash
data: dig 27.prd.vine.co
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.343Z'
platforms:
  - Linux
  - macOS
tags:
  - dns
  - recon
verified: false
validated: true
submitted: true
---

# dig-resolve-subdomain

## Command

```bash
dig 27.prd.vine.co
```

## Description

This command performs a DNS lookup to resolve the A record for the specified subdomain, useful for identifying IP addresses in reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `27.prd.vine.co` | The subdomain to resolve | Yes |

## Examples

### Basic Usage

```bash
dig 27.prd.vine.co
```

### Advanced Usage

```bash
dig +short 27.prd.vine.co
```

## Expected Output

DNS response with QUESTION SECTION, ANSWER SECTION showing IP (e.g., 3.14.159.XX), and authority info. Look for AWS-owned IPs.

## Related

- [[Related Procedure]]
