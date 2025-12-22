---
id: new-uuid-for-list-apis
name: aws-apigateway-list-rest-apis
type: command
executor: bash
data: 'aws apigateway list-rest-apis --query ''items[*].[id,name,createdDate]'''
output: null
created_at: '2023-04-10T20:20:15.000000+00:00'
updated_at: '2023-04-10T20:20:15.000000+00:00'
platforms:
  - AWS
tags:
  - discovery
  - cloud
verified: true
validated: true
---

# aws-apigateway-list-rest-apis

## Command

```bash
aws apigateway list-rest-apis --query 'items[*].[id,name,createdDate]'
```

## Description

This command lists all REST APIs in the AWS account using the API Gateway service. It is used during initial discovery to identify existing APIs and their basic metadata without requiring specific API IDs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--query 'items[*].[id,name,createdDate]'` | JMESPath query to filter output to API ID, name, and creation date | No (but recommended for readability) |
| `--position` | Token for pagination if more than 500 APIs exist | No |

## Examples

### Basic Usage

```bash
aws apigateway list-rest-apis
```

### Filtered Usage

```bash
aws apigateway list-rest-apis --query 'items[*].[id,name]'
```

## Expected Output

```
[
  [
    "a1b2c3d4",
    "MyApi",
    "2023-01-15T10:00:00Z"
  ],
  [
    "e5f6g7h8",
    "AnotherApi",
    "2023-02-20T14:30:00Z"
  ]
]
```

A JSON array of arrays, each containing the API ID, name, and creation date. Empty array if no APIs exist.

## Related

- [[procedures/AWS-API-Gateway-Information-Gathering]]
- [[commands/aws-apigateway-get-rest-api]]
