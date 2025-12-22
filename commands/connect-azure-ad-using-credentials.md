---
id: 789a6fe0-48da-4e4f-8107-a82c4bbbc188
name: connect-azure-ad-using-credentials
type: command
executor: powershell
data: >-
  $passwd = ConvertTo-SecureString "$_PASSWORD" -AsPlainText -Force; $creds =
  New-Object
  System.Management.Automation.PSCredential("$_UPN@$_TENANT.onmicrosoft.com",
  $passwd); Connect-AzureAD -Credential $creds
output: null
created_at: '2023-05-30T13:47:18.323598+00:00'
updated_at: '2023-05-30T13:47:19.298036+00:00'
platforms:
  - Cloud
tags:
  - azure-ad
  - authentication
verified: true
validated: true
---

# Connect Azure AD Using Credentials

## Command

```powershell
$passwd = ConvertTo-SecureString "$_PASSWORD" -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential("$_UPN@$_TENANT.onmicrosoft.com", $passwd)
Connect-AzureAD -Credential $creds
```

## Description

This command sets up secure credentials from a plaintext password and UPN, then connects to the Azure AD tenant. It establishes an authenticated session for subsequent enumeration cmdlets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PASSWORD | Plaintext password for the account | Yes |
| $_UPN | User Principal Name without domain (e.g., testuser) | Yes |
| $_TENANT | Tenant name (e.g., contoso) | Yes |
| -Credential | Uses the PSCredential object for auth | Built-in |

## Examples

### Basic Usage

```powershell
$passwd = ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential("testuser@contoso.onmicrosoft.com", $passwd)
Connect-AzureAD -Credential $creds
```

### Advanced Usage

For service principals, use -CertificateThumbprint instead, but this variant sticks to username/password.

## Expected Output

Welcome To Azure AD PowerShell!

To get started, run Get-AzureADUser -SearchString "<your UPN>"

Or, to view all cmdlets, type Get-Command | Where-Object {$_.Source -eq "AzureAD"}

No errors indicate successful connection.

## Related

- [[procedures/azure-ad-enumeration-using-powershell-with-credentials]]
- [[commands/get-all-azure-ad-users]]
