---
id: a3db7f5f-65a8-427a-835a-43fb2befd955
name: Share-AWS-AMI-Image-with-Another-Account
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:35.145457+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Modify Cloud Compute Infrastructure]]'
sub_techniques: []
tags:
  - '[[tags/AWS]]'
  - '[[tags/Cloud]]'
commands:
  - '[[commands/aws-ec2-add-launch-permission-to-ami]]'
  - '[[commands/aws-ec2-remove-launch-permission-from-ami]]'
platforms:
  - Cloud
tools:
  - '[[tools/AWS-CLI]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# Share-AWS-AMI-Image-with-Another-Account

## Summary

This procedure allows sharing an Amazon Machine Image (AMI) with another AWS account, enabling the recipient to launch instances from the shared AMI. It can be used in attack scenarios to bypass detection mechanisms that monitor EC2 instance launches but overlook AMI creation or sharing, allowing stealthy deployment of potentially malicious images.

## Description

In AWS, AMIs can be shared explicitly with specific AWS accounts via the EC2 API, granting launch permissions on the image and its associated EBS snapshots. This technique evades alarms focused solely on instance provisioning by performing the sharing step separately. Once shared, the target account can launch instances from the AMI without triggering instance-creation alerts. After deployment, permissions can be revoked to limit exposure. This requires EC2 permissions like ec2:ModifyImageAttribute and operates within the AWS cloud environment. For official documentation, see [AWS AMI Sharing Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html).

## Requirements

1. AWS CLI installed and configured with credentials that have ec2:ModifyImageAttribute permissions on the source AMI.
2. The AMI ID of the image to share (e.g., ami-0abcdef1234567890).
3. The AWS account ID of the target user or account (e.g., 123456789012).
4. Network access to AWS APIs (no specific ports, as it uses HTTPS).

## Defense

Defensive measures and detection strategies:

- Enable AWS CloudTrail logging for EC2 API calls and monitor for ec2:ModifyImageAttribute events, particularly those adding or removing launch permissions.
- Implement AWS Config rules to alert on unauthorized AMI sharing outside approved accounts.
- Use IAM policies to restrict ec2:ModifyImageAttribute to least-privilege roles, preventing broad sharing.
- Regularly audit shared AMIs via the AWS console or API (describe-image-attribute) and revoke unnecessary permissions.

## Objectives

1. Grant launch permissions on an AMI to a target AWS account for stealthy instance deployment.
2. Verify the sharing to ensure the target can access the AMI.
3. Revoke permissions post-deployment to minimize persistence and detection risk.
4. Expected outcome: Target account launches instances from the shared AMI without direct instance-creation alerts.

## Instructions

### Step 1: Add Launch Permission to the AMI

**Context**: This step grants the target AWS account permission to launch instances from the specified AMI, including access to the underlying EBS volumes. It is the core action for sharing and should be performed only after confirming the AMI is ready for deployment.

**Command** ([[commands/aws-ec2-add-launch-permission-to-ami]]):
```bash
aws ec2 modify-image-attribute --image-id $AMI_ID --launch-permission "Add=[{UserId=$TARGET_ACCOUNT_ID}]"
```

> This command modifies the AMI's launch attribute to add the specified account. Replace $AMI_ID with your AMI identifier and $TARGET_ACCOUNT_ID with the 12-digit AWS account ID. The command returns a success response if executed correctly.

### Step 2: Verify the Shared Permission

**Context**: After adding the permission, verify it was applied correctly to ensure the target account can access the AMI. This step uses a describe command to check launch permissions without alerting unnecessary logs.

**Command** ([[commands/aws-ec2-describe-image-attribute-launch-permission]]):
```bash
aws ec2 describe-image-attribute --image-id $AMI_ID --attribute launchPermission
```

> Run this to list current launch permissions. Look for the target account ID in the LaunchPermissions array. If present, the share is successful; proceed to deployment in the target account using aws ec2 describe-images --image-ids $AMI_ID --owners self (from the target account).

### Step 3: Remove Launch Permission from the AMI

**Context**: Once the target account has launched instances from the AMI, revoke the permission to clean up and reduce the window for detection or misuse. This is a defensive step to limit ongoing access.

**Command** ([[commands/aws-ec2-remove-launch-permission-from-ami]]):
```bash
aws ec2 modify-image-attribute --image-id $AMI_ID --launch-permission "Remove=[{UserId=$TARGET_ACCOUNT_ID}]"
```

> This removes the specified account from launch permissions. Verify removal using the describe command from Step 2. Success is indicated by the absence of the account in the permissions list.
