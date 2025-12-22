---
type: command
executor: bash
data: crackmapexec ldap $_DC_IP -u $_USERNAME -p $_PASSWORD --admin-count
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
tags:
  - active-directory
  - enumeration
  - remote
verified: true
validated: true
---

# crackmapexec-ldap-admincount-enum

## Command

```bash
crackmapexec ldap $_DC_IP -u $_USERNAME -p $_PASSWORD --admin-count
```

## Description

Uses CrackMapExec to perform remote LDAP enumeration over SMB/LDAP, identifying users and groups with AdminCount=1.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DC_IP | IP address of the domain controller | Yes |
| -u $_USERNAME | Username for authentication | Yes |
| -p $_PASSWORD | Password or NTLM hash | Yes |
| --admin-count | Flag to enumerate adminCount=1 objects | Yes |

## Examples

### Basic Usage

```bash
crackmapexec ldap 10.10.10.10 -u user -p pass --admin-count
```

### Advanced Usage

```bash
crackmapexec ldap 10.10.10.10 -u user -H :hash --admin-count -d domain.com
```

## Expected Output

```
LDAP                 10.10.10.10:389  user:pass *********
AdminCount Users: adminuser, protecteduser
AdminCount Groups: Domain Admins
```

## Related

- [[procedures/AdminCount-Abuse]]
- [[commands/python-ldapdomaindump-domain-dump]]
