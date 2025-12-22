---
id: new-for-rpc-users
name: rpcclient-enumdomusers
type: command
executor: bash
data: rpcclient -U "" //$_TARGET_IP -c "enumdomusers"
output: |
  rpcclient $> enumdomusers
  user:[Administrator] rid:[0x1f4]
  user:[Guest] rid:[0x1f5]
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

# rpcclient-enumdomusers

## Command

```bash
rpcclient -U "" //$_TARGET_IP -c "enumdomusers"
```

## Description

Connects to SMB/RPC endpoint and enumerates domain user accounts using null session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target hostname or IP | Yes |
| -U "" | Null authentication | Yes for anon |
| -c "enumdomusers" | RPC command to list users | Yes |

## Examples

### Basic Usage

```bash
rpcclient -U "" //dc01.domain.com -c "enumdomusers"
```

### Authenticated

```bash
rpcclient -U domain/user%pass //$_TARGET_IP -c "enumdomusers"
```

## Expected Output

rpcclient $> enumdomusers
user:[Administrator] rid:[0x1f4]
user:[Guest] rid:[0x1f5]

## Related

- [[procedures/List-Domain-Users-and-Groups-via-MS-RPC-over-SMB]]
