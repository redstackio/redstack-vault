---
id: 7df9f49d-577c-464a-a5e6-423db51ab503
name: get-all-azure-ad-users
type: command
executor: powershell
data: Get-AzureADUser -All $true
output: null
created_at: '2023-05-23T19:33:22.164030+00:00'
updated_at: '2023-05-23T19:33:22.785549+00:00'
platforms:
  - Cloud
tags:
  - azure-ad
  - enumeration
  - users
verified: true
validated: true
---

# Get All Azure AD Users

## Command

```powershell
Get-AzureADUser -All $true
```

## Description

Retrieves all user objects in the Azure AD tenant, including guest and service accounts. Use after connecting to list directory users comprehensively.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -All | Retrieves all objects beyond the default page size | Yes |
| $true | Boolean flag to enable all results | Built-in |

## Examples

### Basic Usage

```powershell
Get-AzureADUser -All $true
```

### Advanced Usage

Pipe to select specific properties: Get-AzureADUser -All $true | Select-Object DisplayName, UserPrincipalName

## Expected Output

ObjectId                             DisplayName         UserPrincipalName                    UserType
--------                             -----------         -----------------                    --------
12345678-...                        John Doe            john.doe@contoso.onmicrosoft.com     Member
87654321-...                        Jane Smith          jane.smith@contoso.onmicrosoft.com   Member

## Related

- [[procedures/azure-ad-enumeration-using-powershell-with-credentials]]
- [[commands/get-azure-ad-users-userprincipalname]]
