---
id: a0769209-fd4b-488f-b8e1-0890af854776
name: curl-retrieve-ec2-user-data-imdsv1
type: command
executor: bash
data: 'curl http://169.254.169.254/latest/user-data/'
output: null
created_at: '2023-04-06T03:56:38.514610+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
  - Linux
tags:
  - cloud-metadata
  - aws-imds
verified: true
validated: true
---

# curl-retrieve-ec2-user-data-imdsv1

## Command

```bash
curl http://169.254.169.254/latest/user-data/
```

## Description

This command queries the AWS Instance Metadata Service (IMDSv1) to retrieve user data passed to the EC2 instance at launch. Use it on instances not enforcing IMDSv2 for quick access to bootstrapping scripts or secrets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| http://169.254.169.254/latest/user-data/ | Fixed IMDS endpoint for user data | Yes |

## Examples

### Basic Usage

```bash
curl http://169.254.169.254/latest/user-data/
```

### With Silent Output

```bash
curl -s http://169.254.169.254/latest/user-data/
```

## Expected Output

Raw user data as text or base64 (e.g., #!/bin/bash
aws s3 cp s3://bucket/config.txt /etc/ or MIME-multi-part content). Empty response if no user data set; 404 if endpoint invalid.

## Related

- [[procedures/Retrieve-AWS-EC2-User-Data-via-Instance-Metadata-Service]]
- [[commands/curl-retrieve-ec2-user-data-imdsv2]]
