---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - aws
  - lambda
  - discovery
  - cloud
commands:
  - '[[commands/aws-lambda-get-function-details]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Enumerate-AWS-Lambda-Function-Details

## Summary

This procedure retrieves detailed configuration information about a specific AWS Lambda function, including its ARN, runtime environment, memory allocation, timeout settings, and code size. It is useful for attackers with compromised AWS credentials to map the cloud environment, identify misconfigurations, or plan further exploitation such as function invocation or code inspection.

## Description

In an AWS environment, Lambda functions are serverless compute resources that can be enumerated to understand the target's architecture. By querying a specific function's details, an attacker gains insights into its dependencies, execution environment, and potential vulnerabilities like outdated runtimes or excessive permissions. This technique aligns with cloud discovery tactics, enabling reconnaissance without direct execution. The procedure assumes access to AWS CLI with appropriate IAM permissions and focuses on the `get-function` API call to fetch metadata. Success provides actionable intelligence for pivoting to related services like S3 buckets or IAM roles associated with the function.

## Requirements

1. Valid AWS credentials (access key and secret key) configured in the environment or via AWS CLI profiles, with at least `lambda:GetFunction` permission on the target function.
2. AWS CLI installed and accessible (version 2 recommended for full feature support).
3. Network access to AWS endpoints (no VPC restrictions blocking API calls).
4. Knowledge of the target Lambda function name, obtained from prior enumeration like listing all functions.

## Defense

- Implement least-privilege IAM policies, restricting `lambda:GetFunction` to only necessary roles and monitoring usage via CloudTrail.
- Enable AWS CloudTrail logging for Lambda API calls and set up alerts for anomalous queries from unexpected IPs or roles.
- Use AWS Organizations SCPs to deny broad Lambda access across accounts and regularly audit function configurations with AWS Config.
- Rotate credentials frequently and employ MFA for IAM users to limit the impact of compromised access.

## Objectives

1. Retrieve comprehensive metadata on a specified AWS Lambda function to map the cloud infrastructure.
2. Identify potential misconfigurations, such as high memory limits or long timeouts, that could aid in exploitation.
3. Gather runtime and code details to assess for vulnerabilities like insecure dependencies or exposed secrets.

## Instructions

### Step 1: Configure AWS Credentials

**Context**: Ensure AWS CLI is set up with credentials that have permission to query Lambda functions. This step verifies authentication before enumeration.

Use the AWS CLI to configure or test credentials:

```bash
aws configure list
```

> This command displays current profile settings. If not configured, run `aws configure` to input access key, secret key, region (e.g., us-east-1), and output format (json). Expected output includes profile details without errors.

### Step 2: Retrieve Lambda Function Details

**Context**: Execute the core enumeration command to fetch the function's configuration. Replace the function name with the actual target, obtained from prior discovery.

**Command** ([[commands/aws-lambda-get-function-details]]):

```bash
aws lambda get-function --function-name my-lambda-function
```

> This invokes the Lambda GetFunction API, returning JSON with details like FunctionArn, Runtime (e.g., nodejs14.x), MemorySize, Timeout, CodeSha256, and LastModified. Parse the output for insights; errors indicate insufficient permissions or non-existent function. Use `--region` if targeting a specific AWS region.

### Step 3: Parse and Analyze Output

**Context**: Review the JSON response to extract key intelligence, such as code size for potential download feasibility or runtime for known vulnerabilities.

Use jq for parsing if available:

```bash
aws lambda get-function --function-name my-lambda-function | jq '.Configuration'
```

> Filters to the Configuration object, showing runtime, handler, and environment variables. Expected output highlights exploitable attributes, like large code sizes (>50MB) suggesting complex logic.
