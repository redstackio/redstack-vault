---
id: 4b29c207-83b4-4694-b50c-fe7e669c269e
name: nltest-dsgetdc-domain
type: command
executor: cmd
data: 'nltest /dsgetdc:$_DOMAIN_NAME'
output: null
created_at: '2023-04-06T03:56:28.627255+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - domain
  - discovery
verified: true
validated: true
---

# nltest-dsgetdc-domain

## Command

```cmd
nltest /dsgetdc:$_DOMAIN_NAME
```

## Description

Gets detailed information about the domain controller for the specified domain, including GUIDs and flags.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /dsgetdc:$_DOMAIN_NAME | Domain name | Yes |
| $_DOMAIN_NAME | FQDN of the domain | Yes |

## Examples

### Basic Usage

```cmd
nltest /dsgetdc:contoso.com
```

## Expected Output

```
DC: \dc01.contoso.com
Address: \192.168.1.10
Dom Guid: {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}
OurSiteName: Default-First-Site-Name
Flags: PDC GC DS LDAP KDC TIMESERV GTIMESERV WRITABLE
The command completed successfully
```

Details DC capabilities (e.g., PDC, GC).

## Related

- [[procedures/windows-user-enumeration-and-privilege-check]]
- [[commands/nltest-dclist-domain]]
