---
id: 337285d5-3f6e-46ca-91b5-2ae7cbb29db9
name: Disable-CloudTrail-on-AWS
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.757215+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Disable-or-Modify-Tools|T1562 - Disable or Modify Tools]]'
sub_techniques:
  - '[[techniques/Disable-Cloud-Logging|T1562.001 - Disable Cloud Logging]]'
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Disable CloudTrail]]'
commands:
  - '[[commands/aws-cloudtrail-delete-trail]]'
  - '[[commands/aws-cloudtrail-update-trail-no-global-events]]'
  - '[[commands/aws-cloudtrail-update-trail-single-region]]'
platforms:
  - AWS
tools: []
validated: true
---

# Disable-CloudTrail-on-AWS

## Summary

This procedure outlines how to disable AWS CloudTrail logging to evade detection by preventing the recording of API calls and account activities. By deleting trails or modifying trail configurations to exclude global events and multi-region monitoring, attackers can reduce visibility into their actions within the AWS environment.

## Description

AWS CloudTrail is a service that logs API activity across AWS services, providing a trail of events for auditing and forensics. Disabling it hinders defenders' ability to detect unauthorized access, configuration changes, or data exfiltration. This technique is useful post-initial access to an AWS account with sufficient IAM permissions, such as those allowing cloudtrail:DeleteTrail and cloudtrail:UpdateTrail. The procedure covers deletion of a trail entirely or selective disabling of event types and regions via the AWS CLI, assuming the attacker has configured credentials (e.g., via profiles). Note that disabling CloudTrail may alert administrators if monitored, and trails can be re-enabled, but it temporarily impairs logging. This applies to AWS environments where CloudTrail is enabled for compliance or security monitoring.

## Requirements

1. AWS CLI installed and configured with credentials having cloudtrail:DeleteTrail, cloudtrail:UpdateTrail, and related permissions (e.g., IAM role or access keys for an administrator profile).
2. Knowledge of the target CloudTrail trail name (e.g., obtained via enumeration with aws cloudtrail describe-trails).
3. Network access to AWS APIs (no direct VPC restrictions assumed).
4. Optional: Specific region configured if targeting regional trails.

## Defense

- Enable AWS CloudTrail in all regions and for global services, with logs delivered to secure S3 buckets protected by MFA Delete and versioning.
- Use AWS Config to monitor CloudTrail configurations and alert on changes via Amazon CloudWatch Events or AWS GuardDuty.
- Implement least-privilege IAM policies to restrict cloudtrail:UpdateTrail and cloudtrail:DeleteTrail to trusted roles only.
- Regularly audit CloudTrail logs for disablement attempts and correlate with IAM access events.

## Objectives

1. Eliminate or reduce logging of API calls to evade detection of attacker activities.
2. Minimize the attack footprint in AWS audit trails to facilitate persistence and lateral movement.
3. Prevent defenders from reconstructing the attack timeline through event logs.
4. Maintain operational secrecy in the cloud environment during exploitation.

## Instructions

1. Verify permissions and identify the target trail before proceeding. Use aws cloudtrail describe-trails to list existing trails and confirm the name (e.g., cloudgoat_trail).

   **Command** ([[commands/aws-cloudtrail-delete-trail]]):
   ```bash
   aws cloudtrail delete-trail --name $_TRAIL_NAME --profile $_PROFILE_NAME
   ```

   > This command permanently deletes the specified CloudTrail trail, stopping all logging associated with it. The --name parameter specifies the trail to delete, and --profile uses a pre-configured AWS CLI profile with appropriate credentials. Run this if the goal is complete removal of logging. Expected output includes a confirmation message like "Trail deleted successfully" if permissions are sufficient; errors indicate insufficient privileges or non-existent trail.

2. If deletion is not desired, disable monitoring of global service events (e.g., IAM, CloudFront) to reduce log volume while keeping regional logging.

   **Command** ([[commands/aws-cloudtrail-update-trail-no-global-events]]):
   ```bash
   aws cloudtrail update-trail --name $_TRAIL_NAME --no-include-global-service-events --profile $_PROFILE_NAME
   ```

   > This updates the trail to exclude global service events, limiting logs to regional AWS services only. The --no-include-global-service-events flag toggles off global monitoring. This step is useful for targeted evasion without full disablement. Expected output: JSON response showing the updated trail configuration with "IncludeGlobalServiceEvents": false.

3. For multi-region trails, disable multi-region support and limit to a specific region to further scope down logging.

   **Command** ([[commands/aws-cloudtrail-update-trail-single-region]]):
   ```bash
   aws cloudtrail update-trail --name $_TRAIL_NAME --no-include-global-service-events --no-is-multi-region-trail --region $_REGION --profile $_PROFILE_NAME
   ```

   > This configures the trail as single-region only, excluding global events, for the specified AWS region (e.g., eu-west-1). The --no-is-multi-region-trail flag ensures logging is regionalized, and --region sets the target. Use this to disable broad coverage. Expected output: Updated trail JSON with "IsMultiRegionTrail": false and region-specific settings. If the trail was multi-region, this narrows its scope immediately.
