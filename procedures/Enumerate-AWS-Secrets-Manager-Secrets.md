---
id: 74916d14-b703-440b-a551-ee716a2350b6
name: Enumerate-AWS-Secrets-Manager-Secrets
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.081307+00:00'
updated_at: '2023-04-10T20:20:52.309272+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Cloud Service Discovery]]'
sub_techniques: []
tags:
  - cloud-aws
  - enumeration
  - aws-secrets-manager
commands:
  - '[[commands/aws-secretsmanager-list-secrets]]'
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
tools: []
validated: true
---

# Enumerate-AWS-Secrets-Manager-Secrets

## Summary

This procedure uses the AWS CLI to enumerate all secrets stored in AWS Secrets Manager, revealing sensitive information such as database credentials, API keys, and other confidential data that can aid in further compromise of the AWS environment.

## Description

AWS Secrets Manager is a service for securely storing and retrieving secrets like passwords and tokens. An attacker with compromised AWS credentials possessing the `secretsmanager:ListSecrets` permission can query the API to list all secrets in the account. This discovery technique helps identify valuable assets for lateral movement, privilege escalation, or data exfiltration. The procedure assumes the attacker has obtained initial access to AWS credentials via prior techniques like credential dumping or misconfiguration exploitation. Success provides a list of secret ARNs and names, which can then be retrieved individually if permissions allow.

## Requirements

1. Valid AWS credentials configured in the environment (e.g., via `aws configure`) with at least `secretsmanager:ListSecrets` permission.
2. AWS CLI version 2 installed and accessible in the PATH.
3. Network connectivity to AWS API endpoints (no VPC endpoints required for public access).
4. Optional: Specified AWS region if targeting a non-default region.

## Defense

- Implement least privilege access: Restrict `secretsmanager:ListSecrets` to only necessary roles and monitor usage via IAM policies.
- Enable AWS CloudTrail for API logging: Track `ListSecrets` calls and alert on anomalous access patterns, such as from unusual IPs or high-volume queries.
- Use resource-based policies on Secrets Manager to deny listing from untrusted principals.
- Regularly audit and rotate secrets, and integrate with AWS GuardDuty for behavioral anomaly detection.

## Objectives

1. Retrieve a complete list of all secrets stored in the target AWS account's Secrets Manager.
2. Identify high-value secrets (e.g., database creds, service tokens) for subsequent retrieval and exploitation.
3. Map the secret inventory to potential attack paths, such as accessing linked resources like RDS databases or S3 buckets.

## Instructions

### Step 1: Configure AWS CLI and List Secrets

**Context**: Ensure AWS credentials are set up, then execute the list command to query Secrets Manager. This step assumes default region; adjust if needed for multi-region environments. The output is JSON, which can be piped to `jq` for parsing if available.

**Command** ([[commands/aws-secretsmanager-list-secrets]]):
```bash
aws secretsmanager list-secrets
```

> This command queries the AWS Secrets Manager API and returns a JSON array of secrets. If the account has no secrets, an empty list is returned. Review the `Name` and `ARN` fields to identify targets; descriptions may hint at contents (e.g., "prod-db-password"). If permissions are insufficient, an `AccessDeniedException` error occurs—indicating a need for privilege escalation.

**Expected Output**:
```json
{
    "SecretList": [
        {
            "ARN": "arn:aws:secretsmanager:us-east-1:123456789012:secret:prod-db-creds-ABC123",
            "Name": "prod-db-creds",
            "Description": "Database credentials for production RDS instance",
            "CreatedDate": "2023-01-15T10:30:00Z",
            "LastChangedDate": "2023-04-01T14:20:00Z",
            "LastAccessedDate": null,
            "DeletedDate": null,
            "KmsKeyId": null,
            "RotationEnabled": false,
            "RotationLambdaARN": null,
            "RotationRules": null,
            "Tags": []
        }
    ],
    "NextToken": null
}
```

**Success Indicators**:
- JSON response contains `SecretList` array with one or more entries.
- No `AccessDenied` or `InvalidParameter` errors in the output.
- Secret names or descriptions reveal sensitive resources (e.g., containing "key", "password", or service names).
