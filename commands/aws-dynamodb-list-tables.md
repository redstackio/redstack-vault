---
id: e508e9ff-ef21-4759-8b9d-c0df860088e3
name: aws-dynamodb-list-tables
type: command
executor: bash
data: aws --endpoint-url $_ENDPOINT_URL dynamodb list-tables
output: null
created_at: '2023-04-06T03:56:09.810371+00:00'
updated_at: '2023-04-10T20:20:03.428570+00:00'
platforms:
  - AWS
tags:
  - cloud
  - discovery
  - aws-cli
verified: true
validated: true
---

# aws-dynamodb-list-tables

## Command

```bash
aws --endpoint-url $_ENDPOINT_URL dynamodb list-tables
```

## Description

This command uses the AWS CLI to list all DynamoDB tables in the authenticated account or at a specified custom endpoint. It is essential for cloud discovery phases to map out database resources without needing console access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --endpoint-url $_ENDPOINT_URL | Custom URL for the DynamoDB service endpoint (e.g., for lab environments; omit for production AWS) | No (default: AWS regional endpoint) |
| dynamodb | AWS service namespace for DynamoDB operations | Yes |
| list-tables | Subcommand to retrieve table names | Yes |

## Examples

### Basic Usage (Production AWS)

```bash
aws dynamodb list-tables
```

### Advanced Usage (Custom Endpoint for Lab)

```bash
aws --endpoint-url http://s3.bucket.htb dynamodb list-tables --output json
```

## Expected Output

Successful execution returns a JSON object with an array of table names:

```json
{
    "TableNames": [
        "users",
        "sessions"
    ]
}
```

If no tables exist:

```json
{
    "TableNames": []
}
```

Errors may include AccessDeniedException if permissions are insufficient.

## Related

- [[procedures/AWS-DynamoDB-Table-Enumeration]] (procedure using this command)
- [[commands/aws-sts-get-caller-identity]] (for credential verification)
