---
data: whois crossinstall.com | grep Org
tags:
  - whois
  - domain
type: command
output: |-
  Registrant Organization: Twitter, Inc.
  Admin Organization: Twitter, Inc.
  Tech Organization: Twitter, Inc.
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.966Z'
id: a8c3ef7d-6fdd-4d4a-9b8b-f608f02f1d68
verified: false
validated: true
submitted: true
---
# whois-domain-ownership-check

## Command

```bash
whois crossinstall.com | grep Org
```

## Description

Queries WHOIS for domain details and filters for organization fields to quickly check ownership.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `crossinstall.com` | Target domain | Yes |
| `| grep Org` | Filters lines containing 'Org' | No |

## Examples

### Basic Usage

```bash
whois crossinstall.com | grep Org
```

### Advanced Usage

```bash
whois crossinstall.com | grep -E 'Org|Name'
```

## Expected Output

Registrant Organization: Twitter, Inc.
Admin Organization: Twitter, Inc.
Tech Organization: Twitter, Inc.

## Related

- [[Related Procedure: Check-Domain-Ownership-with-WHOIS]]
