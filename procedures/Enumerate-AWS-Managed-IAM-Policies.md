---
id: 8b0900b9-2e3d-4fe5-a1bb-31eecc78a7b0
name: Enumerate-AWS-Managed-IAM-Policies
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.292361+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - enumerating-policies
  - cloud-aws
  - iam-discovery
commands:
  - '[[commands/aws-iam-list-managed-policies]]'
  - '[[commands/aws-iam-get-policy-metadata]]'
  - '[[commands/aws-iam-get-policy-document]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Enumerate-AWS-Managed-IAM-Policies

## Summary

This procedure enumerates AWS managed IAM policies by listing available policies, retrieving their metadata, and extracting the policy documents to identify permissions and potential misconfigurations that could reveal attack paths in an AWS environment.

## Description

In an AWS environment, managed IAM policies define permissions for users, groups, and roles. Attackers use this procedure during discovery to map out policy structures, identify overly permissive policies, and uncover paths to privilege escalation or unauthorized resource access. The technique leverages AWS IAM APIs via the CLI to query managed policies (those created by AWS), which are scoped to 'AWS'. This reveals policy ARNs, versions, and JSON documents containing statements with actions, resources, and conditions. Prerequisites include authenticated AWS CLI access with iam:ListPolicies, iam:GetPolicy, and iam:GetPolicyVersion permissions. The procedure helps in understanding the permission landscape without alerting if done stealthily.

## Requirements

1. AWS CLI installed and configured with credentials having IAM read permissions (e.g., iam:ListPolicies, iam:GetPolicy, iam:GetPolicyVersion).
2. Network access to AWS APIs (no VPC endpoints required for public IAM).
3. Basic knowledge of AWS ARNs and JSON policy structure.

## Defense

- Implement least-privilege IAM policies to restrict read access to policies.
- Enable AWS CloudTrail logging for IAM API calls and monitor for unusual GetPolicy or ListPolicies requests.
- Use AWS Config rules to audit policy attachments and permissions regularly.

## Objectives

1. List all AWS managed IAM policies to obtain ARNs.
2. Retrieve policy metadata including attachment counts and versions.
3. Extract policy documents to analyze permissions for vulnerabilities.

## Instructions

### Step 1: List Managed Policies

**Context**: Begin by listing all AWS-managed policies to discover available policies and their ARNs. This step uses the --scope AWS flag to filter only AWS-created policies, excluding customer-managed ones.

**Command** ([[commands/aws-iam-list-managed-policies]]):
```bash
aws iam list-policies --scope AWS --query 'Policies[].{PolicyName:PolicyName,Arn:Arn}' --output table
```

> This command queries the IAM service for managed policies and outputs a table of policy names and ARNs. Use the --query option to focus on relevant fields for easier parsing. If no policies are returned, verify credentials or permissions.

### Step 2: Retrieve Policy Metadata

**Context**: Select a policy ARN from the list and fetch its metadata, such as creation date, attachment count, and default version. This helps assess the policy's usage and age without downloading the full document.

**Command** ([[commands/aws-iam-get-policy-metadata]]):
```bash
aws iam get-policy --policy-arn arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess
```

> Replace the ARN with a specific one from Step 1. The output includes details like IsAttachable (true for usable policies) and UpdateDate. High attachment counts may indicate critical policies worth further scrutiny.

### Step 3: Extract Policy Document

**Context**: Using the default version ID from the metadata, retrieve the full policy document in JSON format. This reveals the exact permissions (e.g., ec2:DescribeInstances) and conditions, allowing analysis for excessive privileges or weak resource restrictions.

**Command** ([[commands/aws-iam-get-policy-document]]):
```bash
aws iam get-policy-version --policy-arn arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess --version-id v1
```

> The --version-id is typically 'v1' for default versions. Parse the PolicyVersion.Document field for statements. Look for wildcards like '*' in Actions or Resources, which could indicate over-permissions.
