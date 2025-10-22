---
id: 53ae71fe-88eb-4dd8-bf85-3e319ea0cb13
name: SSRF Attack on AWS Lambda through Invocation Events
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.343798+00:00'
updated_at: '2023-04-10T20:24:06.924911+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF URL for AWS Lambda]]'
- '[[SSRF URL for Cloud Instances]]'
commands:
- '[[Request Next Invocation]]'
- '[[Request Next Invocation]]'
---

# SSRF Attack on AWS Lambda through Invocation Events

## Summary

A Server-Side Request Forgery (SSRF) attack can be performed on AWS Lambda through the use of Invocation Events. An attacker can craft a malicious request to the AWS Lambda service, which will trigger the Lambda function to execute with the attacker's payload. This can lead to remote code execution

## Description

# Description

A Server-Side Request Forgery (SSRF) attack can be performed on AWS Lambda through the use of Invocation Events. An attacker can craft a malicious request to the AWS Lambda service, which will trigger the Lambda function to execute with the attacker's payload. This can lead to remote code execution and other malicious activities. To perform this attack, the attacker needs to have the ability to send requests to the AWS Lambda service, which can be achieved through a compromised AWS account or by exploiting a vulnerable web application that makes use of the Lambda function.

## Requirements

1. Access to the AWS Lambda service

1. Ability to craft malicious requests

## Defense

1. Ensure that the AWS Lambda function is running with the least privilege required to perform its intended function

1. Implement network segmentation to limit access to the AWS Lambda service

1. Regularly monitor and review AWS account activity for suspicious behavior

## Objectives

1. Execute arbitrary code on the AWS Lambda service

1. Gain access to sensitive data stored within the Lambda function

1. Move laterally within the AWS environment

# Instructions

1. To receive invocation events from AWS Lambda, use the provided HTTP API and send a cURL request to the specified endpoint. The endpoint URL is provided in the 'data' field of this JSON object. Replace the '${AWS_LAMBDA_RUNTIME_API}' placeholder in the URL with the actual runtime API endpoint provided by AWS.

**Code**: [[http://localhost:9001/2018-06-01/runtime/invocatio]]

> When a Lambda function is invoked, AWS Lambda sends an invocation event to the custom runtime. The custom runtime can receive this event by sending a GET request to the provided HTTP API endpoint. The request will block until an invocation event is available or a timeout occurs. Once an invocation event is received, the custom runtime can process it and send a response back to AWS Lambda using the same HTTP API endpoint.

**Command** ([[Request Next Invocation]]):

```bash
curl "http://localhost:9001/2018-06-01/runtime/invocation/next"
```

**Command** ([[Request Next Invocation]]):

```bash
curl "http://${AWS_LAMBDA_RUNTIME_API}/2018-06-01/runtime/invocation/next"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Request Next Invocation]]
- [[Request Next Invocation]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF URL for AWS Lambda]]
- [[SSRF URL for Cloud Instances]]
