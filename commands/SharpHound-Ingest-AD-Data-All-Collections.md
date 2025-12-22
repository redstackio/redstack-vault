---
id: c7f78e78-40b6-4eb9-b292-a59d1329a88e
name: SharpHound-Ingest-AD-Data-All-Collections
type: command
executor: powershell
data: >-
  SharpHound.exe -c All -d $_DOMAIN --LDAPUsername $_USERNAME --LDAPPassword
  $_PASSWORD
output: |-
  -----------------------------------------------
  Initializing SharpHound at 4:16 PM on 3/15/2020
  -----------------------------------------------

  ... Enumeration finished ... SharpHound Enumeration Completed!
created_at: '2020-03-15T23:15:05.164898+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - ad-enum
  - sharphound
verified: true
validated: true
---

# SharpHound-Ingest-AD-Data-All-Collections

## Command

```powershell
SharpHound.exe -c All -d $_DOMAIN --LDAPUsername $_USERNAME --LDAPPassword $_PASSWORD
```

## Description

This command runs SharpHound to ingest Active Directory data using all available collection methods, including users, groups, ACLs, sessions, and trusts. It authenticates via provided LDAP credentials and outputs JSON files for BloodHound analysis. Use this for comprehensive AD enumeration during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c All` | Collects all data types (users, groups, computers, trusts, ACLs, sessions) | Yes |
| `-d $_DOMAIN` | The target domain name (e.g., contoso.com) | Yes |
| `--LDAPUsername $_USERNAME` | Username for LDAP authentication | Yes |
| `--LDAPPassword $_PASSWORD` | Password for the LDAP user | Yes |

## Examples

### Basic Usage

```powershell
SharpHound.exe -c All -d contoso.com --LDAPUsername bob --LDAPPassword s3cr3tPASS
```

### Remote DC

```powershell
SharpHound.exe -c All -d contoso.com -dc 192.168.1.10 --LDAPUsername bob --LDAPPassword s3cr3tPASS
```

## Expected Output

The command initializes SharpHound, performs enumeration, and generates JSON files in the current directory (e.g., contoso-users.json, contoso-computers.json). Successful completion shows:

```
-----------------------------------------------
Initializing SharpHound at 4:16 PM on 3/15/2020
-----------------------------------------------

... Enumeration finished ... SharpHound Enumeration Completed!
```

Look for JSON files confirming data collection. Errors may indicate insufficient privileges or network issues.

## Related

- [[procedures/Map-Active-Directory-with-SharpHound]]
- [[tools/SharpHound]]
