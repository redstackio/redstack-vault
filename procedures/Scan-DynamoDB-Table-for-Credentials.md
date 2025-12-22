---
id: f4503bd6-ad71-4663-9d24-2cbec7ffde73
name: Scan-DynamoDB-Table-for-Credentials
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - '[[sub-techniques/Cloud Services|T1552.005 - Cloud Services]]'
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/DynamoDB]]'
commands:
  - '[[commands/aws-dynamodb-scan-table-for-credentials]]'
platforms:
  - AWS
tools: []
validated: true
---

# Scan-DynamoDB-Table-for-Credentials

## Summary

This procedure demonstrates how to scan an AWS DynamoDB table to extract sensitive credential information, such as usernames and passwords, stored insecurely. It uses the AWS CLI to perform a full table scan and jq to parse the JSON output, targeting scenarios where credentials are embedded in cloud databases without proper encryption or access controls.

## Description

In cloud environments, attackers with compromised AWS credentials or IAM roles may access DynamoDB tables to harvest unsecured credentials. DynamoDB, a NoSQL database service, stores data in items that can include plaintext credentials if not properly secured. This procedure assumes the attacker has permissions to scan the target table (e.g., via an over-privileged IAM role). The technique leverages the AWS SDK or CLI to query the database, retrieving all items and filtering for credential fields. This is particularly effective in misconfigured environments where sensitive data like application secrets or user accounts are stored without encryption. Success allows lateral movement to other AWS resources using the harvested credentials. Note that in production, DynamoDB access should be restricted via IAM policies, and data encrypted at rest.

## Requirements

1. Valid AWS credentials with DynamoDB read permissions (e.g., dynamodb:Scan on the target table).
2. AWS CLI installed and configured with the credentials (via environment variables, ~/.aws/credentials, or IAM role assumption).
3. jq installed for JSON parsing.
4. Network access to the DynamoDB endpoint (or a mocked/local endpoint in lab environments).
5. Knowledge of the target table name containing credential data.

## Defense

- Implement least-privilege IAM policies to restrict Scan operations on DynamoDB tables.
- Enable AWS CloudTrail logging for DynamoDB API calls and monitor for unusual Scan queries.
- Encrypt sensitive attributes in DynamoDB using AWS KMS and avoid storing plaintext credentials.
- Use DynamoDB Streams or AWS Lambda to alert on access to credential-like fields.
- Regularly audit DynamoDB tables for unsecured data with tools like AWS Config or Prowler.

## Objectives

1. Retrieve all items from a specified DynamoDB table.
2. Parse and extract credential fields (e.g., username, password) from the JSON response.
3. Identify usable credentials for further exploitation in the AWS environment.
4. Validate the output to confirm successful credential harvesting without triggering alerts.

## Instructions

### Step 1: Verify AWS CLI Configuration and Permissions

**Context**: Ensure your AWS environment is set up correctly and you have the necessary permissions to scan the target DynamoDB table. This prevents errors during execution and confirms access.

Run a test command to list DynamoDB tables:

**Command** ([[commands/aws-dynamodb-list-tables]]):
```bash
aws dynamodb list-tables --endpoint-url $_ENDPOINT_URL
```

> This command queries the DynamoDB service to list available tables. Replace $_ENDPOINT_URL with the service endpoint (e.g., a local mock like http://localhost:8000 for testing). Expected output is a JSON array of table names. If the command fails with an access denied error, adjust IAM permissions.

### Step 2: Scan the Target Table for Credentials

**Context**: Perform a full scan of the DynamoDB table to retrieve all items, then use jq to filter and display credential fields. This step assumes the table stores credentials as string attributes (e.g., 'username' and 'password'). Scanning reads every item, which can be resource-intensive on large tables.

**Command** ([[commands/aws-dynamodb-scan-table-for-credentials]]):
```bash
aws --endpoint-url $_ENDPOINT_URL dynamodb scan --table-name $_TABLE_NAME | jq -r '.Items[] | {username: .username.S, password: .password.S} // empty'
```

> This invokes the DynamoDB scan operation via AWS CLI, piping the JSON output to jq for selective extraction. The --table-name flag specifies the target table (e.g., 'users'). The jq filter extracts 'username' and 'password' if present as string (S) types, skipping items without them. In a lab or mocked environment, use a custom endpoint like http://s3.bucket.htb. Expected output includes credential pairs; if no credentials are found, the output will be empty. Review for sensitive data and store securely for testing.
