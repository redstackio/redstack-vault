---
id: 1dd0b68a-765d-4b7f-84fc-9230a2288f0c
type: code
language: ps1
verified: false
created_at: '2023-05-23T16:08:30.904878+00:00'
updated_at: '2023-05-23T16:09:07.782201+00:00'
---

# Code Snippet 1dd0b68a

**Language**: ps1

```ps1
$body = @{
    "client_id" =     "1950a258-227b-4e31-a9cf-717495945fc2"
    "resource" =      "https://graph.microsoft.com" # Microsoft Graph API 
}
$UserAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
$Headers=@{}
$Headers["User-Agent"] = $UserAgent
$authResponse = Invoke-RestMethod `
    -UseBasicParsing `
    -Method Post `
    -Uri "https://login.microsoftonline.com/common/oauth2/devicecode?api-version=1.0" `
    -Headers $Headers `
    -Body $body
```


