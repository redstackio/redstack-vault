---
id: cmd-aquatone-discover
data: aquatone-discover --domain zomato.com
tags:
  - subdomain
type: command
output: 'Discovered subdomains: auth.zomato.com'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:32.238Z'
verified: false
validated: true
submitted: true
---
# aquatone-enumerate

## Command

```bash
aquatone-discover --domain zomato.com
```

## Description

Discovers subdomains and takes screenshots.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --domain | Target domain | Yes |

## Examples

### Basic Usage

```bash
aquatone-discover --domain zomato.com
```

## Expected Output

Subdomain list with screenshots.

## Related

- [[commands/dns-scan-enum]]
