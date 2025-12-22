---
id: 35182687-d3af-437e-a7ba-9f8294033bcc
name: net-user-info-and-groups
type: command
executor: command_prompt
data: net user $_USER
output: |-
  User name                    Bob
  Full Name
  Comment
  User's comment
  Country/region code          000 (System Default)
  Account active               Yes
  Account expires              Never

  Password last set            3/10/2020 12:50:20 PM
  Password expires             Never
  Password changeable          3/10/2020 12:50:20 PM
  Password required            No
  User may change password     Yes

  Workstations allowed         All
  Logon script
  User profile
  Home directory
  Last logon                   3/10/2020 6:34:36 PM

  Logon hours allowed          All

  Local Group Memberships      *Administrators       *docker-users
                               *Hyper-V Administrator*Performance Log Users
  Global Group memberships     *None
  The command completed successfully.
created_at: '2020-03-20T20:55:40.966792+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - windows
verified: true
validated: true
---

# net-user-info-and-groups

## Command

```command_prompt
net user $_USER
```

## Description

Retrieves detailed information and group memberships for a specific local user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USER | Username (e.g., Bob) | Yes |

## Examples

### Basic Usage

```command_prompt
net user Administrator
```

### For Domain User

```command_prompt
net user DOMAIN\user
```

## Expected Output

Description: User details including active status, last logon, and group memberships.

## Related

- [[procedures/Enumerate-Local-Users-and-Groups-on-Windows]]
