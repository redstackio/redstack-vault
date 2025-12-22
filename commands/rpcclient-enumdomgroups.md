---
id: new-for-rpc-groups
name: rpcclient-enumdomgroups
type: command
executor: bash
data: rpcclient -U "" //$_TARGET_IP -c "enumdomgroups"
output: |
  rpcclient $> enumdomgroups
  group:[Domain Admins] rid:[0x201]
  group:[Domain Users] rid:[0x202]
created_at: '2020-03-13T23:58:22.902373+00:00'
updated_at: '2023-05-29T16:48:53.162677+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - rpc
verified: true
validated: true
---

# rpcclient-enumdomgroups

## Command

```bash
rpcclient -U "" //$_TARGET_IP -c "enumdomgroups"
```

## Description

Enumerates domain groups via RPC over SMB with null session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP/hostname | Yes |
| -U "" | Null auth | Yes |
| -c "enumdomgroups" | Command to list groups | Yes |

## Examples

### Basic Usage

```bash
rpcclient -U "" //10.10.10.10 -c "enumdomgroups"
```

## Expected Output

rpcclient $> enumdomgroups
group:[Domain Admins] rid:[0x201]
group:[Domain Users] rid:[0x202]

## Related

- [[procedures/List-Domain-Users-and-Groups-via-MS-RPC-over-SMB]]
