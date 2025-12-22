---
id: b9e9873d-7ed3-49d3-98b0-5ff2e3a8d8ba
type: command
executor: cmd
data: net localgroup Administrators $_USERNAME /add
output: |-
  C:\Windows\system32> net localgroup Administrators hacker /add
  The command completed successfully.
created_at: '2019-11-14T00:19:34.666164+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - persistence
  - privilege-escalation
verified: true
validated: true
---

# windows-add-user-to-local-administrators-group

## Command

```cmd
net localgroup Administrators $_USERNAME /add
```

## Description

This command adds an existing local user to the Administrators group on a Windows system, granting full administrative privileges. It is a key step in persistence after user creation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | The username to add to the group (must exist) | Yes |
| /add | Flag to add the user to the group (built-in) | Yes |

## Examples

### Basic Usage

```cmd
net localgroup Administrators backupadmin /add
```

### Advanced Usage

To verify membership: `net localgroup Administrators`. This command assumes the user already exists.

## Expected Output

```
C:\Windows\system32> net localgroup Administrators hacker /add
The command completed successfully.
```

Errors may occur if the user does not exist or if privileges are insufficient.

## Related

- [[procedures/Add-Local-Administrator-to-Windows]]
