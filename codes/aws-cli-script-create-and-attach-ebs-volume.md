---
id: 123633b5-e19a-4053-b34f-85cc03d39567
name: aws-cli-script-create-and-attach-ebs-volume
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:09.541814+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - aws
  - ebs
  - script
  - cloud
validated: true
---

# aws-cli-script-create-and-attach-ebs-volume

## Code

```bash
aws ec2 create-volume –snapshot-id snapshot_id --availability-zone zone
aws ec2 attach-volume –-volume-id volume_id –-instance-id instance_id --device device
```

## Description

This script uses AWS CLI to create an EBS volume from a snapshot and immediately attach it to an EC2 instance, streamlining the process for quick data access in cloud environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| snapshot_id | ID of the source snapshot | snap-0123456789abcdef0 |
| zone | Availability Zone | us-east-1a |
| volume_id | ID of the created volume (output from first command) | vol-0123456789abcdef0 |
| instance_id | Target EC2 instance ID | i-0123456789abcdef0 |
| device | Device name | /dev/sdf |

## Usage

Save as a .sh file, make executable (chmod +x), and run after replacing placeholders. Use in scenarios where rapid volume duplication and attachment is needed, such as forensic analysis of compromised snapshots. Pipe volume_id from first command to second for automation.

## Detection

- CloudTrail events for CreateVolume and AttachVolume API calls.
- Unusual volume attachments to instances not owned by the same user.
- IAM access logs showing ec2 permissions usage from unexpected sources.

## Related

- [[procedures/Mount-EBS-Volume-to-EC2-Linux-Instance]]
- [[tools/aws-cli]]
