---
id: 33424625-7a38-4703-8103-b4a286ec68c9
name: AWS-API-Gateway-Resource-Listing
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.834650+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - cloud-aws
  - api-gateway
  - discovery
commands:
  - '[[commands/aws-apigateway-get-resource]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS-API-Gateway-Resource-Listing

## Summary

The AWS API Gateway Resource Listing procedure retrieves detailed information about a specific resource within an Amazon API Gateway REST API using the AWS CLI. This technique is commonly used in cloud discovery phases to map out API structures, identify potential entry points, and detect misconfigurations that could expose sensitive endpoints or enable further lateral movement in an AWS environment.

## Description

In offensive security operations, listing API Gateway resources helps attackers understand the architecture of serverless APIs, revealing paths, methods, and integrations that might be exploitable. For instance, discovering unsecured resources could lead to unauthorized access to backend services like Lambda functions or DynamoDB. Defensively, this procedure aids in auditing configurations to ensure resources are properly permissioned. The process relies on AWS Identity and Access Management (IAM) permissions for the API Gateway service and assumes the attacker has valid credentials with read access. It targets REST APIs specifically, returning metadata such as resource IDs, parent IDs, and path parts, which can be chained with other discovery techniques like listing all APIs or resources.

## Requirements

1. Valid AWS credentials with `apigateway:GET` permissions on the target REST API.
2. AWS CLI version 2 or later installed and configured with the appropriate profile.
3. Network connectivity to AWS endpoints (no VPC endpoints required for public APIs).
4. Knowledge of the REST API ID and the specific resource ID to query.

## Defense

- Implement least-privilege IAM policies to restrict `apigateway:GET` actions to necessary roles only.
- Enable AWS CloudTrail logging for API Gateway to monitor and alert on resource listing attempts.
- Use AWS Config rules to detect overly permissive API Gateway configurations and enforce resource-level access controls.
- Regularly rotate credentials and monitor for anomalous API calls via Amazon GuardDuty.

## Objectives

1. Retrieve metadata for a specific API Gateway resource to map API structures.
2. Identify potential misconfigurations or exposed endpoints in the AWS environment.
3. Support broader cloud discovery by providing details for chaining to other API explorations.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure your AWS CLI is set up with credentials that have the required permissions to avoid authentication errors during execution.

Run the following to test configuration:

```bash
aws sts get-caller-identity
```

> This command verifies your identity and permissions. If it fails, update your credentials using `aws configure`.

**Expected Output**: JSON response showing your AWS account, user ARN, and session details.

### Step 2: Retrieve the API Gateway Resource

**Context**: Use the AWS CLI to query the specific resource, providing the REST API ID and resource ID obtained from prior enumeration (e.g., via listing all resources).

**Command** ([[commands/aws-apigateway-get-resource]]):

```bash
aws apigateway get-resource --rest-api-id $_REST_API_ID --resource-id $_RESOURCE_ID
```

> This fetches the resource details. Replace placeholders with actual values: $_REST_API_ID is the unique identifier of the REST API (e.g., 'a1b2c3d4'), and $_RESOURCE_ID is the resource's ID (e.g., 'abc123'). If the resource exists and permissions allow, it returns JSON metadata.

**Expected Output**: JSON object with fields like `id`, `parentId`, `pathPart`, `path`, and `resourceMethods` indicating the resource's structure and associated methods.

### Step 3: Parse and Analyze Output

**Context**: Review the output to identify key details such as path segments or integrated methods, which can inform further attacks like method enumeration.

Use `jq` for parsing if available:

```bash
aws apigateway get-resource --rest-api-id $_REST_API_ID --resource-id $_RESOURCE_ID | jq '.path'
```

> This extracts the full path for quick analysis. Look for sensitive paths (e.g., /admin) or unusual integrations.

**Expected Output**: Extracted path string, e.g., "/users/{userId}", confirming the resource's endpoint structure.
