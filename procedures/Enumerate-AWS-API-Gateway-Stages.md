---
id: 94c9f495-f3be-4a34-bdd2-74918c82ec5f
name: Enumerate-AWS-API-Gateway-Stages
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.442138+00:00'
updated_at: '2023-04-10T20:20:45.313831+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Service Discovery]]'
sub_techniques: []
tags:
  - cloud-aws
  - enumeration
  - api-gateway-stages
commands:
  - '[[commands/aws-apigateway-get-stages]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Enumerate-AWS-API-Gateway-Stages

## Summary

This procedure uses the AWS CLI to retrieve a list of all stages associated with a specified API Gateway REST API. Stages represent different deployment versions or environments (e.g., dev, staging, prod) of the API, allowing attackers to identify potentially vulnerable configurations or outdated versions for further exploitation in cloud environments.

## Description

AWS API Gateway enables the creation and management of REST APIs at scale. Each API can have multiple stages, which are essentially named references to deployments, each potentially running different versions of the API logic. Enumerating stages reveals deployment IDs, stage names, and associated URLs, which can expose misconfigurations, deprecated versions susceptible to known vulnerabilities, or paths for privilege escalation through API interactions. This technique is particularly useful in AWS discovery phases where an attacker has compromised credentials, as it maps the API landscape without direct API calls that might trigger alerts. The procedure assumes the attacker has the REST API ID, which can be obtained via prior enumeration of APIs using AWS CLI or console access.

## Requirements

1. Valid AWS credentials with permissions to call `apigateway:GetStages` (e.g., attached to a role or IAM user with API Gateway read access).
2. AWS CLI installed and configured with the target account's credentials (via `aws configure` or environment variables).
3. The REST API ID for the target API Gateway REST API.
4. Network access to AWS endpoints (no VPC restrictions blocking CLI calls).

## Defense

- Implement least-privilege IAM policies to restrict `apigateway:GetStages` and related actions to only necessary roles.
- Enable AWS CloudTrail logging for API Gateway to monitor CLI and SDK calls, alerting on unusual enumeration patterns.
- Use AWS Config rules to audit API stages regularly and rotate or deprecate unused/vulnerable stages.
- Integrate with SIEM tools to detect anomalous AWS CLI usage from unexpected IPs or user agents.

## Objectives

1. Retrieve a complete list of stages for a given AWS API Gateway REST API.
2. Identify stage names, deployment IDs, and URLs to map API versions and potential attack surfaces.
3. Detect misconfigurations or outdated deployments that could lead to exploitation.

## Instructions

### Step 1: Verify AWS CLI Configuration and Permissions

**Context**: Before enumerating stages, ensure the AWS CLI is set up with credentials that have the required permissions. This step prevents authentication errors and confirms access to the target account.

Run `aws sts get-caller-identity` to verify your identity and permissions.

**Command** ([[commands/aws-sts-get-caller-identity]]):
```bash
aws sts get-caller-identity
```

> This command outputs your AWS account ID, user ARN, and session details. If it fails with an access denied error, update your IAM policy to include `apigateway:GetStages`.

**Expected Output**:
```json
{
  "UserId": "AIDAXYZ...",
  "Account": "123456789012",
  "Arn": "arn:aws:iam::123456789012:user/example-user"
}
```

### Step 2: Enumerate API Gateway Stages

**Context**: With the REST API ID known (e.g., from prior API listing via `aws apigateway get-rest-apis`), use this step to fetch all stages. This reveals version-like deployments, enabling targeted attacks on weaker stages.

**Command** ([[commands/aws-apigateway-get-stages]]):
```bash
aws apigateway get-stages --rest-api-id $_REST_API_ID
```

> Replace `$_REST_API_ID` with the actual API ID (e.g., `a1b2c3d4e5`). The command queries the API Gateway service and returns a JSON array of stages. If no stages exist, it returns an empty list—indicating a potentially new or unconfigured API worth monitoring.

**Expected Output**:
```json
{
  "item": [
    {
      "stageName": "prod",
      "deploymentId": "abc123",
      "cacheClusterEnabled": false,
      "cacheClusterStatus": "AVAILABLE",
      "description": "Production deployment",
      "documentationVersion": "v1"
    },
    {
      "stageName": "dev",
      "deploymentId": "def456",
      "cacheClusterEnabled": true,
      "cacheClusterStatus": "AVAILABLE",
      "description": "Development stage",
      "documentationVersion": "v0.5"
    }
  ]
}
```

**Success Indicators**:
- JSON response contains an "item" array with stage details.
- No errors like "AccessDeniedException" or "InvalidApiIdException".
