---
id: c2f3g4h5-i6j7-8902-fghi-6789012345
data: |
  whois $DOMAIN
tags:
  - whois
  - domain
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:51:26.516Z'
verified: false
validated: true
submitted: true
---
# whois-domain-check

## Command

```bash
whois $DOMAIN
```

## Description

Retrieves WHOIS information for a domain to check registration status and availability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$DOMAIN` | Target domain (e.g., ████.azurewebsites.net) | Yes |

## Examples

### Basic Usage

```bash
whois ████.azurewebsites.net
```

### Advanced Usage

```bash
whois -h whois.verisign-grs.com example.com
```

## Expected Output

No registrant if available; otherwise, owner details.

## Related

- [[commands/dig-dns-query]]
- [[procedures/Verify-Unclaimed-Domain-Availability]]
