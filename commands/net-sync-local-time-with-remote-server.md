---
id: 0d241a40-a23f-4a15-a205-33589cbbf414
name: net-sync-local-time-with-remote-server
type: command
executor: cmd
data: net time \\$_TARGET_IP /SET
output: The command completed successfully.
created_at: '2020-06-25T00:11:34.104899+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - setup
  - time-sync
verified: true
validated: true
---

# net-sync-local-time-with-remote-server

## Command

```cmd
net time \\$_TARGET_IP /SET
```

## Description

This command sets the local Windows system's clock to match the time of a remote server or domain controller via SMB, ensuring synchronization for domain authentication protocols like Kerberos.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the remote server (prefixed with \\) | Yes |
| /SET | Flag to set the local time to the remote server's time (alternative to set -S) | Yes |

## Examples

### Basic Usage

```cmd
net time \\192.168.1.10 /SET
```

### Advanced Usage

```cmd
net time \\DC01.domain.local /SET
```

## Expected Output

The command completed successfully.

## Related

- [[procedures/Sync-Local-Clock-with-Remote-Domain-Controller]]
