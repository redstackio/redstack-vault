---
id: 99eea854-d8b5-48aa-a448-949e408c01fa
name: wmic-list-user-accounts-with-sid
type: command
executor: command_prompt
data: 'wmic.exe useraccount get name,sid'
output: |-
  C:\Windows\system32> wmic.exe useraccount get name,sid
  Name                SID
  Administrator       S-1-5-21-2422005997-3268604389-1371308432-500
  DefaultAccount      S-1-5-21-2422005997-3268604389-1371308432-503
  Guest               S-1-5-21-2422005997-3268604389-1371308432-501
  localadmin          S-1-5-21-2422005997-3268604389-1371308432-1001
  WDAGUtilityAccount  S-1-5-21-2422005997-3268604389-1371308432-504
  Administrator       S-1-5-21-1576920733-1301476157-954876328-500
  Guest               S-1-5-21-1576920733-1301476157-954876328-501
  krbtgt              S-1-5-21-1576920733-1301476157-954876328-502
  alice               S-1-5-21-1576920733-1301476157-954876328-1106
  Administrator       S-1-5-21-3428605742-3005092657-1212549955-500
  Guest               S-1-5-21-3428605742-3005092657-1212549955-501
  krbtgt              S-1-5-21-3428605742-3005092657-1212549955-502
  superadmin          S-1-5-21-3428605742-3005092657-1212549955-1105
  dave                S-1-5-21-3428605742-3005092657-1212549955-1106
  bob                 S-1-5-21-3428605742-3005092657-1212549955-1109
  sally               S-1-5-21-3428605742-3005092657-1212549955-1110
created_at: '2020-07-21T05:42:41.809918+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - users
  - sid
verified: true
validated: true
---

# wmic-list-user-accounts-with-sid

## Command

```command_prompt
wmic.exe useraccount get name,sid
```

## Description

This command queries Windows Management Instrumentation (WMI) to list all local user accounts along with their Security Identifiers (SIDs). It is useful for identifying target users during post-exploitation to locate profile paths or protected data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `useraccount` | WMI class for user accounts | Yes (built-in) |
| `get name,sid` | Fields to retrieve: username and SID | Yes (built-in) |

## Examples

### Basic Usage

```command_prompt
wmic.exe useraccount get name,sid
```

Lists all users in a table format.

### Advanced Usage

```command_prompt
wmic.exe useraccount get name,sid where name="bob"
```

Filters for a specific user.

## Expected Output

A table showing usernames and their SIDs, such as:

```
Name                SID
Administrator       S-1-5-21-2422005997-3268604389-1371308432-500
bob                 S-1-5-21-3428605742-3005092657-1212549955-1109
```

## Related

- [[procedures/Extract-Chrome-Credentials-and-Cookies-Using-User-Password]]
- [[tools/Mimikatz]]
