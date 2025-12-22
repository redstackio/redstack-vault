---
id: 4c642631-4911-40f6-bf48-e834fc4a6fd3
name: guestmount
type: tool
verified: true
created_at: '2019-08-28T21:17:33.920358+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
  - '[[commands/guestmount-mount-vhd-image]]'
platforms:
  - Linux
tags:
  - data-exposure
  - file-system
url: 'https://libguestfs.org/guestmount.1.html'
validated: true
---

# guestmount

**Status**: Unverified

## Overview

Guestmount is a command-line tool for mounting virtual machine disk images and filesystems directly on the host system. It leverages the libguestfs library to access guest filesystems and uses FUSE (Filesystem in Userspace) to present them as mountable devices. Commonly used in security testing for forensic analysis, data recovery, or inspecting disk images without running the virtual machine.

## Description

Guestmount provides a safe way to read from and, optionally, write to virtual disk formats like VHD, VMDK, QCOW2, and raw images. It supports read-only mounts to prevent accidental data corruption, making it valuable for red team operations involving evidence gathering or post-exploitation file access. The tool automatically detects partitions and filesystems, simplifying the mounting process for complex images.

## Features

- Feature 1: Supports multiple disk image formats (VHD, VMDK, QCOW2, ISO, etc.)
- Feature 2: Read-only and read-write mounting options with FUSE integration
- Feature 3: Automatic filesystem detection and mounting via inspector mode
- Feature 4: Integration with libguestfs for advanced guest OS access

## Installation

### Requirements

- Linux kernel with FUSE support
- libguestfs-tools package

### Install Commands

```bash
# On Kali Linux (pre-installed in most cases)
apt update && apt install libguestfs-tools

# On Ubuntu/Debian
sudo apt update
sudo apt install libguestfs-tools fuse

# On Fedora/CentOS
sudo dnf install libguestfs-tools fuse
```

## Basic Usage

```bash
guestmount --help
```

### Common Options

| Option | Description |
|--------|-------------|
| --add <image> | Add a disk image to the appliance |
| --inspector | Automatically mount filesystems found in the image |
| --ro | Mount in read-only mode |
| --rw | Mount in read-write mode (use cautiously) |
| -m <device> | Mount a specific device/partition |

## Examples

### Example 1: Basic Usage

Mount a VHD image read-only:

```bash
guestmount --add disk.vhd --inspector --ro /mnt/guest
```

### Example 2: Advanced Usage

Mount a specific partition from a raw image:

```bash
guestmount --add raw.img -m /dev/sda1 /mnt/guest
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credential Dumping]] OS Credential Dumping (for accessing credential stores in images)
- [[Archive Collected Data]] Archive Collected Data (for handling forensic images)

### Tactics

- [[Collection]] Collection
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for libguestfs processes (e.g., `virt-*` binaries) or FUSE mounts of unusual images
- Detection method 2: Log filesystem mounts in /proc/mounts or auditd for guestmount executions
- Detection method 3: Network traces if images are transferred prior to mounting

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/libguestfs]]
- [[tools/volatility]]

## References

- Official documentation: https://libguestfs.org/
- Man page: https://libguestfs.org/guestmount.1.html
