---
id: 64f90c07-fdce-4a70-bbc1-97e7b91f3520
name: Azure Token Generation and Authentication with SharpAzToken
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.338573+00:00'
updated_at: '2023-05-24T07:41:56.224480+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Steal Application Access Token|T1528 - Steal Application Access Token]]'
tags:
- '[[Cloud - Azure]]'
- '[[Refresh Tokens]]'
- '[[Token from Managed Identity]]'
commands:
- '[[SharpAzToken Cookie]]'
- '[[SharpAzToken Token with Refresh Token]]'
- '[[SharpAzToken Token with Username and Password]]'
---

# Azure Token Generation and Authentication with SharpAzToken

**Status**: ✓ Verified

## Summary

The SharpAzToken tool offers three essential commands for generating  tokens and creating a PRT-Cookie for browser authentication. These  commands, namely 'cookie', 'token', and 'refreshtoken', serve different  purposes in the token generation process. They allow you to obtain  tokens based on vari

## Description

# Description

The SharpAzToken tool offers three essential commands for generating  tokens and creating a PRT-Cookie for browser authentication. These  commands, namely 'cookie', 'token', and 'refreshtoken', serve different  purposes in the token generation process. They allow you to obtain  tokens based on various authentication factors such as derived keys,  credentials, or refresh tokens. This procedure focuses on utilizing  these commands to authenticate and access Azure resources effectively.

## Requirements

1. The SharpAzToken tool is installed and accessible.

1. The required authentication factors (derived key, context, PRT, username, password, refresh token) are available.

1. Proper permissions are granted to interact with Azure resources.

## Defense

1. Limit the usage of the SharpAzToken tool to trusted individuals or applications.

1. Regularly monitor logs and audit trails for any suspicious activities.

1. Implement strong password policies and consider multi-factor authentication.

## Objectives

1. Create a PRT-Cookie for browser authentication using derived keys and context.

1. Generate a token based on a username and password for authentication.

1. Obtain a token from a refresh token for continuous access to Azure resources.

# Instructions

*<u>Overvi*ew </u>

**Code**: [[# Create a PRT-Cookie for the browser
SharpAzToken]]

> The 'cookie' command requires the derived key, context, and PRT obtained from Mimikatz. The 'mdm' command requires the access token, device name, and output PFX file path. The 'token' command requires either a username and password combination or a refresh token. The 'devicekeys' command requires the PFX file path and either a refresh token or a username and password combination.

**1. Create a PRT-Cookie for the browser using the 'cookie' command**

**Command** ([[SharpAzToken Cookie]]):

```bash
SharpAzToken.exe cookie --derivedkey <Key from Mimikatz> --context <Context from Mimikatz> --prt <PRT from Mimikatz>
```

- Replace `<Key from Mimikatz>` with the derived key obtained from Mimikatz.
Provide the `<Context from Mimikatz>` acquired from Mimikatz.
Specify the `<PRT from Mimikatz>` obtained from Mimikatz.

**2. Create a token using the 'token' command with a username and password:**

**Command** ([[SharpAzToken Token with Username and Password]]):

```bash
SharpAzToken.exe token --username <Username> --password <Password>
```

- Replace `<Username>` with the appropriate username for authentication.
Provide the `<Password>` associated with the provided username.

**3. Generate a token from a refresh token using the 'token' command:**

**Command** ([[SharpAzToken Token with Refresh Token]]):

```bash
SharpAzToken.exe token --refreshtoken <RefreshToken>
```

- Specify the `<RefreshToken>` acquired from a previous token.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Steal Application Access Token|T1528 - Steal Application Access Token]]

## Commands Used

- [[SharpAzToken Cookie]]
- [[SharpAzToken Token with Refresh Token]]
- [[SharpAzToken Token with Username and Password]]

## Tags

- [[Cloud - Azure]]
- [[Refresh Tokens]]
- [[Token from Managed Identity]]
