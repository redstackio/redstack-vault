---
id: cmd-uuid-002
data: dig subdomain.example.com
tags:
  - dns
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.488Z'
verified: false
validated: true
submitted: true
---
# dig-verify-fix

## Command

```bash
dig subdomain.example.com
```

## Description

Performs a DNS lookup for the A record of a subdomain post-fix to confirm the removal of the vulnerable CNAME and resolution to a legitimate IP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `subdomain.example.com` | The domain or subdomain to query | Yes |
| (implicit) | Query type IN A (default) | No |

## Examples

### Basic Usage

```bash
dig subdomain.example.com
```

### Advanced Usage

```bash
dig +trace subdomain.example.com
```

## Expected Output

ANSWER SECTION: subdomain.example.com. 300 IN A 10.0.48.31 (with NOERROR status, NS records, and additional section details confirming fix).

## Related

- [[Related Procedure: Verify-TLD-Registration-and-Fix]]
