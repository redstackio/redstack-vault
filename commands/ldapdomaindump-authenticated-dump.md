---
id: 76311a64-9d9b-4c24-b469-48b539df2a63
name: ldapdomaindump-authenticated-dump
type: command
executor: bash
data: ldapdomaindump -u '$_DOMAIN\\$_USERNAME' -p $_PASSWORD $_DC_IP -o $_OUTPUT_DIR
output: null
created_at: '2023-04-06T03:56:04.401546+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - ad-enumeration
  - ldap-dump
verified: true
validated: true
---

# ldapdomaindump-authenticated-dump

## Command

```bash
ldapdomaindump -u '$_DOMAIN\\$_USERNAME' -p $_PASSWORD $_DC_IP -o $_OUTPUT_DIR
```

## Description

This command dumps Active Directory domain information using ldapdomaindump with authentication, generating LDIF files for offline analysis of user descriptions and other attributes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u '$_DOMAIN\\$_USERNAME' | Authenticated user in DOMAIN\user format | Yes |
| -p $_PASSWORD | Password for authentication | Yes |
| $_DC_IP | Target DC IP or hostname | Yes |
| -o $_OUTPUT_DIR | Output directory for dump files | Yes |

## Examples

### Basic Usage

```bash
ldapdomaindump -u 'LAB\user' -p pass 10.10.10.10 -o ./ad_dump
```

## Expected Output

LDIF files in $_OUTPUT_DIR, e.g., users.ldif with:
```
dn: CN=Admin,CN=Users,DC=lab,DC=local
description: Password stored here: Secret456
```

## Related

- [[procedures/Enumerate-Passwords-in-AD-User-Descriptions]]
- [[commands/grep-search-file-for-password-pattern]]
