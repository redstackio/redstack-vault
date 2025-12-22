---
id: f4883608-8078-496c-8c02-c704f14b88d9
name: aws-apigateway-get-stages
type: command
executor: bash
data: aws apigateway get-stages --rest-api-id $_REST_API_ID --region $_AWS_REGION
output: null
created_at: '2023-04-06T03:56:11.881085+00:00'
updated_at: '2023-04-10T20:20:33.400217+00:00'
platforms:
  - AWS
tags:
  - cloud
  - enumeration
  - aws-cli
verified: true
validated: true
---

# aws-apigateway-get-stages

## Command

```bash
aws apigateway get-stages --rest-api-id $_REST_API_ID --region $_AWS_REGION
```

## Description

This command retrieves a list of stages for a specified REST API in AWS API Gateway. Stages represent deployment snapshots with configurations; enumerating them helps identify environments like production or staging for potential targeting in cloud attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--rest-api-id` | The ID of the REST API (obtained via get-rest-apis) | Yes |
| `$_REST_API_ID` | Placeholder for the API ID | Yes |
| `--region` | AWS region for the API | No (defaults to default region) |
| `$_AWS_REGION` | Placeholder for the target region | Yes |
| `--position` | Token for pagination if results exceed limits | No |

## Examples

### Basic Usage

```bash
aws apigateway get-stages --rest-api-id a1b2c3d4e5 --region us-east-1
```

### With Pagination

```bash
aws apigateway get-stages --rest-api-id a1b2c3d4e5 --position nextToken --region us-west-2
```

## Expected Output

Returns a JSON object with stage details:

```json
{
  "item": [
    {
      "stageName": "prod",
      "deploymentId": "dep123",
      "createDate": "2023-01-01T12:00:00Z",
      "description": "Production stage",
      "variables": {
        "dbEndpoint": "prod-db.example.com"
      }
    }
  ]
}
```

Check `variables` for sensitive data and `deploymentId` for version info.

## Related

- [[procedures/AWS-API-Gateway-Stage-Enumeration]]
- [[commands/aws-apigateway-get-rest-apis]]
