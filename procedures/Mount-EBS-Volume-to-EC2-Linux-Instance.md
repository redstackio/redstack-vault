---
id: 2a914e7d-ff82-4ce2-8388-6aad83eda32b
name: Mount-EBS-Volume-to-EC2-Linux-Instance
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.547207+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - '[[techniques/Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
sub_techniques: []
tags:
  - '[[tags/AWS]]'
  - '[[tags/Cloud]]'
  - '[[tags/EBS]]'
  - '[[tags/EC2]]'
commands:
  - '[[commands/create-ebs-volume-from-snapshot]]'
  - '[[commands/attach-ebs-volume-to-ec2-instance]]'
  - '[[commands/lsblk-list-block-devices]]'
  - '[[commands/mount-ebs-volume]]'
platforms:
  - AWS
  - Linux
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Mount-EBS-Volume-to-EC2-Linux-Instance

## Summary

This procedure outlines how to create an EBS volume from a snapshot (if needed), attach it to an EC2 Linux instance using AWS CLI, and then mount it to the instance's file system for data access. In an offensive security context, this can enable attackers with AWS credentials to access sensitive data stored on detached or snapshotted volumes, facilitating data exfiltration or persistence in cloud environments.

## Description

Attaching and mounting an EBS (Elastic Block Store) volume to an EC2 Linux instance allows expansion of storage or recovery of data from snapshots. From a red team perspective, if an attacker has obtained AWS API credentials (e.g., via instance metadata exploitation), they can create volumes from existing snapshots, attach them to controlled instances, and mount to extract confidential information like configuration files, databases, or logs. This technique aligns with cloud data collection tactics, assuming the attacker has the necessary IAM permissions (e.g., ec2:CreateVolume, ec2:AttachVolume). The process involves AWS-side operations via CLI and Linux-side mounting. Prerequisites include AWS CLI configured with valid credentials and SSH access to the EC2 instance. Potential risks include triggering CloudTrail logs for volume operations.

## Requirements

1. AWS CLI installed and configured with credentials having ec2:CreateVolume, ec2:AttachVolume, and ec2:DescribeVolumes permissions.
2. An existing EBS snapshot ID (optional, if creating from snapshot) or volume ID.
3. A running EC2 Linux instance in the same Availability Zone as the volume.
4. SSH access to the EC2 instance for mounting.
5. Sufficient IAM role or access keys for the attacker.

## Defense

- Implement least-privilege IAM policies to restrict ec2:AttachVolume and ec2:CreateVolume actions to trusted roles only.
- Enable encryption at rest for EBS volumes using AWS KMS to protect data even if mounted.
- Monitor CloudTrail for unauthorized volume attachments or creations, alerting on cross-account or unusual instance-volume pairings.
- Use AWS Config rules to detect unencrypted or publicly accessible snapshots.

## Objectives

1. Create a new EBS volume from a snapshot if required.
2. Attach the EBS volume to the target EC2 Linux instance.
3. Mount the volume on the instance's file system to access stored data.
4. Verify data accessibility for exfiltration or analysis.

## Instructions

### Step 1: Create EBS Volume from Snapshot (Optional)

**Context**: If starting from a snapshot (e.g., to duplicate a compromised volume), create a new EBS volume in the same Availability Zone as your EC2 instance. This step ensures the volume is ready for attachment without modifying the original.

**Command** ([[commands/create-ebs-volume-from-snapshot]]):
```bash
aws ec2 create-volume --snapshot-id $_SNAPSHOT_ID --availability-zone $_AVAILABILITY_ZONE --volume-type $_VOLUME_TYPE --size $_SIZE_GB
```

> This command creates a new EBS volume based on the specified snapshot. Replace placeholders with actual values (e.g., snap-0123456789abcdef0 for snapshot ID, us-east-1a for zone). The --volume-type defaults to gp2 if omitted, and --size specifies GB (must match or exceed snapshot size). Expected output includes the VolumeId for use in the next step.

### Step 2: Attach EBS Volume to EC2 Instance

**Context**: Once the volume exists (or if using an existing one), attach it to the EC2 instance as a block device. This makes the volume available to the instance's OS.

**Command** ([[commands/attach-ebs-volume-to-ec2-instance]]):
```bash
aws ec2 attach-volume --volume-id $_VOLUME_ID --instance-id $_INSTANCE_ID --device $_DEVICE_NAME
```

> Attach the volume using its ID (vol-0123456789abcdef0), instance ID (i-0123456789abcdef0), and a device name like /dev/sdf (AWS maps to /dev/xvdf internally). Poll with describe-volumes to confirm 'attached' state. If the device is in use, choose another (e.g., /dev/sdg).

### Step 3: Identify the Attached Volume on the Instance

**Context**: SSH into the EC2 instance and use lsblk to identify the new block device (e.g., /dev/xvdf), as AWS renames devices.

**Command** ([[commands/lsblk-list-block-devices]]):
```bash
lsblk
```

> Run this on the instance to list block devices. Look for the new unmounted volume (size matches expected). No parameters needed. Expected output shows device tree, e.g., xvdf without a mountpoint.

### Step 4: Format and Mount the Volume

**Context**: If the volume is new or unformatted, create a filesystem (warning: this erases data). Then mount it to a directory for access. For existing volumes, skip formatting.

**Command** ([[commands/mount-ebs-volume]]):
```bash
sudo mkfs -t ext4 /dev/xvdf  # Only if new/unformatted
sudo mkdir /mnt/ebs
sudo mount /dev/xvdf /mnt/ebs
```

> Format with mkfs if needed (use xfs or ntfs for other FS). Create mount point, then mount. Add to /etc/fstab for persistence: echo '/dev/xvdf /mnt/ebs ext4 defaults,nofail 0 2' | sudo tee -a /etc/fstab. Expected output: No errors, and df -h shows /mnt/ebs mounted. Access files via ls /mnt/ebs.
