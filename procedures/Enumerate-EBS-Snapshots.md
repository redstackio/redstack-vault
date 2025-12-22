---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.778224+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Elastic Block Store]]'
  - '[[tags/Exploitation & Data Exfiltration]]'
  - '[[tags/Listing snapshots]]'
  - aws
  - cloud-discovery
commands:
  - '[[commands/aws-ec2-describe-snapshots]]'
tools:
  - '[[tools/aws-cli]]'
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
validated: true
---

# Enumerate-EBS-Snapshots

## Summary

This procedure demonstrates how to enumerate all available Elastic Block Store (EBS) snapshots in an AWS account using the AWS CLI. It allows attackers with compromised credentials to discover point-in-time copies of EBS volumes, potentially revealing sensitive data structures, volume IDs, and creation details that can inform further attacks like data exfiltration or instance recreation.

## Description

EBS snapshots are incremental backups of EBS volumes attached to EC2 instances, providing a way to restore or replicate data. In an attack scenario, enumerating snapshots helps identify valuable assets such as databases, configuration files, or application data stored in volumes. This technique requires authenticated access to the AWS account via IAM permissions like ec2:DescribeSnapshots. Once snapshots are listed, attackers can analyze descriptions, sizes, and encryption status to prioritize targets. For example, unencrypted public snapshots might contain exposed data. This maps to cloud service discovery by revealing infrastructure details without direct volume access.

## Requirements

1. Valid AWS credentials with ec2:DescribeSnapshots permission (e.g., via IAM user, role, or assumed credentials).
2. AWS CLI installed and configured with the target account's access key and secret key.
3. Network access to AWS API endpoints (no VPC restrictions blocking outbound HTTPS to ec2.amazonaws.com).
4. Knowledge of the target AWS region, as snapshots are region-specific.

## Defense

- Implement least privilege access: Restrict ec2:DescribeSnapshots to only necessary roles and monitor usage via IAM policies.
- Enable AWS CloudTrail for API logging to detect anomalous describe-snapshots calls, especially from unusual IPs or high volumes.
- Use AWS Config to enforce encryption on all snapshots and limit public visibility.
- Set up Amazon GuardDuty to alert on reconnaissance activities like snapshot enumeration.
- Regularly audit and delete unnecessary snapshots to reduce the attack surface.

## Objectives

1. List all EBS snapshots in the target AWS account to identify volume associations and metadata.
2. Analyze snapshot details (e.g., IDs, descriptions, sizes) for potential sensitive data indicators.
3. Determine if snapshots are encrypted or public, enabling further exploitation paths like copying or restoring.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is properly set up with credentials for the target account to avoid authentication errors during enumeration.

Use the [[commands/aws-configure-list]] command to check current configuration:

```bash
aws configure list
```

> This displays the current profile, region, and credential source. If not configured, run `aws configure` to set access key, secret key, default region (e.g., us-east-1), and output format (json).

Expected Output: JSON or text showing profile details without errors.

If credentials are invalid, reconfigure or assume a role using `aws sts assume-role`.

### Step 2: List All EBS Snapshots

**Context**: Execute the core enumeration command to retrieve a complete list of snapshots, providing visibility into the account's storage assets.

Execute [[commands/aws-ec2-describe-snapshots]]:

```bash
aws ec2 describe-snapshots --region $_AWS_REGION
```

> This queries the EC2 API for all snapshots owned by the account. The --region flag specifies the AWS region; omit for default. Output includes SnapshotId, VolumeId, State, StartTime, Progress, Description, and Encrypted status. Pipe to jq for parsing if needed: `| jq '.Snapshots[] | {SnapshotId, VolumeId, Description}'`.

Expected Output: JSON array of snapshot objects, e.g., {"Snapshots": [{"SnapshotId": "snap-123", "VolumeId": "vol-abc", "Description": "Backup of prod DB"}]}. Success if no AccessDenied errors.

### Step 3: Filter and Analyze Results

**Context**: Narrow down the snapshot list to focus on relevant ones, such as those associated with specific volumes or unencrypted, to identify high-value targets.

Rerun the enumeration with filters using [[commands/aws-ec2-describe-snapshots]]:

```bash
aws ec2 describe-snapshots --filters "Name=volume-id,Values=$_VOLUME_ID" --region $_AWS_REGION
```

> Replace $_VOLUME_ID with a known volume ID (e.g., vol-0a1b2c3d4e5f67890). Other filters: Name=description,Values=*sensitive*; Name=encrypted,Values=false. This reduces output noise and highlights exploitable snapshots.

Expected Output: Filtered JSON list, e.g., snapshots matching the criteria. If no results, the filter is too narrow—broaden or check permissions.

### Step 4: Export and Review for Sensitive Data

**Context**: Save the output for offline analysis to spot patterns like frequent backups of critical volumes.

Redirect output to a file:

```bash
aws ec2 describe-snapshots --output table > snapshots.txt
```

> The --output table formats for readability. Review for indicators like 'prod', 'db', or large sizes (>100GB). Cross-reference with other discoveries (e.g., EC2 instances).

Expected Output: Text file with tabular snapshot info. Success if file populates without errors and reveals actionable intel.
