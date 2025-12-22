---
id: b5f54428-ca16-4caf-a631-18915d9c30dd
type: tool
verified: true
created_at: '2019-08-28T21:17:18.735209+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - forensics
  - data-recovery
  - ext4
  - ext3
url: 'https://extundelete.sourceforge.net/'
validated: true
---

# extundelete

**Status**: Unverified

## Overview

extundelete is a command-line utility designed for recovering deleted files from ext3 or ext4 file systems, which are common in Linux distributions such as Ubuntu, Mint, and Fedora. It leverages the journaling mechanism of these file systems to reconstruct deleted data, making it valuable in digital forensics, incident response, and post-exploitation scenarios where attackers or defenders need to recover artifacts like logs, configurations, or user files.

## Description

extundelete examines the file system's journal and inode structures to identify and restore files that have been deleted but not yet overwritten. It is particularly useful when files are deleted using the standard 'rm' command, as the data blocks may remain intact until reused. The tool supports operations like listing deleted inodes, restoring specific files or directories, and recovering all possible data. While it cannot guarantee 100% recovery due to potential overwriting, it provides a non-destructive way to analyze and retrieve data from unmounted partitions. In security testing, it aids in persistence by recovering deleted payloads or in defense by restoring evidence.

## Features

- **Journal-Based Recovery**: Uses ext3/ext4 journal logs to trace deleted file metadata.
- **Inode Inspection**: Allows viewing details of deleted inodes without altering the file system.
- **Selective Restoration**: Restore individual files, directories, or all deleted content to a specified output directory.
- **Superblock Analysis**: Dumps file system superblock information for integrity checks.
- **Non-Destructive**: Operates on block devices without mounting, preserving evidence chain.

## Installation

### Requirements

- Linux kernel with ext3/ext4 support (standard on most distributions).
- Access to the block device (e.g., /dev/sda1) – the partition must be unmounted.
- Root privileges for raw device access.

### Install Commands

```bash
# On Ubuntu/Debian (including Kali Linux)
sudo apt update
sudo apt install extundelete

# On Fedora/CentOS/RHEL
sudo dnf install extundelete  # or yum for older versions

# From source (if needed)
# Download from https://extundelete.sourceforge.net/
# Extract and compile with e2fsprogs development libraries
sudo apt install libext2fs-dev  # Ubuntu
./configure
make
sudo make install
```

## Basic Usage

```bash
extundelete --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--help, -h` | Display help message and exit |
| `--version` | Show version information |
| `--superblock` | Dump superblock details |
| `--inode <num>` | Display information for a specific inode |
| `--restore-all` | Recover all deleted files to RECOVERED_FILES directory |
| `--restore-file <path>` | Restore a specific deleted file |
| `--restore-inode <num>` | Restore file by inode number |
| `--after <date>` | Only recover files deleted after a specific date (YYYY-MM-DD HH:MM:SS) |
| `--before <date>` | Only recover files deleted before a specific date |
| `<device>` | Path to the block device (e.g., /dev/sda1) – required for all operations |

## Examples

### Example 1: Basic Usage – List Deleted Inodes

Use this to scan for recently deleted files without restoring them.

```bash
sudo extundelete --list-deleted /dev/sda1
```

### Example 2: Advanced Usage – Restore All Deleted Files

Recovers everything possible to a local directory.

```bash
sudo extundelete --restore-all /dev/sda1
ls RECOVERED_FILES/
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Local System]] Data from Local System (for collecting deleted artifacts in post-exploitation)
- [[Timestomp]] Indicator Removal on Host (recovering traces of deleted files)

### Tactics

- [[Collection]] Collection
- [[Exfiltration]] Exfiltration (recovering data for analysis)

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring: Look for 'extundelete' in running processes via `ps aux` or Sysdig.
- File system access logs: Audit access to raw block devices (/dev/sd*) in auditd or journalctl.
- Created directories: Presence of 'RECOVERED_FILES' or similar output dirs with timestamps matching recovery attempts.
- Network-free, but correlate with unmount/mount events or forensic tool deployments.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/testdisk]] (Broader file recovery suite)
- [[tools/foremost]] (Carving tool for deleted files)
- [[tools/scalpel]] (File carving alternative)

## References

- Official documentation: https://extundelete.sourceforge.net/
- SourceForge repository: https://sourceforge.net/projects/extundelete/
- Related resource: e2fsprogs documentation for ext file system internals
