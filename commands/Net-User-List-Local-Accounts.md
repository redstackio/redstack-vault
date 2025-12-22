---
type: command
executor: command_prompt
data: net user
output: >-
  User accounts for \\TARGET


  -------------------------------------------------------------------------------

  Administrator            Guest                    testuser

  The command completed successfully.
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - users
verified: true
validated: true
---

# Net-User-List-Local-Accounts

## Command

```command_prompt
net user
```

## Description

Lists all local user accounts on the system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| net user | Built-in command | Yes |

## Examples

### Basic Usage

```command_prompt
net user
```

### Advanced Usage

```command_prompt
net user /domain
```

Domain users.

## Expected Output

List of local accounts.

## Related

- [[procedures/List-Local-Users-on-Windows]]
