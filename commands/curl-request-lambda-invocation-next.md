---
id: 10e92dc7-c31f-4fa1-ae0d-3b7af885fe47
name: curl-request-lambda-invocation-next
type: command
executor: bash
data: 'curl "http://${AWS_LAMBDA_RUNTIME_API}/2018-06-01/runtime/invocation/next"'
output: null
created_at: '2023-04-06T03:56:38.338342+00:00'
updated_at: '2023-04-10T20:24:06.950737+00:00'
platforms:
  - AWS
  - Linux
tags:
  - ssrf
  - aws-lambda
  - cloud
verified: true
validated: true
---

# curl-request-lambda-invocation-next

## Command

```bash
curl "http://${AWS_LAMBDA_RUNTIME_API}/2018-06-01/runtime/invocation/next"
```

## Description

This command sends a GET request to the AWS Lambda runtime API endpoint to retrieve the next pending invocation event. It is used in custom Lambda runtimes to poll for events from AWS, blocking until an event arrives or a timeout occurs. In an SSRF context, this allows interception and manipulation of events to inject malicious payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ${AWS_LAMBDA_RUNTIME_API} | The runtime API endpoint URL (e.g., 127.0.0.1:9001 or the provided runtime host:port) | Yes |
| /2018-06-01/runtime/invocation/next | Fixed API path for polling the next invocation event | Built-in |

## Examples

### Basic Usage

```bash
curl "http://127.0.0.1:9001/2018-06-01/runtime/invocation/next"
```

### Advanced Usage

Add timeout and verbose output for debugging:

```bash
curl --max-time 60 -v "http://${AWS_LAMBDA_RUNTIME_API}/2018-06-01/runtime/invocation/next"
```

## Expected Output

On success, the command returns a JSON object representing the invocation event, such as:

```json
{
  "requestContext": {
    "requestId": "12345678-1234-1234-1234-123456789012",
    "functionName": "my-function",
    "deadlineMs": 1234567890
  },
  "body": "base64-encoded-payload"
}
```

If no event is available, it hangs until timeout (default 30 seconds) or returns an empty response/HTTP 200 with no body.

## Related

- [[procedures/SSRF-Attack-on-AWS-Lambda-via-Invocation-Events]]
