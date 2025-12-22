---
type: command
executor: bash
data: aws apigateway get-resources --rest-api-id $_REST_API_ID
output: null
platforms:
  - AWS
tags:
  - cloud
  - enumeration
  - aws
verified: true
validated: true
---

# AWS APIGateway Get Resources

## Command

```bash
aws apigateway get-resources --rest-api-id $_REST_API_ID
```

## Description

This command queries the AWS API Gateway service to retrieve a list of all resources (paths and methods) associated with a specific REST API. It is used for discovering the structure of APIs during reconnaissance to identify potential attack vectors like exposed endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--rest-api-id` | The unique ID of the target REST API (e.g., 'a1b2c3d4') | Yes |
| `$_REST_API_ID` | Placeholder for the REST API ID value | Yes |

## Examples

### Basic Usage

```bash
aws apigateway get-resources --rest-api-id a1b2c3d4
```

### With Output Formatting

```bash
aws apigateway get-resources --rest-api-id a1b2c3d4 | jq '.items[] | {id: .id, path: .path}'
```

## Expected Output

A JSON object containing an array of resources:

```json
{
    "items": [
        {
            "id": "xyz789",
            "path": "/api/v1/users",
            "parentId": "root"
        }
    ]
}
```

Success is indicated by the presence of the `items` array without error messages. Errors may include `AccessDeniedException` if permissions are insufficient.

## Related

- [[commands/aws-sts-get-caller-identity]]
- [[procedures/aws-api-gateway-resource-enumeration]]
