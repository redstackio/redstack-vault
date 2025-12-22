---
id: 15fbc227-49aa-4542-9e2d-c23a23066209
name: nltest-dclist-domain
type: command
executor: cmd
data: 'nltest /dclist:$_DOMAIN_NAME'
output: null
created_at: '2023-04-06T03:56:28.627102+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - domain
  - discovery
verified: true
validated: true
---

# nltest-dclist-domain

## Command

```cmd
nltest /dclist:$_DOMAIN_NAME
```

## Description

Lists all domain controllers in the specified domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /dclist:$_DOMAIN_NAME | Domain name to query (e.g., contoso.com) | Yes |
| $_DOMAIN_NAME | FQDN of the domain | Yes |

## Examples

### Basic Usage

```cmd
nltest /dclist:contoso.com
```

## Expected Output

```
Getting list of DCs from [\contoso.com]:
    DC: \dc01.contoso.com
        Address: \192.168.1.10
        Dom Guid: {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}
        Site: Default-First-Site-Name
...
The command completed successfully
```

Provides DC IPs and GUIDs for targeting.

## Related

- [[procedures/windows-user-enumeration-and-privilege-check]]
- [[commands/nltest-dcname-domain]]
