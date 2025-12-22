---
type: command
executor: bash
data: sudo smbpasswd -a $_USERNAME
output: null
platforms:
  - Linux
tags:
  - samba
  - user-management
verified: true
validated: true
---

# add-samba-user

## Command

```bash
sudo smbpasswd -a $_USERNAME
```

## Description

Adds a user to the Samba password database for authenticating access to shares. Essential for secure SMB shares in RFI exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Samba username to add (e.g., smbuser) | Yes |

## Examples

### Basic Usage

```bash
sudo smbpasswd -a smbuser
```

### Advanced Usage

Add with existing system user: Ensure user exists via `sudo useradd smbuser` first.

## Expected Output

New SMB password: Retype new SMB password:

Success: User added; test with `smbclient //localhost/share -U $_USERNAME`.

## Related

- [[procedures/Remote-File-Inclusion-via-SMB]]
