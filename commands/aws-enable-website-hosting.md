---
data: >-
  aws s3 website s3://storybook.lystit.com --index-document index.html
  --error-document error.html
tags:
  - aws
  - s3
  - hosting
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:01.892Z'
id: 117c4620-38af-4cc0-8a2a-67b1ae42c0d8
verified: false
validated: true
submitted: true
---
# aws-enable-website-hosting

## Command

```bash
aws s3 website s3://storybook.lystit.com --index-document index.html --error-document error.html
```

## Description

Enables static website hosting on an S3 bucket.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `s3://bucket` | Bucket URI | Yes |
| `--index-document` | Default index file | Yes |
| `--error-document` | Error page | Yes |

## Examples

### Basic Usage

```bash
aws s3 website s3://storybook.lystit.com --index-document index.html
```

### Advanced Usage

```bash
aws s3 website s3://storybook.lystit.com --index-document index.html --error-document error.html
```

## Expected Output

Website configuration details.

## Related

- [[Related Procedure: Enable Static Website Hosting on S3 Bucket]]
