---
id: c0692055-6f3d-4932-b392-2fa27200bfbb
name: Authenticate user to Microsoft Graph API in PowerShell
type: command
executor: bash
data: "$body = @{\n    \"client_id\" =     \"1950a258-227b-4e31-a9cf-717495945fc2\"\
  \n    \"resource\" =      \"https://graph.microsoft.com\" # Microsoft Graph API\
  \ \n}\n$UserAgent = \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36\
  \ (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36\"\n$Headers=@{}\n$Headers[\"\
  User-Agent\"] = $UserAgent\n$authResponse = Invoke-RestMethod `\n    -UseBasicParsing\
  \ `\n    -Method Post `\n    -Uri \"https://login.microsoftonline.com/common/oauth2/devicecode?api-version=1.0\"\
  \ `\n    -Headers $Headers `\n    -Body $body"
output: null
created_at: '2023-05-23T16:09:07.769036+00:00'
updated_at: '2023-05-23T16:09:07.798899+00:00'
---

# Authenticate user to Microsoft Graph API in PowerShell

```bash
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


