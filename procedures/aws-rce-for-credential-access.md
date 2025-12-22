---
id: 24dc5d9d-0bab-46ea-b90b-83f05ebfd840
name: aws-rce-for-credential-access
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.536371+00:00'
updated_at: '2023-04-10T20:20:14.751160+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Credential Access]]'
  - '[[tags/Getting credentials using RCE]]'
  - rce
  - aws
commands:
  - '[[commands/retrieve-aws-environment-variables]]'
platforms:
  - AWS
  - Web
tools: []
validated: true
---

# aws-rce-for-credential-access

## Summary

This procedure exploits a remote code execution (RCE) vulnerability in an AWS public-facing application, such as an API Gateway integrated with Lambda, to retrieve environment variables that may contain sensitive AWS credentials like access keys and secret keys. By sending a crafted request to an insecure endpoint, attackers can execute system commands to dump environment details, enabling subsequent unauthorized access to AWS resources.

## Description

In AWS environments, public-facing applications like API Gateways can be misconfigured to allow direct command execution through parameters in HTTP requests, leading to RCE. This procedure targets such vulnerabilities to execute the 'env' command on the underlying system (often a Lambda runtime or EC2 instance), capturing output that includes AWS-specific environment variables. These variables typically hold temporary or long-term credentials used by the application for IAM roles or direct key access. The technique is effective in cloud reconnaissance and credential theft scenarios, particularly when combined with SSRF or other initial access vectors. Success depends on the endpoint's exposure and lack of input sanitization, allowing attackers to pivot to broader AWS compromise.

## Requirements

1. Network access to the vulnerable AWS API Gateway or public-facing endpoint (no authentication required if unauthenticated RCE).
2. Knowledge of the exact endpoint URL structure, such as '/prod/system?cmd=' for command injection.
3. Tools like curl for sending HTTP requests; a proxy like Burp Suite for interception and modification if needed.
4. Basic understanding of AWS environment variables (e.g., AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY).

## Defense

- Regularly scan and audit public-facing AWS services (API Gateway, Lambda) for command injection vulnerabilities using tools like AWS Inspector or third-party scanners.
- Implement input validation and sanitization on all API parameters to prevent direct command execution.
- Use least-privilege IAM roles for applications, avoiding long-term credentials in environment variables; prefer temporary STS tokens.
- Enable AWS CloudTrail and GuardDuty for monitoring anomalous API calls and environment variable access patterns.
- Apply Web Application Firewall (WAF) rules to block suspicious query parameters like 'cmd='.

## Objectives

1. Execute arbitrary commands on the target AWS system via RCE to dump environment variables.
2. Extract AWS credentials from the output for further resource access.
3. Establish a foothold in the AWS environment for lateral movement or data exfiltration.

## Instructions

### Step 1: Identify and Verify the Vulnerable Endpoint

**Context**: Confirm the presence of the RCE endpoint by probing the API Gateway URL. This step ensures the target is reachable and the parameter is accepted without immediate errors, setting up for command execution.

Use a basic curl request to test connectivity:

```bash
curl -v "https://apigateway/prod/system?cmd=echo+test"
```

> This sends a harmless echo command to verify if the endpoint processes 'cmd' parameters. Look for the echoed response in the output to confirm RCE potential.

### Step 2: Retrieve Environment Variables

**Context**: Execute the 'env' command to dump all system environment variables, which often include AWS credentials configured for the application.

**Command** ([[commands/retrieve-aws-environment-variables]]):

```bash
curl "https://apigateway/prod/system?cmd=env"
```

> This command injects 'env' via the 'cmd' parameter, returning a list of environment variables. Parse the response for keys like AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, or AWS_ROLE_ARN, which indicate successful credential exposure.

### Step 3: Extract and Validate Credentials

**Context**: From the dumped variables, isolate AWS-specific credentials and test them to confirm usability, ensuring they provide access to AWS resources.

Save the output to a file for analysis:

```bash
curl "https://apigateway/prod/system?cmd=env" > env_output.txt
grep -i aws env_output.txt
```

> This filters for AWS-related variables. If credentials are found, validate by exporting them and running an AWS CLI command like 'aws sts get-caller-identity' (assuming AWS CLI is available locally). Success is indicated by valid identity details without authentication errors.
