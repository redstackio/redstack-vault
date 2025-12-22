---
type: command
executor: cmd
data: nslookup domain.com
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - reconnaissance
  - dns
verified: true
validated: true
---

# nslookup-domain-resolution

## Command

```cmd
nslookup domain.com
```

## Description

Performs a basic DNS A record lookup for the specified domain, resolving IP addresses of hosts associated with it, often including domain controllers in AD environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain.com | Target domain name (e.g., contoso.com) | Yes |

## Examples

### Basic Usage

```cmd
nslookup contoso.com
```

### With Specific DNS Server

```cmd
nslookup contoso.com 8.8.8.8
```

## Expected Output

Server:  dc01.contoso.com
Address:  192.168.1.10

Name:    contoso.com
Addresses:  192.168.1.10
            192.168.1.11

## Related

- [[procedures/Active-Directory-Domain-Controller-Lookup]]
- [[commands/nslookup-srv-ldap-domain-controllers]]
