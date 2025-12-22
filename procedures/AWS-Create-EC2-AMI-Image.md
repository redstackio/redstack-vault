---
id: a5540974-84db-45f0-9477-05cd7f8a974e
name: AWS-Create-EC2-AMI-Image
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:34.254229+00:00'
updated_at: '2023-05-25T20:08:07.978661+00:00'
tactics:
  - '[[Persistence]]'
  - '[[Defense Evasion]]'
techniques:
  - '[[Modify Cloud Compute Infrastructure]]'
sub_techniques: []
tags:
  - AWS
  - Cloud
  - AMI
  - EC2
  - Persistence
  - Defense Evasion
commands:
  - '[[commands/aws-ec2-create-image]]'
  - '[[commands/aws-ec2-create-image-no-reboot]]'
platforms:
  - Cloud
tools: []
validated: true
---

# AWS-Create-EC2-AMI-Image

## Summary

This procedure demonstrates how to create an Amazon Machine Image (AMI) from an existing EC2 instance using the AWS CLI, optionally without rebooting the instance. The resulting AMI can then be shared with another AWS account, allowing attackers to export snapshots of compromised instances to their controlled accounts for later deployment, thereby evading detection from instance-specific alarms and monitoring.

## Description

In cloud environments, attackers with compromised credentials can snapshot running EC2 instances into AMIs to preserve their access or exfiltrate virtual machine states. Creating an AMI captures the instance's root volume and any additional volumes, producing a reusable template. The --no-reboot option allows imaging without interrupting the instance, which is useful for maintaining persistence during active compromise. Once created, the AMI can be modified to change permissions and shared with an external account ID via the AWS console or CLI, enabling the attacker to launch identical instances in their infrastructure without triggering victim-side notifications from CloudTrail or third-party tools. This technique is particularly effective in multi-account AWS setups where cross-account sharing is permitted. Prerequisites include AWS CLI configured with sufficient IAM permissions (e.g., ec2:CreateImage, ec2:ModifyImageAttribute).

## Requirements

1. AWS CLI installed and configured with access keys from a compromised account having EC2 permissions (e.g., AmazonEC2FullAccess policy).
2. Knowledge of the target EC2 instance ID.
3. Network access to AWS APIs (no direct instance access required).
4. Optional: Permissions to modify AMI attributes for sharing (ec2:ModifyImageAttribute).

## Defense

- Monitor CloudTrail logs for ec2:CreateImage API calls, especially from unexpected IAM roles or with --no-reboot flag.
- Implement IAM least privilege: Restrict ec2:CreateImage to admin roles only and enable MFA.
- Use AWS Config rules to alert on AMI creation and sharing events.
- Enable GuardDuty for detection of unusual EC2 activity, including snapshot exports.
- Regularly audit shared AMIs and revoke cross-account permissions.

## Objectives

1. Capture the state of a compromised EC2 instance as an AMI for preservation or exfiltration.
2. Avoid rebooting the instance to maintain ongoing access and operations.
3. Share the AMI with an attacker-controlled account to deploy replicas outside the victim environment.
4. Evade detection by moving assets away from monitored instances.

## Instructions

### Step 1: Create Standard AMI from EC2 Instance

**Context**: This step initiates the creation of an AMI from the specified EC2 instance, which will reboot the instance by default to ensure a consistent snapshot. Use this when downtime is acceptable or to guarantee data integrity. The command requires the instance ID, a name, and description for the AMI.

**Command** ([[commands/aws-ec2-create-image]]):
```bash
aws ec2 create-image --instance-id $AWS_INSTANCE_ID --name $AWS_AMI_NAME --description $AWS_AMI_DESCRIPTION
```

This command sends a request to the AWS EC2 API to snapshot the instance's volumes. The process may take several minutes depending on instance size. Monitor progress with `aws ec2 describe-images --image-ids $AMI_ID` after obtaining the AMI ID from the response. Expected outcome: An AMI ID is returned, and the instance status changes to 'stopping' then 'stopped' during imaging.

### Step 2: Create AMI Without Rebooting Instance (Optional)

**Context**: For scenarios requiring uninterrupted instance operation, use the --no-reboot flag. This performs a 'dirty' snapshot, which may include inconsistent file system states but allows the instance to continue running. Ideal for active persistence where stopping the instance would alert defenders.

**Command** ([[commands/aws-ec2-create-image-no-reboot]]):
```bash
aws ec2 create-image --instance-id $AWS_INSTANCE_ID --name $AWS_AMI_NAME --description $AWS_AMI_DESCRIPTION --no-reboot
```

The command executes similarly to the standard version but skips the reboot, returning an AMI ID immediately. Verify completeness by checking the AMI state (available) via `aws ec2 describe-images`. If issues arise (e.g., inconsistent snapshot), recreate with reboot. This step reduces detection risk from instance state changes but increases the chance of corrupted images.
