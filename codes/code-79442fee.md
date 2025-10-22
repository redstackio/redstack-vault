---
id: 79442fee-71bf-4d48-8e76-19c49386186b
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:14.749693+00:00'
updated_at: '2023-05-23T16:08:30.924678+00:00'
---

# Code Snippet 79442fee

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

# This command authenticates the user to the Microsoft Graph API in PowerShell. 
# The command sends a POST request to the Microsoft authentication endpoint with the client ID and resource details.
# The response includes a device code and a verification URL that the user must use to authenticate.
# Once the user is authenticated, the response includes an access token that can be used to access the Microsoft Graph API.

```
