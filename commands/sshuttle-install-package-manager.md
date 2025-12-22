---
id: da8854c3-6d79-4f0e-aa97-97ab0045a13a
name: sshuttle-install-package-manager
type: command
executor: bash
data: |-
  pacman -Sy sshuttle
  apt-get install sshuttle
output: null
created_at: '2023-04-06T03:56:22.694840+00:00'
updated_at: '2023-04-10T20:25:19.583732+00:00'
platforms:
  - Linux
tags:
  - installation
  - sshuttle
verified: true
validated: true
---

# sshuttle-install-package-manager

## Command

```bash
# For Arch Linux (using pacman)
pacman -Sy sshuttle

# For Debian/Ubuntu (using apt-get)
apt-get install sshuttle
```

## Description

Installs the sshuttle tool using system package managers on supported Linux distributions. Use the appropriate line based on your OS to fetch and install the package.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| pacman -Sy | Synchronize package database and install sshuttle (Arch Linux) | Yes (for Arch) |
| apt-get install | Install sshuttle from repositories (Debian/Ubuntu) | Yes (for Debian/Ubuntu) |

## Examples

### Basic Usage

```bash
# Arch Linux
pacman -Sy sshuttle

# Debian/Ubuntu
apt-get install sshuttle
```

### Advanced Usage

If repositories are not updated, run `pacman -Syu` first for Arch or `apt-get update` for Debian.

## Expected Output

For pacman: ":: Synchronizing package databases...\nresolving dependencies...\nchecking package integrity...\n:: sshuttle is up to date"

For apt-get: "Reading package lists... Done\nBuilding dependency tree... Done\n...\nsshuttle is already the newest version."

## Related

- [[procedures/network-pivoting-with-sshuttle]]
- [[tools/sshuttle]]
