---
id: 1d6c6b4c-eec8-4822-a999-2eaf2539bdb6
name: Disable-CloudTrail-on-Specific-Regions
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.184238+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Disable or Modify Tools|T1562.001 - Disable or Modify Tools]]'
sub_techniques: []
tags:
  - '[[tags/CloudTrail]]'
  - '[[tags/AWS]]'
  - '[[tags/Defense Evasion]]'
  - '[[tags/Logging]]'
commands:
  - '[[commands/aws-cloudtrail-update-trail-disable-logging]]'
platforms:
  - AWS
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Disable-CloudTrail-on-Specific-Regions

## Summary

This procedure disables AWS CloudTrail logging for a specific trail in a targeted region by updating the trail configuration to exclude global service events and limit it to a single region. This action impairs the collection of audit logs, allowing attackers to evade detection by preventing the recording of management events in CloudTrail, which is useful for covering tracks after initial compromise in an AWS environment.

## Description

AWS CloudTrail provides a record of actions taken by users, roles, or services in an AWS account, including API calls and management events. Disabling or modifying CloudTrail trails in specific regions reduces visibility into attacker activities, such as lateral movement or data exfiltration, within that region. This procedure uses the AWS CLI to update an existing trail, setting it to non-multi-region and excluding global events, effectively stopping comprehensive logging. It is particularly effective in multi-region setups where attackers want to maintain persistence without triggering alerts from centralized logging. The target environment is an AWS account with existing CloudTrail trails, and success results in no further logging of events in the specified region for that trail.

## Requirements

1. AWS CLI installed and configured with credentials that have permissions to update CloudTrail trails (e.g., cloudtrail:UpdateTrail policy).
2. Access to the AWS account where the CloudTrail trail exists.
3. Knowledge of the trail name and target region (e.g., eu-west-1).
4. Network access to AWS endpoints (no specific ports beyond standard HTTPS).

## Defense

- Enable CloudTrail data events and integrate with Amazon GuardDuty or CloudWatch for anomaly detection on trail modifications.
- Implement IAM policies with least privilege to restrict UpdateTrail actions to authorized roles only.
- Regularly audit CloudTrail configurations using AWS Config rules to detect changes to logging settings.
- Use multi-account strategies with centralized logging in a separate account to maintain visibility even if regional trails are disabled.

## Objectives

1. Update the CloudTrail trail to disable multi-region and global event logging in a specific region.
2. Impair audit logging to evade detection and maintain stealth in the compromised AWS environment.
3. Verify the change to ensure no further events are captured by the modified trail.

## Instructions

### Step 1: Verify Existing CloudTrail Trails

**Context**: Before updating, confirm the trail exists and note its current configuration to ensure the update targets the correct resource. This step prevents errors and provides baseline for verification.

Use the AWS CLI to list trails in the target region.

**Command** ([[commands/aws-cloudtrail-describe-trails]]):
```bash
aws cloudtrail describe-trails --region eu-west-1
```

> This command queries the CloudTrail service for all trails in the specified region. Expected output includes details like trail name, multi-region status, and include-global-service-events flag. Look for the target trail (e.g., example_trail) and confirm its ARN and current settings. If the trail is multi-region or includes global events, proceed to update.

### Step 2: Update the CloudTrail Trail Configuration

**Context**: Modify the trail to disable multi-region support and global event inclusion, which stops logging of cross-region and global API calls, reducing the trail's effectiveness for detection.

Execute the update using the AWS CLI with the specific flags to alter the trail settings.

**Command** ([[commands/aws-cloudtrail-update-trail-disable-logging]]):
```bash
aws cloudtrail update-trail --name example_trail --no-include-global-service-events --no-is-multi-region --region eu-west-1
```

> The --name specifies the trail to update, --no-include-global-service-events excludes IAM and STS events, --no-is-multi-region limits the trail to the specified region, and --region targets eu-west-1. Expected output is a JSON response confirming the update, including the modified trail attributes like "IsMultiRegionTrail": false and "IncludeGlobalServiceEvents": false. No errors should occur if permissions are sufficient; otherwise, check IAM roles.

### Step 3: Verify the Update

**Context**: Confirm the changes took effect by re-describing the trail and checking that logging is impaired. This ensures the procedure succeeded and logging is evaded.

Re-run the describe command from Step 1.

**Command** ([[commands/aws-cloudtrail-describe-trails]]):
```bash
aws cloudtrail describe-trails --region eu-west-1
```

> Compare the output to the baseline from Step 1. Success is indicated by updated flags: "IsMultiRegionTrail": false and "IncludeGlobalServiceEvents": false for the target trail. Test by performing a benign API call (e.g., list S3 buckets) and checking if it appears in the trail's S3 bucket logs—no new events should be recorded for global or multi-region aspects.
