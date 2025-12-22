---
id: c2f91bbe-e227-4f8d-8f32-c9b7788b7604
name: AWS-DynamoDB-Table-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.815899+00:00'
updated_at: '2023-04-10T20:20:03.406928+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/DynamoDB]]'
commands:
  - '[[commands/aws-dynamodb-list-tables]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS-DynamoDB-Table-Enumeration

## Summary

This procedure enumerates all DynamoDB tables within an AWS account or a specified endpoint, enabling attackers to discover data storage resources for potential further exploitation such as data exfiltration or identifying sensitive information stores.

## Description

In cloud environments, DynamoDB serves as a NoSQL database service where tables hold application data. Enumerating these tables reveals the structure and potential targets within the account. This technique leverages the AWS CLI to query the DynamoDB service via the ListTables API, which returns a list of table names. It is particularly useful in compromised AWS environments or lab setups with custom endpoints to map out resources without direct console access. The procedure assumes valid credentials with dynamodb:ListTables permission and can target production AWS or mocked endpoints like those in penetration testing labs.

## Requirements

1. Valid AWS credentials (access key and secret key) with at least `dynamodb:ListTables` permission.
2. AWS CLI installed and configured (version 2 recommended for full feature support).
3. Network access to the DynamoDB endpoint (default: https://dynamodb.us-east-1.amazonaws.com) or a custom endpoint for lab environments.
4. If using a custom endpoint, ensure it mimics the DynamoDB API (e.g., in HackTheBox labs).

## Defense

- Implement least privilege access: Restrict IAM policies to deny `dynamodb:ListTables` unless necessary.
- Enable AWS CloudTrail logging for DynamoDB API calls to detect unauthorized enumeration attempts.
- Use AWS Organizations SCPs to limit discovery actions across accounts.
- Monitor for anomalous CLI usage via AWS GuardDuty or custom CloudWatch alarms on API calls.

## Objectives

1. Retrieve a complete list of DynamoDB table names in the targeted account or endpoint.
2. Identify potential high-value tables for subsequent data access or manipulation.
3. Validate AWS credentials' scope without triggering alerts on more invasive actions.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is installed and credentials are set up to authenticate API calls. This prevents errors during enumeration and confirms permission levels.

If not already configured, run `aws configure` to set your access key, secret key, default region, and output format (json). Test with a simple command like `aws sts get-caller-identity` to verify credentials without listing resources.

**Expected Output**: JSON response showing account details, user ARN, and no permission errors.

### Step 2: Enumerate DynamoDB Tables

**Context**: Use the AWS CLI to invoke the ListTables operation, which queries the DynamoDB service for all table names. Specify a custom endpoint if targeting a lab or mocked service to avoid real AWS charges or detection.

**Command** ([[commands/aws-dynamodb-list-tables]]):
```bash
aws --endpoint-url http://s3.bucket.htb dynamodb list-tables
```

> This command sends a request to the specified endpoint (replace with actual URL if different) and returns a JSON array of table names. The `--endpoint-url` flag overrides the default AWS endpoint for controlled environments. If no tables exist, an empty array is returned. For paginated results in large accounts, add `--max-items` or handle `LastEvaluatedTableName` token in follow-up calls.

**Expected Output**:
```json
{
    "TableNames": [
        "users"
    ]
}
```

### Step 3: Analyze and Document Results

**Context**: Parse the output to identify tables of interest, such as those with names suggesting sensitive data (e.g., 'users', 'credentials'). Pipe the output to jq for filtering if needed.

**Command** (using jq for parsing):
```bash
aws --endpoint-url http://s3.bucket.htb dynamodb list-tables | jq '.TableNames[]'
```

> This extracts individual table names for easier review. Document findings for use in subsequent procedures like table scanning or data exfiltration.

**Expected Output**: List of table names, e.g., "users".

**Success Indicators**:
- JSON response contains a non-empty "TableNames" array.
- No authentication or permission denied errors.
- Table names match expected resources in the target environment.
