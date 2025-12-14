---
id: net-session-001
data: net session
tags:
  - privilege-check
type: command
output: There are no entries in this list.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.081Z'
verified: false
validated: true
submitted: true
---
# net-session-check-admin

## Command

```cmd
net session
```

## Description

Checks if the current user has Administrator privileges by attempting to query active network sessions, which requires elevated access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; runs default query | No |

## Examples

### Basic Usage

```cmd
net session
```

### Advanced Usage

Not applicable; simple command.

## Expected Output

For Admin: "The command completed successfully. There are no entries in the list." For standard user: "Access is denied."

## Related

- [[Related Procedure|procedures/Verify-Admin-Privileges-and-Escalate-to-SYSTEM]]
