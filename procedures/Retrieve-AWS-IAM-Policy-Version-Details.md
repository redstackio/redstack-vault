---
id: d698bc9a-db5d-46c9-afc3-74278058a21f
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.258417+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud-Service-Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/IAM Enumeration]]'
  - '[[tags/Policy Discovery]]'
commands:
  - '[[commands/aws-iam-get-policy-version]]'
platforms:
  - AWS
tools: []
validated: true
---

# Retrieve-AWS-IAM-Policy-Version-Details

## Summary

This procedure retrieves detailed information about a specific version of an AWS IAM policy, allowing an attacker to analyze permissions, identify misconfigurations, and discover potential privilege escalation paths or sensitive access rights within the AWS environment.

## Description

In an AWS cloud attack scenario, understanding IAM policies is crucial for mapping out access controls and identifying weaknesses. This procedure uses the AWS CLI to fetch a specific policy version by its ARN and version ID. The retrieved policy document can reveal allowed actions, resources, and conditions that might enable lateral movement, data exfiltration, or further reconnaissance. It requires valid AWS credentials with iam:GetPolicyVersion permission. The output includes the policy's JSON document, which can be parsed to spot overly permissive statements, such as wildcard resource access (*). This technique is commonly used post-initial access to enumerate cloud permissions without triggering alerts, as it mimics legitimate administrative queries.

## Requirements

1. AWS CLI installed and configured with credentials that have iam:GetPolicyVersion permission.
2. Knowledge of the target policy's ARN and a specific version ID (obtainable via prior enumeration like listing policies).
3. Network access to AWS APIs (no direct target access needed, but credentials must be valid for the target account).

## Defense

- Implement least privilege principles by regularly auditing IAM policies with tools like AWS IAM Access Analyzer to detect overly broad permissions.
- Enable AWS CloudTrail logging for IAM API calls and monitor for unusual GetPolicyVersion requests, especially from unexpected IP ranges or roles.
- Use IAM policy conditions to restrict access to policy metadata based on source IP, MFA, or time of day.

## Objectives

1. Obtain the JSON document of a specific IAM policy version to analyze permissions.
2. Identify misconfigurations like wildcard actions or excessive resource access.
3. Support further attacks such as privilege escalation or targeted data exfiltration based on discovered permissions.

## Instructions

### Step 1: Retrieve the Policy Version Details

**Context**: Use the AWS CLI to query the specific version of the IAM policy. This step fetches the policy document, which includes statements defining allowed actions and resources. Ensure you have the policy ARN (e.g., from prior listing) and version ID (e.g., v1, v2). If the version ID is unknown, first list versions using a separate enumeration procedure.

**Command** ([[commands/aws-iam-get-policy-version]]):
```bash
aws iam get-policy-version --policy-arn $_POLICY_ARN --version-id $_VERSION_ID
```

> This command queries the AWS IAM service for the specified policy version. Replace $_POLICY_ARN with the full ARN (e.g., arn:aws:iam::123456789012:policy/MyPolicy) and $_VERSION_ID with the version (e.g., v1). The response includes the policy name, ARN, version details, and the full JSON policy document. Success is indicated by a 200 OK response with the document; errors like AccessDenied occur if permissions are insufficient. Review the JSON for statements like "Effect": "Allow" with broad "Resource": "*" to identify risks.
