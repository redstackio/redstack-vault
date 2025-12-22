---
id: edb0b0e5-77e3-4f69-9e08-9270192ec526
name: connect-to-azure-ad
type: command
executor: powershell
data: Connect-AzureAD -Credential (Get-Credential)
output: null
created_at: '2023-04-06T03:56:15.819994+00:00'
updated_at: '2023-04-10T20:19:27.894315+00:00'
platforms:
  - azure-ad
tags:
  - authentication
  - azure
verified: true
validated: true
---

# connect-to-azure-ad

## Command

```powershell
Connect-AzureAD -Credential (Get-Credential)
```

## Description

This command initiates an interactive login to Azure Active Directory using provided credentials, establishing a session for subsequent AzureAD module operations like user management.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Credential | Specifies the user credentials for authentication (prompts interactively) | Yes |

## Examples

### Basic Usage

```powershell
Connect-AzureAD -Credential (Get-Credential)
```

### Advanced Usage

For non-interactive use with stored credentials:

```powershell
$SecurePassword = ConvertTo-SecureString "password" -AsPlainText -Force
$Credential = New-Object System.Management.Automation.PSCredential("user@tenant.com", $SecurePassword)
Connect-AzureAD -Credential $Credential
```

## Expected Output

Welcome To Azure AD PowerShell
...
Account : user@tenant.onmicrosoft.com
TenantId : xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

This indicates a successful connection to the specified tenant.

## Related

- [[procedures/Set-Secondary-Email-for-Azure-AD-User]]
