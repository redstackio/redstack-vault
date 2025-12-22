---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: dnstool-query-dns-records
type: command
executor: bash
data: >-
  python dnstool.py -u '$_DOMAIN\$_USERNAME' -p '$_PASSWORD' --record
  '$_RECORD_TYPE' --action query $_DC_HOSTNAME --legacy
output: null
created_at: '2023-04-06T03:56:06.634711Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
  - Linux
tags:
  - dns-query
  - active-directory
verified: true
validated: true
---

# dnstool-query-dns-records

## Command

```bash
python dnstool.py -u '$_DOMAIN\$_USERNAME' -p '$_PASSWORD' --record '$_RECORD_TYPE' --action query $_DC_HOSTNAME --legacy
```

## Description

This command uses dnstool.py from the Impacket suite to query DNS records stored in Active Directory via LDAP. It supports wildcard queries for broad enumeration and includes a legacy mode for older domain controllers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u '$_DOMAIN\$_USERNAME' | Domain credentials in DOMAIN\user format | Yes |
| -p '$_PASSWORD' | Password for the user | Yes |
| --record '$_RECORD_TYPE' | Record type to query (e.g., '*', 'A', 'SRV') | Yes |
| --action query | Action to perform: query records | Yes |
| $_DC_HOSTNAME | Domain controller hostname or IP | Yes |
| --legacy | Enable compatibility for Windows Server 2003/2008 | No |

## Examples

### Basic Usage

```bash
python dnstool.py -u 'CORP\attacker' -p 'Passw0rd' --record '*' --action query dc.corp.local
```

### Advanced Usage

```bash
python dnstool.py -u 'CORP\attacker' -p 'Passw0rd' --record 'SRV' --action query 192.168.1.10 --legacy
```

## Expected Output

```
[*] Querying DNS records on dc.corp.local
Record: dc.corp.local A 192.168.1.10
Record: _ldap._tcp.corp.local SRV 0 100 389 dc.corp.local
[*] Query complete
```

Outputs matching DNS records with type, name, and data.

## Related

- [[procedures/Active-Directory-Integrated-DNS-Enumeration]]
- [[tools/dnstool]]
