---
id: 5c4deba9-6179-4a73-87de-b37f580269cb
name: Enumerate-AWS-API-Gateway-REST-APIs
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.348603+00:00'
updated_at: '2023-04-10T20:20:51.266590+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Remote System Discovery|T1018 - Remote System Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/API Enumeration]]'
commands:
  - '[[commands/aws-apigateway-get-rest-api]]'
platforms:
  - AWS
tools: []
validated: true
---

# Enumerate-AWS-API-Gateway-REST-APIs

## Summary

This procedure uses the AWS CLI to retrieve detailed information about a specific REST API in Amazon API Gateway, enabling attackers to map the target's API structure, identify resources, stages, and potential misconfigurations for further exploitation in cloud environments.

## Description

In an AWS environment, enumerating API Gateway REST APIs allows an attacker with valid credentials to gather intelligence on deployed APIs, including their names, descriptions, endpoint configurations, and associated resources. This discovery technique is useful during reconnaissance or lateral movement phases to uncover exposed endpoints that may lead to unauthorized access, data exfiltration, or privilege escalation. The procedure relies on the AWS API Gateway service and requires authenticated access via AWS CLI. It helps identify vulnerabilities such as overly permissive API policies or unmonitored stages.

## Requirements

1. Valid AWS credentials with read access to API Gateway (e.g., `apigateway:GET` permissions).
2. AWS CLI installed and configured with the target account's credentials (via `aws configure`).
3. The REST API ID, which can be obtained from prior enumeration (e.g., listing APIs with `aws apigateway get-rest-apis`).
4. Network access to AWS endpoints (no specific ports beyond standard HTTPS/443).

## Defense

- Implement least-privilege access controls using IAM policies to restrict `apigateway:GET` actions on sensitive APIs.
- Enable AWS CloudTrail logging for API Gateway to monitor and alert on unauthorized enumeration attempts.
- Use API keys or resource policies to limit unauthenticated access to API details.
- Regularly audit API configurations with AWS Config rules to detect exposed or misconfigured APIs.

## Objectives

1. Retrieve comprehensive details on a target REST API to map its structure and resources.
2. Identify potential misconfigurations, such as public endpoints or weak authorization, for exploitation.
3. Gain insights into the target's API deployment to support further attacks like API abuse or chaining to other AWS services.

## Instructions

### Step 1: Retrieve REST API Details

**Context**: Use the AWS CLI to query the API Gateway service for details on a specific REST API. This step requires knowing the API's unique ID, which uniquely identifies the API in the region. The output provides JSON data on the API's metadata, helping to understand its scope and configuration.

**Command** ([[commands/aws-apigateway-get-rest-api]]):
```bash
aws apigateway get-rest-api --rest-api-id $_REST_API_ID
```

> This command fetches the API's ID, name, description, creation date, endpoint configuration (e.g., regional or edge-optimized), binary media types, and minimum compression size. Replace `$_REST_API_ID` with the actual API ID (e.g., `a1b2c3d4`). If the API ID is invalid or access is denied, an error will be returned. Success is indicated by a JSON response with the API's `id` and `name` fields populated.

### Step 2: Parse and Analyze Output

**Context**: Review the JSON output to extract key information like resources, stages, and policies. This manual step helps identify actionable intelligence, such as deployable stages or resource paths that could be targeted next.

**Command** (Use standard JSON tools like `jq` for parsing):
```bash
aws apigateway get-rest-api --rest-api-id $_REST_API_ID | jq '.name, .description, .endpointConfiguration'
```

> Pipe the output to `jq` (if available) to filter relevant fields. Expected output includes the API name, description, and endpoint type. Look for indicators like `cloneOf` (if cloned) or policy attachments that suggest inheritance or broader access.
