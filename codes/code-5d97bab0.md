---
id: 5d97bab0-a01e-400c-9403-abb60ead49ef
type: code
language: ps1
verified: false
created_at: '2023-05-23T16:19:36.987180+00:00'
updated_at: '2023-05-23T16:19:52.233652+00:00'
---

# Code Snippet 5d97bab0

**Language**: ps1

```ps1
$body=@{
    "client_id" =  "1950a258-227b-4e31-a9cf-717495945fc2"
    "grant_type" = "urn:ietf:params:oauth:grant-type:device_code"
    "code" =       $authResponse.device_code
}
$Tokens = Invoke-RestMethod `
    -UseBasicParsing `
    -Method Post `
    -Uri "https://login.microsoftonline.com/Common/oauth2/token?api-version=1.0" `
    -Headers $Headers `
    -Body $body
$Tokens
```
