---
id: 387eecdb-b5c1-4e64-b870-656017519fcb
name: Azure Graph API Refresh Token
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:14.758396+00:00'
updated_at: '2023-05-23T16:10:37.176125+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]'
platforms:
- Cloud
tags:
- '[[Authenticating to the Microsoft Graph API in PowerShell]]'
- '[[Cloud - Azure]]'
- '[[Graph API Refresh Token]]'
- '[[powershell]]'
commands:
- '[[Authenticate user to Microsoft Graph API in PowerShell]]'
---

# Azure Graph API Refresh Token

**Status**: ✓ Verified

## Summary

This procedure outlines the steps to authenticate to the Microsoft Graph API in PowerShell using a refresh token. The Graph API is a RESTful web API that enables you to access Microsoft Cloud service resources. By authenticating to the Graph API, attackers can gain access to sensitive data such as 

## Description

# Description

This procedure outlines the steps to authenticate to the Microsoft Graph API in PowerShell using a refresh token. The Graph API is a RESTful web API that enables you to access Microsoft Cloud service resources. By authenticating to the Graph API, attackers can gain access to sensitive data such as emails, contacts, and files. To authenticate, a refresh token is used to obtain an access token which can then be used to make requests to the API. This procedure provides an offensive use case for attackers to gain access to sensitive data.

 

## Requirements

1. Valid refresh token for the Microsoft Graph API

1. PowerShell installed on the attacker's machine

 

## Defense

1. Use multi-factor authentication to prevent unauthorized access to the Graph API

1. Monitor for unusual activity or requests to the Graph API

1. Limit access to sensitive data within the Graph API to only authorized users

 

## Objectives

1. Gain access to sensitive data such as emails, contacts, and files through the Microsoft Graph API

1. Use PowerShell to authenticate to the Graph API using a refresh token

 

# Instructions

1. Send a POST request to the Microsoft authentication endpoint with the client ID and resource details. The response includes a device code and a verification URL that the user must use to authenticate. Once the user is authenticated, the response includes an access token that can be used to access the Microsoft Graph API.

 



**Code**: [[$body = @{
    "client_id" =     "1950a258-227b-4e]]



> - $body: This variable is a hashtable that contains the client ID and resource details needed to authenticate to the Microsoft Graph API.
- $UserAgent: This variable contains the user agent string that is used in the headers of the authentication request.
- $Headers: This variable is a hashtable that contains the headers for the authentication request. The User-Agent header is set to the value of $UserAgent.
- $authResponse: This variable contains the response from the authentication request. It includes the device code and verification URL that the user must use to authenticate, as well as the access token that can be used to access the Microsoft Graph API.



**Command** ([[Authenticate user to Microsoft Graph API in PowerShell]]):

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



## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]

## Commands Used

- [[Authenticate user to Microsoft Graph API in PowerShell]]

## Tags

- [[Authenticating to the Microsoft Graph API in PowerShell]]
- [[Cloud - Azure]]
- [[Graph API Refresh Token]]
- [[powershell]]


