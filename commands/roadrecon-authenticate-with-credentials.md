---
id: e88ed08d-c82e-491b-9e01-98770f7a31f0
type: command
executor: bash
data: roadrecon auth -u test@<TENANT NAME>.onmicrosoft.com -p <PASSWORD>
output: null
created_at: '2023-04-06T03:56:14.584727+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - auth
  - azure
verified: true
validated: true
---

# roadrecon-authenticate-with-credentials

## Command

```bash
roadrecon auth -u $_USERNAME -p $_PASSWORD
```

## Description

Authenticates to Azure AD using username and password for ROADRecon tool, obtaining tokens for subsequent data gathering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u, $_USERNAME | Azure AD username (e.g., user@tenant.onmicrosoft.com) | Yes |
| -p, $_PASSWORD | Password for the account | Yes |
| -t, $_TENANT | Tenant name (optional, inferred from username) | No |
| --device-code | Use device code flow for MFA | No |

## Examples

### Basic Usage

```bash
roadrecon auth -u test@contoso.onmicrosoft.com -p MyPassword
```

### With Tenant

```bash
roadrecon auth -u test@contoso.onmicrosoft.com -p MyPassword -t contoso
```

## Expected Output

Tokens saved to tokenfile; success message: "Authentication successful".

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/ROADRecon]]
