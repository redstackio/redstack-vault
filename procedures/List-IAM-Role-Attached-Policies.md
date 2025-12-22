---
id: c4425000-12d2-4360-bfaa-4c7767c9dd4c
name: List-IAM-Role-Attached-Policies
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.006501+00:00'
updated_at: '2023-04-10T20:19:59.250263+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[T1087.004]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/IAM-enumeration]]'
  - '[[tags/Discovery]]'
  - '[[tags/Persistence]]'
commands:
  - '[[commands/aws-iam-list-attached-role-policies]]'
tools:
  - '[[tools/AWS-CLI]]'
platforms:
  - AWS
skill_level: beginner
impact_level: low
detection_risk: medium
validated: true
---

# List-IAM-Role-Attached-Policies

## Summary

This procedure uses the AWS CLI to list all managed policies attached to a specific IAM role, providing visibility into the permissions granted to that role. It is commonly used in cloud security assessments to identify overly permissive policies that could enable privilege escalation or unauthorized access to AWS resources.

## Description

In AWS Identity and Access Management (IAM), roles define permissions for entities like EC2 instances or users assuming the role. Listing attached policies reveals the actions allowed by the role, such as access to S3 buckets or EC2 instances. From an offensive security perspective, attackers with initial AWS access can enumerate these to map permissions and pivot to higher-privilege actions. Defensively, this helps audit roles for least-privilege violations. The procedure requires AWS CLI configured with credentials that have iam:ListAttachedRolePolicies permission. It targets a single role and outputs policy ARNs, names, and descriptions in JSON format for further analysis.

## Requirements

1. AWS CLI installed and configured with access keys or IAM role assuming credentials that include iam:ListAttachedRolePolicies permission.
2. Network access to AWS API endpoints (no specific ports beyond standard HTTPS/443).
3. Target IAM role name known or discoverable via prior enumeration (e.g., from assuming a role or listing roles).

## Defense

- Implement least-privilege access: Attach only necessary managed policies to IAM roles and regularly audit attachments using AWS IAM Access Analyzer.
- Enable AWS CloudTrail logging for IAM API calls to detect unauthorized enumeration attempts.
- Use IAM policies to deny iam:ListAttachedRolePolicies for non-administrative roles and monitor for anomalous API usage via Amazon GuardDuty.

## Objectives

1. Retrieve a list of all managed policies attached to the specified IAM role.
2. Analyze policy permissions to identify potential privilege escalation paths.
3. Document role capabilities for reporting or further exploitation in a red team engagement.

## Instructions

### Step 1: List Attached Policies for the IAM Role

**Context**: This step queries the AWS IAM service to fetch all managed policies directly attached to the target role. The output provides policy identifiers that can be further inspected with additional commands like aws iam get-policy-version. Ensure your AWS CLI profile has the required permissions; otherwise, the command will fail with an AccessDenied error.

**Command** ([[commands/aws-iam-list-attached-role-policies]]):
```bash
aws iam list-attached-role-policies --role-name $_ROLE_NAME
```

> This command sends a request to the IAM API and returns a JSON object containing an array of attached policies. Each policy entry includes the policy name, ARN, and an optional description. If no policies are attached, the array will be empty. Review the ARNs to identify broad permissions like AdministratorAccess, which indicate high-risk roles. Pipe the output to jq for parsing if needed (e.g., | jq '.AttachedPolicies[].PolicyArn').

**Expected Output**:
```json
{
    "AttachedPolicies": [
        {
            "PolicyName": "AmazonS3ReadOnlyAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess",
            "RoleName": "MyTargetRole"
        }
    ],
    "IsTruncated": false
}
```

### Step 2: Verify and Analyze Output

**Context**: After retrieving the list, validate the results and cross-reference policy names against known AWS managed policies to assess risk. This manual step ensures the enumeration aligns with the engagement scope and identifies escalation opportunities, such as roles with PassRole permissions.

> No specific command here; inspect the JSON output manually or use tools like jq to filter (e.g., aws iam list-attached-role-policies --role-name $_ROLE_NAME | jq '.AttachedPolicies[] | select(.PolicyName | contains("Admin"))'). If policies look permissive, proceed to fetch the full policy document using aws iam get-role-policy or similar for deeper analysis.
