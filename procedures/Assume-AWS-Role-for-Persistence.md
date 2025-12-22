---
id: 1e5933a9-63eb-4ab3-9cb9-d0d02b280e8d
name: Assume-AWS-Role-for-Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.906348+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access Token Manipulation|T1134 - Access Token Manipulation]]'
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - '[[tags/5. Exploitation Scenario]]'
  - '[[tags/Accessing more credentials]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Getting temporary credentials for the role]]'
  - '[[tags/Persistence & Backdooring]]'
commands:
  - '[[commands/assume-aws-role]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Assume-AWS-Role-for-Persistence

## Summary

Assuming an AWS role provides an attacker with persistent access to a target's AWS resources by obtaining temporary security credentials. These credentials allow continued operations even if the original access keys are revoked or rotated. This procedure is particularly useful for lateral movement within an AWS environment, maintaining long-term presence, and accessing sensitive data or services permitted by the role's policy.

## Description

In an AWS environment, roles define permissions that can be assumed by trusted entities. An attacker with initial valid credentials (such as compromised IAM user keys) can use the Security Token Service (STS) AssumeRole API to request temporary credentials for a target role. These credentials include an access key ID, secret access key, and session token, valid for a configurable duration (default 1 hour, up to 12 hours). This technique enables privilege escalation if the role has higher permissions and supports persistence by allowing the attacker to refresh credentials without relying on static keys. It is commonly used post-compromise to evade detection and expand access to S3 buckets, EC2 instances, or other services.

## Requirements

1. Valid AWS credentials (e.g., access key ID and secret access key from a compromised IAM user or assumed role) configured in the AWS CLI.
2. AWS CLI installed and accessible on the attacker's system.
3. Knowledge of the target role's ARN (Amazon Resource Name), typically obtained through enumeration of IAM policies or instance metadata.
4. Network access to AWS STS endpoints (requires internet connectivity or VPC endpoint configuration).

## Defense

Defensive measures and detection strategies:

- Enforce the principle of least privilege by limiting role permissions and requiring MFA for role assumption where possible.
- Monitor AWS CloudTrail logs for AssumeRole API calls, focusing on unusual source IPs, session names, or roles assumed from unexpected principals.
- Implement AWS Organizations SCPs (Service Control Policies) to restrict cross-account role assumptions.
- Enable GuardDuty for threat detection on anomalous IAM activities and use CloudWatch alarms on STS events.

## Objectives

1. Assume a specified AWS IAM role using existing credentials.
2. Obtain temporary security credentials (access key, secret key, session token) for the role.
3. Use the temporary credentials to perform authorized actions on AWS resources, establishing persistence.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Before assuming a role, ensure the AWS CLI is installed and configured with valid credentials. This step confirms access to AWS services and prevents authentication errors during role assumption.

Use the [[commands/aws-configure-list]] command to check current configuration:

```bash
aws configure list
```

> This command displays the current profile, region, and credential source. If credentials are not set, configure them using `aws configure` with your access key, secret key, and default region (e.g., us-east-1). Expected output includes credential file paths and no errors.

### Step 2: Assume the Target AWS Role

**Context**: Use the STS AssumeRole operation to request temporary credentials for the specified role. This step generates short-lived tokens that inherit the role's permissions, allowing the attacker to operate under elevated privileges without exposing long-term keys.

Execute [[commands/assume-aws-role]] with the role ARN and a unique session name:

```bash
aws sts assume-role --role-arn $_ROLE_ARN --role-session-name $_SESSION_NAME
```

> Replace $_ROLE_ARN with the full ARN of the target role (e.g., arn:aws:iam::123456789012:role/MyTargetRole) and $_SESSION_NAME with an identifier like "attacker-session-001". This command sends a request to STS, which validates the caller's permissions to assume the role. If successful, it returns JSON with temporary credentials. Export these to environment variables for subsequent AWS API calls (e.g., export AWS_ACCESS_KEY_ID=...).

### Step 3: Validate Assumed Role Credentials

**Context**: Test the temporary credentials by performing a simple authorized action, such as listing S3 buckets if permitted by the role. This verifies persistence and confirms the assumption worked without issues.

Use [[commands/aws-s3-ls]] to list buckets:

```bash
aws s3 ls
```

> Run this after exporting the temporary credentials from Step 2. Expected output lists S3 buckets accessible to the role. If the role lacks S3 permissions, use another API call like `aws iam get-user` to confirm identity. Success indicates the role is assumed and credentials are active.
