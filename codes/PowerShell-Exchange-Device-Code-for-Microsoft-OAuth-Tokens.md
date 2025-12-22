---
type: code
language: powershell
verified: true
platforms:
  - Cloud
tags:
  - oauth
  - device-code
  - microsoft-graph
  - access-token
  - powershell
validated: true
---

# PowerShell-Exchange-Device-Code-for-Microsoft-OAuth-Tokens

## Code

```powershell
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

## Description

This PowerShell code snippet exchanges a device code for OAuth access and refresh tokens using Microsoft's token endpoint. It is part of the device code authorization flow for the Microsoft Graph API, allowing token acquisition after user consent on a separate device. The code assumes $authResponse from the initial device code request and $Headers (typically empty or with content-type). It preserves the original hardcoded client_id for Azure PowerShell compatibility but can be parameterized.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $authResponse.device_code | Device code from authorization request | "GMh..." |
| $Headers | Optional headers (e.g., @{ContentType='application/x-www-form-urlencoded'}) | @{ } |
| client_id | Azure AD app client ID (hardcoded in original) | "1950a258-227b-4e31-a9cf-717495945fc2" |

## Usage

Embed this in a polling loop after requesting the device code (e.g., while no access_token, run this every interval seconds). Once tokens are obtained, use $Tokens.access_token in Authorization: Bearer headers for Graph API calls like GET /me. Ideal for scripts in restricted environments or red team ops for credential persistence via API access.

## Detection

- Monitor Azure AD sign-in logs for device code flow events with unusual client_ids or IPs.
- PowerShell execution logs (ModuleLogging, ScriptBlockLogging) capturing Invoke-RestMethod to login.microsoftonline.com.
- Graph API audit logs showing token usage from unexpected sources.
- Network traffic to /devicecode and /token endpoints without corresponding user consent.

## Related

- [[procedures/Obtain-Microsoft-Graph-API-Access-Token-via-Device-Code-Flow]]
- [[powershell-exchange-microsoft-oauth-device-code-for-tokens]]
