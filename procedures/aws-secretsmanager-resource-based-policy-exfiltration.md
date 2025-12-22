---
id: b96dd824-adba-416d-a697-4820a5f1c209
name: aws-secretsmanager-resource-based-policy-exfiltration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.331643+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Credential Exfiltration]]'
  - '[[tags/Getting resource-based policy attached to an specific secret]]'
commands:
  - '[[commands/aws-secretsmanager-get-resource-policy]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS Secrets Manager Resource-Based Policy Exfiltration

## Summary

This procedure demonstrates how to retrieve and exfiltrate the resource-based policy attached to a specific secret in AWS Secrets Manager using the AWS CLI. The policy defines access permissions to the secret, potentially revealing sensitive IAM roles, users, or conditions that can be abused for further credential access or lateral movement within the AWS environment.

## Description

AWS Secrets Manager stores sensitive data such as database credentials, API keys, and configuration secrets. Resource-based policies attached to these secrets control who can access them and what actions they can perform, similar to IAM policies but scoped to the secret itself. An attacker with read access to the policy (via appropriate permissions like secretsmanager:GetResourcePolicy) can use the AWS CLI or API to fetch this policy, exposing details about allowed principals and actions. This information can be used to identify weak access controls, impersonate allowed entities, or chain to other attacks like assuming roles for privilege escalation. The procedure assumes the attacker has AWS credentials with the necessary permissions and focuses on the exfiltration step, which is useful in post-compromise scenarios for mapping access to secrets.

## Requirements

1. Configured AWS CLI with credentials that have secretsmanager:GetResourcePolicy permission on the target secret.
2. Knowledge of the secret's ARN or name (SecretId).
3. Access to a system where AWS CLI is installed (e.g., Linux, macOS, or Windows with AWS CLI).
4. Network connectivity to AWS endpoints (no VPC restrictions blocking CLI access).

## Defense

- Restrict secretsmanager:GetResourcePolicy permissions to only necessary IAM roles and monitor usage via AWS CloudTrail.
- Enable AWS Config rules to alert on overly permissive resource-based policies attached to secrets.
- Use AWS Secrets Manager's rotation and least-privilege principles to minimize exposed access details.
- Regularly audit policies with tools like Prowler or Scout Suite for misconfigurations.

## Objectives

1. Retrieve the resource-based policy attached to a specific AWS Secrets Manager secret.
2. Exfiltrate policy details containing access permissions and principals.
3. Identify opportunities for further access to secrets or related AWS resources.

## Instructions

### Step 1: Identify the Target Secret

**Context**: Before retrieving the policy, determine the SecretId (ARN or name) of the target secret. This can be done via AWS console enumeration or listing secrets with appropriate permissions.

Use the AWS CLI to list secrets if you have secretsmanager:ListSecrets permission:

**Command** ([[commands/aws-secretsmanager-list-secrets]]):
```bash
aws secretsmanager list-secrets --max-results 10
```

> This command outputs a list of secrets with ARNs and names. Select the target SecretId from the response. Expected output includes JSON with SecretList array containing secret metadata.

### Step 2: Retrieve the Resource-Based Policy

**Context**: Execute the get-resource-policy command to fetch the policy. This step exfiltrates the JSON policy document, which may contain sensitive access rules.

**Command** ([[commands/aws-secretsmanager-get-resource-policy]]):
```bash
aws secretsmanager get-resource-policy --secret-id $_SECRET_ID
```

> Replace $_SECRET_ID with the actual secret ARN or name (e.g., my-secret). The command queries the Secrets Manager API and returns the policy in JSON format, including Version, Statement array with Effect, Principal, Action, and Condition details. If no policy is attached, it returns an empty or null response. Verify success by checking for a non-empty Arn and the policy document.
