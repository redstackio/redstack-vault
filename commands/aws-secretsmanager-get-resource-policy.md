---
id: f001a12e-aee6-49d2-91ec-448db9c9dd84
name: aws-secretsmanager-get-resource-policy
type: command
executor: bash
data: aws secretsmanager get-resource-policy --secret-id $_SECRET_ID
output: null
created_at: '2023-04-06T03:56:12.327799+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - cloud-aws
  - secrets-manager
verified: true
validated: true
---

# AWS Secrets Manager Get Resource Policy

## Command

```bash
aws secretsmanager get-resource-policy --secret-id $_SECRET_ID
```

## Description

This command retrieves the resource-based IAM policy attached to a specific secret in AWS Secrets Manager. It is used to inspect access controls on the secret, which can reveal permitted principals and actions for exfiltration or abuse in credential access scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --secret-id $_SECRET_ID | The ARN or name of the secret to retrieve the policy for (e.g., arn:aws:secretsmanager:us-east-1:123456789012:secret:my-secret-AbCdEf or my-secret) | Yes |

## Examples

### Basic Usage

```bash
aws secretsmanager get-resource-policy --secret-id my-app-secret
```

### Advanced Usage

```bash
aws secretsmanager get-resource-policy --secret-id arn:aws:secretsmanager:us-east-1:123456789012:secret:prod-db-credentials-XYZ --output json
```

## Expected Output

Successful execution returns a JSON response like:

```json
{
    "ARN": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-secret-AbCdEf",
    "Name": "my-secret",
    "ResourcePolicy": "{\n    \"Version\": \"2012-10-17\",\n    \"Statement\": [\n        {\n            \"Effect\": \"Allow\",\n            \"Principal\": {\n                \"AWS\": \"arn:aws:iam::123456789012:root\"\n            },\n            \"Action\": [\n                \"secretsmanager:GetSecretValue\"\n            ],\n            \"Resource\": \"*\"\n        }\n    ]\n}"
}
```

If no policy is attached, the ResourcePolicy field is an empty string or null. Errors occur if permissions are insufficient (e.g., AccessDeniedException).

## Related

- [[commands/aws-secretsmanager-list-secrets]]
- [[procedures/aws-secretsmanager-resource-based-policy-exfiltration]]
