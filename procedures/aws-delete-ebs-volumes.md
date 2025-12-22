---
id: 51803bb8-456c-4478-b57f-f8f62e5df6fa
name: aws-delete-ebs-volumes
type: procedure
verified: true
submitted: false
created_at: '2020-07-31T04:25:34.168246+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Impact|TA0040 - Impact]]'
techniques:
  - '[[techniques/Data Destruction|T1485 - Data Destruction]]'
sub_techniques: []
platforms:
  - Cloud
tags:
  - '[[tags/AWS]]'
  - '[[tags/Cloud]]'
commands:
  - '[[commands/aws-ec2-delete-volume]]'
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# aws-delete-ebs-volumes

## Summary

This procedure outlines how to delete Amazon EBS volumes using the AWS CLI, either individually by volume ID or in bulk for unused (available) volumes. It is primarily useful for cleanup during penetration tests where a client requests removal of test volumes, or for SecDevOps automation to maintain a clean attack surface by removing orphaned volumes via cron jobs.

## Description

EBS volumes are block storage devices attached to EC2 instances in AWS. Deleting them permanently removes the data, which can be a destructive action aligned with impact tactics in adversarial operations. In a pentest context, this might be requested for ephemeral test environments. For automation, scripts can query available volumes (those not attached to instances) and delete them to prevent resource sprawl and potential security risks from forgotten snapshots or data. The procedure requires appropriate IAM permissions (e.g., ec2:DeleteVolume) and uses the AWS CLI tool. Note that deletion is irreversible, so verify volumes before proceeding.

## Requirements

1. AWS CLI installed and configured with credentials having ec2:DescribeVolumes and ec2:DeleteVolume permissions.
2. Access to the target AWS region and account.
3. For bulk deletion, basic bash scripting knowledge and jq or awk for parsing JSON output (though the provided scripts use grep and awk).
4. Optional: Named AWS profile for multi-account management.

## Defense

- Implement IAM policies with least privilege to restrict DeleteVolume actions to approved roles.
- Enable AWS CloudTrail logging to monitor API calls for volume deletions.
- Use AWS Config rules to alert on detached or available volumes older than a threshold.
- Enable MFA and condition keys in IAM policies to prevent unauthorized deletions.

## Objectives

1. Permanently delete a specific EBS volume to clean up test artifacts.
2. Automate deletion of unused volumes to reduce attack surface.
3. Ensure no data remnants from testing persist in the environment.

## Instructions

### Step 1: Delete a Specific EBS Volume

**Context**: Identify the volume ID (e.g., via AWS Console or describe-volumes command) and delete it directly. This is the core action for targeted cleanup.

**Command** ([[commands/aws-ec2-delete-volume]]):
```bash
aws ec2 delete-volume --region $AWS_REGION --volume-id $AWS_VOLUME_ID
```

> This command sends a delete request to the specified region's EC2 service. It returns a success message if the volume is deletable (not in-use). Verify the volume status first with `aws ec2 describe-volumes --volume-ids $AWS_VOLUME_ID` to ensure it's available or detached.

### Step 2: Delete All Available EBS Volumes

**Context**: For bulk cleanup, query all available (unused) volumes in the region and loop through deletions. This automates removal of orphaned volumes, useful in cron jobs run weekly.

**Code** ([[codes/bash-delete-available-ebs-volumes]]):
```bash
for x in $(aws ec2 describe-volumes --filters Name=status,Values=available --profile <your_profile_name>|grep VolumeId|awk '{print $2}' | tr ',|"' ' '); do aws ec2 delete-volume --region <region> --volume-id $x; done
```

> The script filters for available volumes, extracts IDs using grep/awk, and deletes each. Run in a safe environment first; it skips in-use volumes.

### Step 3: Delete Available EBS Volumes Using a Specific AWS Profile

**Context**: If managing multiple AWS accounts, specify a named profile to scope the operation. This variant ensures deletions occur in the correct account.

**Code** ([[codes/bash-delete-available-ebs-volumes-with-profile]]):
```bash
for x in $(aws ec2 describe-volumes --filters Name=status,Values=available --profile <your_profile_name>|grep VolumeId|awk '{print $2}' | tr ',|"' ' '); do aws ec2 delete-volume --region <region> --volume-id $x --profile <your_profile_name>; done
```

> Similar to Step 2 but applies the profile to both describe and delete commands, preventing cross-account errors.
