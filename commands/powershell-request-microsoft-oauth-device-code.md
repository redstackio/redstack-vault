---
type: command
executor: powershell
data: |-
  $body = @{
      "client_id" = "$_CLIENT_ID"
      "scope" = "https://graph.microsoft.com/.default"
  }
  $authResponse = Invoke-RestMethod `
      -UseBasicParsing `
      -Method Post `
      -Uri "https://login.microsoftonline.com/common/oauth2/devicecode" `
      -Body $body
  $authResponse
output: null
platforms:
  - Cloud
tags:
  - oauth
  - device-code
  - microsoft-graph
verified: true
validated: true
---

# powershell-request-microsoft-oauth-device-code

## Command

```powershell
$body = @{
    "client_id" = "$_CLIENT_ID"
    "scope" = "https://graph.microsoft.com/.default"
}
$authResponse = Invoke-RestMethod `
    -UseBasicParsing `
    -Method Post `
    -Uri "https://login.microsoftonline.com/common/oauth2/devicecode" `
    -Body $body
$authResponse
```

## Description

Requests a device code from the Microsoft OAuth authorization server to start the device code flow for Microsoft Graph API authentication. This is the first step in obtaining tokens without a local browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_CLIENT_ID | Azure AD application client ID | Yes |
| scope | Scopes for the token (default: https://graph.microsoft.com/.default for full Graph access) | Yes |

## Examples

### Basic Usage

```powershell
$body = @{
    "client_id" = "1950a258-227b-4e31-a9cf-717495945fc2"
    "scope" = "https://graph.microsoft.com/.default"
}
$authResponse = Invoke-RestMethod -UseBasicParsing -Method Post -Uri "https://login.microsoftonline.com/common/oauth2/devicecode" -Body $body
$authResponse
```

### Advanced Usage

Add custom scopes:

```powershell
$body = @{
    "client_id" = "$_CLIENT_ID"
    "scope" = "https://graph.microsoft.com/User.Read https://graph.microsoft.com/Mail.Read"
}
# ... rest as above
```

## Expected Output

```json
{
  "device_code": "GMh...",
  "user_code": "ABC123",
  "verification_uri": "https://microsoft.com/devicelogin",
  "expires_in": 900,
  "interval": 5,
  "message": "To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code ABC123 to authenticate."
}
```

A JSON object with authorization details. Success if device_code is present; error if invalid client_id (e.g., 400 Bad Request).

## Related

- [[procedures/Obtain-Microsoft-Graph-API-Access-Token-via-Device-Code-Flow]]
- [[commands/powershell-exchange-microsoft-oauth-device-code-for-tokens]]
