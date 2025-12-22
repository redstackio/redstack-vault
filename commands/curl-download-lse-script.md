---
id: 49112ae8-95a2-48d5-95da-852b8805282b
name: curl-download-lse-script
type: command
executor: bash
data: >-
  curl
  "https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh"
  -o lse.sh
output: null
created_at: '2023-04-06T03:56:18.414026+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - download
  - enumeration
verified: true
validated: true
---

# curl-download-lse-script

## Command

```bash
curl "https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh" -o lse.sh
```

## Description

Downloads LSE script using curl.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -o lse.sh | Output file | Yes |

## Examples

### Basic Usage

```bash
curl "https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh" -o lse.sh
```

## Expected Output

Progress bar and file saved.

## Related

- [[procedures/Linux-Privilege-Escalation-Enumeration]]
- [[tools/linux-smart-enumeration]]
