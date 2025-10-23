---
id: 70dae3e8-293e-4b3d-8cef-ae3ea3046063
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:18.915023+00:00'
updated_at: '2023-04-10T20:34:20.934337+00:00'
---

# Code Snippet 70dae3e8

**Language**: Powershell

```powershell
cap_dac_read_search # This command allows the user to read any file on the system, regardless of the file permissions.
cap_setuid+ep # This command sets the effective user ID of the current process to the user ID of the file owner, allowing the user to execute files with elevated privileges.
```


