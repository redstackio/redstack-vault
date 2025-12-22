---
id: 2eeac9d9-26a8-4204-a8b8-a0f9882a2bee
name: aws-s3api-list-objects-in-bucket
type: command
executor: bash
data: aws s3api list-objects-v2 --bucket $_BUCKET_NAME
output: null
created_at: '2023-04-06T03:56:11.067516+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - cloud
  - enumeration
verified: true
validated: true
---

# aws-s3api-list-objects-in-bucket

## Command

```bash
aws s3api list-objects-v2 --bucket $_BUCKET_NAME
```

## Description

This command queries the AWS S3 API to list objects in a specified bucket, returning details like object keys, sizes, and modification dates. Use it during cloud reconnaissance to discover stored data when read permissions are available.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --bucket $_BUCKET_NAME | The name of the S3 bucket to list objects from (e.g., my-bucket) | Yes |
| -v2 | Use the ListObjectsV2 API version for improved pagination and metadata | No (default is v1, but v2 recommended) |
| --prefix $_PREFIX | Filter results to objects with the specified prefix (e.g., folder/) | No |
| --delimiter $_DELIMITER | Group objects by delimiter (e.g., / for folders) | No |
| --max-items $_MAX_ITEMS | Limit the number of returned objects (e.g., 1000) | No |

## Examples

### Basic Usage

```bash
aws s3api list-objects-v2 --bucket mycompany-data
```

### Advanced Usage

```bash
aws s3api list-objects-v2 --bucket mycompany-data --prefix sensitive/ --max-items 100
```

## Expected Output

Successful execution returns JSON output like:

```json
{
    "Contents": [
        {
            "Key": "file1.txt",
            "LastModified": "2023-01-01T12:00:00+00:00",
            "ETag": "\"abc123\"",
            "Size": 1024,
            "StorageClass": "STANDARD"
        }
    ],
    "Name": "mycompany-data",
    "Prefix": "",
    "MaxKeys": 1000,
    "Delimiter": "",
    "IsTruncated": false
}
```

If access is denied: `An error occurred (AccessDenied) when calling the ListObjectsV2 operation: Access Denied`.

## Related

- [[procedures/AWS-S3-Bucket-Object-Enumeration]]
- [[tools/AWS-CLI]]
