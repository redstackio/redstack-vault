---
id: 29165db5-f238-4366-9a52-38a3056b952f
name: AWS-Secrets-Manager-Resource-Policy-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.128097+00:00'
updated_at: '2023-04-10T20:20:02.326393+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Secrets Manager]]'
commands:
  - '[[commands/aws-secretsmanager-get-resource-policy]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS-Secrets-Manager-Resource-Policy-Enumeration

## Summary

This procedure retrieves the resource-based policy attached to a specific AWS Secrets Manager secret, allowing an attacker to analyze access controls and identify misconfigurations that could enable unauthorized access to sensitive data stored in the secret.

## Description

In an AWS environment, Secrets Manager stores sensitive information like database credentials or API keys, protected by resource-based policies that define permissions for principals to perform actions on the secret. This procedure uses the AWS CLI to query the Secrets Manager API and fetch the JSON policy document for a given secret ID. By examining the policy, an attacker can discover overly permissive statements, such as broad IAM role allowances or missing deny rules, which might allow escalation or lateral movement. This is particularly useful in cloud discovery phases where understanding access boundaries is key to mapping the attack surface. The procedure assumes the attacker has obtained valid AWS credentials with at least `secretsmanager:GetResourcePolicy` permissions, often through prior compromise of an IAM user or role.

## Requirements

1. Valid AWS credentials configured in the environment (e.g., via AWS CLI profile) with `secretsmanager:GetResourcePolicy` permission on the target secret.
2. AWS CLI installed and accessible (version 2 recommended for full feature support).
3. Knowledge of the target secret's ARN or name (Secret ID).
4. Network access to AWS endpoints (no VPC endpoints required unless restricted).

## Defense

- Implement least privilege by scoping IAM policies to specific secrets and actions, avoiding wildcard principals.
- Enable AWS CloudTrail logging for Secrets Manager API calls to detect unauthorized policy retrievals.
- Use AWS Config rules to monitor for overly permissive resource policies and alert on changes.
- Regularly audit secrets with tools like AWS IAM Access Analyzer to identify external access risks.

## Objectives

1. Retrieve the JSON resource policy for a specified AWS Secrets Manager secret.
2. Analyze the policy for misconfigurations, such as excessive permissions or unintended principal access.
3. Gain insights into access controls to inform further exploitation, like credential theft or privilege escalation.

## Instructions

### Step 1: Identify the Target Secret ID

**Context**: Before retrieving the policy, confirm the secret's ID (ARN or name) through prior enumeration, such as listing secrets with `aws secretsmanager list-secrets`. This ensures you're targeting the correct resource.

Replace `my-secret-id` with the actual secret name or ARN obtained from discovery.

### Step 2: Retrieve the Resource Policy

**Context**: Execute the AWS CLI command to fetch the policy. This step queries the Secrets Manager service and returns the policy document if one exists, or an empty response if none is attached. Review the output for statements allowing actions like `secretsmanager:GetSecretValue` from unexpected sources.

**Command** ([[commands/aws-secretsmanager-get-resource-policy]]):
```bash
aws secretsmanager get-resource-policy --secret-id my-secret-id
```

> This command outputs a JSON response with the `ARN`, `Name`, and `ResourcePolicy` fields. The `ResourcePolicy` is a string containing the IAM policy JSON. If no policy exists, it returns an empty `ResourcePolicy` field. Errors like `AccessDeniedException` indicate insufficient permissions.

### Step 3: Analyze the Policy Output

**Context**: Parse the returned JSON to evaluate permissions. Look for `Allow` statements with broad `Principal` (e.g., `*` or external accounts) or actions (e.g., `secretsmanager:*`). Use tools like `jq` for filtering if needed.

Example analysis command (optional, for parsing):
```bash
aws secretsmanager get-resource-policy --secret-id my-secret-id | jq '.ResourcePolicy'
```

> Success is indicated by a valid JSON policy document. Misconfigurations might include statements like `"Principal": {"AWS": "*"}` granting global access.
