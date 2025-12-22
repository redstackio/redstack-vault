---
id: 03c23c26-1e6a-48d8-89b8-3d6ec79b8896
name: Curl Azure Get User Realm Info
type: command
executor: bash
data: >-
  curl
  "https://login.microsoftonline.com/getuserrealm.srf?login=<USER>@<DOMAIN>&xml=1"
output: null
created_at: '2023-05-23T17:02:42.392607+00:00'
updated_at: '2023-05-23T17:02:42.699898+00:00'
platforms:
  - Cloud
tags:
  - enumeration
  - azure
verified: true
validated: true
---

# Curl Azure Get User Realm Info

## Command

```bash
curl "https://login.microsoftonline.com/getuserrealm.srf?login=<USER>@<DOMAIN>&xml=1"
```

## Description

This command queries the Microsoft login endpoint to retrieve user realm information for a specified email, revealing if the Azure AD tenant is federated and providing authentication details. Use it during reconnaissance to check tenant configuration without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <USER> | Username part of the email (e.g., admin) | Yes |
| <DOMAIN> | Target domain (e.g., target.com) | Yes |
| -s | Silent mode (optional, suppresses progress) | No |

## Examples

### Basic Usage

```bash
curl "https://login.microsoftonline.com/getuserrealm.srf?login=admin@target.com&xml=1"
```

### With Silent Output

```bash
curl -s "https://login.microsoftonline.com/getuserrealm.srf?login=user@domain.com&xml=1" | xmllint --format -
```

## Expected Output

XML response like:
```xml
<UserRealm xmlns="http://schemas.datacontract.org/2004/07/Microsoft.Online.CORPM.Identity.Model">
  <Name>target.com</Name>
  <DisplayName>Target Domain</DisplayName>
  <IsFederated>true</IsFederated>
  <FederationMetadataUrl>https://target.com/adfs/ls/...</FederationMetadataUrl>
</UserRealm>
```
Indicates federation if <IsFederated>true</IsFederated>; otherwise, managed tenant.

## Related

- [[procedures/Azure Tenant ID Enumeration]]
- [[commands/curl-azure-get-tenant-realm-info]]
