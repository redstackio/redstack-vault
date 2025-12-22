---
type: command
executor: bash
data: |-
  impacket-smbclient $_USERNAME@$_TARGET_IP
  who
output: null
created_at: '2023-04-06T03:56:04Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - smb
  - enumeration
verified: true
validated: true
---

# impacket-smbclient-list-connected-users

## Command

```bash
impacket-smbclient $_USERNAME@$_TARGET_IP
who
```

## Description

Connects to a Windows host via SMB using Impacket and runs 'who' to list active connected users and their session details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Domain username (e.g., Administrator) | Yes |
| $_TARGET_IP | IP address of the target host | Yes |
| who | SMB shell command to list users | Yes |

## Examples

### Basic Usage

```bash
impacket-smbclient Administrator@10.10.10.10
who
```

### Advanced Usage

```bash
impacket-smbclient lowpriv@10.10.10.10 -hashes :hashvalue
who
```

## Expected Output

```
host:  \\10.10.10.10, user: Administrator, active:     1, idle:     0
```
Shows host, user, and session activity.

## Related

- [[procedures/Active-Directory-User-Enumeration]]
- [[tools/Impacket]]
