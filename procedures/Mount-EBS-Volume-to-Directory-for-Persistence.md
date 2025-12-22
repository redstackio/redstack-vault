---
id: a11baa3b-8d0c-4d39-92fc-902391d0b7eb
name: Mount-EBS-Volume-to-Directory-for-Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.856825+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Modify Cloud Compute Infrastructure|T1578 - Modify Cloud
    Compute Infrastructure]]
sub_techniques: []
tags:
  - '[[tags/elastic-block-store]]'
  - '[[tags/exploitation-data-exfiltration]]'
  - '[[tags/mounting-volume]]'
commands:
  - '[[commands/lsblk-list-block-devices]]'
  - '[[commands/mkdir-create-mount-point]]'
  - '[[commands/mount-device-to-directory]]'
platforms:
  - AWS
  - Linux
tools: []
validated: true
---

# Mount-EBS-Volume-to-Directory-for-Persistence

## Summary

This procedure details how to mount an Elastic Block Store (EBS) volume to a directory on a compromised AWS EC2 instance, enabling attackers to establish persistence by storing exfiltrated data on the volume. Once mounted, the directory acts as a persistent storage point that survives instance reboots if configured properly, allowing continued access to stolen data even if the instance is terminated or monitored.

## Description

In cloud environments like AWS, EBS volumes provide block-level storage that can be attached to EC2 instances. Attackers with access to an EC2 instance can mount an existing or newly created EBS volume to a local directory, using it as a stealthy data drop for exfiltration. This technique evades detection by leveraging legitimate cloud infrastructure modifications, potentially storing sensitive files like credentials or logs without alerting host-based monitoring. It is particularly useful in persistence scenarios where the attacker needs to maintain data access across instance lifecycles. The process assumes the volume is already attached to the instance via AWS API or console; if not, additional cloud API calls would be required. Success results in a mounted filesystem accessible via standard file operations, with data persisting independently of the instance.

## Requirements

1. Compromised access to an AWS EC2 instance with sudo privileges.
2. The target EBS volume must be attached to the instance (via AWS Management Console, CLI, or API).
3. Sufficient IAM permissions to manage EBS volumes if creating or attaching new ones (e.g., ec2:AttachVolume).
4. Linux-based EC2 instance (e.g., Amazon Linux, Ubuntu).
5. Basic familiarity with Linux file systems and AWS storage.

## Defense

- Implement least-privilege IAM policies to restrict ec2:AttachVolume and ec2:ModifyVolume actions to authorized roles only.
- Monitor CloudTrail logs for unusual EBS attachment or mount events, such as volumes attached from untrusted instances or high I/O on new volumes.
- Enable EC2 instance logging (e.g., via CloudWatch) to detect sudo mount commands or filesystem changes.
- Use EBS encryption and volume tagging to track and audit usage; alert on untagged or unexpectedly mounted volumes.
- Regularly scan for anomalous storage activity, like sudden increases in EBS throughput correlating with data exfiltration patterns.

## Objectives

1. Attach and mount an EBS volume to create a persistent storage directory on the compromised EC2 instance.
2. Enable secure storage of exfiltrated data, evading instance-specific monitoring.
3. Ensure the mount survives reboots for long-term persistence.

## Instructions

### Step 1: Identify the Attached EBS Device

**Context**: After attaching the EBS volume to the EC2 instance (via AWS console or CLI), identify its device name (e.g., /dev/xvdf) to prepare for mounting. This step verifies the volume is visible at the block device level.

**Command** ([[commands/lsblk-list-block-devices]]):
```bash
sudo lsblk -f
```

> This command lists all block devices, their filesystems, and mount points. Look for the new EBS volume, typically appearing as /dev/xvdX (e.g., /dev/xvdf) without a mount point. If the volume has no filesystem, proceed to format it (mkfs -t ext4 /dev/xvdf), but note this erases data.

### Step 2: Create the Mount Point Directory

**Context**: Create a target directory on the instance's filesystem where the EBS volume will be mounted. Choose a inconspicuous location like /opt/data to blend with legitimate activity.

**Command** ([[commands/mkdir-create-mount-point]]):
```bash
sudo mkdir -p /opt/persistent-data
```

> This creates the directory if it doesn't exist. Verify with ls /opt to ensure it's empty and ready for mounting.

### Step 3: Mount the EBS Device to the Directory

**Context**: Perform the actual mount operation to make the EBS volume's contents accessible via the directory. Use sudo for root privileges required to bind the device.

**Command** ([[commands/mount-device-to-directory]]):
```bash
sudo mount /dev/xvdf /opt/persistent-data
```

> Replace /dev/xvdf with the actual device from Step 1. On success, the directory will now reflect the volume's filesystem. Verify with df -h or lsblk to confirm the mount point is listed.

### Step 4: Verify and Make Persistent (Optional)

**Context**: Test access to the mounted volume and configure /etc/fstab for persistence across reboots, ensuring the data drop remains available.

**Command** ([[commands/mount-device-to-directory]]):
```bash
sudo df -h | grep /opt/persistent-data
sudo blkid /dev/xvdf >> /etc/fstab  # Append UUID for persistence
sudo echo "/dev/xvdf /opt/persistent-data ext4 defaults,nofail 0 2" >> /etc/fstab
```

> The df command shows the mounted volume's usage. For fstab, use blkid to get the UUID for reliable mounting. Test with sudo mount -a; if no errors, the mount is persistent.
