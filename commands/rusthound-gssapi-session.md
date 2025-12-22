---
id: 08d63bb2-069f-448d-bc37-4dfc50144915
name: rusthound-gssapi-session
type: command
executor: bash
data: rusthound.exe -d $_DOMAIN --ldapfqdn $_LDAP_FQDN
output: null
created_at: '2023-04-06T03:56:02.119384+00:00'
updated_at: '2023-10-10T20:26:14.196507+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# rusthound-gssapi-session

## Command

```bash
rusthound.exe -d $_DOMAIN --ldapfqdn $_LDAP_FQDN
```

## Description

Collects AD data using GSSAPI authentication on Windows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d | Domain name | Yes |
| --ldapfqdn | LDAP FQDN | Yes |

## Examples

### Basic Usage

```bash
rusthound.exe -d domain.local --ldapfqdn domain.local
```

## Expected Output

ZIP file with bloodhound.json containing AD graph data.

## Related

- [[procedures/Active-Directory-Reconnaissance-with-BloodHound-and-Certipy]]
- [[tools/RustHound]]
