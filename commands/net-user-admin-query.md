---
id: 466e3376-d9f9-4ad9-8fc1-72308d55908b
name: net-user-admin-query
type: command
executor: cmd
data: net user administrator
output: null
created_at: '2023-04-06T03:56:28.626789+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - discovery
verified: true
validated: true
---

# net-user-admin-query

## Command

```cmd
net user $_USERNAME
```

## Description

Queries detailed information for a specific user account, such as status, password age, and comments. Use for built-in accounts like administrator.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Target username (e.g., administrator, %USERNAME%) | Yes |

## Examples

### Query Administrator

```cmd
net user administrator
```

### Query Current User

```cmd
net user %USERNAME%
```

## Expected Output

```
The request will be processed at a time chosen by the logon server.

User name                    administrator
Full Name                     
Comment                       Built-in account for administering the computer/domain
...
Account active                Yes
Account expires               Never
Password last set             [date]
Password expires              Never
...
The command completed successfully.
```

Reveals if account is locked or password is old.

## Related

- [[procedures/windows-user-enumeration-and-privilege-check]]
- [[commands/net-user-list-all]]
