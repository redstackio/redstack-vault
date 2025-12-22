---
id: 901f52e9-5d9a-4dc8-8485-7129353f7147
name: Invoke-AWS-Lambda-Function-via-API-Gateway
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.960443+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Execution through API|T1106 - Execution through API]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Invoke the Function]]'
  - '[[tags/Persistence]]'
commands:
  - '[[commands/curl-invoke-lambda-endpoint]]'
platforms:
  - AWS
tools: []
validated: true
---

# Invoke-AWS-Lambda-Function-via-API-Gateway

## Summary

This procedure demonstrates how to invoke an AWS Lambda function exposed through an API Gateway endpoint using a simple HTTP request. It is particularly useful for establishing persistence in a cloud environment by periodically triggering the function to execute arbitrary code without managing servers, assuming the endpoint is publicly accessible or authenticated via API keys.

## Description

AWS Lambda enables serverless execution of code in response to events, and when integrated with API Gateway, it can be invoked via standard HTTP requests. Attackers can leverage this for remote code execution and persistence by calling the endpoint to run malicious payloads hosted within the Lambda function. This technique requires knowledge of the specific API Gateway URL and any required authentication. In a typical attack scenario, the endpoint might be discovered through reconnaissance of AWS resources, and invocation can deliver commands, exfiltrate data, or maintain a callback mechanism. Success relies on the function's permissions and the absence of rate limiting or logging controls.

## Requirements

1. The API Gateway endpoint URL for the target Lambda function (e.g., obtained via AWS console, CLI, or reconnaissance).
2. Network access to the internet or the AWS region hosting the endpoint.
3. Optional: AWS API key or IAM credentials if the endpoint requires authentication (not covered in this basic example).
4. Tools like curl installed on the attacker's machine.

## Defense

- Enable AWS CloudTrail and API Gateway access logs to monitor invocation patterns and detect anomalous requests.
- Implement API key rotation, rate limiting, and WAF rules on API Gateway to block unauthorized access.
- Apply least privilege to Lambda functions, restricting execution roles and monitoring for unexpected invocations via AWS GuardDuty or Config.

## Objectives

1. Remotely trigger the execution of code within the AWS Lambda function.
2. Establish persistence by scheduling periodic invocations to maintain access or perform ongoing tasks.
3. Verify successful execution through response data or side effects in the target environment.

## Instructions

### Step 1: Identify the API Gateway Endpoint

**Context**: Before invocation, confirm the exact URL of the API Gateway endpoint proxying to the Lambda function. This can be found in AWS documentation, console, or through enumeration tools like AWS CLI if credentials are available.

No specific command is required here, but use AWS CLI if authenticated: `aws apigateway get-rest-apis` to list endpoints.

> This step ensures the correct target; incorrect URLs will result in 404 errors.

### Step 2: Prepare the Invocation Request

**Context**: Review any required headers or payload for the Lambda invocation. For a basic GET request, no payload is needed, but POST can be used for input data to the function.

Use [[commands/curl-invoke-lambda-endpoint]] to test connectivity:

```bash
curl "$_ENDPOINT_URL"
```

> Replace $_ENDPOINT_URL with the actual API Gateway URL. Expected: HTTP 200 response if accessible.

### Step 3: Invoke the Lambda Function and Verify Response

**Context**: Send the HTTP request to trigger the Lambda execution. Monitor the response for output from the function, which could indicate success or errors.

Execute the invocation using [[commands/curl-invoke-lambda-endpoint]]:

```bash
curl "$_ENDPOINT_URL" -X GET
```

> This sends a GET request; for payloads, add -d '{"key":"value"}'. If successful, the Lambda processes the event and returns a response.

### Step 4: Validate Persistence or Side Effects

**Context**: After invocation, check for expected outcomes like log entries in CloudWatch or data changes triggered by the function.

No command here; manually review AWS console or use `aws logs get-log-events` if creds available.

> Success is confirmed if the function executes without errors and performs the intended action, such as writing to S3 or sending a callback.
