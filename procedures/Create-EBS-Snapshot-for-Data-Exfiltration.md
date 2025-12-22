---
id: 37472d2c-71f5-45c1-ac6f-873328419100
name: Create-EBS-Snapshot-for-Data-Exfiltration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.754858+00:00'
updated_at: '2023-04-10T20:20:36.180679+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - '[[techniques/Data from Local System|T1005 - Data from Local System]]'
sub_techniques: []
tags:
  - '[[tags/Creating a snapshot of a specified volume]]'
  - '[[tags/Elastic Block Store]]'
  - '[[tags/Exploitation & Data Exfiltration]]'
  - aws
  - ebs
  - snapshot
  - data-exfiltration
commands:
  - '[[commands/aws-ec2-create-snapshot]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Create-EBS-Snapshot-for-Data-Exfiltration

## Summary

This procedure demonstrates how to create a snapshot of an Amazon Elastic Block Store (EBS) volume attached to an EC2 instance using the AWS CLI. By capturing a point-in-time copy of the volume, an attacker with compromised AWS credentials can exfiltrate sensitive data stored on the volume, such as configuration files, databases, or application data, without directly accessing the instance.

## Description

In an AWS environment, EBS volumes provide persistent block storage for EC2 instances. Creating a snapshot copies the volume's data to Amazon S3 for durable storage, allowing restoration to new volumes or analysis offline. Attackers can abuse this feature for data exfiltration by targeting volumes containing sensitive information. This requires IAM permissions like 'ec2:CreateSnapshot'. Once created, the snapshot can be shared, copied to another region, or used to launch new instances elsewhere for data extraction. Detection is challenging as legitimate admins also create snapshots, but unusual patterns like snapshots of non-standard volumes or rapid creation/deletion can indicate compromise. This technique aligns with cloud data collection tactics where local system data is mirrored for theft.

## Requirements

1. Valid AWS credentials with 'ec2:CreateSnapshot' permission (e.g., via IAM role, access keys, or assumed role on a compromised EC2 instance).
2. AWS CLI installed and configured with the credentials (version 2.x recommended).
3. Knowledge of the target EBS volume ID (vol-XXXXXXXXX), obtainable via 'aws ec2 describe-volumes'.
4. Network access to AWS API endpoints (no direct internet required if using VPC endpoints).

## Defense

- Implement least-privilege IAM policies: Restrict 'ec2:CreateSnapshot' to specific volumes or tag-based conditions.
- Monitor CloudTrail logs for snapshot creation events, alerting on anomalous volumes, descriptions, or user agents.
- Enable EBS encryption by default and use KMS keys with strict access controls to protect snapshot contents.
- Use AWS Config rules to detect and remediate unauthorized snapshots; integrate with GuardDuty for behavioral anomaly detection.

## Objectives

1. Capture a point-in-time copy of an EBS volume containing sensitive data.
2. Enable offline analysis or restoration of the volume data in a controlled environment.
3. Facilitate data exfiltration by making the snapshot available for download or cross-region copy.

## Instructions

### Step 1: Verify AWS CLI Configuration and Permissions

**Context**: Ensure your AWS credentials are active and have the necessary permissions to create snapshots. This prevents errors during execution and confirms access to the target region.

Run the following command to test authentication:

**Command** ([[commands/aws-ec2-describe-volumes]]):
```bash
aws ec2 describe-volumes --region us-east-1
```

This lists available volumes. Look for the target volume ID in the output.

**Expected Output**: JSON array of volumes, e.g., {"Volumes": [{"VolumeId": "vol-0123456789abcdef0", "State": "in-use"}]}.

If permission denied, adjust IAM policy.

### Step 2: Identify the Target Volume ID

**Context**: You need the exact volume ID to snapshot. If not known, enumerate volumes attached to the instance or across the account.

**Command** ([[commands/aws-ec2-describe-volumes]]):
```bash
aws ec2 describe-volumes --filters "Name=attachment.instance-id,Values=i-0123456789abcdef0" --region us-east-1
```

Replace 'i-0123456789abcdef0' with the instance ID if targeting a specific EC2.

**Expected Output**: JSON with volume details, including "VolumeId": "vol-0123456789abcdef0".

Note the VolumeId for the next step.

### Step 3: Create the EBS Snapshot

**Context**: Execute the snapshot creation using the identified volume ID. Provide a description for tracking, and specify the AWS profile if using named credentials.

**Command** ([[commands/aws-ec2-create-snapshot]]):
```bash
aws ec2 create-snapshot --volume-id $_VOLUME_ID --description "$SNAPSHOT_DESCRIPTION" --profile $_PROFILE_NAME --region us-east-1
```

Replace placeholders: $_VOLUME_ID (e.g., vol-0123456789abcdef0), $SNAPSHOT_DESCRIPTION (e.g., "Backup for analysis"), $_PROFILE_NAME (optional, e.g., default).

**Expected Output**: JSON response like {"SnapshotId": "snap-0123456789abcdef0", "State": "pending", "Description": "Backup for analysis"}. The snapshot enters 'pending' then 'completed' state.

### Step 4: Verify Snapshot Creation

**Context**: Confirm the snapshot is complete and accessible. This allows checking status before further actions like copying or sharing.

**Command** ([[commands/aws-ec2-describe-snapshots]]):
```bash
aws ec2 describe-snapshots --snapshot-ids $_SNAPSHOT_ID --region us-east-1
```

Use the SnapshotId from Step 3.

**Expected Output**: JSON with {"Snapshots": [{"SnapshotId": "snap-0123456789abcdef0", "State": "completed", "VolumeId": "vol-0123456789abcdef0"}]}. If 'completed', the snapshot is ready for exfiltration.

If issues, check CloudTrail for errors.
