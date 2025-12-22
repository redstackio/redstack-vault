---
id: 7dc6be59-6013-4a49-9ac4-89c069761fe8
name: AWS-API-Gateway-Information-Gathering
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.789208+00:00'
updated_at: '2023-04-10T20:20:15.102544+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Information Discovery]]'
sub_techniques: []
tags:
  - cloud-aws
  - api-discovery
  - information-gathering
commands:
  - '[[commands/aws-apigateway-list-rest-apis]]'
  - '[[commands/aws-apigateway-get-rest-api]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# AWS-API-Gateway-Information-Gathering

## Summary

This procedure uses AWS CLI commands to enumerate and retrieve detailed information about REST APIs configured in Amazon API Gateway. It enables attackers with compromised AWS credentials to map out API structures, endpoints, and configurations, identifying potential entry points for further exploitation such as unauthorized access or injection attacks.

## Description

In cloud environments, Amazon API Gateway serves as a frontend for managing and securing APIs. Attackers often begin discovery by listing available REST APIs to obtain identifiers, then querying specific APIs for details like names, descriptions, endpoint configurations, stages, and resources. This intelligence reveals the API's architecture, helping pinpoint misconfigurations, exposed sensitive endpoints, or integration points with backend services like Lambda or DynamoDB. The procedure assumes the attacker has assumed-role or user credentials with read access to API Gateway (e.g., apigateway:GET permissions). It maps to MITRE ATT&CK's Discovery tactic, focusing on system information discovery in cloud contexts. Success provides a JSON output with API metadata, which can inform subsequent attacks like API abuse or privilege escalation.

## Requirements

1. AWS CLI installed and configured with valid credentials (e.g., access key and secret key) that have read permissions on API Gateway (apigateway:ListRestApis and apigateway:GetRestApi).
2. Network access to AWS endpoints (no VPC endpoints required for public APIs).
3. Basic familiarity with JSON output parsing for analysis.

## Defense

Defensive measures and detection strategies:

- Implement least-privilege IAM policies to restrict apigateway:GET and apigateway:ListRestApis actions to authorized roles only.
- Enable AWS CloudTrail logging for API Gateway to monitor unauthorized queries; alert on anomalous CLI usage from unexpected IPs or user agents.
- Use AWS Organizations SCPs to deny discovery actions in sensitive environments and rotate credentials regularly.

## Objectives

1. Enumerate all REST APIs to identify targets for deeper inspection.
2. Retrieve detailed configuration of a specific API to uncover resources, methods, and potential vulnerabilities.
3. Gather intelligence on API endpoints and integrations for exploitation planning.

## Instructions

### Step 1: List All REST APIs

**Context**: Begin by listing all REST APIs in the account to discover API IDs, names, and creation dates. This step provides an overview of the API landscape without targeting a specific API.

**Command** ([[commands/aws-apigateway-list-rest-apis]]):
```bash
aws apigateway list-rest-apis --query 'items[*].[id,name,createdDate]'
```

> This command queries the API Gateway service for a list of REST APIs. The --query flag filters the JSON response to show only relevant fields (ID, name, creation date) for easier analysis. If the account has many APIs, paginate using --position if needed. Expected output is a JSON array of API summaries; parse it to select an ID for the next step.

### Step 2: Retrieve Specific API Details

**Context**: Using an API ID from Step 1, fetch comprehensive details about the API, including endpoint URL, description, policies, resources, and deployment stages. This reveals the API's structure for vulnerability assessment.

**Command** ([[commands/aws-apigateway-get-rest-api]]):
```bash
aws apigateway get-rest-api --rest-api-id $_REST_API_ID
```

> Replace $_REST_API_ID with the actual ID from Step 1 (e.g., 'a1b2c3d4'). This retrieves the full API configuration as JSON, including binaryMediaTypes, endpointConfiguration, policy (IAM policy document), and tags. Review the 'resources' field for endpoint mappings and 'stages' for deployment info. If the API has custom domains or authorizers, they will appear here, indicating potential weak points like missing authentication.
