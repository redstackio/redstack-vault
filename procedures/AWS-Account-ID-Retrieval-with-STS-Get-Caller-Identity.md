---
id: 3df35023-6a80-4112-bef0-84874c2924a9
name: AWS-Account-ID-Retrieval-with-STS-Get-Caller-Identity
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.433316+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/5. Exploitation Scenario]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Exploitation]]'
  - '[[tags/Privilege Escalation]]'
  - '[[tags/Study Case]]'
  - cloud
  - discovery
  - aws
commands:
  - '[[commands/aws-sts-get-caller-identity]]'
platforms:
  - AWS
  - Linux
tools:
  - '[[tools/AWS-CLI]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# AWS-Account-ID-Retrieval-with-STS-Get-Caller-Identity

## Summary

This procedure uses the AWS Security Token Service (STS) GetCallerIdentity API via the AWS CLI to retrieve the AWS account ID, ARN, and user ID associated with the current credentials. It is useful in cloud environments for discovering the scope of access after initial compromise, enabling attackers to map resources and plan privilege escalation.

## Description

In an AWS environment, once an attacker has obtained valid credentials (e.g., via instance metadata, stolen keys, or assumed roles), they can query the STS service to identify the account details without needing additional permissions beyond basic STS access. This reveals the account ID (a 12-digit number), the ARN of the IAM entity (user or role), and a unique user ID. This information helps determine if the credentials belong to a production account, identify the access level, and target further actions like enumerating S3 buckets or EC2 instances tied to that account. The technique is low-risk for detection if credentials are already valid but can trigger API logging if monitored.

## Requirements

1. Valid AWS credentials configured in the environment (e.g., via AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, or IAM role on an EC2 instance).
2. AWS CLI installed and accessible (version 1.x or 2.x).
3. Network access to AWS STS endpoints (typically allowed by default in AWS environments).
4. Permissions to call sts:GetCallerIdentity (usually granted to most IAM users/roles).

## Defense

- Enable multi-factor authentication (MFA) for all IAM users and require it for sensitive actions.
- Monitor CloudTrail logs for sts:GetCallerIdentity calls, especially from unusual sources or high volumes, using AWS GuardDuty or custom alerts.
- Implement least privilege by scoping IAM policies to deny unnecessary STS actions and regularly audit credentials.
- Use AWS Organizations to isolate accounts and detect cross-account access attempts.

## Objectives

1. Retrieve the AWS account ID to identify the compromised account.
2. Obtain the ARN and user ID to assess the IAM entity's permissions.
3. Use the information to pivot to resource enumeration or escalation in the discovered account.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is installed and credentials are properly set up to authenticate API calls. This step confirms the environment before executing the discovery command.

Use [[tools/AWS-CLI]] to check configuration:

```bash
aws configure list
```

> This command displays current credential sources, regions, and output formats. Expected output includes details like profile name and credential file paths. If no credentials are shown, configure them using `aws configure` with access key, secret key, region (e.g., us-east-1), and output format (json).

### Step 2: Execute STS GetCallerIdentity

**Context**: Call the STS API to retrieve identity details. This is the core step that provides the account information without requiring elevated privileges.

**Command** ([[commands/aws-sts-get-caller-identity]]):

```bash
aws sts get-caller-identity
```

> Run this command in a terminal with AWS CLI access. It queries the STS service using the current credentials. If successful, it returns a JSON response with Account, Arn, and UserId fields. For example:

```json
{
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/example-user",
    "UserId": "AIDAXYZ1234567890"
}
```

If the command fails (e.g., invalid credentials), it will error with an AccessDenied or InvalidClientTokenId message—troubleshoot by verifying credentials in Step 1.

### Step 3: Parse and Validate Output

**Context**: Review the JSON output to extract key details and confirm the access scope. This helps decide next actions, such as checking for admin roles.

Use standard tools like `jq` (if available) to parse the JSON:

```bash
aws sts get-caller-identity | jq '.Account'
```

> Expected output: The 12-digit account ID as a string, e.g., "123456789012". Cross-reference the ARN to identify if it's a user, role, or assumed role, and note the account for further enumeration (e.g., list S3 buckets with `aws s3 ls`).

Success is indicated by a valid JSON response without errors; failure suggests credential issues or network blocks.
