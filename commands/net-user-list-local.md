---
id: e9d9221d-da65-41df-81f3-91835a3d1037
name: net-user-list-local
type: command
executor: command_prompt
data: net user
output: >-
  User accounts for \\DESKTOP-29CSGFA


  -------------------------------------------------------------------------------

  Administrator            Bob                      DefaultAccount

  Guest                    Alice                    WDAGUtilityAccount

  The command completed successfully.
created_at: '2020-03-18T01:08:37.458677+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - windows
verified: true
validated: true
---

# net-user-list-local

## Command

```command_prompt
net user
```

## Description

Lists all local user accounts on a Windows system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| net user | Built-in command | Yes |

## Examples

### Basic Usage

```command_prompt
net user
```

### Redirect Output

```command_prompt
net user > users.txt
```

## Expected Output

Description: Table of user accounts like Administrator, Guest.

## Related

- [[procedures/Enumerate-Local-Users-and-Groups-on-Windows]]
