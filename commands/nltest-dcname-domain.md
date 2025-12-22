---
id: eb2a053d-47db-4d45-ad62-f173ad2ec7db
name: nltest-dcname-domain
type: command
executor: cmd
data: 'nltest /dcname:$_DOMAIN_NAME'
output: null
created_at: '2023-04-06T03:56:28.627194+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - domain
  - discovery
verified: true
validated: true
---

# nltest-dcname-domain

## Command

```cmd
nltest /dcname:$_DOMAIN_NAME
```

## Description

Retrieves the name of the domain controller that authenticated the current user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /dcname:$_DOMAIN_NAME | Domain name | Yes |
| $_DOMAIN_NAME | FQDN of the domain | Yes |

## Examples

### Basic Usage

```cmd
nltest /dcname:contoso.com
```

## Expected Output

```
DC: \dc01.contoso.com
The command completed successfully
```

Shows the authenticating DC.

## Related

- [[procedures/windows-user-enumeration-and-privilege-check]]
- [[commands/nltest-dclist-domain]]
