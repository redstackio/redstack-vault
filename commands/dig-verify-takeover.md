---
id: cmd-uuid-dig-verify-1181762
name: dig-verify-takeover
type: command
executor: bash
data: dig %s
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.820Z'
platforms:
  - Linux
  - macOS
  - Windows (with BIND)
tags:
  - dns
  - verification
verified: false
validated: true
submitted: true
---

# dig-verify-takeover

## Command

```bash
dig ███.wavecell.com
```

## Description

Post-takeover, this command verifies if the subdomain DNS now resolves to the attacker's controlled resource, confirming successful hijacking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<domain>` | The subdomain to re-query | Yes |

## Examples

### Basic Usage

```bash
dig ███.wavecell.com
```

### Advanced Usage

```bash
dig +short ███.wavecell.com && curl http://███.wavecell.com
```

## Expected Output

DNS resolution pointing to the new resource IP, with HTTP access serving attacker content, e.g., a custom index page.

## Related

- [[Related Procedure: Claim-Subdomain-via-DNS-Takeover]]
