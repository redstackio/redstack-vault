---
data: net localgroup administrators hacker /add
tags:
  - group
  - escalation
type: command
output: The command completed successfully.
executor: cmd
platforms:
  - Windows
id: 30d0e146-7e06-4999-a347-444608dbbce8
created_at: '2025-12-14T17:26:17.514Z'
updated_at: '2025-12-14T17:26:17.515Z'
verified: false
validated: true
submitted: true
---
# add-user-to-administrators

## Command

```cmd
net localgroup administrators hacker /add
```

## Description

Adds an existing local user to the Administrators group, granting elevated privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| administrators | Group name | Yes |
| hacker | Username | Yes |
| /add | Add to group flag | Yes |

## Examples

### Basic Usage

```cmd
net localgroup administrators hacker /add
```

### Advanced Usage

```cmd
net localgroup administrators hacker /add /domain
```
(Domain context if applicable)

## Expected Output

Success message; user added to group.

## Related

- [[procedures/Perform-Privilege-Escalation-via-Payload-Execution]]
