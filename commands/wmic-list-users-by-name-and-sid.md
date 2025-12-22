---
type: command
executor: command_prompt
data: 'wmic.exe useraccount get name,sid'
tags:
  - discovery
  - users
platforms:
  - Windows
verified: true
validated: true
---

# wmic-list-users-by-name-and-sid

## Command

```command_prompt
wmic.exe useraccount get name,sid
```

## Description

Queries the local system for all user accounts, displaying usernames and their Security Identifiers (SIDs) using the built-in WMIC tool. Useful for identifying target user SIDs in domain environments without external tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| useraccount | WMI class for user accounts | Yes (built-in) |
| get name,sid | Fields to retrieve: username and SID | Yes |

## Examples

### Basic Usage

```command_prompt
wmic.exe useraccount get name,sid
```

### Advanced Usage

Filter by name: wmic.exe useraccount where name="bob" get sid

## Expected Output

Name                SID
Administrator       S-1-5-21-1576920733-1301476157-954876328-500
bob                 S-1-5-21-1576920733-1301476157-954876328-1108

List of local and domain users with SIDs.

## Related

- [[procedures/Extract-Chrome-Cookies-and-Credentials-from-User-Profile-with-Domain-Admin]]
