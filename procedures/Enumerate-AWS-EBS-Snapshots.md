---
id: 8cd85e90-b5f2-474e-901a-dd78237f72b7
name: Enumerate-AWS-EBS-Snapshots
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.729501+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - '[[techniques/Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
sub_techniques: []
tags:
  - '[[tags/Elastic Block Store]]'
  - '[[tags/Enumerating Snapshots]]'
  - '[[tags/Enumeration]]'
  - AWS
  - Cloud
  - EBS
commands:
  - '[[commands/aws-ec2-describe-snapshots-owned]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Enumerate-AWS-EBS-Snapshots

## Summary

This procedure uses the AWS CLI to enumerate snapshots of Elastic Block Store (EBS) volumes owned by the current AWS account. By listing these snapshots, an attacker can identify valuable data backups for further exploitation, such as copying snapshots to attacker-controlled accounts for persistence, defense evasion, or data exfiltration in a cloud environment.

## Description

In AWS, EBS snapshots are point-in-time backups of volumes that can contain sensitive data like application configurations, databases, or system files. Enumerating these snapshots allows an attacker with compromised AWS credentials to discover and target them without direct access to the underlying instances. This technique is particularly useful in post-compromise scenarios where the attacker has assumed an IAM role or user with EC2 read permissions. The procedure relies on the AWS EC2 API via the CLI, filtering for account-owned snapshots to avoid noise from public ones. Success enables subsequent actions like snapshot copying (T1530 sub-techniques) or analysis for credentials. It assumes the attacker has already obtained valid AWS access keys or temporary credentials through prior initial access.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with at least `ec2:DescribeSnapshots` permissions on the target account.
2. AWS CLI installed and configured with the target account's credentials (e.g., via `aws configure`).
3. Network access to AWS endpoints (no VPC restrictions blocking API calls).
4. Optional: jq installed for parsing JSON output if manual analysis is needed.

## Defense

- Implement least-privilege IAM policies: Restrict `ec2:DescribeSnapshots` to only necessary roles and monitor usage via CloudTrail.
- Enable AWS CloudTrail logging for EC2 API calls and set up alerts for unusual snapshot enumeration from unexpected IPs or roles.
- Use AWS Organizations SCPs to deny snapshot listing in sensitive accounts.
- Regularly audit and delete unused snapshots to reduce the attack surface.

## Objectives

1. Discover all EBS snapshots owned by the compromised AWS account.
2. Identify snapshots containing potentially valuable data for exfiltration or manipulation.
3. Gather metadata (e.g., snapshot IDs, creation dates, descriptions) to plan follow-on attacks like unauthorized copying.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is authenticated with the target account's credentials to avoid permission errors during enumeration. This step confirms the session is active and lists basic account info.

**Command** ([[commands/aws-ec2-describe-snapshots-owned]] variant for verification):
```bash
aws sts get-caller-identity
```

> This command returns the account ID, user ARN, and session details. If it fails with an access denied error, reconfigure credentials using `aws configure` with the compromised keys.

### Step 2: Enumerate Account-Owned Snapshots

**Context**: Use the EC2 describe-snapshots API to list all snapshots owned by the current account. The `--owner-ids self` filter ensures only relevant snapshots are returned, reducing output size and focusing on exploitable assets.

**Command** ([[commands/aws-ec2-describe-snapshots-owned]]):
```bash
aws ec2 describe-snapshots --owner-ids self
```

> This retrieves a JSON array of snapshot details including IDs, volumes, states, and descriptions. Review the output for recent or descriptively named snapshots indicating sensitive data (e.g., 'prod-db-backup'). Pipe to `jq` for filtering if needed: `aws ec2 describe-snapshots --owner-ids self | jq '.Snapshots[] | {SnapshotId, Description, StartTime}'`.

### Step 3: Analyze and Document Findings

**Context**: Parse the output to identify high-value targets. Look for snapshots tied to critical volumes (e.g., via VolumeId) or with keywords in descriptions. This step verifies success and prepares for next actions like copying snapshots to an external account.

**Expected Output**: A list of snapshots in JSON format, e.g., confirming at least one snapshot exists.

> Manually inspect or export to a file: `aws ec2 describe-snapshots --owner-ids self > snapshots.json`. Success is indicated by non-empty `Snapshots` array; failure shows empty results or errors like 'UnauthorizedOperation'.
