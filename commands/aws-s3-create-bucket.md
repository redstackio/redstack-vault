---
data: 'aws s3 mb s3://gameday.websummit.net --region eu-west-1'
tags:
  - aws
  - s3
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: f94dad51-f6ae-445b-a40a-0c8f73bd75d4
created_at: '2025-12-14T05:32:24.273Z'
updated_at: '2025-12-14T05:32:24.273Z'
verified: false
validated: true
submitted: true
---
# aws-s3-create-bucket

## Command

```bash
aws s3 mb s3://gameday.websummit.net --region eu-west-1
```

## Description

Creates a new S3 bucket with a specified name and region using AWS CLI, essential for claiming dangling resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `mb` | Make bucket subcommand | Yes |
| `s3://gameday.websummit.net` | Bucket name (globally unique) | Yes |
| `--region eu-west-1` | AWS region for creation | Yes |

## Examples

### Basic Usage

```bash
aws s3 mb s3://gameday.websummit.net --region eu-west-1
```

### Advanced Usage

```bash
aws s3 mb s3://gameday.websummit.net --region eu-west-1 --no-verify-ssl
```

## Expected Output

"make_bucket: gameday.websummit.net"

## Related

- [[Related Procedure]]
