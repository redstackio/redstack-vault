---
id: bf39031c-8403-447f-b347-cbd89ea1f551
name: aws-s3-ls-recursive-no-sign
type: command
executor: bash
data: 'aws s3 ls s3://$_BUCKET_NAME --recursive --no-sign'
output: null
created_at: '2023-04-06T03:55:53.656154+00:00'
updated_at: '2023-04-06T03:55:53.663296+00:00'
platforms:
  - AWS
tags:
  - aws
  - s3
  - recon
verified: true
validated: true
---

# aws-s3-ls-recursive-no-sign

## Command

```bash
aws s3 ls s3://$_BUCKET_NAME --recursive --no-sign
```

## Description

This command uses the AWS CLI to recursively list all objects in a specified S3 bucket without requiring authentication credentials. It is intended for enumerating public buckets during reconnaissance to discover stored data without triggering signed API logs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BUCKET_NAME | The name of the target S3 bucket (e.g., my-public-bucket) | Yes |
| --recursive | Recursively list all objects and sub-prefixes | Yes |
| --no-sign | Disable request signing for anonymous access to public resources | Yes |

## Examples

### Basic Usage

```bash
aws s3 ls s3://example-bucket --recursive --no-sign
```

### Advanced Usage

```bash
aws s3 ls s3://example-bucket --recursive --no-sign --page-size 1000 > objects.txt
```

(Adds pagination limit and redirects output to file for large buckets.)

## Expected Output

A list of objects with timestamps, sizes, and names:

```
2023-04-01 10:30:15    2048 documents/report.pdf
2023-04-02 14:22:07   51200 images/logo.png
2023-04-03 09:15:42       0 folder/empty.txt
```

If access is denied:

`An error occurred (AccessDenied) when calling the ListObjectsV2 operation: Access Denied`

## Related

- [[procedures/Enumerate-S3-Bucket-Size]]
- [[commands/sum-s3-object-sizes]]
