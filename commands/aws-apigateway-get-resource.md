---
id: 79a19e41-4a5e-482b-83b0-f10578e29edf
name: aws-apigateway-get-resource
type: command
executor: bash
data: >-
  aws apigateway get-resource --rest-api-id $_REST_API_ID --resource-id
  $_RESOURCE_ID
output: null
created_at: '2023-04-06T03:56:11.830526+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - cloud-aws
  - discovery
verified: true
validated: true
---

# aws-apigateway-get-resource

## Command

```bash
aws apigateway get-resource --rest-api-id $_REST_API_ID --resource-id $_RESOURCE_ID
```

## Description

This command queries the AWS API Gateway service to retrieve detailed information about a specific resource in a REST API. It is used during cloud discovery to map API endpoints and identify configurations that may be exploitable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --rest-api-id $_REST_API_ID | The unique identifier of the REST API containing the resource (e.g., 'a1b2c3d4') | Yes |
| --resource-id $_RESOURCE_ID | The unique identifier of the resource to retrieve (e.g., 'abc123') | Yes |

## Examples

### Basic Usage

```bash
aws apigateway get-resource --rest-api-id a1b2c3d4 --resource-id abc123
```

### With Output Formatting

```bash
aws apigateway get-resource --rest-api-id a1b2c3d4 --resource-id abc123 --output table
```

## Expected Output

Successful execution returns a JSON object describing the resource:

```json
{
    "id": "abc123",
    "parentId": "parent456",
    "pathPart": "users",
    "path": "/users",
    "resourceMethods": {
        "GET": {}
    }
}
```

Look for fields like `path` and `resourceMethods` to understand endpoint exposure.

## Related

- [[procedures/AWS-API-Gateway-Resource-Listing]]
