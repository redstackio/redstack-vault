---
id: 8c99e625-9683-4352-8fe3-c715fa8e2f82
name: AWS-API-Gateway-Stage-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.885072+00:00'
updated_at: '2023-04-10T20:20:33.329009+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques:
  - '[[sub-techniques/Cloud Account|T1087.004 - Cloud Account]]'
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/API Gateway]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Reconnaissance]]'
commands:
  - '[[commands/aws-apigateway-get-rest-apis]]'
  - '[[commands/aws-apigateway-get-stages]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS-API-Gateway-Stage-Enumeration

## Summary

The AWS API Gateway Stage Enumeration procedure enables attackers with compromised AWS credentials to discover and list deployment stages for REST APIs managed by Amazon API Gateway. Stages represent different deployment environments (e.g., dev, staging, prod) and their configurations, which can reveal outdated versions, custom domain mappings, or misconfigurations that may be exploited for further reconnaissance, persistence, or privilege escalation in cloud environments.

## Description

Amazon API Gateway is a service for creating and managing RESTful APIs at scale. Each REST API can have multiple stages, which are named references to deployments containing configuration details like stage variables, logging settings, and canary deployments. Enumerating stages helps identify potentially vulnerable or legacy deployments, such as those using older API versions susceptible to known exploits or misconfigurations that expose backend services. This technique assumes the attacker has obtained valid AWS credentials (e.g., via unsecured files or stolen tokens) with read access to API Gateway (apigateway:Get permission). It is typically used in post-compromise scenarios to map the target's API infrastructure, supporting broader attack chains like targeting specific stages for injection or data exfiltration. The procedure involves first listing available REST APIs to obtain an API ID, then querying stages for a specific API, providing a complete view of the API lifecycle without alerting basic monitoring if credentials are low-privilege.

## Requirements

1. AWS CLI installed and configured with credentials that have `apigateway:Get` permissions (e.g., read-only access to API Gateway resources).
2. Network access to AWS endpoints (no VPC restrictions blocking CLI calls).
3. Knowledge of the target AWS region where the API Gateway is deployed (default is us-east-1 if unspecified).
4. Optional: jq installed for parsing JSON output if manual analysis is needed.

## Defense

- Implement least-privilege IAM policies to restrict `apigateway:Get*` actions to necessary roles only.
- Enable AWS CloudTrail logging for API Gateway and monitor for unusual `GetStages` or `GetRestApis` calls from unexpected IPs or users.
- Rotate access keys regularly and use temporary credentials via STS to limit exposure.
- Use AWS Config to audit API stages for compliance and alert on enumeration patterns.

## Objectives

1. Discover all REST APIs in the target AWS account to identify API Gateway usage.
2. Enumerate stages for a specific API to map deployments, versions, and configurations.
3. Identify potential vulnerabilities in outdated or misconfigured stages for follow-on exploitation.

## Instructions

### Step 1: List All REST APIs to Obtain API ID

**Context**: Before enumerating stages, identify the target REST API by listing all APIs in the region. This step reveals API names and IDs, allowing selection of the relevant API for stage enumeration. Use this if the API ID is unknown; it requires `apigateway:Get` permission.

**Command** ([[commands/aws-apigateway-get-rest-apis]]):
```bash
aws apigateway get-rest-apis --region $_AWS_REGION
```

> This command queries AWS for a JSON list of REST APIs. Replace `$_AWS_REGION` with the target region (e.g., us-west-2). If successful, parse the output to note the `id` of the desired API (e.g., via `jq '.items[] | {id: .id, name: .name}'`). This step confirms API existence and provides the prerequisite ID for the next step.

### Step 2: Enumerate Stages for the Specific REST API

**Context**: Using the API ID from Step 1, retrieve details on all stages associated with that API. This exposes stage names, deployment IDs, variables, and descriptions, which can indicate production vs. development environments or legacy setups vulnerable to exploits.

**Command** ([[commands/aws-apigateway-get-stages]]):
```bash
aws apigateway get-stages --rest-api-id $_REST_API_ID --region $_AWS_REGION
```

> Execute this to get a paginated JSON response listing stages. The `$_REST_API_ID` is required (from Step 1 output), and `$_AWS_REGION` ensures region-specific results. Success is indicated by a 200 OK response with an `item` array containing stage objects (e.g., `{ "stageName": "prod", "deploymentId": "abc123", "variables": { "env": "production" } }`). Review for sensitive variables or old deployments; if no stages exist, the API may be unused or in error state—retry with correct ID.

### Step 3: Analyze Output for Vulnerabilities

**Context**: Post-enumeration, manually or script-based analysis identifies actionable insights. This decision point checks for indicators like unsecured variables or multiple stages pointing to the same backend, which could enable targeted attacks.

**Instructions**: Pipe the output from Step 2 to jq for filtering (e.g., `aws apigateway get-stages ... | jq '.item[] | select(.stageName == "prod")'`). If variables contain secrets (e.g., database endpoints), note for exfiltration. If stages reference old deployments, cross-reference with known CVEs for API Gateway versions.

> No specific command here, but use built-in AWS CLI output. Expected: Filtered JSON highlighting key stages. If analysis reveals issues, proceed to related procedures like backend enumeration; otherwise, the API is hardened.
