---
type: command
executor: bash
data: sudo nano /etc/samba/smb.conf
output: null
platforms:
  - Linux
tags:
  - samba
  - configuration
verified: true
validated: true
---

# configure-samba

## Command

```bash
sudo nano /etc/samba/smb.conf
```

## Description

Opens the Samba configuration file in the nano editor for manual editing. Used to define shares, users, and protocols for SMB hosting in RFI scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Edits /etc/samba/smb.conf as root | Yes |

## Examples

### Basic Usage

```bash
sudo nano /etc/samba/smb.conf
```

### Advanced Usage

Use vim: `sudo vim /etc/samba/smb.conf`

## Expected Output

Nano editor opens with the config file loaded. No stdout; changes saved via Ctrl+O, exit Ctrl+X.

Success: File edited without errors; validate syntax with `testparm`.

## Related

- [[procedures/Remote-File-Inclusion-via-SMB]]
