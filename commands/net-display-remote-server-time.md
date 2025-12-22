---
id: 8cd9c425-1b5d-44bf-be71-1ac1759aa8d8
name: net-display-remote-server-time
type: command
executor: cmd
data: net time \\$_TARGET_IP /QUERY
output: 'The current time according to $_TARGET_IP is Wed Jun 24 20:16:26 2020.'
created_at: '2020-06-25T00:16:01.496565+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - setup
  - time-discovery
verified: true
validated: true
---

# net-display-remote-server-time

## Command

```cmd
net time \\$_TARGET_IP /QUERY
```

## Description

This command queries and displays the current time from a remote Windows server or domain controller via SMB, useful for verifying time alignment before synchronization in Active Directory environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the remote server (prefixed with \\) | Yes |
| /QUERY | Flag to query the time (alternative to -S in some syntax) | Yes |

## Examples

### Basic Usage

```cmd
net time \\192.168.1.10 /QUERY
```

### Advanced Usage

```cmd
net time \\DC01.domain.local /QUERY
```

## Expected Output

The current time according to 192.168.1.10 is Wed Jun 24 20:16:26 2020.

## Related

- [[procedures/Sync-Local-Clock-with-Remote-Domain-Controller]]
