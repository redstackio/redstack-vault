---
id: cmd-uuid-006
data: dig proxy.aw.rs
tags:
  - dns
  - verify
type: command
output: proxy.aw.rs. 60 IN A 127.0.0.1
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.515Z'
verified: false
validated: true
submitted: true
---
# dig-verify-dns

## Command

```bash
dig proxy.aw.rs
```

## Description

Queries DNS for proxy.aw.rs resolution to verify setup or redirection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `proxy.aw.rs` | Domain to query | Yes |

## Examples

### Basic Usage

```bash
dig example.com
```

## Expected Output

ANSWER SECTION with IP and TTL.

## Related

- [[Related Procedure: Set-Up-DNS-for-Proxy-Redirection]]
