---
data: dig feedback.screenhero.com CNAME
tags:
  - dns
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.579Z'
id: 2b2ed94e-74c9-4bf5-bc25-743992415134
verified: false
validated: true
submitted: true
---
# dig-lookup-cname

## Command

```bash
dig feedback.screenhero.com CNAME
```

## Description

This command uses the dig utility to query DNS for the CNAME record of a specific subdomain, useful for discovering misconfigurations in subdomain takeover scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| feedback.screenhero.com | The subdomain to query | Yes |
| CNAME | Specifies CNAME record type | Yes |

## Examples

### Basic Usage

```bash
dig feedback.screenhero.com CNAME
```

### Advanced Usage

```bash
dig +short feedback.screenhero.com CNAME
```

## Expected Output

A section showing the CNAME, e.g., "feedback.screenhero.com. 3600 IN CNAME screenhero.uservoice.com." indicating the pointer.

## Related

- [[Related Procedure]]
