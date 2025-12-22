---
type: command
executor: cmd
data: net localgroup administrators $_USERNAME /add
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - privilege-escalation
verified: true
validated: true
---

# net-localgroup-add-to-administrators

## Command

```cmd
net localgroup administrators $_USERNAME /add
```

## Description

Adds an existing local user to the Administrators group, granting elevated privileges on the system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | The username to add to the group | Yes |
| /add | Adds the user to the specified local group | Built-in |

## Examples

### Basic Usage

```cmd
net localgroup administrators hacker /add
```

### For Remote Desktop Group

```cmd
net localgroup "Remote Desktop Users" hacker /add
```

## Expected Output

The command completed successfully.

## Related

- [[procedures/windows-credential-enumeration]]
- [[commands/net-user-create-local-account]]
