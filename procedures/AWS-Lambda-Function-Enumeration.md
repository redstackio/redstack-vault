---
id: ca37c571-2a75-40c2-bc2d-ad5b952258ce
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.206080+00:00'
updated_at: '2023-04-10T20:20:12.599025+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/AWS-Lambda]]'
commands:
  - '[[commands/aws-lambda-get-function]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS-Lambda-Function-Enumeration

## Summary

This procedure enumerates detailed configuration information about a specific AWS Lambda function using the AWS CLI, allowing attackers or security testers to identify potential vulnerabilities such as misconfigured execution roles, runtime environments, or resource limits that could be exploited for further cloud compromise.

## Description

AWS Lambda functions are serverless compute services that run code in response to events. Enumerating a specific Lambda function reveals critical details like its ARN, runtime version, memory allocation, timeout settings, environment variables, and associated IAM execution role. This information can expose weaknesses, such as overly permissive roles that allow escalation to other AWS services, outdated runtimes vulnerable to known exploits, or custom code that might contain injection flaws. The procedure targets environments where an attacker has obtained valid AWS credentials with lambda:GetFunction permissions, typically through prior credential compromise or misconfiguration. It is commonly used in cloud penetration testing to map the attack surface and chain with other techniques like role assumption or function invocation.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with at least lambda:GetFunction permission.
2. AWS CLI installed and configured with the target account's credentials (e.g., via `aws configure`).
3. Network access to AWS API endpoints (no VPC restrictions blocking outbound API calls).
4. Knowledge of the target Lambda function name, obtained via prior enumeration (e.g., listing functions with `aws lambda list-functions`).

## Defense

- Implement least-privilege IAM policies, restricting lambda:GetFunction to only necessary roles and monitoring for anomalous calls via AWS CloudTrail.
- Enable AWS Config rules to detect and alert on Lambda functions with permissive execution roles or exposed configurations.
- Use AWS Organizations SCPs to limit API actions across accounts and integrate with SIEM for real-time logging of Lambda API queries.
- Rotate credentials regularly and avoid embedding secrets in Lambda code or environment variables.

## Objectives

1. Retrieve configuration details of a target Lambda function to assess its security posture.
2. Identify exploitable elements like IAM roles or runtime versions for potential privilege escalation or code injection.
3. Gather intelligence to support further attacks, such as invoking the function with malicious payloads or assuming its execution role.

## Instructions

### Step 1: Retrieve Lambda Function Configuration

**Context**: Use the AWS CLI to query the Lambda service for details on the specified function. This step requires knowing the exact function name and assumes credentials are already set up. Replace the placeholder with the actual function name to avoid errors.

**Command** ([[commands/aws-lambda-get-function]]):
```bash
aws lambda get-function --function-name $_FUNCTION_NAME
```

> This command sends a GET request to the Lambda API and returns a JSON response with the function's metadata. Verify the output for sensitive details like the execution role ARN, which could be used for role assumption attacks. If the function name is incorrect, expect a ResourceNotFoundException error.

### Step 2: Parse and Analyze Output

**Context**: Review the JSON response to extract key information. This manual step helps identify vulnerabilities without additional tools.

**Command**:
```bash
aws lambda get-function --function-name $_FUNCTION_NAME | jq '.Configuration'
```

> The `jq` filter extracts the Configuration object for easier reading. Look for fields like `Role` (IAM ARN), `Runtime` (e.g., nodejs14.x), `Environment` (variables), and `CodeSha256` (code integrity). Success is indicated by a valid JSON structure without API errors; anomalies like admin-level roles signal high-risk configurations.
