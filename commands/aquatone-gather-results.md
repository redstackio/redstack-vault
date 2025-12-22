---
id: e8606d28-65ae-4fda-becd-bf55f3331d0b
name: aquatone-gather-results
type: command
executor: bash
data: aquatone-gather --domain $_DOMAIN
output: null
created_at: '2023-04-06T03:56:25.578243+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - reporting
verified: true
validated: true
---

# aquatone-gather-results

## Command

```bash
aquatone-gather --domain $_DOMAIN
```

## Description

Compiles discovery and scan results into a final report, including HTML overviews and screenshots of responsive pages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --domain | Target domain to gather results for | Yes |

## Examples

### Basic Usage

```bash
aquatone-gather --domain example.com
```

## Expected Output

[INFO] Gathering results for example.com
[INFO] Generated report.html and screenshots

Creates files like report.html with subdomain status, URLs, and images in ~/.aquatone/$_DOMAIN/.

## Related

- [[procedures/Subdomain-Enumeration-with-Aquatone]]
- [[tools/Aquatone]]
