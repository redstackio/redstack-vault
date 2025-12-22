---
id: ac24dbd6-aefd-4aa9-b3b3-d8f2bd1db0fc
name: List-AWS-API-Gateway-REST-APIs
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.768423+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/API-Gateway]]'
  - '[[tags/Discovery]]'
commands:
  - '[[commands/aws-apigateway-list-rest-apis]]'
platforms:
  - AWS
tools: []
validated: true
---

# List-AWS-API-Gateway-REST-APIs

## Summary

This procedure uses the AWS CLI to enumerate all REST APIs deployed in an AWS account via API Gateway. It provides attackers with visibility into exposed APIs, which can reveal application endpoints, integration points, and potential attack surfaces for further exploitation in cloud environments.

## Description

In an AWS environment, API Gateway manages REST APIs that serve as entry points for applications, microservices, and integrations. Listing these APIs allows discovery of active services, their names, descriptions, and endpoints without needing additional permissions beyond read access to API Gateway. This technique is commonly used during reconnaissance to map the target's cloud infrastructure, identify misconfigurations, or find APIs that may be vulnerable to injection, authentication bypass, or unauthorized access. The procedure assumes the attacker has obtained valid AWS credentials (e.g., via IAM role compromise or access key theft) and the AWS CLI configured with those credentials. Successful execution returns a JSON list of APIs, enabling prioritization of targets based on names or descriptions hinting at sensitive functions like admin panels or data exports.

## Requirements

1. Valid AWS credentials with at least `apigateway:GET` permissions on the API Gateway service.
2. AWS CLI installed and configured with the target account's access key, secret key, and default region (e.g., `us-east-1`).
3. Network access to AWS endpoints (no VPC restrictions blocking CLI calls).

## Defense

- Implement least-privilege IAM policies to restrict `apigateway:GET` actions to necessary roles only.
- Enable AWS CloudTrail logging for API Gateway to monitor and alert on enumeration attempts.
- Use AWS Organizations SCPs to deny listing actions across accounts and integrate with SIEM for anomaly detection on API calls from unusual sources.

## Objectives

1. Enumerate all REST APIs in the target AWS account to identify potential entry points.
2. Gather metadata on API names, IDs, and endpoints for infrastructure mapping.
3. Support subsequent attacks like API abuse or chaining to other cloud services.

## Instructions

### Step 1: Configure AWS CLI and Execute List Command

**Context**: Ensure the AWS CLI is set up with the compromised credentials, then run the command to retrieve the list of REST APIs. This step requires no additional arguments as it queries the default region associated with the credentials.

**Command** ([[commands/aws-apigateway-list-rest-apis]]):
```bash
aws apigateway get-rest-apis
```

> This command queries the API Gateway service and returns a JSON array of all REST APIs. Review the output for API IDs, names, descriptions, and endpoint configurations to identify high-value targets. If the account spans multiple regions, repeat the command with `--region` flags for each (e.g., `aws apigateway get-rest-apis --region us-west-2`).

### Step 2: Parse and Analyze Output

**Context**: The JSON response may be verbose; pipe it to tools like `jq` for filtering or export to a file for offline analysis. This helps in quickly spotting APIs related to sensitive operations.

**Command**:
```bash
aws apigateway get-rest-apis | jq '.items[] | {id: .id, name: .name, description: .description}'
```

> Expected output is a filtered list of API metadata. Look for keywords like "admin", "internal", or integrations with S3/Lambda that could indicate escalation paths.
