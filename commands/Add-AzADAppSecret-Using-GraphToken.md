---
id: f9606cde-728e-429a-83e3-b3d721886d93
name: Add-AzADAppSecret-Using-GraphToken
type: command
executor: powershell
data: |-
  . C:\Tools\Add-AzADAppSecret.ps1
  Add-AzADAppSecret -GraphToken $graphtoken -Verbose
output: null
created_at: '2023-05-24T20:21:06.336735+00:00'
updated_at: '2023-05-24T20:21:06.612131+00:00'
platforms:
  - Cloud
tags:
  - azure-ad
  - service-principal
  - secret-addition
verified: true
validated: true
---

# Add-AzADAppSecret-Using-GraphToken

## Command

```powershell
. C:\Tools\Add-AzADAppSecret.ps1
Add-AzADAppSecret -GraphToken $graphtoken -Verbose
```

## Description

This command sources a custom PowerShell script (Add-AzADAppSecret.ps1) and executes it to add a client secret to an Azure AD application registration using a Microsoft Graph API access token. It is used in scenarios where an attacker or administrator needs to create persistent credentials for service principal authentication without interactive login.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $graphtoken | Valid Microsoft Graph API bearer token with Application.ReadWrite.All scope | Yes |
| -Verbose | Enables verbose logging for detailed output during execution | No |
| C:\Tools\Add-AzADAppSecret.ps1 | Path to the custom script file implementing the secret addition logic | Yes (must exist) |

## Examples

### Basic Usage

```powershell
$graphtoken = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6..."
. C:\Tools\Add-AzADAppSecret.ps1
Add-AzADAppSecret -GraphToken $graphtoken -Verbose
```

### Advanced Usage

Run in a script with error handling:

```powershell
try {
    . C:\Tools\Add-AzADAppSecret.ps1
    Add-AzADAppSecret -GraphToken $graphtoken -Verbose -ErrorAction Stop
    Write-Output "Secret added successfully"
} catch {
    Write-Error "Failed to add secret: $_"
}
```

## Expected Output

VERBOSE: Adding secret to application...
New secret created with value: abc123def456~...
Secret expires on: 2024-05-24T21:56:17Z

The output includes the generated secret value (capture it immediately), expiration details, and any API response errors if permissions are insufficient.

## Related

- [[procedures/Add-Azure-AD-App-Secret-for-Service-Principal-Authentication]]
- [[commands/Connect-AzAccount-As-Service-Principal-Using-Secret]]
