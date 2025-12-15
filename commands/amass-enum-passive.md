---
data: amass enum --passive -d bountypay.h1ctf.com
tags:
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.217Z'
id: a7d6a1a7-80be-4cbb-907d-3d1e243c1521
verified: false
validated: true
submitted: true
---
# amass-enum-passive

## Command

```bash
amass enum --passive -d bountypay.h1ctf.com
```

## Description

Enumerates subdomains passively using public sources without sending probes to the target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --passive | Passive mode only | Yes |
| -d | Domain to enumerate | Yes |

## Examples

### Basic Usage

```bash
amass enum --passive -d example.com
```

### Advanced Usage

```bash
amass enum --passive -d example.com -o output.txt
```

## Expected Output

List of subdomains like app.bountypay.h1ctf.com, api.bountypay.h1ctf.com.

## Related

- [[tools/Amass]]
- [[procedures/Reconnaissance-and-Exposed-Git-Discovery]]
