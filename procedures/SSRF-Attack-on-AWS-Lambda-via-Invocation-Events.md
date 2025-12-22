---
id: 53ae71fe-88eb-4dd8-bf85-3e319ea0cb13
name: SSRF-Attack-on-AWS-Lambda-via-Invocation-Events
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:38.343798+00:00'
updated_at: '2023-04-10T20:24:06.924911+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Server-Side Request Forgery]]'
  - '[[tags/AWS-Lambda]]'
  - '[[tags/SSRF]]'
  - '[[tags/Cloud-Exploitation]]'
commands:
  - '[[commands/curl-request-lambda-invocation-next]]'
platforms:
  - AWS
  - Cloud
tools: []
validated: true
---

# SSRF-Attack-on-AWS-Lambda-via-Invocation-Events

## Summary

This procedure demonstrates a Server-Side Request Forgery (SSRF) attack targeting AWS Lambda functions through manipulation of invocation events. By crafting malicious requests to the Lambda runtime API, an attacker can force the function to process unauthorized payloads, potentially leading to remote code execution (RCE) and unauthorized access within the AWS environment.

## Description

In an SSRF attack on AWS Lambda, the vulnerability arises when a web application or service interacts with Lambda invocation endpoints without proper validation of user-supplied URLs or payloads. An attacker exploits this by sending a forged request that tricks the Lambda service into fetching or executing content from attacker-controlled sources. This can result in the Lambda function making unintended internal requests, such as accessing AWS metadata services, or executing arbitrary code if the runtime environment allows it. The attack requires the ability to interact with the Lambda service, often through a vulnerable frontend application or compromised AWS credentials. Success enables lateral movement, data exfiltration, or further compromise of cloud resources. This technique is particularly effective against custom runtimes where the invocation API is exposed or misconfigured.

## Requirements

1. Valid access to the AWS Lambda service, such as through a compromised AWS account, API keys, or a vulnerable application that proxies requests to Lambda.
2. Knowledge of the Lambda function's runtime API endpoint (e.g., the value of $AWS_LAMBDA_RUNTIME_API environment variable).
3. Tools for sending HTTP requests, such as curl, and optionally a listener for capturing responses.
4. Network access to the target Lambda environment, potentially requiring SSRF in an internal network context.

## Defense

Defensive measures and detection strategies:

- Ensure that the AWS Lambda function is running with the least privilege required to perform its intended function, using IAM roles with minimal permissions.
- Implement network segmentation to limit access to the AWS Lambda service and internal metadata endpoints.
- Regularly monitor and review AWS account activity for suspicious behavior, such as unusual invocation patterns or requests to runtime APIs from unexpected sources.
- Validate and sanitize all user inputs in applications that interact with Lambda, blocking requests to internal or sensitive URLs.
- Enable AWS CloudTrail logging for Lambda invocations and integrate with SIEM for anomaly detection.

## Objectives

1. Execute arbitrary code on the AWS Lambda service by injecting payloads via invocation events.
2. Gain access to sensitive data stored within the Lambda function or accessible via SSRF-routed requests (e.g., instance metadata).
3. Move laterally within the AWS environment to compromise additional resources.

## Instructions

### Step 1: Prepare the Runtime API Endpoint

**Context**: Identify and substitute the AWS Lambda runtime API endpoint, which is typically available as an environment variable in custom runtimes. This endpoint handles invocation events sent by AWS Lambda to the function.

Replace the placeholder ${AWS_LAMBDA_RUNTIME_API} with the actual endpoint URL provided by AWS (e.g., 127.0.0.1:9001 for local testing or the runtime API in a deployed function).

### Step 2: Request the Next Invocation Event

**Context**: Send a GET request to the invocation endpoint to receive pending invocation events from AWS Lambda. This step blocks until an event is available or a timeout occurs, allowing the attacker to intercept and potentially modify the event payload for SSRF exploitation.

**Command** ([[commands/curl-request-lambda-invocation-next]]):
```bash
curl "http://${AWS_LAMBDA_RUNTIME_API}/2018-06-01/runtime/invocation/next"
```

> This command polls the Lambda runtime API for the next invocation event. Upon success, it returns a JSON payload containing the event data, which can be inspected or altered to include SSRF payloads (e.g., URLs pointing to attacker-controlled resources). If no event is available, it times out after 30 seconds by default. Use this in a custom runtime script to process events maliciously, such as fetching external resources or executing code.
