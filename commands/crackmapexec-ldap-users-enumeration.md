---
type: command
executor: bash
data: >-
  crackmapexec ldap $_TARGET_DC -u '$_USERNAME' -p '$_PASSWORD' --kdcHost
  $_TARGET_DC --users
tags:
  - active-directory
  - enumeration
  - ldap
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# crackmapexec-ldap-users-enumeration

## Command

```bash
crackmapexec ldap $_TARGET_DC -u '$_USERNAME' -p '$_PASSWORD' --kdcHost $_TARGET_DC --users
```

## Description

This command uses CrackMapExec to authenticate to an Active Directory domain controller via LDAP and enumerate all user accounts, including the BadPwdCount attribute (failed login attempts) and pwdLastSet (last password change timestamp). It is used during reconnaissance for credential access attacks like password spraying, helping identify vulnerable accounts without excessive noise.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_DC | IP address or hostname of the domain controller (LDAP target) | Yes |
| -u '$_USERNAME' | Username for authenticating to the DC (domain\user format if needed) | Yes |
| -p '$_PASSWORD' | Password corresponding to the username | Yes |
| --kdcHost $_TARGET_DC | Specifies the Kerberos KDC host (often the same as the DC for authentication) | Yes |
| --users | Flag to enumerate LDAP users and their attributes like badpwdcount | Yes |

## Examples

### Basic Usage

```bash
crackmapexec ldap 10.0.2.11 -u 'domain\\user' -p 'Passw0rd' --kdcHost 10.0.2.11 --users
```

### Advanced Usage (with output redirection)

```bash
crackmapexec ldap dc01.contoso.com -u 'user' -p 'password' --kdcHost dc01.contoso.com --users > ad_users.txt
```

## Expected Output

When successful, the command outputs a table of users with status, badpwdcount, and pwdLastSet:

```
LDAP         10.0.2.11       389    dc01       Guest           [normal] badpwdcount: 0 pwdLastSet: <never>
LDAP         10.0.2.11       389    dc01       krbtgt          [normal] badpwdcount: 0 pwdLastSet: <never>
LDAP         10.0.2.11       389    dc01       Administrator   [normal] badpwdcount: 5 pwdLastSet: 2023-01-15 10:30:00
```

Look for [normal] status and analyze badpwdcount > 0 for targeting. Errors like [STATUS_LOGON_FAILURE] indicate invalid credentials.

## Related

- [[procedures/Password-Spraying-with-BadPwdCount-Attribute-Enumeration]]
- [[tools/CrackMapExec]]
