---
id: c6ac19e3-ecee-4ded-a8ed-0f24c5c033c4
name: sharpaztoken-generate-token-username-password
type: command
executor: powershell
data: SharpAzToken.exe token --username $_USERNAME --password $_PASSWORD
output: null
created_at: '2023-05-24T07:39:51.364982+00:00'
updated_at: '2023-05-24T07:39:52.197066+00:00'
platforms:
  - Windows
tags:
  - azure
  - token
  - ropc
verified: true
validated: true
---

# sharpaztoken-generate-token-username-password

## Command

```powershell
SharpAzToken.exe token --username $_USERNAME --password $_PASSWORD
```

## Description

This command generates an Azure access token using username and password credentials through the Resource Owner Password Credentials (ROPC) flow with SharpAzToken. It is applicable when direct credential use is possible, such as in non-MFA enforced scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --username $_USERNAME | The Azure AD username (e.g., user@domain.com) | Yes |
| --password $_PASSWORD | The plaintext password for the account | Yes |

## Examples

### Basic Usage

```powershell
SharpAzToken.exe token --username "user@contoso.com" --password "P@ssw0rd123"
```

### Advanced Usage

With secure string handling:

```powershell
$securePass = ConvertTo-SecureString "P@ssw0rd123" -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential("user@contoso.com", $securePass)
SharpAzToken.exe token --username $credential.UserName --password $credential.GetNetworkCredential().Password
```

## Expected Output

Returns JSON with {"token_type": "Bearer", "access_token": "<jwt>", "expires_in": 3599, "refresh_token": "<refresh>"}, confirming authentication success. Use the access_token in Authorization headers for Azure REST APIs.

## Related

- [[procedures/Generate-Azure-Tokens-with-SharpAzToken]]
- [[tools/SharpAzToken]]
