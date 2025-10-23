---
id: ff54da9a-556e-4615-9f1e-d76acd3ae48f
name: Microsoft Graph API Access Token
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:14.802533+00:00'
updated_at: '2023-05-23T16:24:59.422317+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Modify Authentication Process|T1556 - Modify Authentication Process]]'
platforms:
- Cloud
tags:
- '[[Authenticating to the Microsoft Graph API in PowerShell]]'
- '[[Cloud - Azure]]'
- '[[Graph API Access Token]]'
- '[[powershell]]'
commands:
- '[[Get Microsoft OAuth Tokens]]'
---

# Microsoft Graph API Access Token

**Status**: ✓ Verified

## Summary

This procedure outlines how to authenticate to the Microsoft Graph API in PowerShell using a refresh token. The Microsoft Graph API provides a unified programmability model that you can use to access the tremendous amount of data in Microsoft 365, Windows 10, and Enterprise Mobility + Security. The

## Description

# Description

This procedure outlines how to authenticate to the Microsoft Graph API in PowerShell using a refresh token. The Microsoft Graph API provides a unified programmability model that you can use to access the tremendous amount of data in Microsoft 365, Windows 10, and Enterprise Mobility + Security. The API uses OAuth 2.0 for authentication and authorization, and this procedure demonstrates how to obtain a valid access token for use with the API.

To obtain a refresh token, the user must first authenticate with their Microsoft account and grant consent for the application to access their data. The refresh token can then be used to obtain a new access token without requiring the user to re-authenticate. This procedure is useful for automating tasks that require access to Microsoft Graph API data, such as reporting, monitoring, or data migration.

 

## Requirements

1. Valid Microsoft account credentials

1. Registered Azure AD application with appropriate permissions to access Microsoft Graph API

1. PowerShell version 5.1 or later

1. Azure AD PowerShell module

 

## Defense

1. Use conditional access policies to restrict access to Microsoft Graph API data

1. Enable multi-factor authentication for Microsoft accounts

1. Monitor Microsoft Graph API activity logs for suspicious activity

 

## Objectives

1. Obtain a valid access token for use with the Microsoft Graph API

1. Automate tasks that require access to Microsoft Graph API data

1. Maintain access to Microsoft Graph API data without requiring user re-authentication

 

# Instructions

1. To get the Access Token for Microsoft, use this command in PowerShell.

 



**Code**: [[$body=@{
    "client_id" =  "1950a258-227b-4e31-a9]]



> This command sends a request to Microsoft's authentication server to get a Refresh Token. The Refresh Token is used to obtain a new Access Token when the current one expires. The command requires the device code obtained from the initial authentication request. The command sends a POST request to the Microsoft authentication server with the required parameters. The response from the server contains the Refresh Token, which can be used to obtain new Access Tokens.



**Command** ([[Get Microsoft OAuth Tokens]]):

```bash
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



## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Modify Authentication Process|T1556 - Modify Authentication Process]]

## Commands Used

- [[Get Microsoft OAuth Tokens]]

## Tags

- [[Authenticating to the Microsoft Graph API in PowerShell]]
- [[Cloud - Azure]]
- [[Graph API Access Token]]
- [[powershell]]


