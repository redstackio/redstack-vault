---
id: cmd-uuid-2
data: whois example-domain.us
tags:
  - whois
  - domain
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.820Z'
verified: false
validated: true
submitted: true
---
# whois-domain-query

## Command

```bash
whois example-domain.us
```

## Description

Queries the WHOIS database for domain registration details, used to confirm if a domain is unregistered for takeover exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `example-domain.us` | The domain to check registration status | Yes |

## Examples

### Basic Usage

```bash
whois example-domain.us
```

### Advanced Usage

```bash
whois -h whois.nic.us example-domain.us
```

## Expected Output

IANA WHOIS header for .us TLD, followed by nic.us response: "No match for \"EXAMPLE-DOMAIN.US\"." indicating unregistered.

## Related

- [[Related Procedure: Query-WHOIS-for-Domain-Registration-Status]]
