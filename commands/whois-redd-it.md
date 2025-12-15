---
id: cmd-uuid-1
data: whois redd.it
tags:
  - domain-lookup
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:33.802Z'
verified: false
validated: true
submitted: true
---
# whois-redd-it

## Command

```bash
whois redd.it
```

## Description

Perform a WHOIS lookup on the redd.it domain to verify ownership by Reddit Inc., useful in confirming the legitimacy of subdomains like share.redd.it in vulnerability reports.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Standard whois query on domain | Yes |

## Examples

### Basic Usage

```bash
whois redd.it
```

### Advanced Usage

Pipe to grep for specific info:

```bash
whois redd.it | grep "Registrant Organization"
```

## Expected Output

Domain ownership details showing Reddit Inc. as registrant, including creation date and nameservers.

## Related

- [[Related Procedure]]
