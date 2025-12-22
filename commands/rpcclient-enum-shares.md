---
id: 14b5b1f9-4e23-4cd5-bc4c-0c79dc434e09
name: rpcclient-enum-shares
type: command
executor: bash
data: rpcclient -U "" -N $_TARGET_IP -c enumshares
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

# rpcclient-enum-shares

## Command

```bash
rpcclient -U "" -N $_TARGET_IP -c enumshares
```

## Description

This command lists all available shares on a remote Windows system via null RPC session, helping identify accessible resources for post-exploitation in domain environments like those targeted by MS14-068.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address of the target system | Yes |
| -U "" | Empty username for null session | Yes |
| -N | No password | Yes |
| -c | Execute enumshares command | Yes |

## Examples

### Basic Usage

```bash
rpcclient -U "" -N 10.10.10.10 -c enumshares
```

### Advanced Usage

Filter for IPC shares:

```bash
rpcclient -U "" -N 10.10.10.10 -c enumshares | grep IPC
```

## Expected Output

```
Sharename: IPC$
Type: 0x214f1c53
Comment: Remote IPC
Sharename: ADMIN$
Type: 0x214f1c53
Comment: Remote Admin
```

Displays share names, types, and comments. Administrative shares like ADMIN$ indicate potential escalation paths.

## Related

- [[commands/rpcclient-enum-domain-users]]
- [[procedures/sid-enumeration-and-wmi-query-for-ms14-068-exploitation]]
