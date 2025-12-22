---
type: command
executor: powershell
data: >-
  $body = @{
      "client_id" = "$_CLIENT_ID"
      "resource" = "$_RESOURCE"
  }

  $UserAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

  $Headers=@{}

  $Headers["User-Agent"] = $UserAgent

  $authResponse = Invoke-RestMethod `
      -UseBasicParsing `
      -Method Post `
      -Uri "https://login.microsoftonline.com/common/oauth2/devicecode?api-version=1.0" `
      -Headers $Headers `
      -Body $body
output: null
platforms:
  - Cloud
  - Azure
tags:
  - powershell
  - oauth
  - device-code
  - graph-api
verified: true
validated: true
---

# powershell-request-device-code-for-microsoft-graph-api

## Command

```powershell
$body = @{
    "client_id" = "$_CLIENT_ID"
    "resource" = "$_RESOURCE"
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

## Description

This PowerShell command initiates the OAuth 2.0 device code flow for Microsoft Graph API authentication. It requests a device code from the authorization server, which is used to prompt the user for approval via a separate browser session. Use this in scenarios where direct browser redirects are unavailable, such as on servers or during red team operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_CLIENT_ID | Azure app client ID (e.g., public ID for Graph: 1950a258-227b-4e31-a9cf-717495945fc2) | Yes |
| $_RESOURCE | Target resource URI (e.g., https://graph.microsoft.com for Graph API) | Yes |

## Examples

### Basic Usage

```powershell
# Using public Graph client ID
$body = @{"client_id" = "1950a258-227b-4e31-a9cf-717495945fc2"; "resource" = "https://graph.microsoft.com"}
# ... rest of command
```

### Advanced Usage

```powershell
# Custom app client ID
$_CLIENT_ID = "your-app-client-id"
$_RESOURCE = "https://graph.microsoft.com"
# Run full command
```

## Expected Output

A hashtable object ($authResponse) with device code details:

```json
{
  "device_code": "GMh6yST6j7...",
  "user_code": "ABCD-EFGH",
  "verification_uri": "https://microsoft.com/devicelogin",
  "expires_in": 900,
  "interval": 5,
  "message": "To sign in, use a web browser... enter the code ABCD-EFGH"
}
```

## Related

- [[procedures/Device-Code-Flow-Authentication-to-Microsoft-Graph-API-in-PowerShell]]
- [[commands/powershell-request-token-using-device-code-graph-api]]
