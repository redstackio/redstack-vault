---
type: procedure
verified: true
submitted: false
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques:
  - '[[sub-techniques/Cloud Account|T1087.004 - Cloud Account]]'
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/AWS Secrets Manager]]'
commands:
  - '[[commands/aws-secretsmanager-describe-secret]]'
tools:
  - '[[tools/aws-cli]]'
platforms:
  - AWS
validated: true
---

# AWS Secrets Manager Enumeration

## Summary

This procedure enumerates metadata about a specific secret stored in AWS Secrets Manager using the AWS CLI. It allows an attacker with sufficient permissions to discover details such as the secret's ARN, name, description, associated KMS key, and rotation status, which can reveal sensitive information like database credentials or API keys without retrieving the secret value itself.

## Description

AWS Secrets Manager is a service for securely storing and managing secrets such as database credentials, API keys, and other sensitive data. In an attack scenario, an adversary who has compromised AWS credentials (e.g., via IAM role assumption or stolen access keys) can use this procedure to perform reconnaissance on secrets. By describing a secret, the attacker gains insights into the environment's secret management practices, identifies valuable targets for further exploitation (e.g., retrieving the actual secret value with additional permissions), and maps out resource dependencies. This is particularly useful in cloud persistence or lateral movement phases, where understanding secret storage helps in credential access. The procedure assumes the attacker has at least 'secretsmanager:DescribeSecret' permission and focuses on a single secret by its ID (name or ARN). It does not retrieve the secret value but provides metadata that can guide subsequent actions like secret retrieval or rotation disruption.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with 'secretsmanager:DescribeSecret' permission on the target secret.
2. AWS CLI installed and configured with the appropriate profile or default credentials.
3. Knowledge of the target secret's ID (name or ARN), obtained via prior enumeration (e.g., listing secrets with 'aws secretsmanager list-secrets').
4. Network access to AWS endpoints (no VPC-specific restrictions assumed).

## Defense

- Implement least-privilege IAM policies to restrict 'secretsmanager:DescribeSecret' access only to necessary roles and monitor usage via AWS CloudTrail.
- Enable AWS Config rules to detect overly permissive IAM policies on Secrets Manager resources.
- Use AWS CloudTrail and Amazon GuardDuty to log and alert on unusual DescribeSecret API calls, especially from unexpected IP addresses or roles.
- Rotate secrets regularly and enable automatic rotation to limit exposure windows.

## Objectives

1. Retrieve metadata about a specific secret to identify its purpose and dependencies.
2. Verify secret existence and configuration for reconnaissance.
3. Prepare for advanced actions like secret value retrieval or privilege escalation using discovered information.

## Instructions

### Step 1: Configure AWS CLI and Identify Secret

**Context**: Ensure AWS CLI is set up with credentials that have the required permissions. Obtain the secret ID through prior discovery (e.g., via 'list-secrets' if permissions allow). This step verifies access and prepares for description.

Replace placeholders with actual values: use your AWS profile if not default, and specify the secret ID.

**Command** ([[commands/aws-secretsmanager-describe-secret]]):
```bash
aws secretsmanager describe-secret --secret-id my-secret-name --profile my-aws-profile
```

This command queries AWS Secrets Manager for metadata on the specified secret. It returns a JSON response with details like ARN, name, description, KMSKeyId, rotation rules, and tags. If successful, it confirms the secret's existence and provides context for its use (e.g., if it's a database credential). Errors like 'AccessDeniedException' indicate insufficient permissions; 'ResourceNotFoundException' means the secret ID is invalid.

### Step 2: Parse and Analyze Output

**Context**: Review the JSON output to extract key metadata. This helps in understanding the secret's role in the environment and planning next steps, such as attempting to retrieve the value with 'get-secret-value' if permissions allow.

Use jq (if available) to filter output for readability:

**Command** ([[commands/aws-secretsmanager-describe-secret-with-jq]]):
```bash
aws secretsmanager describe-secret --secret-id my-secret-name | jq '.Name, .Description, .KMSKeyId'
```

Expected output includes filtered fields like the secret name, description (e.g., "Database password for prod DB"), and KMS key ARN. Cross-reference the KMS key to assess encryption strength or shared access.
