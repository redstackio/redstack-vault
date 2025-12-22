---
id: 69146a6c-1149-489f-9758-ddc37a5d88f5
name: sharpaztoken-generate-token-refresh
type: command
executor: powershell
data: SharpAzToken.exe token --refreshtoken $_REFRESH_TOKEN
output: null
created_at: '2023-05-24T07:39:51.365669+00:00'
updated_at: '2023-05-24T07:39:52.197066+00:00'
platforms:
  - Windows
tags:
  - azure
  - token
  - refresh
verified: true
validated: true
---

# sharpaztoken-generate-token-refresh

## Command

```powershell
SharpAzToken.exe token --refreshtoken $_REFRESH_TOKEN
```

## Description

This command refreshes an Azure access token using an existing refresh token via the SharpAzToken tool. It is used to obtain new access and refresh tokens without re-entering credentials, supporting persistent access in Azure AD.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --refreshtoken $_REFRESH_TOKEN | The refresh token string from a previous authentication | Yes |

## Examples

### Basic Usage

```powershell
SharpAzToken.exe token --refreshtoken "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6..."
```

### Advanced Usage

In a script to automate refresh:

```powershell
$refreshToken = Get-Content refresh.txt
SharpAzToken.exe token --refreshtoken $refreshToken | ConvertFrom-Json
```

## Expected Output

JSON output including {"access_token": "<jwt>", "refresh_token": "<new_refresh>", "expires_in": 3600}, indicating successful refresh. The access_token can be used immediately for Azure API calls.

## Related

- [[procedures/Generate-Azure-Tokens-with-SharpAzToken]]
- [[tools/SharpAzToken]]
