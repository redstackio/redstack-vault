---
id: cmd-uuid-dig-resolve-1181762
name: dig-resolve-dns
type: command
executor: bash
data: dig %s
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.825Z'
platforms:
  - Linux
  - macOS
  - Windows (with BIND)
tags:
  - dns
  - recon
verified: false
validated: true
submitted: true
---

# dig-resolve-dns

## Command

```bash
dig ███.wavecell.com
```

## Description

This command uses the dig utility to perform a DNS lookup on a subdomain, revealing records like A, CNAME, or NS that may point to dangling resources such as terminated AWS EC2 instances. Use it during reconnaissance to identify takeover opportunities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<domain>` | The subdomain or domain to query (e.g., ███.wavecell.com) | Yes |
| `+short` | Optional: Short output format for just the resolved value | No |

## Examples

### Basic Usage

```bash
dig ███.wavecell.com
```

### Advanced Usage

```bash
dig +short ███.wavecell.com | xargs -I {} curl -I http://{} --connect-timeout 5 || echo "Unresponsive"
```

## Expected Output

DNS response with ANSWER SECTION showing IP or CNAME, e.g., "███.wavecell.com. 300 IN A 52.XX.XX.XX" where the IP is non-responsive, indicating a dangling record.

## Related

- [[Related Procedure: Detect-Dangling-DNS-Record-for-Subdomain-Takeover]]
