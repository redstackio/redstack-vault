---
type: command
executor: cmd
data: nslookup -type=srv _ldap._tcp.dc._msdcs.domain.com
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - reconnaissance
  - dns
  - active-directory
verified: true
validated: true
---

# nslookup-srv-ldap-domain-controllers

## Command

```cmd
nslookup -type=srv _ldap._tcp.dc._msdcs.domain.com
```

## Description

Queries DNS for SRV records related to LDAP services on domain controllers, revealing DCs, ports, and priorities in an AD domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain.com | Target domain (e.g., contoso.com) | Yes |
| -type=srv | Specifies SRV record query | Yes |
| _ldap._tcp.dc._msdcs.domain.com | AD-specific SRV record path | Yes |

## Examples

### Basic Usage

```cmd
nslookup -type=srv _ldap._tcp.dc._msdcs.contoso.com
```

## Expected Output

_ldap._tcp.dc._msdcs.contoso.com	service location:
	priority	= 0
	weight    	= 100
	port      	= 389
	svchost   	= dc01.contoso.com [192.168.1.10]

## Related

- [[procedures/Active-Directory-Domain-Controller-Lookup]]
- [[commands/nslookup-domain-resolution]]
