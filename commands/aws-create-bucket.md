---
id: cmd-uuid-aws-create-bucket
data: >-
  aws s3api create-bucket --bucket dangling-subdomain.mozaws.net --region
  us-east-1
tags:
  - aws
  - cloud
type: command
output: '{"Location":"/dangling-subdomain.mozaws.net"}'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.443Z'
verified: false
validated: true
submitted: true
---
# aws-create-bucket

## Command

```bash
aws s3api create-bucket --bucket dangling-subdomain.mozaws.net --region us-east-1
```

## Description

Creates an S3 bucket to claim a dangling resource for subdomain takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--bucket` | Name of the bucket to create | Yes |
| `--region` | AWS region | Yes |

## Examples

### Basic Usage

```bash
aws s3api create-bucket --bucket dangling-subdomain.mozaws.net --region us-east-1
```

### Advanced Usage

```bash
aws s3api create-bucket --bucket dangling-subdomain.mozaws.net --region us-east-1 --create-bucket-configuration LocationConstraint=us-west-2
```

## Expected Output

JSON response confirming bucket creation, e.g., '{"Location":"/dangling-subdomain.mozaws.net"}'.

## Related

- [[procedures/Register-Dangling-Cloud-Resource]]
