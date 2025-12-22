---
id: be99e839-1c84-40b9-a9d9-464de5a38377
name: rpcclient-enum-domain-users
type: command
executor: bash
data: rpcclient -U "" -N $_TARGET_IP -c enumdomusers
output: null
created_at: '2023-04-06T03:56:02Z'
updated_at: '2023-04-10T20:26:04Z'
platforms:
  - Linux
tags:
  - discovery
  - active-directory
verified: true
validated: true
---

# rpcclient-enum-domain-users

## Command

```bash
rpcclient -U "" -N $_TARGET_IP -c enumdomusers
```

## Description

This command enumerates all domain user accounts on a Windows domain controller using a null RPC session. It retrieves usernames and their relative identifiers (RIDs), aiding in account discovery for targeted attacks like MS14-068 exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address of the target domain controller | Yes |
| -U "" | Empty username for null session | Yes |
| -N | No password authentication | Yes |
| -c | Execute enumdomusers command | Yes |

## Examples

### Basic Usage

```bash
rpcclient -U "" -N 10.10.10.10 -c enumdomusers
```

### Advanced Usage

Pipe output to grep for admin users:

```bash
rpcclient -U "" -N 10.10.10.10 -c enumdomusers | grep -i admin
```

## Expected Output

```
user:[Administrator] rid:[0x1f4]
user:[Guest] rid:[0x1f5]
...
```

Lists all domain users with RIDs. Success is indicated by 'result was OK' and user listings; failures show access denied.

## Related

- [[commands/rpcclient-lookup-user-sid]]
- [[procedures/sid-enumeration-and-wmi-query-for-ms14-068-exploitation]]
