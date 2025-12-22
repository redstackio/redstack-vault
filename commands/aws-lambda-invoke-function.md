---
id: 73928ff1-f80b-44ca-aff4-40c200b82ca8
name: aws-lambda-invoke-function
type: command
executor: bash
data: >-
  aws lambda invoke --function-name $_FUNCTION_NAME $_OUTPUT_FILE --region
  $_REGION
output: null
created_at: '2023-04-06T03:56:12.029080+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - cloud
  - aws
  - lambda
verified: true
validated: true
---

# aws-lambda-invoke-function

## Command

```bash
aws lambda invoke --function-name $_FUNCTION_NAME $_OUTPUT_FILE --region $_REGION
```

## Description

This command invokes a specified AWS Lambda function synchronously, executing its code and returning the response. It is used in privilege escalation scenarios where the function's execution role has higher permissions, allowing indirect access to restricted resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --function-name $_FUNCTION_NAME | The name, ARN, or alias of the Lambda function to invoke | Yes |
| $_OUTPUT_FILE | File path to save the invocation response (e.g., response.json); if omitted, output is to stdout | No |
| --region $_REGION | AWS region where the function is located (e.g., us-west-2) | Yes (if not set as default) |
| --payload file://$_PAYLOAD_FILE | Optional JSON payload file for function input | No |
| --invocation-type $_TYPE | Invocation type: RequestResponse (default, synchronous), DryRun (validate), Event (asynchronous) | No |

## Examples

### Basic Usage

```bash
aws lambda invoke --function-name myFunction response.json --region us-west-2
```

### Advanced Usage with Payload

```bash
aws lambda invoke --function-name myFunction --payload file://input.json output.json --region us-west-2 --invocation-type Event
```

## Expected Output

The command returns a request ID on stdout, and the response is written to the specified file. Successful output in response.json:

```json
{
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST",
  "Payload": "...function output..."
}
```

If the function errors, StatusCode may be 200 with an error in Payload, or non-200 for invocation failures.

## Related

- [[procedures/AWS-Lambda-Function-Invocation-for-Privilege-Escalation]]
- [[commands/aws-lambda-list-functions]]
