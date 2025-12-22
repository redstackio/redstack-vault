---
type: command
executor: bash
data: sudo systemctl restart smbd
output: null
platforms:
  - Linux
tags:
  - samba
  - service-management
verified: true
validated: true
---

# restart-smb-service

## Command

```bash
sudo systemctl restart smbd
```

## Description

Restarts the Samba daemon to apply configuration changes, making the SMB share available for remote inclusion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Restarts smbd service | Yes |

## Examples

### Basic Usage

```bash
sudo systemctl restart smbd
```

### Advanced Usage

For older systems: `sudo service smbd restart`

## Expected Output

No output if successful.

Success: Check status with `sudo systemctl status smbd` showing active (running).

## Related

- [[procedures/Remote-File-Inclusion-via-SMB]]
