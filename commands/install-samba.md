---
type: command
executor: bash
data: sudo apt-get update && sudo apt-get install samba
output: null
platforms:
  - Linux
tags:
  - samba
  - installation
verified: true
validated: true
---

# install-samba

## Command

```bash
sudo apt-get update && sudo apt-get install samba
```

## Description

Installs the Samba package on Debian-based Linux systems (e.g., Ubuntu) to enable SMB file sharing. This is the first step in setting up an SMB server for hosting remote files in RFI attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs system update and installs samba package | Yes |

## Examples

### Basic Usage

```bash
sudo apt-get update && sudo apt-get install samba
```

### Advanced Usage

For specific version: `sudo apt-get install samba=2:4.15.13+dfsg-1`

## Expected Output

Reading package lists... Done
Building dependency tree... Done
... (progress)
samba is already the newest version.

Success: No errors, package installed. Verify with `which smbd`.

## Related

- [[procedures/Remote-File-Inclusion-via-SMB]]
