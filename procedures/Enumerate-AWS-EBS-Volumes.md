---
id: a6f3a9e4-7d38-4f11-8395-643b8ea0e5a3
name: Enumerate-AWS-EBS-Volumes
type: procedure
verified: true
submitted: false
created_at: '2020-07-31T04:25:29.602967+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Cloud Service Discovery]]'
sub_techniques: []
tags:
  - AWS
  - Cloud
  - Discovery
commands:
  - '[[commands/aws-ec2-describe-all-volumes]]'
  - '[[commands/aws-ec2-describe-volumes-by-status]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Enumerate-AWS-EBS-Volumes

## Summary

This procedure uses the AWS CLI to enumerate Elastic Block Store (EBS) volumes in an AWS account, identifying potentially unused or orphaned volumes that may contain sensitive data. It is useful for discovering misconfigurations where administrators delete EC2 instances but retain attached volumes, allowing attackers with read access to mount and access them later.

## Description

EBS volumes are block storage devices attached to EC2 instances. A common misconfiguration occurs when EC2 instances are terminated but their EBS volumes are not deleted, leaving persistent storage with potential sensitive information such as configuration files, logs, or data. This procedure lists all volumes and filters them by status to spot available or unused ones. If Multi-Attach is enabled on a volume, it can be mounted to multiple instances simultaneously, increasing the risk of unauthorized access. This technique aids in cloud infrastructure discovery, mapping to MITRE ATT&CK's Discovery tactic by revealing resource details for further exploitation, such as mounting volumes on compromised instances.

## Requirements

1. AWS CLI installed and configured with credentials that have EC2 read permissions (e.g., ec2:DescribeVolumes).
2. Access to an AWS account or assumed role with sufficient IAM permissions.
3. Network connectivity to AWS endpoints (no VPC restrictions blocking CLI access).

## Defense

Defensive measures and detection strategies:

- Implement least-privilege IAM policies to restrict DescribeVolumes API calls to necessary roles only.
- Enable AWS CloudTrail logging for EC2 API actions and monitor for unusual DescribeVolumes queries from unexpected IPs or users.
- Use AWS Config rules to detect orphaned EBS volumes and automate cleanup.
- Set up alerts in Amazon GuardDuty for reconnaissance activities involving EBS enumeration.

## Objectives

1. Identify all EBS volumes in the target AWS account to map storage resources.
2. Filter volumes by status to locate unused or available ones for potential data recovery.
3. Determine if volumes support Multi-Attach for simultaneous mounting risks.
4. Expected outcome: A list of volumes with details like size, status, and attachments, enabling further actions like mounting unused volumes.

## Instructions

### Step 1: List All EBS Volumes

**Context**: Begin by retrieving a complete list of all EBS volumes in the account to get an overview of storage resources, including IDs, sizes, types, and attachment status. This step establishes the baseline for identifying potential targets.

**Command** ([[commands/aws-ec2-describe-all-volumes]]):
```bash
aws ec2 describe-volumes
```

> This command queries the EC2 API for all volumes. Review the JSON output for VolumeId, Size, State (e.g., available), Attachments (to check if mounted), and CreateTime. Look for volumes in 'available' state without attachments, indicating they may be orphaned.

### Step 2: Filter Volumes by Status

**Context**: Narrow down the results to volumes in specific states (e.g., available, in-use) to focus on unused or active ones. This helps prioritize volumes that could be mounted without disrupting running instances. Note: Multi-Attach enabled volumes (io1/io2 types) can be checked in the output for additional risks.

**Command** ([[commands/aws-ec2-describe-volumes-by-status]]):
```bash
aws ec2 describe-volumes --filters "Name=status,Values=available,in-use,optimizing,error"
```

> The --filters parameter uses comma-separated values for multiple states. Expected output is filtered JSON showing only matching volumes. Success is confirmed if available volumes appear, which can then be mounted via [[procedures/Mount-AWS-EBS-Volume]] if access permits. If no filters match, expand to include 'creating' or 'deleting' for ongoing operations.
