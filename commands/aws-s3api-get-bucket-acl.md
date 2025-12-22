---
id: 1cbf869d-8b20-4d96-bbeb-8ea7e713fdb9
name: aws-s3api-get-bucket-acl
type: command
executor: bash
data: aws s3api get-bucket-acl --bucket $_BUCKET_NAME
output: null
created_at: '2023-04-06T03:56:10.995753+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - cloud
  - enumeration
verified: true
validated: true
---

# aws-s3api-get-bucket-acl

## Command

```bash
aws s3api get-bucket-acl --bucket $_BUCKET_NAME
```

## Description

This command retrieves the Access Control List (ACL) for the specified S3 bucket via the AWS CLI's S3 API. It is used during cloud discovery to enumerate permissions and identify potential misconfigurations. Requires AWS credentials with 's3:GetBucketAcl' permission.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --bucket $_BUCKET_NAME | The name of the S3 bucket to query (e.g., 'example-bucket') | Yes |

## Examples

### Basic Usage

```bash
aws s3api get-bucket-acl --bucket my-bucket
```

### Advanced Usage (with JSON formatting)

```bash
aws s3api get-bucket-acl --bucket my-bucket --output json | jq '.'
```

## Expected Output

Successful execution returns a JSON object detailing the ACL:

```json
{
    "Owner": {
        "DisplayName": "bucket-owner",
        "ID": "example-id"
    },
    "Grants": [
        {
            "Grantee": {
                "Type": "CanonicalUser",
                "DisplayName": "grantee-name",
                "ID": "grantee-id"
            },
            "Permission": "FULL_CONTROL"
        }
    ]
}
```

Look for 'Grants' array to see permissions like READ, WRITE, or FULL_CONTROL assigned to users, groups, or public.

## Related

- [[procedures/AWS-S3-Bucket-ACL-Enumeration]]
- [[tools/AWS-CLI]]
