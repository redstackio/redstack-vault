---
data: 'curl -s https://███████.travelproducts.jetblue.com/'
tags:
  - recon
  - aws
type: command
executor: bash
platforms:
  - Linux
  - AWS
id: c7aee062-70f0-42c6-a300-63ab67e6083f
created_at: '2025-12-14T17:25:13.444Z'
updated_at: '2025-12-14T17:25:13.444Z'
verified: false
validated: true
submitted: true
---
# curl-list-s3-bucket

## Command

```bash
curl -s https://███████.travelproducts.jetblue.com/
```

## Description

Lists contents of a public S3 bucket.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | Yes |
| URL | Bucket root | Yes |

## Examples

### Basic Usage

```bash
curl -s https://███████.travelproducts.jetblue.com/
```

### Advanced Usage

```bash
curl -s https://███████.travelproducts.jetblue.com/ | grep '<Key>'
```

## Expected Output

XML listing bucket keys.

## Related

- [[Related Procedure: List-Contents-of-Public-AWS-S3-Bucket]]
