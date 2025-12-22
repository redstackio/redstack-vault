---
type: command
executor: bash
data: mitm6 -d $_DOMAIN
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - mitm
  - ipv6-spoof
verified: true
validated: true
---

# mitm6-run

## Command

```bash
mitm6 -d $_DOMAIN
```

## Description

Runs Mitm6 to spoof IPv6 DNS and WPAD for NTLM coercion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d $_DOMAIN | Target domain | Yes |

## Examples

### Basic Usage

```bash
mitm6 -d lab.local
```

## Expected Output

"Spoofing IPv6 for domain lab.local".

## Related

- [[tools/Mitm6]]
