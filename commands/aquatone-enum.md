---
id: cmd-aquatone-927413
data: aquatone-discover --domain zomato.com --threads 10
tags:
  - subdomain
type: command
output: |
  Discovered subdomains: auth.zomato.com, api.zomato.com
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.610Z'
verified: false
validated: true
submitted: true
---
# aquatone-enum

## Command

```bash
aquatone-discover --domain zomato.com --threads 10
```

## Description

Discovers subdomains using Aquatone for Zomato recon.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--domain` | Target domain | Yes |
| `--threads 10` | Parallel threads | No |

## Examples

### Basic Usage

```bash
aquatone-discover --domain example.com
```

### Advanced Usage

```bash
aquatone-discover --domain zomato.com --wordlist list.txt
```

## Expected Output

List of subdomains discovered.

## Related

- [[Related Procedure: Subdomain-Enumeration-with-Aquatone]]
