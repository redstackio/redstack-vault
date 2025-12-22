---
id: 97fdc350-f50f-4e6c-a7fa-67df12c237a0
name: az-login-with-username-password
type: command
executor: bash
data: az login -u $_USERNAME -p $_PASSWORD
output: null
created_at: '2023-05-25T04:48:48.222530+00:00'
updated_at: '2023-05-25T04:48:49.579271+00:00'
platforms:
  - Cloud
tags:
  - az-cli
  - authentication
verified: true
validated: true
---

# az-login-with-username-password

## Command

```bash
az login -u $_USERNAME -p $_PASSWORD
```

## Description

This command authenticates to Azure using username and password credentials, establishing a session for subsequent az-cli operations. Use this in scenarios where interactive browser login is not feasible, such as automated scripts or compromised environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u, --username $_USERNAME | Azure AD username (e.g., user@tenant.onmicrosoft.com) | Yes |
| -p, --password $_PASSWORD | Password for the account | Yes |

## Examples

### Basic Usage

```bash
az login -u test@contoso.onmicrosoft.com -p SecurePass123
```

### Advanced Usage

For tenant-specific login:
```bash
az login -u test@contoso.onmicrosoft.com -p SecurePass123 --tenant $_TENANT_ID
```

## Expected Output

Successful login displays:
```
[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "xxxx-xxxx-xxxx-xxxx",
    "id": "https://management.azure.com/",
    "isDefault": true,
    "managedByTenants": [],
    "name": "AzureCloud",
    "state": "LoggedIn",
    "tenantId": "xxxx-xxxx-xxxx-xxxx",
    "user": {
      "name": "test@contoso.onmicrosoft.com",
      "type": "user"
    }
  }
]
Note: current account is 'test@contoso.onmicrosoft.com' in tenant 'contoso.onmicrosoft.com'.
```

If failed, it shows authentication errors like invalid credentials.

## Related

- [[procedures/Azure-Tenant-Enumeration-with-Az-CLI]]
- [[tools/Azure-CLI]]
