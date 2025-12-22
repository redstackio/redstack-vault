---
id: bd1b738f-d413-4e50-85d2-715930fdb9c6
name: aws-lambda-list-event-source-mappings
type: command
executor: bash
data: aws lambda list-event-source-mappings --function-name $_FUNCTION_NAME
output: null
created_at: '2023-04-06T03:56:11.251519+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - cloud
  - enumeration
  - aws-lambda
verified: true
validated: true
---

# aws-lambda-list-event-source-mappings

## Command

```bash
aws lambda list-event-source-mappings --function-name $_FUNCTION_NAME
```

## Description

This command queries the AWS Lambda service to list all event source mappings associated with a specific Lambda function. It is useful for discovering how the function is triggered by other AWS services, aiding in cloud infrastructure reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --function-name $_FUNCTION_NAME | The name or ARN of the Lambda function to query | Yes |
| --region (optional) | AWS region (defaults to configured region) | No |
| --profile (optional) | AWS CLI profile to use | No |

## Examples

### Basic Usage

```bash
aws lambda list-event-source-mappings --function-name my-lambda-function
```

### Advanced Usage

```bash
aws lambda list-event-source-mappings --function-name my-lambda-function --region us-west-2 --output json
```

## Expected Output

Successful execution returns a JSON object with an "EventSourceMappings" array, each containing fields like UUID, EventSourceArn (e.g., arn:aws:sqs:us-east-1:123456789012:my-queue), FunctionArn, State (e.g., Enabled), and BatchSize.

Example:

```json
{
  "EventSourceMappings": [
    {
      "UUID": "123e4567-e89b-12d3-a456-426614174000",
      "EventSourceArn": "arn:aws:sqs:us-east-1:123456789012:my-queue",
      "FunctionArn": "arn:aws:lambda:us-east-1:123456789012:function:my-function",
      "State": "Enabled",
      "BatchSize": 10
    }
  ]
}
```

If no mappings exist, returns an empty array. Errors occur if permissions are insufficient (e.g., AccessDenied).

## Related

- [[procedures/AWS-Lambda-Event-Source-Mapping-Enumeration]]
- [[tools/AWS-CLI]]
