---
id: new-uuid-1234-5678-9abc-def0
name: aws-apigateway-get-rest-apis
type: command
executor: bash
data: aws apigateway get-rest-apis --region $_AWS_REGION
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - AWS
tags:
  - cloud
  - enumeration
  - aws-cli
verified: true
validated: true
---

# aws-apigateway-get-rest-apis

## Command

```bash
aws apigateway get-rest-apis --region $_AWS_REGION
```

## Description

This command lists all REST APIs created in the specified AWS region using the API Gateway service. It is useful for reconnaissance to discover API endpoints and their IDs in a compromised AWS account, enabling further enumeration of resources like stages or integrations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | AWS region to query (e.g., us-east-1) | No (defaults to default region) |
| `$_AWS_REGION` | Placeholder for the target AWS region | Yes |

## Examples

### Basic Usage

```bash
aws apigateway get-rest-apis --region us-east-1
```

### With Output Parsing

```bash
aws apigateway get-rest-apis --region us-west-2 | jq '.items[] | {id: .id, name: .name}'
```

## Expected Output

Successful execution returns a JSON object with an `items` array of API details:

```json
{
  "items": [
    {
      "id": "a1b2c3d4e5",
      "name": "MyRestApi",
      "createdDate": "2023-01-01T12:00:00Z",
      "apiKeySource": "HEADER"
    }
  ]
}
```

Look for the `id` field to use in subsequent commands like getting stages.

## Related

- [[procedures/AWS-API-Gateway-Stage-Enumeration]]
- [[commands/aws-apigateway-get-stages]]
