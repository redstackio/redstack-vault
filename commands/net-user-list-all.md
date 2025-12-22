---
id: fc6ad199-5f9c-4ed0-9bb6-9de662ed18ad
name: net-user-list-all
type: command
executor: cmd
data: net user
output: null
created_at: '2023-04-06T03:56:28.626849+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - discovery
verified: true
validated: true
---

# net-user-list-all

## Command

```cmd
net user
```

## Description

Lists all local user accounts on the system with basic status info like account active and password required.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Lists all users | Yes |

## Examples

### Basic Usage

```cmd
net user
```

## Expected Output

```
The request will be processed at a time chosen by the logon server.

User accounts for \\COMPUTERNAME

-------------------------------------------------------------------------------
Administrator            Guest                    DefaultAccount
...
The command completed successfully.
```

Shows usernames; follow with net user <name> for details.

## Related

- [[procedures/windows-user-enumeration-and-privilege-check]]
- [[commands/net-user-admin-query]]
