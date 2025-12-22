---
id: 19af4a11-d042-4012-8f0e-b4488aefdfdb
type: tool
verified: true
created_at: '2020-02-06T21:03:08.865021+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - File System
url: 'https://man7.org/linux/man-pages/man8/mount.8.html'
commands:
  - '[[commands/mount-filesystem-to-mount-point]]'
validated: true
---

# mount

**Status**: ✓ Verified

## Overview

Mount is a standard Linux command-line utility used to attach file systems from storage devices or partitions to the directory tree of the host system. It is essential for accessing data on disks, encrypted volumes, network shares, and various file system types in security testing scenarios, such as post-exploitation data extraction or mounting encrypted partitions after decryption.

## Description

The mount command supports a wide range of file systems, including ext3/ext4 (native Linux), VFAT/FAT32, NTFS (Windows), HFS+/APFS (macOS), and network protocols like NFS and SMB/CIFS. In offensive security, it is commonly used to mount decrypted volumes (e.g., LUKS-encrypted drives) for data access, share enumeration over networks, or preparing persistent storage. It requires root privileges for most operations and can specify mount options for read-only access, noexec, or specific file system behaviors to minimize risks during analysis.

## Features

- Support for local block devices, loop devices, and network file systems (NFS, SMB).
- Auto-detection of file system types or manual specification with -t.
- Mount options (-o) for tuning behavior, such as read-only (ro), no suid (nosuid), or user-mountable (user).
- Integration with fstab for persistent mounts and temporary mounts via /etc/mtab.
- Handling of encrypted filesystems after unlocking with tools like cryptsetup.

## Installation

### Requirements

- Root or sudo access on the target system.
- Kernel support for the file system type (most are built-in on modern Linux).

### Install Commands

Mount is pre-installed on all major Linux distributions.

For additional file system support (e.g., NTFS):

```bash
# On Debian/Ubuntu
sudo apt update && sudo apt install ntfs-3g

# On Fedora/RHEL
sudo dnf install ntfs-3g

# For NFS support (usually default)
sudo apt install nfs-common

# For SMB/CIFS support
sudo apt install cifs-utils
```

## Basic Usage

```bash
mount --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help message and exit |
| `-V, --version` | Output version information |
| `-t FSTYPE` | Specify file system type (e.g., ext4, ntfs, nfs) |
| `-o OPTIONS` | Specify mount options (e.g., ro, rw, noexec) |
| `-a` | Mount all file systems in /etc/fstab |

## Examples

### Example 1: Basic Usage

Mount a local ext4 partition:

```bash
sudo mount /dev/sda1 /mnt
```

### Example 2: Advanced Usage

Mount an NFS share with specific options:

```bash
sudo mount -t nfs -o rw,vers=3 192.168.1.100:/share /mnt/nfs
```

Mount an SMB share:

```bash
sudo mount -t cifs -o username=user,password=pass //server/share /mnt/smb
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery (accessing mounted volumes for enumeration)
- [[Data from Local System]] Data from Local System (extracting data from mounted file systems)

### Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

## Detection

- Monitor sudo/mount command executions via auditd or syslogs for unusual device paths or mount points.
- Watch for mounts of encrypted devices (/dev/mapper/) in post-exploitation contexts.
- Network shares (NFS/SMB) mounts can be detected via traffic to internal IPs or credential usage logs.
- File system changes in /proc/mounts or df output.

## Related Procedures

No specific procedures linked yet. Commonly used in file system access workflows.

## Related Tools

- [[tools/cryptsetup]] (for unlocking LUKS before mounting)
- [[umount]] (for unmounting file systems)
- [[df]] (for verifying mounts)

## References

- Official man page: https://man7.org/linux/man-pages/man8/mount.8.html
- Arch Linux Wiki: https://wiki.archlinux.org/title/Mount
