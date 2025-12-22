---
id: 66cb512c-2707-4555-9813-008dbbb3d1d2
name: Describe-AWS-Secrets-Manager-Secret
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.308419+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - '[[sub-techniques/Credentials In Files|T1552.001 - Credentials In Files]]'
  - >-
    [[sub-techniques/Credentials in Registry|T1552.002 - Credentials in
    Registry]]
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Credential Exfiltration]]'
  - '[[tags/Listing information about a specific secret]]'
commands:
  - '[[commands/aws-secretsmanager-describe-secret]]'
tools:
  - '[[tools/AWS-CLI]]'
platforms:
  - AWS
validated: true
---

# Describe-AWS-Secrets-Manager-Secret

## Summary

This procedure uses the AWS CLI to retrieve metadata and details about a specific secret stored in AWS Secrets Manager, potentially exposing sensitive information such as usernames, passwords, API keys, or other credentials that can be used for further lateral movement or privilege escalation within the cloud environment.

## Description

In an attack scenario, an adversary with compromised AWS credentials may enumerate and describe secrets in Secrets Manager to harvest unsecured credentials. The DescribeSecret API call returns the secret's ARN, name, description, tags, creation date, and version information, but does not directly return the secret value (which requires a separate GetSecretValue call). However, this metadata can reveal valuable insights into the environment, such as secret purposes or associated resources. This technique targets misconfigured IAM policies granting excessive DescribeSecret permissions. It applies to AWS environments where Secrets Manager is used for credential storage, and success depends on the attacker's ability to authenticate via AWS CLI with appropriate permissions.

## Requirements

1. AWS CLI installed and configured with valid credentials (e.g., access key ID and secret access key) that have at least `secretsmanager:DescribeSecret` permission on the target secret.
2. Network access to AWS endpoints (no VPC endpoints required unless restricted).
3. Knowledge of the target secret's name or ARN.
4. [[tools/AWS-CLI]] tool available on the attacker's system.

## Defense

Defensive measures and detection strategies:

- Implement least-privilege IAM policies to restrict DescribeSecret actions to only necessary roles and users.
- Enable AWS CloudTrail logging for Secrets Manager API calls and monitor for anomalous DescribeSecret requests, such as from unexpected IP addresses or high-volume queries.
- Use AWS Config rules to audit Secrets Manager permissions and alert on overly permissive policies.
- Rotate credentials regularly and avoid storing sensitive data in secrets without encryption or rotation policies.

## Objectives

1. Retrieve metadata about a specific secret, including ARN, description, tags, and version details.
2. Identify potential sensitive information locations for follow-on retrieval (e.g., via GetSecretValue).
3. Gain insights into the target's credential management practices to facilitate broader environment compromise.

## Instructions

### Step 1: Configure AWS CLI Authentication

**Context**: Before querying Secrets Manager, ensure the AWS CLI is authenticated with credentials that have the necessary permissions. This step sets up the environment to avoid authentication errors during the describe operation.

If not already configured, run `aws configure` to set your access key, secret key, region, and output format. Verify permissions by testing a basic AWS command like `aws sts get-caller-identity`.

**Expected Output**: JSON response showing the caller's ARN and account details, confirming successful authentication.

### Step 2: Describe the Target Secret

**Context**: Use the AWS CLI to send a DescribeSecret request, specifying the secret ID to retrieve its metadata. This reveals non-sensitive details that can guide further attacks without directly exposing the secret value.

**Command** ([[commands/aws-secretsmanager-describe-secret]]):
```bash
aws secretsmanager describe-secret --secret-id $_SECRET_ID
```

> This command queries the Secrets Manager API for the specified secret. Replace $_SECRET_ID with the name or ARN of the target secret (e.g., "my-app/db-password"). The response includes fields like ARN, Name, Description, CreatedDate, and StagingLabels, but not the actual secret value. If the secret does not exist or permissions are insufficient, it will error with AccessDenied or ResourceNotFoundException.

**Expected Output**: A JSON object with secret metadata, for example:
```json
{
  "ARN": "arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret-abc123",
  "Name": "mysecret",
  "Description": "Database credentials",
  "CreatedDate": "2023-01-01T12:00:00+00:00",
  "StagingLabels": [
    {
      "LastAccessedDate": "2023-09-01T10:00:00+00:00",
      "Label": "AWSCURRENT"
    }
  ],
  "Tags": []
}
```

### Step 3: Parse and Validate Output

**Context**: Review the output for key indicators of success and actionable information. This step ensures the metadata is useful and identifies any errors for troubleshooting.

Use `jq` or manual inspection to extract fields like Description or Tags, which may hint at the secret's purpose (e.g., "API key for S3 bucket"). If the response lacks expected fields or shows errors, check IAM permissions or secret existence.

**Command** (using jq for parsing):
```bash
aws secretsmanager describe-secret --secret-id $_SECRET_ID | jq '.Description'
```

**Expected Output**: Extracted description string, e.g., "Database credentials", confirming the secret's role.

**Success Indicators**:
- JSON response contains ARN and Name matching the input.
- No AccessDeniedException in the output.
- Description or tags provide context for the secret's contents.
