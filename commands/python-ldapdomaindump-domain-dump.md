---
type: command
executor: bash
data: python3 ldapdomaindump.py -u "$_DOMAIN\\$_USERNAME" -p $_PASSWORD $_DC_IP
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - active-directory
  - enumeration
  - dump
verified: true
validated: true
---

# python-ldapdomaindump-domain-dump

## Command

```bash
python3 ldapdomaindump.py -u "$_DOMAIN\\$_USERNAME" -p $_PASSWORD $_DC_IP
```

## Description

Dumps the entire Active Directory domain structure via LDAP to JSON files for offline analysis, including all users, groups, and attributes like adminCount.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u "$_DOMAIN\\$_USERNAME" | Domain\username for auth | Yes |
| -p $_PASSWORD | Password | Yes |
| $_DC_IP | Domain controller IP | Yes |

## Examples

### Basic Usage

```bash
python3 ldapdomaindump.py -u 'domain\user' -p pass 10.10.10.10
```

### Advanced Usage

```bash
python3 ldapdomaindump.py -u 'domain\user' -p pass --scope sub 10.10.10.10
```

## Expected Output

```
[*] Dumping domain: domain.com
[*] Wrote users to domain_users.json
[*] Wrote groups to domain_groups.json
```

## Related

- [[procedures/AdminCount-Abuse]]
- [[commands/jq-filter-admincount-accounts]]
