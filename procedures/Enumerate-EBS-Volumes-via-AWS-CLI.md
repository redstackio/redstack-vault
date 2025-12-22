---
id: ba178458-4178-4501-85cd-b6a0e324cc80
name: Enumerate-EBS-Volumes-via-AWS-CLI
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.705047+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Elastic Block Store]]'
  - '[[tags/Enumerating EBS volumes]]'
  - '[[tags/Enumeration]]'
  - AWS
  - Cloud
commands:
  - '[[commands/aws-ec2-describe-volumes]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Enumerate-EBS-Volumes-via-AWS-CLI

## Summary

This procedure uses the AWS CLI to enumerate Elastic Block Store (EBS) volumes in an AWS account, revealing details such as volume IDs, sizes, states, and attachment information. It is useful for discovering persistent storage resources that may contain sensitive data or serve as targets for further cloud-based attacks, such as mounting volumes to unauthorized instances.

## Description

Elastic Block Store (EBS) provides block-level storage volumes for use with Amazon EC2 instances, often holding critical data like databases, logs, or configuration files. In an attack scenario, an adversary with compromised AWS credentials can enumerate EBS volumes to map the storage landscape, identify unencrypted or misconfigured volumes, and plan subsequent actions like snapshot creation, volume attachment, or data exfiltration. This technique targets the EC2 service API and requires permissions like 'ec2:DescribeVolumes'. The output includes metadata that can reveal business-critical assets, such as production databases. Detection relies on CloudTrail monitoring for API calls, and defense involves least-privilege IAM policies.

## Requirements

1. AWS CLI installed and configured with credentials (e.g., access key and secret key) that have 'ec2:DescribeVolumes' permission.
2. Network access to AWS endpoints (no VPC endpoints required for basic enumeration).
3. Target AWS region specified if not using default.

## Defense

- Configure IAM policies to deny 'ec2:DescribeVolumes' to untrusted roles or users, using conditions like MFA or IP restrictions.
- Enable AWS CloudTrail logging and monitor for anomalous 'DescribeVolumes' API calls, especially from unusual IPs or high-volume queries.
- Implement encryption at rest for EBS volumes with AWS KMS keys restricted to specific services, and use volume-level access controls.

## Objectives

1. Identify all EBS volumes in the target AWS account and region.
2. Gather metadata including volume ID, size, state, and attachment details to assess potential value.
3. Spot opportunities for further exploitation, such as unattached or encrypted volumes.
4. Collect information for targeted attacks on sensitive storage.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is properly set up with credentials that allow EC2 volume description. This step confirms authentication before enumeration to avoid permission errors.

Use the [[commands/aws-configure-list]] command from the AWS CLI tool to check current configuration:

```bash
aws configure list
```

> This command displays profile settings, region, and output format. If credentials are missing, run 'aws configure' to set them. Expected output includes access key (masked), region, and format.

### Step 2: Enumerate EBS Volumes

**Context**: Retrieve a list of all EBS volumes in the current region, including key attributes like ID, size in GB, state (available/attached), and attachment details (instance ID, device name). This core step performs the discovery.

**Command** ([[commands/aws-ec2-describe-volumes]]):

```bash
aaws ec2 describe-volumes
```

> Run this in the terminal after configuring AWS CLI. It queries the EC2 API and returns JSON output. Filter with --filters if needed (e.g., --filters "Name=tag-key,Values=Environment" for tagged volumes). If successful, parse the JSON for volumes array; errors indicate insufficient permissions.

### Step 3: Analyze and Filter Output

**Context**: Review the JSON response to identify high-value volumes, such as large unattached ones or those attached to critical instances. This step involves manual or scripted parsing to prioritize targets.

Use jq (if installed) or manual inspection on the output from Step 2:

```bash
aaws ec2 describe-volumes | jq '.Volumes[] | {VolumeId, Size, State, Attachments}'
```

> This pipes the output to jq for cleaner viewing, showing only relevant fields. Expected: Structured list of volumes. Look for 'State: available' volumes as easier targets for attachment. Document findings for chaining to procedures like volume mounting.
