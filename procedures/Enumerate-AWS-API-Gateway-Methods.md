---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/API-Gateway-Enumeration]]'
  - '[[tags/Discovery]]'
commands:
  - '[[commands/aws-apigateway-get-method]]'
platforms:
  - AWS
tools: []
validated: true
---

# Enumerate-AWS-API-Gateway-Methods

## Summary

This procedure uses the AWS CLI to retrieve detailed information about specific methods configured in an AWS API Gateway REST API. It allows attackers or security testers to enumerate HTTP methods, integration types, and request/response models associated with a given resource, aiding in the discovery of potential misconfigurations or vulnerabilities in API endpoints.

## Description

In cloud environments, AWS API Gateway serves as a front door for APIs, managing methods like GET, POST, PUT, and DELETE for various resources. Enumerating method information reveals how endpoints are integrated with backend services (e.g., Lambda, HTTP), authorization settings, and data models. From an offensive perspective, this discovery technique helps identify exposed functionalities, weak integrations, or overly permissive configurations that could lead to unauthorized access, data leakage, or further exploitation. The procedure requires authenticated access via AWS credentials and targets a specific REST API ID, resource ID, and HTTP method. Defenders can monitor API Gateway logs for unusual GET-method requests to detect reconnaissance activity.

## Requirements

1. AWS CLI installed and configured with valid credentials (e.g., IAM user or role with `apigateway:GET` permissions on the target API).
2. Knowledge of the target REST API ID, resource ID, and HTTP method (obtainable via prior enumeration of APIs and resources).
3. Network access to AWS endpoints (no direct VPC peering required for public APIs).

## Defense

- Implement least-privilege IAM policies to restrict `apigateway:GET` actions to necessary roles only.
- Enable AWS CloudTrail logging for API Gateway to track method enumeration attempts.
- Use API keys, IAM authentication, or custom authorizers to protect endpoints and log access patterns.
- Regularly audit API configurations via AWS Config or tools like Prowler for misconfigurations.

## Objectives

1. Retrieve configuration details for a specific API Gateway method to understand endpoint behavior.
2. Identify potential security weaknesses, such as unsecured integrations or exposed models.
3. Map API structures for targeted follow-on attacks or defensive hardening.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure your AWS credentials are set up correctly to authenticate requests. This step confirms access to the API Gateway service without errors.

Run `aws sts get-caller-identity` to validate your identity and permissions.

**Expected Output**: JSON response showing your AWS account, user ARN, and session details, with no permission denied errors.

### Step 2: Enumerate the Specific Method

**Context**: Use the AWS CLI to query the method details for the target resource. This reveals integration URI, authorization settings, and model schemas, which can indicate vulnerabilities like direct backend exposure.

**Command** ([[commands/aws-apigateway-get-method]]):
```bash
aws apigateway get-method --rest-api-id $_REST_API_ID --resource-id $_RESOURCE_ID --http-method $_HTTP_METHOD
```

> Replace `$_REST_API_ID` with the API's unique identifier (e.g., 'abc123'), `$_RESOURCE_ID` with the resource path ID (e.g., 'xyz789'), and `$_HTTP_METHOD` with the method (e.g., 'GET'). The command outputs JSON with method properties. If the method exists, you'll see details like `httpMethod`, `authorizationType`, and `integration`. Errors like 'NotFoundException' indicate the method doesn't exist or access is denied.

**Expected Output**: JSON object, e.g., {"httpMethod": "GET", "authorizationType": "NONE", "integration": {"type": "HTTP", "uri": "https://example.com"}}.

### Step 3: Analyze the Output for Insights

**Context**: Parse the response to identify risks, such as 'NONE' authorization or mock integrations that might bypass security.

Use `jq` to filter key fields: `aws apigateway get-method ... | jq '.authorizationType, .integration.uri'`.

**Expected Output**: Extracted values highlighting configuration details for manual review or scripting further actions.
