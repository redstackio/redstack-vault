---
id: 7460b8eb-0e39-4c17-9b92-742127ba9ffe
name: AWS-API-Gateway-Method-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.417383+00:00'
updated_at: '2023-04-10T20:19:54.335935+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/API Gateway]]'
commands:
  - '[[commands/aws-apigateway-get-method]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# AWS-API-Gateway-Method-Enumeration

## Summary

This procedure enumerates the configuration details of HTTP methods for a specific resource in an AWS API Gateway REST API. It uses the AWS CLI to retrieve information about supported methods (e.g., GET, POST), authorization types, and integration settings, helping identify exposed endpoints, misconfigurations, or potential attack surfaces in cloud-based APIs.

## Description

AWS API Gateway is a service for creating and managing RESTful APIs at scale. Enumerating methods reveals the structure of an API, including which HTTP operations are enabled on resources. This is useful in red teaming or penetration testing to map API endpoints, detect overly permissive configurations (e.g., no authentication), or find opportunities for method override attacks. The procedure assumes access to AWS credentials and focuses on a single method retrieval, which can be repeated for multiple methods to build a full API map. It targets deployed APIs and requires knowing the REST API ID and resource ID, often obtained from prior enumeration of API resources.

## Requirements

1. AWS credentials with `apigateway:GetMethod` permission (e.g., via IAM role or access keys configured in AWS CLI).
2. AWS CLI version 2.x installed and authenticated (`aws configure` or environment variables set).
3. Knowledge of the target REST API ID (e.g., from `aws apigateway get-rest-apis`) and Resource ID (e.g., from `aws apigateway get-resources --rest-api-id <API_ID>`).
4. Network access to AWS endpoints (no VPC-specific restrictions unless using private APIs).

## Defense

- Implement least-privilege IAM policies to restrict `apigateway:GetMethod` access to authorized users only.
- Enable AWS CloudTrail logging for API Gateway actions to detect unauthorized enumeration attempts.
- Use API Gateway resource policies and authorizers (e.g., AWS_IAM, Cognito) to limit method exposure.
- Monitor for anomalous CLI usage via AWS GuardDuty or CloudWatch, focusing on API Gateway API calls from unexpected IPs.

## Objectives

1. Retrieve detailed configuration of a specific HTTP method on an API resource.
2. Identify supported methods, authorization settings, and integration types to assess API security.
3. Detect misconfigurations like unauthenticated methods that could enable unauthorized access or data exposure.

## Instructions

### Step 1: Retrieve Specific Method Details

**Context**: This step queries AWS API Gateway for the configuration of a targeted HTTP method on a resource, providing insights into its setup. It is the core action for enumeration and should be run after identifying the API and resource IDs. If the method does not exist, the command will return a 404 error, indicating it is not configured.

**Command** ([[commands/aws-apigateway-get-method]]):
```bash
aws apigateway get-method --rest-api-id $_REST_API_ID --resource-id $_RESOURCE_ID --http-method $_HTTP_METHOD
```

> Run this command to fetch the method details. Replace `$_REST_API_ID` with the API's unique identifier (e.g., `abc123def`), `$_RESOURCE_ID` with the resource's ID (e.g., `xyz789`), and `$_HTTP_METHOD` with the method (e.g., `GET`, `POST`). The output is JSON, which can be piped to `jq` for parsing (e.g., `| jq '.authorizationType'`). If successful, it confirms the method's existence and exposes configuration details like integration URI or API key requirements. Verify by checking for non-empty JSON response; errors indicate permission issues or invalid IDs.
