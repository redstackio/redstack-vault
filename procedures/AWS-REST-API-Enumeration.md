---
id: 16176625-0362-47b6-a68f-da9036342a44
name: AWS-REST-API-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.325163+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/System Service Discovery|T1007 - System Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud-AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/REST-API-Listing]]'
commands:
  - '[[commands/aws-apigateway-get-rest-apis]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS-REST-API-Enumeration

## Summary

AWS REST API Enumeration is a discovery technique that uses the AWS CLI to query and list all REST APIs deployed in an AWS account via API Gateway. This procedure helps identify exposed API endpoints, which can serve as potential entry points for further reconnaissance or exploitation in cloud environments.

## Description

In AWS, API Gateway manages REST APIs that expose backend services. Enumerating these APIs reveals their IDs, names, descriptions, and creation dates, allowing attackers to map the attack surface during the reconnaissance phase. This is particularly useful in compromised accounts with read access to API Gateway. The technique relies on the AWS CLI tool and requires credentials with permissions like 'apigateway:GET'. Success provides a catalog of APIs for targeting sensitive operations, such as those integrated with Lambda or other services. This procedure assumes a Linux or macOS environment with AWS CLI configured.

## Requirements

1. AWS credentials (access key and secret key) with read permissions on API Gateway (e.g., 'apigateway:GET' policy).
2. AWS CLI installed and configured with the target account's profile.
3. Network access to AWS endpoints (no VPC restrictions blocking API calls).
4. Basic familiarity with JSON output parsing for analysis.

## Defense

- Restrict API Gateway permissions to least privilege; avoid broad 'apigateway:*' access.
- Enable AWS CloudTrail logging for API Gateway to monitor enumeration attempts.
- Use AWS Organizations SCPs to deny listing actions on sensitive APIs.
- Implement API keys or IAM roles for API access and rotate credentials regularly.

## Objectives

1. List all REST APIs in the target AWS account to identify exposed services.
2. Gather metadata (IDs, names, versions) for potential follow-on attacks like API abuse.
3. Validate API Gateway usage and detect misconfigurations in the environment.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Before enumerating APIs, ensure the AWS CLI is installed and authenticated with credentials that have the necessary permissions. This step prevents authentication errors during the query.

Use [[tools/AWS-CLI]] to check configuration:

```bash
aws configure list
```

> This command displays the current profile settings. If not configured, run `aws configure` to set access key, secret key, region (e.g., us-east-1), and output format (json).

**Expected Output**: Profile details including access keys (masked) and default region.

### Step 2: Enumerate REST APIs

**Context**: Query API Gateway to retrieve a list of all REST APIs. This reveals the full inventory without needing additional filters, providing a complete view of deployed APIs.

Execute [[commands/aws-apigateway-get-rest-apis]]:

```bash
aws apigateway get-rest-apis
```

> This command calls the API Gateway service to list APIs. It returns a JSON array with details like id, name, description, createdDate, and version. Pipe to `jq` for better readability if available (e.g., `| jq '.items[] | {id, name, description}'`).

**Expected Output**:

```json
{
    "items": [
        {
            "id": "abc123",
            "name": "MyAPI",
            "description": "Sample REST API",
            "createdDate": 1627849200,
            "version": "v1"
        }
    ]
}
```

### Step 3: Analyze Results

**Context**: Review the output to identify valuable APIs, such as those with public endpoints or sensitive integrations. This step involves manual or scripted parsing to prioritize targets.

Save output to a file and inspect:

```bash
aws apigateway get-rest-apis > apis.json
cat apis.json
```

> Look for APIs with names indicating critical services (e.g., admin, user-data). Note any without descriptions, as they may be overlooked.

**Expected Output**: JSON file with API details; success if 'items' array is non-empty.
