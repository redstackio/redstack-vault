---
tags:
  - aws
  - iam
  - recon
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/aws-iam-get-role]]'
  - '[[commands/aws-iam-list-attached-role-policies]]'
  - '[[commands/aws-iam-get-policy-version]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1087.004]]'
updated_at: '2025-12-14T17:30:26.671Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 27240147-0882-42f4-ba49-fd46f98e38ea
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
---
# Review-IAM-Role-Policies

## Summary

This procedure examines the IAM policies attached to the role created by the deployed Serverless application, identifying the permissive sts:AssumeRole action on all resources.

## Description

After deployment, the IAM role for the ExtractCarbonEmissionsFunction uses AWS-managed policies that allow sts:AssumeRole without resource restrictions, enabling role assumption across the organization. This reconnaissance step confirms the vulnerability before exploitation.

## Requirements

1. AWS CLI configured with iam:GetRole and iam:ListAttachedRolePolicies permissions
2. Role ARN from the deployment step
3. Access to the AWS account where the role was created

## Defense

Defensive measures and detection strategies:

- Enable IAM Access Analyzer to detect overly broad policies
- Audit all Lambda roles for permissions boundaries
- Log and alert on iam:GetRole API calls from unexpected sources via CloudTrail

## Objectives

1. Retrieve role details and attached policies
2. Verify the presence of '*' resource in sts:AssumeRole
3. Document the misconfiguration for exploitation planning

## Instructions

### Step 1: Get Role Details

**Context**: Fetch the basic role information to confirm existence and ARN.

**Command** ([[commands/aws-iam-get-role]]):
```bash
aws iam get-role --role-name ExtractCarbonEmissionsFunction-role-xyz
```

> Replace role-name with the actual name. Output includes Role ARN and assume role policy document.

### Step 2: List Attached Policies

**Context**: Identify policies attached to the role, focusing on those granting STS permissions.

**Command** ([[commands/aws-iam-list-attached-role-policies]]):
```bash
aws iam list-attached-role-policies --role-name ExtractCarbonEmissionsFunction-role-xyz
```

> Output lists policy ARNs, such as AWSLambdaBasicExecutionRole.

### Step 3: Get Policy Version

**Context**: Inspect the policy document to confirm permissive actions.

**Command** ([[commands/aws-iam-get-policy-version]]):
```bash
aws iam get-policy-version --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole --version-id v1
```

> Look for "sts:AssumeRole" with "Resource": "*". This confirms the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[T1087.004]]

### Sub-Techniques


## Commands Used

- [[commands/aws-iam-get-role]]
- [[commands/aws-iam-list-attached-role-policies]]
- [[commands/aws-iam-get-policy-version]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- iam
- reconnaissance
