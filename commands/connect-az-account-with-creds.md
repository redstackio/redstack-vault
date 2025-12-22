---
type: command
executor: powershell
data: >-
  $passwd = ConvertTo-SecureString "$_PASSWORD" -AsPlainText -Force

  $creds = New-Object System.Management.Automation.PSCredential
  ("$_USERNAME@$_TENANT_NAME.onmicrosoft.com", $passwd)

  Connect-AzAccount -Credential $creds
output: null
platforms:
  - Cloud
tags:
  - az-powershell
  - authentication
verified: true
validated: true
---

# Connect to Azure Account with Creds

## Command

```powershell
$passwd = ConvertTo-SecureString "$_PASSWORD" -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential ("$_USERNAME@$_TENANT_NAME.onmicrosoft.com", $passwd)
Connect-AzAccount -Credential $creds
```

## Description

This command creates a PSCredential object from a plaintext password and connects to an Azure account using non-interactive authentication. Use it when you have username/password creds for initial tenant access during enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PASSWORD | Plaintext password for the Azure AD user | Yes |
| $_USERNAME | Username without domain (e.g., 'test') | Yes |
| $_TENANT_NAME | Azure tenant name (e.g., 'contoso') | Yes |
| -Credential | Specifies the credential object for authentication | Built-in |

## Examples

### Basic Usage

```powershell
$passwd = ConvertTo-SecureString "MyP@ssw0rd" -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential ("test@contoso.onmicrosoft.com", $passwd)
Connect-AzAccount -Credential $creds
```

### Advanced Usage

For multi-tenant: Add -TenantId parameter to Connect-AzAccount if needed.

```powershell
Connect-AzAccount -Credential $creds -TenantId "xxxx-xxxx-xxxx-xxxx"
```

## Expected Output

Successful connection returns a JSON object:

```json
{
  "environmentName": "AzureCloud",
  "account": {
    "id": "test@contoso.onmicrosoft.com",
    "type": "user"
  },
  "context": {
    "tenant": {
      "id": "yyyy-yyyy-yyyy-yyyy"
    },
    "subscription": {
      "id": "zzzz-zzzz-zzzz-zzzz"
    }
  }
}
```

If failed: Error like "AADSTS50126: Invalid username or password."

## Related

- [[Azure Tenant Enumeration with Az PowerShell (Creds)]
- [[tools/az-powershell-module]]
