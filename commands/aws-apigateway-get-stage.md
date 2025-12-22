---
id: 3d3ae1f6-9189-4a51-a36b-fe43bcd9049a
name: aws-apigateway-get-stage
type: command
executor: bash
data: aws apigateway get-stage --rest-api-id $_REST_API_ID --stage-name $_STAGE_NAME
output: null
created_at: '2023-04-06T03:56:11.905476+00:00'
updated_at: '2023-04-10T20:20:09.425017+00:00'
platforms:
  - AWS
tags:
  - Discovery
  - AWS CLI
  - API Gateway
verified: true
validated: true
---

# aws-apigateway-get-stage

## Command

```bash
aws apigateway get-stage --rest-api-id $_REST_API_ID --stage-name $_STAGE_NAME
```

## Description

This command retrieves detailed information about a specific stage in an AWS API Gateway REST API. It is used during reconnaissance to enumerate stage configurations, endpoints, and variables without modifying resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --rest-api-id $_REST_API_ID | The ID of the target REST API (e.g., 'abc123def') | Yes |
| --stage-name $_STAGE_NAME | The name of the stage to query (e.g., 'prod', 'dev') | Yes |
| --region | AWS region (defaults to configured region) | No |
| --output | Output format (json, text, table; defaults to json) | No |

## Examples

### Basic Usage

```bash
aws apigateway get-stage --rest-api-id abc123 --stage-name prod
```

### Advanced Usage

```bash
aws apigateway get-stage --rest-api-id abc123 --stage-name prod --output json --region us-east-1
```

## Expected Output

Successful execution returns a JSON object with stage details:

```json
{
  "stageName": "prod",
  "deploymentId": "depl:abc123",
  "endpointUrl": "https://abc123.execute-api.us-east-1.amazonaws.com/prod",
  "variables": {
    "stageVariable": "value"
  },
  "cacheClusterEnabled": false,
  "cacheClusterSize": "0.5",
  "throttlingBurstLimit": 500,
  "throttlingRateLimit": 1000
}
```

Look for `endpointUrl` and `variables` to confirm accessible configuration data. Errors like 'AccessDeniedException' indicate insufficient permissions.
