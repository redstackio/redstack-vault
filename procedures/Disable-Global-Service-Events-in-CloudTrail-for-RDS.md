---
id: 1cfb27e7-1525-4a31-9728-46f3cfc9631f
name: Disable-Global-Service-Events-in-CloudTrail-for-RDS
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.161052+00:00'
updated_at: '2023-04-10T20:20:25.379104+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Disable or Modify Tools]]'
sub_techniques: []
tags:
  - '[[tags/CloudTrail]]'
  - '[[tags/Disable-Global-Service-Events]]'
  - '[[tags/RDS]]'
  - '[[tags/Useful-Commands]]'
commands:
  - '[[commands/aws-cloudtrail-update-trail-disable-global-events]]'
platforms:
  - AWS
tools: []
validated: true
---

# Disable-Global-Service-Events-in-CloudTrail-for-RDS

## Summary

This procedure disables the inclusion of global service events in an AWS CloudTrail trail specifically configured for monitoring RDS activities. By excluding global events, attackers can reduce the visibility of cross-account or management plane actions related to RDS, aiding in evasion of detection while performing malicious operations on RDS instances without triggering comprehensive logging.

## Description

AWS CloudTrail logs management events, data events, and global service events across AWS services, including RDS. Global service events capture actions like IAM policy changes or cross-region activities that might indicate broader compromise. Disabling these in a trail focused on RDS allows an attacker with sufficient permissions to perform actions such as unauthorized database modifications or data exfiltration without logging those global interactions. This technique is particularly useful post-initial access in cloud environments to impair logging mechanisms. The procedure uses the AWS CLI to update the trail configuration, requiring administrative access to CloudTrail. Success results in reduced log volume and omitted events that could alert security teams to anomalous RDS-related activities.

## Requirements

1. AWS CLI installed and configured with credentials that have permissions to update CloudTrail trails (e.g., cloudtrail:UpdateTrail).
2. An existing CloudTrail trail name configured for RDS event monitoring.
3. Access to a system with network connectivity to AWS endpoints.
4. Knowledge of the specific trail name to target.

## Defense

- Regularly audit CloudTrail configurations using AWS Config rules to detect unauthorized changes to trail settings.
- Implement least-privilege IAM policies restricting UpdateTrail actions to approved administrators.
- Enable multi-account and multi-region CloudTrail trails with organization-wide logging to maintain visibility even if individual trails are modified.
- Monitor CloudTrail logs themselves for API calls like UpdateTrail via CloudWatch alarms or SIEM integration.

## Objectives

1. Update the CloudTrail trail to exclude global service events, reducing detection risk for RDS-targeted actions.
2. Verify the configuration change to ensure global events are no longer included.
3. Enable stealthy persistence or lateral movement within the AWS environment involving RDS without comprehensive logging.

## Instructions

### Step 1: Update CloudTrail Trail Configuration

**Context**: This step modifies the existing CloudTrail trail to disable the logging of global service events. Global events include management actions across AWS services that could reveal attacker activities beyond the RDS instance. Ensure you have the trail name ready and that the AWS CLI is authenticated with appropriate credentials.

**Command** ([[commands/aws-cloudtrail-update-trail-disable-global-events]]):
```bash
aws cloudtrail update-trail --name $_TRAIL_NAME --no-include-global-service-events
```

> This command updates the specified CloudTrail trail to stop including global service events. The `--no-include-global-service-events` flag explicitly disables this feature. Upon success, the AWS CLI will return a JSON response confirming the trail's updated attributes, including the new inclusion status set to false for global events. If the trail does not exist or permissions are insufficient, an error will be returned. Verify the change by querying the trail details with `aws cloudtrail describe-trails --trail-names $_TRAIL_NAME` and checking the `IncludeGlobalServiceEvents` field is false.

### Step 2: Verify the Configuration Change

**Context**: After updating, confirm the modification took effect to ensure global events are excluded. This prevents partial failures where logging might still capture sensitive actions.

**Command**:
```bash
aws cloudtrail describe-trails --trail-names $_TRAIL_NAME
```

> Run this command to retrieve the trail's current configuration. Look for the `IncludeGlobalServiceEvents` parameter in the output JSON; it should be `false`. If it remains `true`, re-run the update command or check for permission issues. Expected output includes trail details like name, S3 bucket, and the disabled global events flag, confirming successful evasion setup.
