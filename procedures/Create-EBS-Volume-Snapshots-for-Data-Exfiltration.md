---
id: 3381f0e2-68a4-4229-9184-08e758e3a753
name: Create-EBS-Volume-Snapshots-for-Data-Exfiltration
type: procedure
verified: true
submitted: false
created_at: '2020-07-31T04:25:23.822633+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Cloud Storage]]'
sub_techniques: []
tags:
  - '[[tags/AWS]]'
  - '[[tags/Bypass]]'
  - '[[tags/Cloud]]'
  - persistence
  - data-exfiltration
commands:
  - '[[commands/aws-ec2-create-snapshot-with-volume-id]]'
  - '[[commands/aws-ec2-create-snapshot-with-volume-id-and-description]]'
platforms:
  - Cloud
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Create-EBS-Volume-Snapshots-for-Data-Exfiltration

## Summary

This procedure demonstrates how to create snapshots of Amazon EBS volumes using the AWS CLI, enabling attackers with compromised credentials to capture volume data for later exfiltration or mounting on a new EC2 instance under their control. This technique can facilitate data theft or persistence in cloud environments by bypassing direct volume access restrictions.

## Description

In an AWS environment, EBS volumes store critical data for EC2 instances. An attacker with EC2 permissions can create snapshots of these volumes, which are point-in-time copies stored in S3-like storage. These snapshots can then be used to create new volumes attached to attacker-controlled EC2 instances with a new key pair, allowing data access without alerting admins to direct volume manipulations. While CloudTrail logs these actions, in automated or high-volume environments, such alerts may be ignored or suppressed. This procedure assumes the attacker has valid AWS credentials with ec2:CreateSnapshot permissions and focuses on the snapshot creation phase, which is a key step in cloud data exfiltration or persistence workflows.

## Requirements

1. AWS CLI installed and configured with compromised credentials that have ec2:CreateSnapshot and ec2:DescribeVolumes permissions.
2. Knowledge of the target EBS volume ID (obtainable via aws ec2 describe-volumes).
3. Access to an environment where CloudTrail alerts for EC2 actions may not be monitored closely.
4. Optional: A wordlist or timestamp format for backdating descriptions to evade detection.

## Defense

Defensive measures and detection strategies:

- Enable and monitor AWS CloudTrail for API calls to CreateSnapshot, filtering for unusual volume IDs or user agents.
- Implement IAM least privilege, restricting ec2:CreateSnapshot to necessary roles only.
- Use AWS Config rules to alert on snapshot creation outside normal patterns and integrate with SIEM for anomaly detection.
- Enable S3 bucket policies on snapshot storage to prevent unauthorized access or deletion.

## Objectives

1. Capture a point-in-time copy of an EBS volume containing sensitive data.
2. Optionally backdate the snapshot description to blend with legitimate activity and reduce suspicion.
3. Prepare the snapshot for mounting on a new, attacker-controlled EC2 instance to exfiltrate or analyze data.
4. Maintain stealth in automated cloud environments where such actions may not trigger immediate alerts.

## Instructions

### Step 1: Identify Target Volume and Create Basic Snapshot

**Context**: Begin by ensuring you have the target volume ID (e.g., from prior enumeration via describe-volumes). Then create a snapshot to copy the volume's data. This step accomplishes data capture without additional metadata that could reveal timing.

**Command** ([[commands/aws-ec2-create-snapshot-with-volume-id]]):
```bash
aws ec2 create-snapshot --volume-id $AWS_VOLUME_ID
```

> This command initiates the snapshot creation asynchronously. Replace $AWS_VOLUME_ID with the actual volume ID (e.g., vol-0123456789abcdef0). The snapshot will be created in the same region as the volume. Expected output includes a JSON response with SnapshotId, StartTime, and State (e.g., "pending" initially, then "completed").

### Step 2: Create Backdated Snapshot for Evasion

**Context**: For added stealth, create a snapshot with a custom description that includes a timestamp to mimic older, legitimate backups. This helps fool investigators reviewing snapshot histories, as the actual creation time is logged in CloudTrail but the description may mislead casual audits.

**Command** ([[commands/aws-ec2-create-snapshot-with-volume-id-and-description]]):
```bash
aws ec2 create-snapshot --volume-id $AWS_VOLUME_ID --description $AWS_DESCRIPTION
```

> Set $AWS_DESCRIPTION to a value like "Automated backup - $(date -d '30 days ago' +'%Y-%m-%d')" to backdate appearance. The command returns similar JSON output as Step 1, including the Description field. Verify completion with aws ec2 describe-snapshots --snapshot-id $SNAPSHOT_ID. If the volume is large, wait for the state to change to "completed" before proceeding to volume creation from the snapshot.
