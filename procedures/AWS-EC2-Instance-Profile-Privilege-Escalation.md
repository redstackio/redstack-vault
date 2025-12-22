---
id: 956735b5-bb28-4c5f-8c29-908fe72e84b0
name: AWS-EC2-Instance-Profile-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.533522+00:00'
updated_at: '2023-04-10T20:20:54.100763+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Cloud Instance Metadata API|T1522 - Cloud Instance Metadata
    API]]
sub_techniques: []
tags:
  - '[[tags/Attach an instance profile to an EC2 instance]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Exploitation]]'
  - '[[tags/Privilege Escalation]]'
commands:
  - '[[commands/aws-ec2-associate-iam-instance-profile]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS-EC2-Instance-Profile-Privilege-Escalation

## Summary

This procedure demonstrates how to escalate privileges on an AWS EC2 instance by attaching an IAM instance profile with elevated permissions using the AWS CLI. It allows an attacker with sufficient IAM permissions to modify the instance's role, enabling access to sensitive resources via the instance metadata service.

## Description

In AWS environments, EC2 instances can be associated with IAM roles through instance profiles, which provide temporary credentials accessible via the Instance Metadata Service (IMDS). An attacker who has compromised an EC2 instance or has IAM permissions to manage instance profiles can attach a higher-privilege instance profile to the target instance. This escalates the effective permissions of processes running on the instance, allowing unauthorized actions such as data access, resource modification, or lateral movement. The technique relies on the AWS CLI or SDKs and requires the attacker to know the instance ID and the target instance profile name. Once attached, the new credentials become available immediately through IMDS, without restarting the instance. This is particularly effective in misconfigured environments where instance profile management permissions are overly permissive.

## Requirements

1. AWS CLI installed and configured with credentials that have permissions to call `ec2:AssociateIamInstanceProfile` (e.g., via IAM policy allowing EC2 instance modifications).
2. Access to the target EC2 instance ID (discoverable via `aws ec2 describe-instances` if permissions allow).
3. Knowledge of an existing IAM instance profile with elevated permissions (e.g., admin role) that can be attached.
4. The target EC2 instance must not already have an incompatible instance profile or be in a stopped state.

## Defense

Defensive measures and detection strategies:

- Ensure that instance profiles are assigned the principle of least privilege and regularly audit IAM policies for excessive `ec2:AssociateIamInstanceProfile` permissions.
- Monitor changes to instance profiles attached to EC2 instances using AWS CloudTrail logs for the `AssociateIamInstanceProfile` API call, and set up alerts for unauthorized modifications.
- Implement network segmentation and IMDSv2 enforcement to limit lateral movement and metadata access within the cloud environment.
- Use AWS Config rules to detect and remediate instances with unexpectedly high-privilege roles.

## Objectives

1. Escalate privileges of an EC2 instance by attaching a higher-privilege IAM instance profile.
2. Gain access to sensitive data or resources via the updated instance metadata credentials.
3. Execute unauthorized actions within the AWS cloud environment using the elevated permissions.

## Instructions

### Step 1: Identify the Target Instance and Profile

**Context**: Before attaching the profile, confirm the target EC2 instance ID and ensure the desired IAM instance profile exists with elevated permissions. This step verifies prerequisites and avoids errors.

Use AWS CLI to describe the instance if needed (assuming you have `ec2:DescribeInstances` permission):

**Command** ([[commands/aws-ec2-describe-instances]]):
```bash
aws ec2 describe-instances --instance-ids i-1234567890abcdef0
```

> This command lists details about the instance, including its current instance profile. Expected output includes JSON with instance metadata; look for the current `IamInstanceProfile` ARN to confirm it's low-privilege.

### Step 2: Attach the Elevated IAM Instance Profile

**Context**: Associate the new IAM instance profile with the target EC2 instance. This immediately updates the instance's role, allowing processes on the instance to assume the new permissions via IMDS.

**Command** ([[commands/aws-ec2-associate-iam-instance-profile]]):
```bash
aws ec2 associate-iam-instance-profile --instance-id i-1234567890abcdef0 --iam-instance-profile Name=MyElevatedProfile
```

> Replace `i-1234567890abcdef0` with the actual instance ID and `MyElevatedProfile` with the name of the target instance profile. Expected output is JSON confirming the association, including the `InstanceProfileAssociationId`. If successful, no errors occur, and the change is effective within seconds.

### Step 3: Verify the Escalation

**Context**: Confirm the new profile is attached and test elevated access by querying instance metadata from the EC2 instance or using the new credentials.

SSH into the target instance (if accessible) and curl the metadata service:

**Command** ([[commands/curl-imds-get-role]]):
```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

> Expected output lists the new role name from the attached profile. Further, test a privileged action like listing S3 buckets with `aws s3 ls` using instance credentials to confirm escalation.
