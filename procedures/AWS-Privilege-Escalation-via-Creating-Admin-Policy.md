---
id: 540f3976-3757-4dd9-9dbb-89f1464eb457
name: AWS-Privilege-Escalation-via-Creating-Admin-Policy
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.517831+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - >-
    [[techniques/Steal Application Access Token|T1528 - Steal Application Access
    Token]]
sub_techniques: []
tags:
  - '[[tags/5. Exploitation Scenario]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Exploitation]]'
  - '[[tags/Privilege Escalation]]'
  - '[[tags/Study Case]]'
commands:
  - '[[commands/aws-iam-list-attached-user-policies]]'
  - '[[commands/aws-iam-create-policy]]'
  - '[[commands/aws-iam-attach-user-policy]]'
  - '[[commands/aws-sts-get-session-token]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS-Privilege-Escalation-via-Creating-Admin-Policy

## Summary

This procedure exploits partial IAM permissions on a compromised AWS account to create and attach a full administrative policy, escalating privileges to gain unrestricted access across the AWS environment. By discovering current permissions and crafting a broad policy document, an attacker can assume god-like control, enabling data exfiltration, resource modification, or further lateral movement.

## Description

In AWS, if a compromised user or role has permissions to create and attach IAM policies (e.g., iam:CreatePolicy, iam:AttachUserPolicy), an attacker can craft a custom policy granting full access to all services and resources. This technique leverages the AWS IAM system's flexibility against itself, often stemming from overly permissive default or inherited roles. The process involves listing existing policies to understand the baseline, creating a new policy with wildcard permissions, attaching it to the current user/role, and then generating elevated session tokens via STS. This can lead to complete environment compromise, such as deleting S3 buckets or launching EC2 instances. It targets cloud environments where least-privilege is not enforced, typically requiring initial access via stolen credentials from an EC2 instance or API key exposure.

## Requirements

1. Valid AWS access key ID and secret access key for a compromised IAM user or role with at least iam:List* and iam:CreatePolicy permissions.
2. AWS CLI installed and configured with the compromised credentials (aws configure).
3. Network access to AWS APIs (no VPC endpoints blocking IAM/STF calls).
4. Basic knowledge of IAM policy syntax to customize the policy if needed.

## Defense

- Enforce strict least-privilege IAM policies and avoid granting iam:CreatePolicy or iam:Attach* to non-admin roles.
- Enable AWS CloudTrail logging for IAM actions and monitor for policy creation/attachment events using CloudWatch or SIEM tools.
- Use IAM Access Analyzer to review and revoke overly broad policies regularly.
- Implement MFA for all IAM users and rotate credentials frequently.
- Set AWS Organizations SCPs to deny wildcard (*) actions on sensitive resources.

## Objectives

1. Discover current IAM permissions to identify escalation vectors.
2. Create and attach a full-access policy to the compromised entity.
3. Generate elevated session tokens for persistent high-privilege access.
4. Achieve administrative control over AWS resources for further exploitation.

## Instructions

### Step 1: List Attached User Policies

**Context**: Begin by enumerating the current policies attached to the compromised IAM user to understand existing permissions and confirm the ability to create/attach new ones. This discovery step maps the baseline access and identifies if escalation is feasible.

**Command** ([[commands/aws-iam-list-attached-user-policies]]):
```bash
aws iam list-attached-user-policies --user-name $COMPROMISED_USER
```

> This command queries the IAM service for managed policies linked to the user. Replace $COMPROMISED_USER with the target username (e.g., from aws sts get-caller-identity). If the response includes policies like AdministratorAccess, escalation may already be possible; otherwise, proceed if no blocking denials appear. Expected output is a JSON array of policy ARNs; look for partial permissions like "iam:CreatePolicy" in policy details.

### Step 2: Create Admin Policy Document

**Context**: Prepare a local JSON file defining a full-access IAM policy. This policy uses wildcards to allow all actions on all resources, exploiting the lack of restrictions to grant admin rights.

**Instructions**: Create a file named admin-policy.json with the following content (reference [[codes/AWS-IAM-Full-Access-Policy]] for the exact snippet):

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "*"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

> Save this file locally. The Version should be 2012-10-17 for compatibility (updated from original). Verify syntax with a JSON linter. This step doesn't interact with AWS yet but prepares the payload for upload.

### Step 3: Upload and Create the Policy in AWS

**Context**: Use the AWS CLI to create a new managed policy from the local JSON file. This step requires iam:CreatePolicy permission; if denied, the attack fails here—pivot to role assumption if available.

**Command** ([[commands/aws-iam-create-policy]]):
```bash
aws iam create-policy --policy-name AdminEscalationPolicy --policy-document file://admin-policy.json --description "Escalated admin policy for compromised access"
```

> This uploads the policy and returns an ARN (e.g., arn:aws:iam::123456789012:policy/AdminEscalationPolicy). Note the ARN for the next step. If successful, the policy is now available account-wide. Expected output: JSON with Policy ARN and creation date.

### Step 4: Attach Policy to Compromised User

**Context**: Attach the newly created policy to the compromised user or role to immediately escalate privileges. This grants the full access defined in the policy.

**Command** ([[commands/aws-iam-attach-user-policy]]):
```bash
aws iam attach-user-policy --user-name $COMPROMISED_USER --policy-arn $POLICY_ARN
```

> Replace $POLICY_ARN with the ARN from Step 3. No output if successful (HTTP 200). Verify attachment by re-running Step 1. If the user lacks iam:AttachUserPolicy, attempt role attachment via --role-name if targeting a role.

### Step 5: Generate Elevated Session Token

**Context**: With the admin policy attached, generate temporary STS credentials for safer, time-bound access. This steals application-level tokens for further operations without exposing long-term keys.

**Command** ([[commands/aws-sts-get-session-token]]):
```bash
aws sts get-session-token --duration-seconds 3600 --serial-number $MFA_ARN --token-code $MFA_CODE
```

> If MFA is required, provide it; otherwise, omit for non-MFA users. Expected output: JSON with AccessKeyId, SecretAccessKey, and SessionToken. Export these (export AWS_ACCESS_KEY_ID=...) for use in subsequent AWS CLI calls. Success confirms escalation—test with aws s3 ls to access restricted buckets.
