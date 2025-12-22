---
id: cff31ded-34e6-4527-a683-861fe9f58cd3
name: Curl Azure Get Tenant Realm Info
type: command
executor: bash
data: >-
  curl
  "https://login.microsoftonline.com/getuserrealm.srf?login=root@<TENANT-NAME>.onmicrosoft.com&xml=1"
output: null
created_at: '2023-05-23T17:02:42.393622+00:00'
updated_at: '2023-05-23T17:02:42.699898+00:00'
platforms:
  - Cloud
tags:
  - enumeration
  - azure
verified: true
validated: true
---

# Curl Azure Get Tenant Realm Info

## Command

```bash
curl "https://login.microsoftonline.com/getuserrealm.srf?login=root@<TENANT-NAME>.onmicrosoft.com&xml=1"
```

## Description

This command checks the tenant-level realm information using the onmicrosoft.com domain, determining federation status for the entire Azure AD tenant. Ideal for initial validation when user details are unknown.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <TENANT-NAME> | Suspected tenant name (e.g., target) | Yes |
| -s | Silent mode (optional) | No |

## Examples

### Basic Usage

```bash
curl "https://login.microsoftonline.com/getuserrealm.srf?login=root@target.onmicrosoft.com&xml=1"
```

### Formatted Output

```bash
curl -s "https://login.microsoftonline.com/getuserrealm.srf?login=root@tenant.onmicrosoft.com&xml=1" | xmllint --format -
```

## Expected Output

XML similar to user realm, e.g.:
```xml
<UserRealm>
  <Name>target.onmicrosoft.com</Name>
  <IsFederated>false</IsFederated>
</UserRealm>
```
Success if valid XML without 'not found' errors.

## Related

- [[procedures/Azure Tenant ID Enumeration]]
- [[commands/curl-azure-get-user-realm-info]]
