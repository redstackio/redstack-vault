---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Share Discovery|T1135 - Network Share Discovery]]'
sub_techniques: []
tags:
  - data-exposure
  - network
commands:
  - '[[commands/mount-cifs-share-null-session]]'
  - '[[commands/mount-cifs-share-with-credentials]]'
platforms:
  - Linux
tools: []
validated: true
---

# Mount-Windows-CIFS-Share

## Summary

This procedure demonstrates how to mount a Windows CIFS (Common Internet File System) share, which is Microsoft's implementation of the SMB protocol, on a Linux system. Mounting allows an attacker or tester to access and navigate shared directories as if they were local drives, facilitating discovery and potential data exfiltration from network shares.

## Description

CIFS shares are commonly used in Windows environments to share files and resources across a network. On Linux, the `mount` command with the CIFS filesystem type can be used to attach these shares to a local mount point. This technique is useful in scenarios where an attacker has network access to a target Windows host and aims to enumerate or access exposed shares without interactive logins. It supports both authenticated mounts (using username and password) and null sessions (anonymous access, often enabled for guest shares). Once mounted, files can be read, written, or copied using standard Linux file operations. This procedure assumes a Linux attacker machine and focuses on discovery tactics, but can lead to lateral movement if credentials are obtained.

## Requirements

1. Linux system (e.g., Ubuntu or Kali) with root or sudo access for mounting.
2. Network connectivity to the target Windows host (SMB ports 445/TCP open).
3. `cifs-utils` package installed (provides CIFS mount support; ntfs-3g is optional for NTFS compatibility but recommended).
4. Target share path (e.g., //TARGET_IP/SHARE) and optional credentials.
5. A local mount point directory (e.g., /mnt/share) created with mkdir.

## Defense

- Monitor for unusual SMB mount attempts using tools like auditd or Sysmon (Event ID 5145 for share access).
- Disable null sessions and guest access on Windows shares via Group Policy (SMB security hardening).
- Implement network segmentation and firewall rules to restrict SMB traffic to trusted zones.
- Enable SMB signing and encryption to prevent man-in-the-middle attacks during mounts.

## Objectives

1. Gain read/write access to a remote Windows CIFS share for file enumeration and potential exfiltration.
2. Perform anonymous (null session) access if guest shares are exposed.
3. Verify share contents to identify sensitive data or further pivot points.
4. Successfully mount and unmount without errors, confirming network share discovery.

## Instructions

### Step 1: Install Required Packages

**Context**: Ensure the system has CIFS mount support. The `cifs-utils` package is essential, and `ntfs-3g` enhances compatibility with Windows filesystems. Run this on Ubuntu/Debian-based systems.

```bash
apt update && apt install cifs-utils ntfs-3g -y
```

> This command updates the package list and installs the necessary tools. Expected output includes progress bars for downloads and installation confirmation like "ntfs-3g is already the newest version" or successful install messages. If already installed, it will skip without errors.

### Step 2: Create Mount Point

**Context**: Prepare a local directory to serve as the mount point for the remote share.

```bash
mkdir -p /mnt/target_share
```

> This creates the directory if it doesn't exist. Expected output is no output if successful, or an error if permissions are insufficient (use sudo if needed).

### Step 3: Mount with Credentials

**Context**: Use provided username and password to authenticate and mount an authenticated share. This is suitable when valid credentials are available from prior enumeration.

**Command** ([[commands/mount-cifs-share-with-credentials]]):
```bash
mount -t cifs //$_TARGET_IP/$_SHARE -o 'username="$_USERNAME",password="$_PASSWORD",vers=3.0' /$_MOUNT_POINT
```

> Replace placeholders with actual values (e.g., //192.168.1.100/IPC$, username=guest, password=pass). The `vers=3.0` option ensures SMB3 compatibility for security. Expected output includes mount success like "mount: /mnt/target_share mounted" and no permission errors. Verify with `ls /$_MOUNT_POINT` to see share contents.

### Step 4: Mount with Null Session (Anonymous)

**Context**: Attempt anonymous access for publicly exposed shares. This requires null sessions to be enabled on the target Windows system.

**Command** ([[commands/mount-cifs-share-null-session]]):
```bash
mount -t cifs //$_TARGET_IP/$_SHARE -o 'username="",password="",vers=3.0,guest' /$_MOUNT_POINT
```

> Use empty credentials for null session. The `guest` option explicitly requests guest access. Expected output is successful mount if allowed, showing share files upon `ls`. If denied, errors like "Permission denied" or "mount error(13): Permission denied" appear.

### Step 5: Verify and Access Share

**Context**: Confirm the mount and interact with the share contents.

```bash
ls -la /$_MOUNT_POINT
umount /$_MOUNT_POINT
```

> List files to verify access (expected: directory listing of share contents). Unmount when done to clean up. Expected output for unmount: no output if successful.

> Decision point: If mount fails with version errors, try `vers=2.1` or `vers=1.0` for older Windows systems. If authentication fails, fall back to null session or obtain better credentials.
