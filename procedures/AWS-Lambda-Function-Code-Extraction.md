---
id: 831d0f25-f41d-4cf9-801c-53962e04e073
name: AWS-Lambda-Function-Code-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.670742+00:00'
updated_at: '2023-04-10T20:19:52.646957+00:00'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Cloud Storage]]'
sub_techniques: []
tags:
  - '[[tags/AWS - Lambda - Extract function''s code]]'
  - '[[tags/Cloud - AWS]]'
  - aws
  - lambda
  - code-extraction
commands:
  - '[[commands/aws-lambda-list-functions]]'
  - '[[commands/aws-lambda-get-function-code-location]]'
  - '[[commands/wget-download-lambda-code-zip]]'
platforms:
  - AWS
  - Linux
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# AWS-Lambda-Function-Code-Extraction

## Summary

This procedure outlines how to extract the source code of an AWS Lambda function using the AWS CLI. By listing available functions, retrieving the code download URL, and downloading the ZIP archive, attackers with compromised AWS credentials can obtain the function's code to search for embedded secrets like API keys or database credentials, enabling further compromise of the cloud environment.

## Description

AWS Lambda functions contain executable code that may hardcode sensitive information such as credentials or configuration details. With valid AWS credentials granting access to the Lambda service (e.g., lambda:ListFunctions and lambda:GetFunction permissions), an attacker can enumerate functions, obtain a presigned URL to the function's code package (stored in S3), and download it as a ZIP file. Once extracted, the code can be inspected for vulnerabilities or secrets. This technique is particularly useful in post-compromise scenarios where initial access to AWS accounts has been achieved via stolen credentials or misconfigurations. The procedure assumes the AWS CLI is configured with the attacker's profile and targets an AWS account with Lambda functions deployed.

## Requirements

1. AWS CLI installed and configured with credentials that have lambda:ListFunctions, lambda:GetFunction, and s3:GetObject permissions.
2. Network access to AWS endpoints (no VPC restrictions blocking CLI calls).
3. Bash environment (Linux/macOS) for command execution.
4. Knowledge of the target AWS region if functions are region-specific (default to us-east-1 if unspecified).

## Defense

- Implement least-privilege IAM policies to restrict Lambda API access; use resource-based policies to limit GetFunction calls to specific functions.
- Enable AWS CloudTrail logging for Lambda and S3 events to monitor function downloads and code accesses.
- Store sensitive data in AWS Secrets Manager or Parameter Store instead of hardcoding in Lambda code; use environment variables encrypted with KMS.
- Regularly scan Lambda functions for secrets using tools like TruffleHog and rotate any exposed credentials.
- Monitor for anomalous CLI usage via AWS GuardDuty or custom CloudWatch alarms on Lambda API calls.

## Objectives

1. Enumerate all Lambda functions in the target AWS account to identify potential targets.
2. Retrieve the presigned download URL for a specific function's code package.
3. Download and extract the ZIP file containing the function code for analysis.
4. Identify and exfiltrate any embedded secrets from the code.

## Instructions

### Step 1: List Available Lambda Functions

**Context**: Begin by querying the AWS Lambda service to list all functions in the account. This step discovers potential targets without alerting if logs are not monitored. Use the attacker's AWS profile to authenticate the request.

**Command** ([[commands/aws-lambda-list-functions]]):
```bash
aws lambda list-functions --profile $_PROFILE
```

> This command outputs a JSON array of Lambda functions, including names, runtimes, and ARNs. Review the output to select a target function (e.g., one handling sensitive operations). If no functions appear, verify permissions or try specifying a region with --region $_REGION. Success is indicated by a non-empty "Functions" array in the JSON response.

### Step 2: Get Code Download Location for Target Function

**Context**: For the selected function, retrieve the presigned S3 URL pointing to its code package. This URL is temporary and grants direct download access without additional authentication. Replace placeholders with values from Step 1.

**Command** ([[commands/aws-lambda-get-function-code-location]]):
```bash
aws lambda get-function --function-name "$_FUNCTION_NAME" --query 'Code.Location' --output text --profile $_PROFILE
```

> The command returns a plain-text URL (e.g., https://bucket.s3.region.amazonaws.com/key?signature...). Copy this URL for the next step. If the function has inline code (not ZIP), it may return a different location; focus on ZIP-deployed functions. Success is a valid HTTPS URL starting with s3.amazonaws.com.

### Step 3: Download the Function Code ZIP

**Context**: Use the presigned URL to download the code package as a ZIP file. Since the URL is presigned, no AWS credentials are needed for wget. Extract the ZIP afterward to access the code files (e.g., index.js, requirements.txt).

**Command** ([[commands/wget-download-lambda-code-zip]]):
```bash
wget -O $_OUTPUT_FILE $_URL
```

> This downloads the ZIP to the specified file (e.g., lambda-code.zip). Verify the download with ls -la $_OUTPUT_FILE (should show a non-zero size). Unzip with unzip $_OUTPUT_FILE and grep for secrets (e.g., grep -r "password" .). Success is a complete ZIP file containing the function's source code and dependencies.
