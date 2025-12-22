---
id: f6144f1b-160c-41be-9b4e-4cad22af5b9b
name: AWS-API-Key-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.488492+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud-Service-Discovery|T1526 - Cloud Service Discovery]]'
  - '[[techniques/Data-from-Cloud-Storage|T1530 - Data from Cloud Storage]]'
sub_techniques: []
tags:
  - cloud-aws
  - enumeration
  - api-keys
commands:
  - '[[commands/aws-apigateway-get-api-keys-including-values]]'
platforms:
  - AWS
  - Cloud
tools: []
validated: true
---

# AWS API Key Enumeration

## Summary

AWS API Key Enumeration is a procedure to discover and extract API keys associated with an AWS account, particularly those linked to Amazon API Gateway. This technique allows attackers with initial access to AWS credentials to identify usable keys for further unauthorized actions, such as accessing APIs or escalating privileges in cloud environments.

## Description

In cloud environments like AWS, API keys serve as credentials for accessing services such as API Gateway. Once an attacker gains initial foothold through compromised IAM credentials, they can enumerate these keys to map out accessible resources. This procedure leverages the AWS CLI to query API Gateway directly, revealing key IDs, values, and associated details. It is typically used in post-compromise scenarios to collect credentials for lateral movement or data exfiltration. The approach assumes the attacker has IAM permissions like `apigateway:GET` on API keys. Success enables chaining to other attacks, like invoking protected APIs or stealing data from connected services.

## Requirements

1. Valid AWS credentials (IAM user/role) with permissions to list API keys (e.g., `apigateway:ListApiKeys`, `apigateway:GetApiKey`).
2. AWS CLI installed and configured with the compromised credentials (via `aws configure` or environment variables).
3. Access to an environment where AWS CLI can reach the API Gateway service (no network blocks on outbound HTTPS to AWS endpoints).
4. Basic familiarity with JSON output parsing for key extraction.

## Defense

- Implement least privilege access by granting IAM users and roles only the permissions they need, avoiding broad `apigateway:*` rights.
- Enable AWS CloudTrail for API Gateway and monitor logs for `GetApiKeys` or `ListApiKeys` calls from unusual sources.
- Regularly rotate API keys and store them securely using AWS Secrets Manager or Parameter Store, avoiding hardcoding in configurations.
- Use AWS IAM Access Analyzer to identify and revoke unused or over-privileged API keys.
- Enable MFA for IAM users and monitor for anomalous credential usage via AWS GuardDuty.

## Objectives

1. Discover all API keys associated with the AWS account in API Gateway.
2. Extract key values for potential reuse in further attacks.
3. Identify associated metadata (e.g., enabled status, stages) to assess usability.
4. Validate key functionality without alerting defenders.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is set up with the compromised credentials to authenticate requests to AWS services. This step confirms access before enumeration to avoid errors.

Run `aws sts get-caller-identity` to verify the current identity and permissions.

**Expected Output**: JSON response showing Account ID, User ARN, and role details, confirming authenticated session.

If output shows the expected identity, proceed; otherwise, update credentials via `aws configure`.

### Step 2: Enumerate API Keys

**Context**: Use the AWS CLI to query API Gateway for all API keys, including their secret values. This retrieves a list of keys that can be used for API access.

**Command** ([[commands/aws-apigateway-get-api-keys-including-values]]):
```bash
aws apigateway get-api-keys --include-values
```

> This command calls the API Gateway service to list all keys. The `--include-values` flag exposes the sensitive key strings, which are normally hidden. Pipe output to `jq` for easier parsing if available (e.g., `| jq '.items[] | {id: .id, value: .value, enabled: .enabled}'`).

**Expected Output**: JSON array of API key objects, each containing `id`, `value` (the secret key), `enabled` status, `stageKeys`, and `createdDate`. Example:
```
{
    "items": [
        {
            "id": "abc123def456",
            "value": "sk-abc123XYZ789...",
            "enabled": true,
            "stageKeys": {...},
            "createdDate": 1696118400
        }
    ]
}
```

### Step 3: Parse and Validate Keys

**Context**: Extract and test the discovered keys to confirm usability. This involves saving keys to a file and optionally testing against an API endpoint.

Save the output to a file: `aws apigateway get-api-keys --include-values > api_keys.json`. Then, extract values using `jq` or manual inspection.

To validate, use a key in an API call, e.g., `curl -H "x-api-key: <key_value>" https://<api_id>.execute-api.<region>.amazonaws.com/<stage>/`.

**Expected Output**: For valid keys, API responses (e.g., 200 OK or expected data); for invalid, 403 Forbidden or authentication errors.

If keys are enabled and return data, they are viable for further exploitation; disable or rotate them post-enumeration if simulating defense.
