---
type: procedure
description: >-
  This procedure outlines how to create a copy of an EC2 instance by generating
  an AMI from the source instance and launching a new instance from it, enabling
  lateral movement or persistence in an AWS environment.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Impact]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Inhibit System Recovery]]'
  - '[[Remote Services]]'
sub_techniques:
  - '[[Windows Remote Management]]'
tags:
  - aws
  - ec2
  - ami
  - cloud
  - lateral-movement
  - persistence
commands:
  - '[[commands/aws-ec2-describe-images-by-region]]'
  - '[[commands/aws-ec2-create-image-from-instance]]'
  - '[[commands/aws-ec2-import-key-pair]]'
  - '[[commands/aws-ec2-run-instances-from-ami]]'
  - '[[commands/aws-ec2-describe-instance-by-id]]'
  - '[[commands/aws-ec2-modify-instance-attribute-groups]]'
  - '[[commands/aws-ec2-stop-instance-by-id]]'
  - '[[commands/aws-ec2-terminate-instance-by-id]]'
tools:
  - '[[tools/AWS-CLI]]'
platforms:
  - AWS
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Copy-EC2-Instance-via-AMI-Creation-in-AWS

## Summary

This procedure demonstrates how to duplicate an EC2 instance in AWS by creating an Amazon Machine Image (AMI) from a source instance and launching a new instance from that AMI. In an offensive security context, this can facilitate lateral movement by replicating a compromised instance to gain access to additional resources while maintaining the same configuration, security groups, and IAM roles. It is useful for persistence, scaling attacks, or creating backup footholds in cloud environments.

## Description

Copying EC2 instances via AMI creation involves stopping or snapshotting the source instance to generate a reusable image, then using that image to spin up identical instances. Technically, the process captures the instance's root volume and configuration into an AMI, which can then be used with run-instances to launch clones. Offensively, an attacker with compromised AWS credentials can use this to propagate access across the infrastructure, potentially evading detection by mimicking legitimate scaling operations. The new instance inherits the source's settings but gets a new instance ID, IP, and hostname. This maps to cloud-specific lateral movement and impact tactics, as it can inhibit recovery by duplicating malicious configurations or using remote services for propagation.

## Requirements

1. AWS CLI installed and configured with credentials that have EC2 permissions (e.g., AmazonEC2FullAccess policy or specific permissions like ec2:CreateImage, ec2:RunInstances, ec2:ImportKeyPair, ec2:DescribeInstances, ec2:ModifyInstanceAttribute, ec2:StopInstances, ec2:TerminateInstances).
2. Source EC2 instance ID and access to its region.
3. SSH key pair for accessing the new instance (public key available locally).
4. Knowledge of the source instance's security groups, subnet, and AMI ID (if launching from an existing AMI).

## Defense

- Implement least privilege IAM policies to restrict ec2:CreateImage and ec2:RunInstances to authorized roles only.
- Enable AWS CloudTrail logging and monitor for unusual AMI creations or instance launches via Amazon GuardDuty or custom CloudWatch alarms.
- Use AWS Config rules to detect changes in instance attributes and tag instances for better tracking.
- Regularly audit EC2 instances for unauthorized duplicates and implement resource limits on AMI storage.

## Objectives

1. Duplicate a compromised EC2 instance to establish persistence or lateral movement in the AWS account.
2. Launch a new instance with identical configuration for further exploitation without altering the source.
3. Verify and clean up test instances to avoid unnecessary costs while simulating attack propagation.

## Instructions

### Step 1: List Available AMIs in the Region

**Context**: Before creating a new AMI, enumerate existing images to identify available options or verify the source instance's base AMI. This step helps in planning the copy and ensuring no conflicts.

**Command** ([[commands/aws-ec2-describe-images-by-region]]):
```bash
aws ec2 describe-images --region $_REGION
```

> This command queries AMIs in the specified region. Add --owners self or --filters "Name=tag-key,Values=Name" for targeted results. Why: Provides visibility into the environment and confirms the process feasibility.

### Step 2: Create AMI from Source Instance

**Context**: Generate an AMI snapshot of the source EC2 instance to capture its current state, including OS, applications, and configurations. The instance must be stopped for consistency, but this can be done running with noReboot option (less reliable).

**Command** ([[commands/aws-ec2-create-image-from-instance]]):
```bash
aws ec2 create-image --instance-id $_INSTANCE_ID --name "$_IMAGE_NAME" --description "$_DESCRIPTION" --region $_REGION
```

> Wait for the AMI to become available (status: available) by polling describe-images. Why: This creates the template for duplication; offensively, it preserves malware or backdoors on the instance.

### Step 3: Import SSH Key Pair

**Context**: Ensure an SSH key is available in AWS for secure access to the new instance. If not already present, import a public key to enable login.

**Command** ([[commands/aws-ec2-import-key-pair]]):
```bash
aws ec2 import-key-pair --key-name "$_KEY_NAME" --public-key-material file://$_PUBLIC_KEY_PATH --region $_REGION
```

> The public key file should be in PEM format. Why: Allows SSH access to the cloned instance without relying on existing keys that might be restricted.

### Step 4: Launch New Instance from AMI

**Context**: Use the created AMI to start a new EC2 instance, matching the source's security groups and subnet for seamless lateral movement.

**Command** ([[commands/aws-ec2-run-instances-from-ami]]):
```bash
aws ec2 run-instances --image-id $_AMI_ID --security-group-ids "$_SECURITY_GROUP_ID" --subnet-id $_SUBNET_ID --count 1 --instance-type $_INSTANCE_TYPE --key-name "$_KEY_NAME" --query "Instances[0].InstanceId" --region $_REGION
```

> Capture the output InstanceId for the new instance. Why: This deploys the duplicate, enabling access to the same resources as the source.

### Step 5: Describe the New Instance

**Context**: Verify the launched instance's status and details to confirm successful creation and readiness.

**Command** ([[commands/aws-ec2-describe-instance-by-id]]):
```bash
aws ec2 describe-instances --instance-ids $_INSTANCE_ID --region $_REGION
```

> Check State.Name: running. Why: Validates the copy and identifies the new IP for connection.

### Step 6: Modify Instance Attributes (If Needed)

**Context**: Adjust security groups or other attributes on the new instance to match the source or evade detection.

**Command** ([[commands/aws-ec2-modify-instance-attribute-groups]]):
```bash
aws ec2 modify-instance-attribute --instance-id $_INSTANCE_ID --groups "$_SECURITY_GROUP_ID" --region $_REGION
```

> Use if the launch didn't inherit correctly. Why: Ensures network access parity for lateral operations.

### Step 7: Stop the Instance

**Context**: Temporarily halt the new instance to save costs or simulate testing without full runtime.

**Command** ([[commands/aws-ec2-stop-instance-by-id]]):
```bash
aws ec2 stop-instances --instance-ids $_INSTANCE_ID --region $_REGION
```

> Why: Reduces exposure and costs during assessment.

### Step 8: Terminate the Instance

**Context**: Clean up the duplicate instance after use to avoid detection or billing issues.

**Command** ([[commands/aws-ec2-terminate-instance-by-id]]):
```bash
aws ec2 terminate-instances --instance-ids $_INSTANCE_ID --region $_REGION
```

> This is irreversible; confirm before running. Why: Maintains operational security by removing artifacts.

## Expected Output

Successful execution results in a new EC2 instance ID from the run-instances command, confirmed via describe-instances showing running state with matching configuration. AMI creation returns an AMI ID that appears in describe-images as available. No errors in CloudTrail logs for unauthorized actions.
