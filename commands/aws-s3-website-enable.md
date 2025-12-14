---
id: uuid-c3
data: 'aws s3 website s3://delivery.yelp.com --index-document index.html'
tags:
  - aws-cli
  - s3
type: command
output: Website endpoint configured
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.105Z'
verified: false
validated: true
submitted: true
---
# aws-s3-website-enable

## Command

```bash
aws s3 website s3://delivery.yelp.com --index-document index.html
```

## Description

Enables static website hosting on an S3 bucket, specifying the index document for default page serving.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://bucket` | Bucket URI | Yes |
| `--index-document` | Default file (e.g., index.html) | Yes |

## Examples

### Basic Usage

```bash
aws s3 website s3://mybucket --index-document index.html
```

### Advanced Usage

```bash
aws s3 website s3://mybucket --index-document index.html --error-document error.html
```

## Expected Output

Configuration details including the website endpoint URL.

## Related

- [[Related Procedure: Enable-Static-Website-Hosting-on-S3]]
