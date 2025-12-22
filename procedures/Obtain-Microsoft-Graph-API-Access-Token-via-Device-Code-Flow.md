---
type: procedure
verified: true
submitted: true
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Steal-Application-Access-Token|T1528 - Steal Application Access
    Token]]
  - '[[techniques/Valid-Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - oauth
  - device-code-flow
  - microsoft-graph-api
  - powershell
  - cloud-azure
  - graph-api-access-token
  - authenticating-to-microsoft-graph-api
commands:
  - '[[commands/powershell-request-microsoft-oauth-device-code]]'
  - '[[commands/powershell-exchange-microsoft-oauth-device-code-for-tokens]]'
platforms:
  - Cloud
tools: []
validated: true
---

# Obtain-Microsoft-Graph-API-Access-Token-via-Device-Code-Flow

## Summary

This procedure demonstrates how to authenticate to the Microsoft Graph API using PowerShell via the OAuth 2.0 device code authorization flow. It obtains an access token (and refresh token) for accessing Microsoft 365 data, such as user information, emails, or files, without interactive browser login on the same machine. This is useful for automation, scripting, or maintaining persistent API access in environments where GUI interaction is limited.

## Description

The Microsoft Graph API provides a RESTful endpoint to interact with Microsoft cloud services like Azure AD, Exchange Online, and SharePoint. Authentication uses OAuth 2.0, and the device code flow is ideal for devices without browsers or for command-line tools. The process involves requesting a device code from Microsoft's authorization server, having a user authenticate on another device (e.g., phone), and then polling for tokens. Once obtained, the access token can be used in subsequent API calls (e.g., via Invoke-RestMethod with Authorization header). This technique can enable persistence by registering or using an Azure AD app to acquire long-lived tokens, or in red team scenarios, to exfiltrate data using valid credentials. Prerequisites include an Azure AD app registration with Microsoft Graph permissions (e.g., User.Read). The flow ensures secure token exchange without exposing credentials directly in scripts.

## Requirements

1. Valid Microsoft account credentials for initial authorization.
2. Registered Azure AD application with Microsoft Graph API permissions (e.g., delegated or application permissions like User.Read.All).
3. PowerShell 5.1 or later (Core recommended for cross-platform).
4. Network access to login.microsoftonline.com (no proxy issues).
5. Client ID from the Azure AD app registration.

## Defense

- Implement conditional access policies in Azure AD to restrict device code flow usage to trusted devices/IPs.
- Enable multi-factor authentication (MFA) and monitor for unusual authorization patterns in Azure AD sign-in logs.
- Use Azure AD Privileged Identity Management (PIM) to limit app permissions and require just-in-time access.
- Monitor Graph API audit logs for anomalous queries or token issuances via Microsoft Defender for Cloud Apps.
- Rotate client secrets and review app registrations regularly for unauthorized changes.

## Objectives

1. Acquire a valid access token for Microsoft Graph API calls without browser interaction on the executing machine.
2. Enable automated or scripted access to Microsoft 365 resources for data collection or manipulation.
3. Establish persistent API access using refresh tokens to avoid repeated user authentication.

## Instructions

### Step 1: Request Device Code

**Context**: Initiate the device code flow by sending a POST request to the authorization endpoint. This generates a unique device_code, user_code, and verification URI. The user must then authenticate on a separate device using the provided URI and code. This step sets up the authorization context and explains why it's performed: to bypass local browser requirements while ensuring user consent.

**Command** ([[commands/powershell-request-microsoft-oauth-device-code]]):

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

> This command requests the device authorization from Microsoft's endpoint. If successful, it returns the device_code (for polling), user_code (for user input), verification_uri (where user enters code), and interval (polling frequency in seconds). Display the user_code and verification_uri to the user for manual authentication. Expected: JSON response with these fields; failure if invalid client_id or scopes.

### Step 2: User Authentication

**Context**: The user visits the verification_uri in a browser on any device, enters the user_code, and grants consent to the app's permissions. This step is manual and ensures legitimate authorization; monitor for completion as it triggers token availability.

**Instructions**: Inform the user to open verification_uri and enter user_code. Wait for the "authorization pending" message to change to success. No command needed here; poll status manually or via logs.

**Expected Output**: User sees consent screen; upon approval, the polling in Step 3 succeeds.

### Step 3: Exchange Device Code for Tokens

**Context**: Poll the token endpoint using the device_code until the user completes authentication. This retrieves the access_token, refresh_token, and id_token. Perform this in a loop based on the interval from Step 1 to avoid rate limits. This finalizes token acquisition for API use.

**Command** ([[commands/powershell-exchange-microsoft-oauth-device-code-for-tokens]]):

```powershell
$body = @{
    "client_id" = "$_CLIENT_ID"
    "scope" = "https://graph.microsoft.com/.default"
    "grant_type" = "urn:ietf:params:oauth:grant-type:device_code"
    "code" = "$authResponse.device_code"
}
$tokens = Invoke-RestMethod `
    -UseBasicParsing `
    -Method Post `
    -Uri "https://login.microsoftonline.com/common/oauth2/token" `
    -Body $body
$tokens
```

> This command exchanges the device_code for OAuth tokens. Run it repeatedly (e.g., in a loop with Start-Sleep $authResponse.interval) until success. On success, it returns access_token (short-lived, ~1 hour), refresh_token (long-lived for renewal), and expires_in. Use the access_token in headers for Graph API calls, e.g., @{Authorization = "Bearer $tokens.access_token"}. If user hasn't authorized, it returns "authorization_pending"; after expiry, restart flow.
