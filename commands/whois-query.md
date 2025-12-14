---
id: cmd-whois-query
data: whois doesfranshaveashell.com | grep -E 'Expiration|Status'
tags:
  - recon
  - domain
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.949Z'
verified: false
validated: true
submitted: true
---
# Whois Query

## Command

```bash
whois doesfranshaveashell.com | grep -E 'Expiration|Status'
```

## Description

This command queries WHOIS data for a domain and filters for key fields like expiration and status, aiding in detecting expired registrations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain | Target domain name | Yes |
| `\| grep -E 'Expiration\|Status'` | Filter for relevant lines | No |

## Examples

### Basic Usage

```bash
whois example.com
```

### Advanced Usage

```bash
whois doesfranshaveashell.com > whois.txt
```

## Expected Output

Lines like "Expiration Date: 2019-09-02" and "Status: clientTransferProhibited"

## Related

- [[commands/curl-access-url]]
- [[procedures/Detect-Expired-Domain-Registration]]
