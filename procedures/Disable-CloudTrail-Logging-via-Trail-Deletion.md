---
id: cd1b027b-19d3-4292-842e-f7a5fe718c9e
name: Disable-CloudTrail-Logging-via-Trail-Deletion
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.135138+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Disable-or-Modify-Cloud-Logging|T1562.007 - Disable or Modify
    Cloud Logging]]
sub_techniques: []
tags:
  - '[[tags/CloudTrail]]'
  - '[[tags/AWS]]'
  - '[[tags/Defense Evasion]]'
  - '[[tags/Logging]]'
commands:
  - '[[commands/aws-cloudtrail-delete-trail]]'
platforms:
  - AWS
tools: []
validated: true
---

# Disable-CloudTrail-Logging-via-Trail-Deletion

## Summary

This procedure disables AWS CloudTrail logging by deleting an existing trail, preventing the capture of API calls and related events. It serves as a defense evasion technique to hide attacker activities from monitoring and auditing tools in an AWS environment.

## Description

AWS CloudTrail records API calls and account activity, enabling detection of suspicious behavior. Attackers with sufficient permissions can delete a CloudTrail trail to stop logging, creating gaps in audit records that make incident response and forensics more challenging. This technique is particularly useful post-compromise to cover tracks during lateral movement or data exfiltration. The procedure uses the AWS CLI to issue the deletion command, which permanently removes the trail and its associated log files. Note that this action is irreversible, and any required logs should be exported beforehand. It requires IAM permissions like cloudtrail:DeleteTrail and applies to multi-region or organization trails as well.

## Requirements

1. AWS CLI installed and configured with credentials (e.g., access keys or IAM role) that have cloudtrail:DeleteTrail permission.
2. Knowledge of the target trail name (discoverable via aws cloudtrail describe-trails).
3. Optional: Named profile for multi-account management.

## Defense

- Monitor CloudTrail logs for API calls to delete-trail and investigate any logging gaps or unauthorized deletions.
- Enable CloudTrail log file validation and integrate with Amazon GuardDuty or CloudWatch for anomaly detection on logging changes.
- Implement least-privilege IAM policies to restrict DeleteTrail actions to authorized administrators only.
- Use AWS Config to track trail configurations and alert on modifications.

## Objectives

1. Permanently disable CloudTrail logging for the specified trail to evade detection.
2. Create audit gaps to obscure subsequent malicious activities.
3. Minimize forensic evidence of the attacker's presence in the AWS environment.

## Instructions

### Step 1: Identify and Delete the CloudTrail Trail

**Context**: Locate the trail name if unknown (using aws cloudtrail describe-trails) and execute the deletion command. This step accomplishes the core objective of stopping logging by removing the trail configuration.

**Command** ([[commands/aws-cloudtrail-delete-trail]]):
```bash
aws cloudtrail delete-trail --name $_TRAIL_NAME --profile $_PROFILE_NAME
```

> This command deletes the specified CloudTrail trail, halting all associated event logging. Replace $_TRAIL_NAME with the actual trail identifier (e.g., my-trail) and $_PROFILE_NAME with your AWS CLI profile (optional; defaults to the current profile if omitted). The deletion is permanent and cannot be undone; ensure logs are backed up if needed. Run this from a machine with AWS CLI access.

**Expected Output**: A JSON response indicating successful deletion, such as {"Name": "$_TRAIL_NAME", "DeletionStatus": "DELETING"} or similar confirmation. Verify success by running aws cloudtrail describe-trails to confirm the trail is no longer listed.
