---
id: 64f90c07-fdce-4a70-bbc1-97e7b91f3520
name: Generate-Azure-Tokens-with-SharpAzToken
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.338573+00:00'
updated_at: '2023-05-24T07:41:56.224480+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Steal Application Access Token|T1528 - Steal Application Access
    Token]]
sub_techniques: []
tags:
  - '[[tags/Cloud-Azure]]'
  - '[[tags/Refresh-Tokens]]'
  - '[[tags/Token-from-Managed-Identity]]'
commands:
  - '[[commands/sharpaztoken-generate-cookie]]'
  - '[[commands/sharpaztoken-generate-token-refresh]]'
  - '[[commands/sharpaztoken-generate-token-username-password]]'
platforms:
  - Windows
  - Azure
tools:
  - '[[tools/SharpAzToken]]'
validated: true
---

# Generate-Azure-Tokens-with-SharpAzToken

## Summary

This procedure uses the SharpAzToken tool to generate Azure access tokens and Primary Refresh Token (PRT) cookies for authentication. It covers three methods: creating a PRT-cookie from Mimikatz-extracted data for browser-based access, generating a token using username and password credentials, and refreshing a token from an existing refresh token. These techniques enable attackers with initial access to Azure environments to obtain valid tokens for further lateral movement or resource access without interactive logons.

## Description

SharpAzToken is a .NET-based tool designed to manipulate Azure Active Directory (AAD) authentication artifacts, particularly for generating tokens and cookies that can be used to authenticate to Azure resources. In an attack scenario, this is often used post-compromise on a domain-joined Windows machine where tools like Mimikatz have already extracted Kerberos tickets or primary refresh tokens (PRTs). The procedure assumes the attacker has local administrator access or equivalent to run the tool and extract necessary inputs. Tokens generated can be used to access Azure APIs, management portals, or cloud resources, bypassing some multi-factor authentication requirements if refresh tokens are available. This aligns with credential access tactics in cloud environments, where stolen tokens enable persistence and privilege escalation.

## Requirements

1. SharpAzToken.exe must be downloaded and placed in the current working directory or PATH on a Windows machine.
2. For the cookie method: Derived key, context, and PRT must be extracted using Mimikatz from a compromised Azure AD-joined device.
3. For the username/password method: Valid Azure AD username and password credentials.
4. For the refresh token method: A valid refresh token from a prior authentication session.
5. PowerShell execution policy must allow running unsigned scripts, or the tool must be executed via command line.
6. Network access to Azure AD endpoints (e.g., login.microsoftonline.com).

## Defense

- Monitor for anomalous token issuance from unusual IP addresses or user agents using Azure AD sign-in logs and Microsoft Defender for Cloud Apps.
- Implement Conditional Access Policies to restrict token issuance to trusted devices and locations.
- Enable Privileged Identity Management (PIM) to require just-in-time elevation for sensitive roles.
- Regularly rotate credentials and refresh tokens, and use short-lived access tokens where possible.
- Detect Mimikatz usage through endpoint detection and response (EDR) tools monitoring for LSASS access or suspicious PowerShell executions.

## Objectives

1. Generate a PRT-cookie for seamless browser authentication to Azure portals using extracted device credentials.
2. Obtain an access token via username and password for API calls or service principal impersonation.
3. Refresh an existing token to maintain persistent access without re-authentication.
4. Validate token usability by testing against Azure resource endpoints.

## Instructions

### Step 1: Generate PRT-Cookie from Mimikatz Data

**Context**: This step creates a browser-compatible PRT-cookie using derived keys and context from a compromised device's authentication artifacts. It is useful for maintaining session persistence in browser-based Azure management interfaces without prompting for credentials.

**Command** ([[commands/sharpaztoken-generate-cookie]]):
```powershell
SharpAzToken.exe cookie --derivedkey $_DERIVED_KEY --context $_CONTEXT --prt $_PRT
```

> Replace $_DERIVED_KEY, $_CONTEXT, and $_PRT with values extracted from Mimikatz (e.g., via 'sekurlsa::tickets' or 'dpapi::cloudap' modules). Run this on the compromised host. The command authenticates against Azure AD using the provided PRT and outputs a cookie string that can be imported into a browser session.

### Step 2: Generate Token Using Username and Password

**Context**: Use this method when username and password credentials are available, such as from a harvested credential dump. It performs a Resource Owner Password Credentials (ROPC) flow to obtain an access token for Azure resources, which can be used in subsequent API requests.

**Command** ([[commands/sharpaztoken-generate-token-username-password]]):
```powershell
SharpAzToken.exe token --username $_USERNAME --password $_PASSWORD
```

> Substitute $_USERNAME and $_PASSWORD with the target Azure AD account details. This step initiates an authentication request to Azure AD and returns a JSON response with access_token, refresh_token, and id_token if successful. Verify the token by decoding it at jwt.ms to confirm scopes and expiry.

### Step 3: Generate Token from Refresh Token

**Context**: When a refresh token is available (e.g., from a previous token acquisition), this step exchanges it for a new access token, enabling long-term persistence without exposing passwords. It is ideal for maintaining access after initial compromise.

**Command** ([[commands/sharpaztoken-generate-token-refresh]]):
```powershell
SharpAzToken.exe token --refreshtoken $_REFRESH_TOKEN
```

> Provide the $_REFRESH_TOKEN from a prior authentication. The command sends a refresh request to Azure AD and outputs updated tokens. Success is indicated by a new access_token with extended validity; test it against an Azure endpoint like graph.microsoft.com.
