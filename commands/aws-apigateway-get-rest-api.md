---
id: 0e2ff5f2-113a-4281-9d82-c6bdc9878859
name: aws-apigateway-get-rest-api
type: command
executor: bash
data: aws apigateway get-rest-api --rest-api-id $_REST_API_ID
output: null
created_at: '2023-04-06T03:56:11.785538+00:00'
updated_at: '2023-04-10T20:20:15.123903+00:00'
platforms:
  - AWS
tags:
  - discovery
  - cloud
verified: true
validated: true
---

# aws-apigateway-get-rest-api

## Command

```bash
aws apigateway get-rest-api --rest-api-id $_REST_API_ID
```

## Description

This command retrieves detailed information about a specific REST API in AWS API Gateway, including configuration, resources, and policies. Use it after listing APIs to gather in-depth intelligence on a target API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--rest-api-id $_REST_API_ID` | The unique ID of the REST API (e.g., 'a1b2c3d4') | Yes |

## Examples

### Basic Usage

```bash
aws apigateway get-rest-api --rest-api-id a1b2c3d4
```

### With Output Formatting

```bash
aws apigateway get-rest-api --rest-api-id a1b2c3d4 --query '{
  name: name,
  endpoint: endpointConfiguration.types,
  resources: resources
}'
```

## Expected Output

```
{
  "id": "a1b2c3d4",
  "name": "MyApi",
  "description": "Sample API",
  "createdDate": "2023-01-15T10:00:00Z",
  "endpointConfiguration": {
    "types": ["REGIONAL"]
  },
  "policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\"...",
  "resources": {
    "/": {
      "pathPart": "/"
    }
  }
}
```

A JSON object with API metadata, including name, endpoint types, IAM policy, and resource tree.

## Related

- [[procedures/AWS-API-Gateway-Information-Gathering]]
- [[commands/aws-apigateway-list-rest-apis]]
