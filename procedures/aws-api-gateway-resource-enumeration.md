---
type: procedure
description: >-
  Enumerate resources and endpoints in an AWS API Gateway to identify potential
  targets for exploitation.
verified: true
submitted: false
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Discovery]]'
  - '[[tags/API Gateway]]'
commands:
  - '[[commands/aws-apigateway-get-resources]]'
tools:
  - '[[tools/aws-cli]]'
platforms:
  - AWS
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# AWS API Gateway Resource Enumeration

## Summary

This procedure uses the AWS CLI to retrieve a list of all resources and endpoints associated with a specified API Gateway REST API. It enables attackers or security testers to map out the structure of the API, identifying potential entry points for further exploitation such as exposed backend services or misconfigured integrations.

## Description

In cloud environments, AWS API Gateway serves as a front door for serverless applications and backend services. Enumerating its resources reveals the paths, methods, and integrations available, which can expose sensitive endpoints or allow for deeper reconnaissance. This technique is particularly useful during initial discovery phases to understand the attack surface without direct interaction with the API itself. The process involves querying the AWS management API with appropriate credentials, parsing the JSON response to extract resource IDs, paths, and HTTP methods. Success depends on having read access to the API Gateway service, and it assumes the target REST API ID is known (often obtained via prior enumeration of API lists).

## Requirements

1. Valid AWS credentials with at least `apigateway:GET` permissions on the target REST API.
2. AWS CLI installed and configured with the credentials (via `aws configure`).
3. Network access to AWS endpoints (no VPC restrictions blocking API calls).
4. Knowledge of the target REST API ID (e.g., from listing APIs with `aws apigateway get-rest-apis`).

## Defense

- Enforce least privilege access: Limit IAM policies to deny `apigateway:GetResources` unless necessary.
- Enable AWS CloudTrail logging for API Gateway to monitor unauthorized enumeration attempts.
- Use API keys or resource policies to restrict access to specific APIs.
- Implement anomaly detection on unusual API management calls from unexpected sources.

## Objectives

1. Map out all resources, paths, and methods in the target API Gateway.
2. Identify potentially vulnerable or exposed endpoints for follow-on attacks.
3. Gather intelligence on backend integrations without triggering application-level alerts.

## Instructions

### Step 1: Verify AWS CLI Configuration and Permissions

**Context**: Ensure your AWS environment is set up correctly and you have the necessary permissions to query API Gateway. This prevents errors during execution and confirms access.

Run `aws sts get-caller-identity` to verify your identity and permissions.

**Command** ([[commands/aws-sts-get-caller-identity]]):
```bash
aws sts get-caller-identity
```

> This command returns your AWS account details. If it fails with an access denied error, update your IAM policy to include `apigateway:GetResources`.

**Expected Output**:
```json
{
    "UserId": "AIDAXYZ...",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/test-user"
}
```

### Step 2: Retrieve API Gateway Resources

**Context**: Use the AWS CLI to fetch the list of resources for the specified REST API. Replace the REST API ID with the actual value (e.g., obtained from prior API listing). This step extracts the hierarchical structure of paths and methods, providing a blueprint of the API.

**Command** ([[commands/aws-apigateway-get-resources]]):
```bash
aws apigateway get-resources --rest-api-id $_REST_API_ID
```

> The `--rest-api-id` parameter specifies the unique ID of the target REST API. Pipe the output to `jq` for better readability if available (e.g., `| jq '.items[] | {id: .id, path: .path}'`). Review the response for paths like `/users` or `/admin` that may indicate sensitive resources.

**Expected Output**:
```json
{
    "items": [
        {
            "id": "abc123",
            "path": "/",
            "parentId": null
        },
        {
            "id": "def456",
            "path": "/users",
            "parentId": "abc123"
        }
    ]
}
```

### Step 3: Parse and Analyze the Output

**Context**: Manually or script the response to identify key resources. Look for non-standard paths, integration types (e.g., Lambda or HTTP), and potential injection points. This step verifies the enumeration and prepares for next actions like testing endpoints.

Save the output to a file for analysis:
```bash
aws apigateway get-resources --rest-api-id $_REST_API_ID > resources.json
```

> Use tools like `jq` to filter: `jq '.items[] | select(.path | contains("/admin"))' resources.json`. Document any discovered paths for inclusion in attack planning.

**Expected Output**: Filtered list of interesting resources, e.g., paths with administrative or data-access implications.

**Success Indicators**:
- JSON response contains `items` array with resource details.
- No permission errors; paths match expected API structure.
- Identification of at least one potentially exploitable endpoint.
