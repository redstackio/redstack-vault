---
id: 363c2716-0a46-437a-a2f9-844b2551eed7
name: AWS-Secrets-Manager-Credential-Exfiltration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.356352+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
  - '[[techniques/Cloud Services|T1552.005 - Cloud Services]]'
  - >-
    [[techniques/Data from Cloud Storage Objects|T1530 - Data from Cloud Storage
    Objects]]
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Credential Exfiltration]]'
  - '[[tags/Getting the secret value]]'
commands:
  - '[[commands/aws-secretsmanager-get-secret-value]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# AWS-Secrets-Manager-Credential-Exfiltration

## Summary

This procedure demonstrates how an attacker with compromised AWS credentials can exfiltrate sensitive information, such as database credentials or API keys, stored in AWS Secrets Manager using the AWS CLI. It targets the retrieval of secret values, which can then be used for lateral movement or further compromise within the cloud environment.

## Description

AWS Secrets Manager is a service designed to store, manage, and retrieve secrets like passwords, API keys, and certificates securely. However, if an attacker gains access to an AWS account with read permissions on Secrets Manager (e.g., via stolen IAM credentials), they can enumerate and retrieve secret values directly. This procedure focuses on using the AWS CLI to call the GetSecretValue API, which returns the secret in plaintext (SecretString) or binary format. The attack assumes the attacker has configured AWS CLI with valid credentials and knows the secret ID (ARN or name). Once retrieved, the secret can enable access to databases, other services, or be exfiltrated further. This is particularly dangerous in multi-tenant environments or where least-privilege is not enforced, leading to potential data breaches or privilege escalation.

## Requirements

1. Valid AWS credentials with `secretsmanager:GetSecretValue` permission (e.g., compromised IAM user/role keys).
2. AWS CLI installed and configured with the target account's access key ID and secret access key (via `aws configure`).
3. Knowledge of the secret ID (e.g., from enumeration via `aws secretsmanager list-secrets` or prior reconnaissance).
4. Network access to AWS endpoints (no VPC endpoints required unless restricted).

## Defense

- Implement least-privilege IAM policies: Restrict `GetSecretValue` to only necessary roles and monitor usage with AWS CloudTrail.
- Enable AWS Secrets Manager rotation and versioning to limit exposure of static secrets.
- Use AWS GuardDuty or CloudTrail alerts for anomalous API calls to Secrets Manager from unusual IPs or roles.
- Encrypt secrets at rest (enabled by default) and monitor for exfiltration patterns, such as large data transfers post-retrieval.

## Objectives

1. Retrieve plaintext secret values from AWS Secrets Manager.
2. Exfiltrate credentials for use in further attacks (e.g., database access).
3. Validate success by parsing the returned secret data.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is authenticated with credentials that have access to the target secret. This step confirms the session before attempting retrieval, preventing permission errors.

Run `aws sts get-caller-identity` to verify the assumed role or user.

**Command** ([[commands/aws-sts-get-caller-identity]]):
```bash
aws sts get-caller-identity
```

> This command outputs the current AWS identity. If it returns the expected account/user without errors, proceed. If not, reconfigure credentials using `aws configure` with the access key, secret key, and region.

### Step 2: Retrieve the Secret Value

**Context**: Use the GetSecretValue API to fetch the secret. Replace the secret ID with the target (ARN or name). This step directly exfiltrates the data, which can be piped to a file or further processed.

**Command** ([[commands/aws-secretsmanager-get-secret-value]]):
```bash
aws secretsmanager get-secret-value --secret-id mySecret
```

> The command returns a JSON response with the SecretString field containing the plaintext secret. Success is indicated by HTTP 200 and the presence of SecretString. Pipe to `jq` for parsing if needed: `aws secretsmanager get-secret-value --secret-id mySecret | jq '.SecretString'`. If the secret is binary, use SecretBinary instead.
