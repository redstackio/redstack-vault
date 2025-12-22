---
id: d0328dbb-8175-4f32-8e91-d6260eb99b45
name: AWS-IAM-Policy-Information-Gathering
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.672409+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud-Service-Dashboard|T1538 - Cloud Service Dashboard]]'
sub_techniques: []
tags:
  - '[[tags/Checking-informations-about-a-specific-policy]]'
  - '[[tags/Cloud-AWS]]'
  - '[[tags/Persistence]]'
commands:
  - '[[commands/aws-iam-get-policy-version]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS-IAM-Policy-Information-Gathering

## Summary

This procedure retrieves detailed information about a specific IAM policy in an AWS account using the AWS CLI, allowing attackers or auditors to inspect the policy document, permissions, and versions to identify potential privilege escalation paths or misconfigurations.

## Description

In an AWS environment, IAM policies define permissions for users, groups, and roles. This procedure focuses on querying a specific policy's version via the AWS API to obtain the JSON policy document, which can be analyzed for overly permissive actions like unrestricted S3 access or admin privileges. It is typically used during discovery phases of an engagement to map access rights without alerting monitoring, assuming the attacker has credentials with iam:GetPolicyVersion permission. The output reveals statements, effects (Allow/Deny), resources, and conditions, enabling further targeting of exploitable permissions. This aligns with cloud reconnaissance to understand the attack surface in multi-tenant or compromised AWS accounts.

## Requirements

1. Valid AWS credentials with at least iam:GetPolicyVersion permission.
2. AWS CLI installed and configured with the target account's access keys or role.
3. Network access to AWS API endpoints (no VPC restrictions blocking IAM calls).
4. Knowledge of the target policy's ARN and version ID (obtainable via prior enumeration like aws iam list-policies).

## Defense

- Implement least privilege: Restrict iam:GetPolicyVersion to only necessary roles and monitor its usage via CloudTrail.
- Enable AWS CloudTrail logging for IAM API calls and set up alerts for unusual policy queries from unexpected IPs or roles.
- Use IAM Access Analyzer to review policies for external access risks and rotate credentials regularly.
- Apply AWS Organizations SCPs to limit policy inspection in sensitive accounts.

## Objectives

1. Retrieve the JSON document of a specific IAM policy version.
2. Analyze permissions to identify escalation opportunities, such as wildcard actions or broad resource access.
3. Gather intelligence on AWS IAM configurations for targeted exploitation or auditing.

## Instructions

### Step 1: Retrieve the IAM Policy Version

**Context**: Use the AWS CLI to fetch the policy document for a given ARN and version ID. This step requires knowing the policy ARN (e.g., from prior listing) and version ID (default is the current version if not specified). The command outputs the policy in JSON format, which can be piped to jq for parsing or saved for offline analysis.

**Command** ([[commands/aws-iam-get-policy-version]]):
```bash
aws iam get-policy-version --policy-arn $_POLICY_ARN --version-id $_VERSION_ID
```

> This command queries the AWS IAM service and returns the policy details if successful. If the version ID is invalid or permissions are insufficient, it errors with AccessDenied or NoSuchEntity. Review the output JSON for 'PolicyVersion' > 'Document' to see the permissions array, checking for high-risk actions like '*:*' or access to critical services (e.g., ec2:RunInstances).

### Step 2: Analyze the Policy Document

**Context**: Parse the retrieved JSON to identify exploitable permissions. This manual step involves inspecting the policy statements for Allow effects on sensitive actions, resources, or conditions that could lead to escalation (e.g., assuming roles with admin policies).

> Use tools like jq to filter: `aws iam get-policy-version ... | jq '.PolicyVersion.Document.Statement[] | select(.Effect == "Allow")'`. Look for patterns like Resource: "*" or actions including iam:PassRole, which could enable further compromise. Document findings for chaining with other procedures like role assumption.
