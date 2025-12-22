---
id: c877d351-abc3-4cf3-9da4-95b3607c2d12
name: AWS-SSRF-Credential-Access-via-Lambda-Function
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.559019+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Unsecured Credentials|T1552.005 - Cloud Instance Metadata
    Service]]
sub_techniques: []
tags:
  - cloud-aws
  - ssrf
  - credential-access
  - lambda
commands:
  - '[[commands/curl-aws-lambda-ssrf-invoke]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS-SSRF-Credential-Access-via-Lambda-Function

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability in an AWS Lambda function exposed through API Gateway to access the AWS Instance Metadata Service (IMDS). By crafting a malicious request that redirects the Lambda invocation to the IMDS endpoint (169.254.169.254), an attacker can retrieve temporary IAM credentials associated with the Lambda's execution role, enabling privilege escalation and access to sensitive AWS resources.

## Description

AWS Lambda functions running in a VPC or with attached IAM roles can access the IMDS to obtain temporary credentials. If the Lambda function processes user-supplied URLs without validation (e.g., via an API Gateway proxy), an attacker can perform SSRF to query the IMDS for credentials. This technique targets the Lambda runtime API or chained invocations but pivots to metadata retrieval. It is effective against misconfigured serverless applications where input sanitization is absent. Success allows the attacker to assume the Lambda's role permissions, potentially leading to data exfiltration or further compromise. This maps to cloud environments where Lambda functions handle external inputs like webhooks or API calls.

## Requirements

1. Publicly accessible API Gateway endpoint proxying to the vulnerable Lambda function.
2. Knowledge of the API Gateway URL and any required authentication (e.g., API key or no auth).
3. Network access to send HTTP requests (no AWS credentials needed initially).
4. Tools like curl for request crafting; optionally Burp Suite for interception.

## Defense

- Implement strict URL whitelisting and input validation in Lambda functions to block internal IP ranges like 169.254.169.254.
- Use AWS IAM policies to minimize Lambda role permissions (least privilege).
- Enable IMDSv2 on EC2 instances (though Lambda uses a similar service) and monitor CloudTrail for anomalous API calls.
- Deploy AWS WAF rules to detect SSRF patterns in API Gateway requests.
- Regularly audit Lambda functions for SSRF vulnerabilities using tools like AWS Inspector.

## Objectives

1. Exploit SSRF to access the AWS IMDS endpoint via the Lambda function.
2. Retrieve temporary IAM credentials (AccessKeyId, SecretAccessKey, SessionToken).
3. Use the stolen credentials for privilege escalation in the AWS environment.

## Instructions

### Step 1: Identify the Vulnerable API Gateway Endpoint

**Context**: Locate the API Gateway URL that invokes the Lambda function. This is typically exposed publicly and accepts a 'url' parameter for SSRF. Inspect the application for endpoints handling user input like webhooks or file uploads that trigger Lambda.

No specific command; use reconnaissance tools like browser dev tools or [[commands/curl-basic-probe]] to test the endpoint.

> Expected: Confirmation of the endpoint accepting GET/POST with a 'url' query parameter, e.g., https://apigateway.execute-api.region.amazonaws.com/prod/example.

### Step 2: Craft SSRF Payload to Target IMDS

**Context**: Modify the 'url' parameter to point to the IMDS endpoint instead of the legitimate Lambda runtime API. This tricks the Lambda into making an internal request on behalf of the attacker, retrieving metadata.

Use the following command to send the SSRF request:

**Command** ([[commands/curl-aws-lambda-ssrf-invoke]]):
```bash
curl "https://$_API_GATEWAY_URL?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/$_ROLE_NAME"
```

> This command sends a GET request to the API Gateway, injecting the IMDS URL to fetch IAM role credentials. Replace $_API_GATEWAY_URL with the actual endpoint (e.g., https://abc123.execute-api.us-east-1.amazonaws.com/prod/example) and $_ROLE_NAME with the Lambda's assumed role name if known (probe /latest/meta-data/iam/security-credentials/ first to list roles). If the endpoint requires POST, adjust to -X POST -d "url=...". Expected output includes JSON with temporary credentials if successful; errors indicate blocked requests or invalid role.

### Step 3: Extract and Verify Credentials

**Context**: Parse the response for the credential JSON. Test the credentials using AWS CLI to confirm validity and scope.

Save the output to a file and use AWS CLI:
```bash
aws sts get-caller-identity --access-key-id $_ACCESS_KEY_ID --secret-access-key $_SECRET_ACCESS_KEY --token $_SESSION_TOKEN
```

> Expected: JSON response showing the assumed role ARN and account details, confirming access. If invalid, the SSRF may have been blocked or the role lacks permissions.

### Step 4: Escalate with Stolen Credentials

**Context**: Use the credentials to perform further actions, such as listing S3 buckets or invoking other services, based on the role's policy.

Example: List S3 buckets.
```bash
aws s3 ls --access-key-id $_ACCESS_KEY_ID --secret-access-key $_SECRET_ACCESS_KEY --token $_SESSION_TOKEN
```

> Expected: List of accessible S3 buckets or resources, indicating successful escalation. Monitor for expiration (credentials are temporary, typically 1-6 hours).
