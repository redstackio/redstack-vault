---
id: 156b1cbc-8748-4a82-a29b-67b3ce2f24cf
name: aws-s3api-get-object-acl
type: command
executor: bash
data: aws s3api get-object-acl --bucket $_BUCKET_NAME --key $_OBJECT_KEY
output: null
created_at: '2023-04-06T03:56:11.089610+00:00'
updated_at: '2023-04-10T20:20:21.145437+00:00'
platforms:
  - AWS
tags:
  - cloud
  - enumeration
  - aws-cli
verified: true
validated: true
---

# aws-s3api-get-object-acl

## Command

```bash
aws s3api get-object-acl --bucket $_BUCKET_NAME --key $_OBJECT_KEY
```

## Description

This command retrieves the Access Control List (ACL) for a specific object in an S3 bucket using the AWS CLI's low-level s3api interface. It is used during cloud reconnaissance to enumerate permissions without downloading the object itself.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --bucket | The name of the S3 bucket containing the object (use $_BUCKET_NAME as placeholder) | Yes |
| --key | The key (path/filename) of the object within the bucket (use $_OBJECT_KEY as placeholder) | Yes |

## Examples

### Basic Usage

```bash
aws s3api get-object-acl --bucket my-sensitive-bucket --key confidential/file.txt
```

### Advanced Usage

```bash
aws s3api get-object-acl --bucket my-sensitive-bucket --key confidential/file.txt --profile attacker-profile
```

## Expected Output

Successful execution returns JSON with the object's owner and grants:

```json
{
    "Owner": {
        "ID": "canonical-user-id",
        "DisplayName": "owner-display-name"
    },
    "Grants": [
        {
            "Grantee": {
                "Type": "CanonicalUser",
                "ID": "grantee-id",
                "DisplayName": "grantee-name"
            },
            "Permission": "FULL_CONTROL"
        }
    ]
}
```

Look for grants with broad permissions like FULL_CONTROL to identify risks. Errors include AccessDenied if permissions are insufficient.

## Related

- [[Related Procedure]]: [[procedures/aws-s3-object-acl-enumeration]]
