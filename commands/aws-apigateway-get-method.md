---
id: 7ec8e0e6-890d-41bb-a24a-31976b353c50
name: aws-apigateway-get-method
type: command
executor: bash
data: >-
  aws apigateway get-method --rest-api-id $_REST_API_ID --resource-id
  $_RESOURCE_ID --http-method $_HTTP_METHOD
output: null
created_at: '2023-04-06T03:56:11.858662+00:00'
updated_at: '2023-04-10T20:20:28.556332+00:00'
platforms:
  - AWS
tags:
  - enumeration
  - aws-cli
verified: true
validated: true
---

# aws-apigateway-get-method

## Command

```bash
aws apigateway get-method --rest-api-id $_REST_API_ID --resource-id $_RESOURCE_ID --http-method $_HTTP_METHOD
```

## Description

This command retrieves the configuration details of a specific HTTP method (e.g., GET, POST) for a resource in an AWS API Gateway REST API. Use it during cloud reconnaissance to map API structures and identify permissive endpoints. It requires prior knowledge of the API and resource IDs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --rest-api-id | The string identifier of the associated RestApi (e.g., `abc123def`) | Yes |
| --resource-id | The Resource identifier for the method (e.g., `xyz789`) | Yes |
| --http-method | The HTTP method (case-sensitive: GET, POST, PUT, DELETE, etc.) | Yes |

## Examples

### Basic Usage

```bash
aws apigateway get-method --rest-api-id abc123def --resource-id xyz789 --http-method GET
```

### Advanced Usage

```bash
aws apigateway get-method --rest-api-id abc123def --resource-id xyz789 --http-method POST --region us-east-1
```

## Expected Output

Successful execution returns a JSON object with method details:

```json
{
    "apiKeyRequired": false,
    "authorizationType": "NONE",
    "httpMethod": "GET",
    "methodResponses": {
        "200": {}
    },
    "requestParameters": {},
    "requestModels": {
        "application/json": "Empty"
    },
    "type": "MOCK"
}
```

Look for fields like `authorizationType` (e.g., "NONE" indicates no auth) or `integration` for backend details. Errors include 404 (method not found) or 403 (insufficient permissions).

## Related

- [[procedures/AWS-API-Gateway-Method-Enumeration]]
- [[tools/aws-cli]]
