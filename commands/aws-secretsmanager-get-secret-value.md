---
id: 1d62cccb-1679-4e14-ab24-9e533bb93c35
name: aws-secretsmanager-get-secret-value
type: command
executor: bash
data: >-
  aws secretsmanager get-secret-value --secret-id $_SECRET_ID --version-stage
  $_VERSION_STAGE --version-id $_VERSION_ID
output: null
created_at: '2023-04-06T03:56:12.351851+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - cloud
  - aws
  - exfiltration
  - secrets
verified: true
validated: true
---

# aws-secretsmanager-get-secret-value

## Command

```bash
aws secretsmanager get-secret-value --secret-id $_SECRET_ID --version-stage $_VERSION_STAGE --version-id $_VERSION_ID
```

## Description

This command retrieves the encrypted secret value from AWS Secrets Manager for a specified secret ID. It decrypts and returns the secret in plaintext (SecretString) or binary (SecretBinary) format, enabling exfiltration of credentials or keys.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --secret-id $_SECRET_ID | The ARN or name of the secret to retrieve (e.g., "mySecret" or "arn:aws:secretsmanager:us-east-1:123456789012:secret:mySecret-abc123") | Yes |
| --version-stage $_VERSION_STAGE | The secret version stage (e.g., "AWSCURRENT", "AWSPENDING"). Defaults to AWSCURRENT | No |
| --version-id $_VERSION_ID | Specific version ID of the secret (overrides stage) | No |

## Examples

### Basic Usage

```bash
aws secretsmanager get-secret-value --secret-id mySecret
```

### Retrieve Specific Version

```bash
aws secretsmanager get-secret-value --secret-id mySecret --version-stage AWSPENDING
```

## Expected Output

```
{
    "ARN": "arn:aws:secretsmanager:us-east-1:123456789012:secret:mySecret-abc123",
    "Name": "mySecret",
    "VersionId": "EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE",
    "SecretString": "{"username":"admin","password":"supersecret"}",
    "VersionStages": ["AWSCURRENT"],
    "CreatedDate": "2023-04-06T03:56:12.356352+00:00"
}
```
Success shows the SecretString with the decrypted value. Use `jq` to extract: `| jq -r '.SecretString'`. Errors include AccessDeniedException if permissions are insufficient.

## Related

- [[procedures/AWS-Secrets-Manager-Credential-Exfiltration]]
- [[commands/aws-sts-get-caller-identity]]
