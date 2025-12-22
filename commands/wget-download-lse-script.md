---
id: 13b3db12-d9f2-4419-8a0c-e42fe15ad505
name: wget-download-lse-script
type: command
executor: bash
data: >-
  wget
  "https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh"
  -O lse.sh
output: null
created_at: '2023-04-06T03:56:18.413964+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - download
  - enumeration
verified: true
validated: true
---

# wget-download-lse-script

## Command

```bash
wget "https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh" -O lse.sh
```

## Description

Downloads the Linux Smart Enumeration script using wget for priv esc analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -O lse.sh | Output file | Yes |

## Examples

### Basic Usage

```bash
wget "https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh" -O lse.sh
```

## Expected Output

Similar to wget output, file saved as lse.sh.

## Related

- [[procedures/Linux-Privilege-Escalation-Enumeration]]
- [[tools/linux-smart-enumeration]]
