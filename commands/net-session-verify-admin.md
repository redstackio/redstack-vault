---
data: net session
tags:
  - discovery
  - privilege-check
type: command
output: There are no entries in this list
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.407Z'
id: 356e4248-71c5-42c4-a95b-4e71ea0aad06
verified: false
validated: true
submitted: true
---
# Net Session Verify Admin

## Command

```cmd
net session
```

## Description

Checks for open administrative sessions to confirm elevated privileges in a Windows command shell. Used post-exploitation to verify admin access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | No parameters; queries current sessions | No |

## Examples

### Basic Usage

```cmd
net session
```

### Advanced Usage

Not applicable; single command.

## Expected Output

Admin: "The command completed successfully. There are no entries in this list." Non-admin: "Access is denied."

## Related

- [[Related Procedure: Verify Administrative Privileges]]
