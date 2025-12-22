---
id: e5179d86-a4d9-4aaf-900f-91e68e7344fa
name: AWS-IAM-Managed-Policy-Version-Retrieval
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.027273+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - cloud-aws
  - iam-discovery
  - policy-enumeration
commands:
  - '[[commands/aws-iam-get-policy-version]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# AWS-IAM-Managed-Policy-Version-Retrieval

## Summary

The AWS IAM Managed Policy Version Retrieval procedure enables the extraction of version details for managed policies in AWS Identity and Access Management (IAM). This allows attackers to assess policy evolution, identify outdated or misconfigured permissions, and map access controls for subsequent exploitation in a cloud environment.

## Description

In an AWS environment, managed policies define permissions attached to users, groups, or roles. Retrieving version information reveals historical changes, default versions, and policy documents, which can expose overly permissive configurations or recent modifications that indicate defensive updates. This procedure is typically used during the discovery phase to enumerate IAM structures without alerting defenders, as it leverages standard API calls. It requires IAM read permissions and is executed via the AWS CLI, providing JSON output with policy documents, version IDs, and creation dates. Attackers can chain this with other IAM enumeration to build a comprehensive view of privileges, facilitating persistence or lateral movement.

## Requirements

1. Valid AWS credentials with iam:GetPolicyVersion permission (or broader IAM read access).
2. AWS CLI installed and configured with the target account's credentials (via aws configure or environment variables).
3. Knowledge of the target policy ARN and version ID, often obtained from prior enumeration like listing policies.
4. Network access to AWS APIs (no direct console access required).

## Defense

- Implement least-privilege access: Restrict iam:GetPolicyVersion to administrative roles only and monitor its usage via AWS CloudTrail.
- Enable comprehensive logging: Use CloudTrail to log all IAM API calls, setting up alerts for unusual policy queries.
- Regularly audit policies: Use AWS Config rules to track policy versions and changes, ensuring no dormant permissive versions exist.
- Multi-factor authentication and session policies: Enforce MFA for IAM users and use session policies to limit query scopes.

## Objectives

1. Retrieve detailed version information for a specific IAM managed policy, including the policy document and metadata.
2. Identify policy updates or misconfigurations that could enable privilege escalation or unauthorized access.
3. Gather intelligence on the target's IAM setup to inform targeted attacks, such as credential abuse or policy modification.

## Instructions

### Step 1: Identify Target Policy and Version

**Context**: Before retrieval, ensure you have the policy ARN (e.g., from aws iam list-policies) and the specific version ID (e.g., 'v1' for the default). This step confirms prerequisites without executing the main query.

Run a preliminary list to verify:

**Command** ([[commands/aws-iam-list-policies]]):

```bash
aws iam list-policies --scope AWS
```

> This lists managed policies. Note the ARN of the target policy (e.g., arn:aws:iam::123456789012:policy/MyManagedPolicy). Then, use aws iam get-policy to get versions if needed. Expected output: JSON array of policies with ARNs. If no policies match, adjust scope or credentials.

### Step 2: Retrieve Policy Version Details

**Context**: Execute the core query to fetch the policy version, revealing the permissions defined in that version. This provides the JSON document for analysis, helping identify actions like s3:* or ec2:RunInstances that could be abused.

**Command** ([[commands/aws-iam-get-policy-version]]):

```bash
aws iam get-policy-version --policy-arn $_POLICY_ARN --version-id $_VERSION_ID
```

> Replace $_POLICY_ARN with the full ARN (e.g., arn:aws:iam::123456789012:policy/MyPolicy) and $_VERSION_ID with the version (e.g., v1). This returns the policy document in JSON, including statements, effects, and resources. Parse the output to check for broad permissions. If the version is default, it indicates active usage. Success is confirmed by a 200 response with PolicyVersion object; errors like AccessDenied indicate insufficient permissions.
