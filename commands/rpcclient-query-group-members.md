---
id: e2bff8d7-7664-4b0a-9848-91b9bfae1e86
name: rpcclient-query-group-members
type: command
executor: bash
data: rpcclient -U "" -N $_TARGET_IP -c 'querygroupmem $_GROUP_SID'
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

# rpcclient-query-group-members

## Command

```bash
rpcclient -U "" -N $_TARGET_IP -c 'querygroupmem $_GROUP_SID'
```

## Description

This command queries the members of a specified group on a domain controller using RPC, by providing the group's SID. It is key for identifying privileged users in groups like Domain Admins during AD reconnaissance for exploits such as MS14-068.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address of the domain controller | Yes |
| $_GROUP_SID | SID of the group (e.g., S-1-5-21-...-512 for Domain Admins) | Yes |
| -U "" | Null username | Yes |
| -N | No password | Yes |
| -c | Execute querygroupmem command | Yes |

## Examples

### Basic Usage

```bash
rpcclient -U "" -N 10.10.10.10 -c 'querygroupmem 0x200'
```

### Advanced Usage

Query Domain Admins:

```bash
rpcclient -U "" -N 10.10.10.10 -c 'querygroupmem S-1-5-21-1234567890-1234567890-1234567890-512'
```

## Expected Output

```
sid:[S-1-5-21-...-500]
  name:[Administrator]
  attributes: 7
```

Lists group members with SIDs, names, and attributes. Empty list or errors indicate access issues.

## Related

- [[commands/rpcclient-lookup-user-sid]]
- [[procedures/sid-enumeration-and-wmi-query-for-ms14-068-exploitation]]
