---
id: 08c48dca-cb91-4932-92d5-2905f9763385
type: command
executor: bash
data: >-
  aws kms get-key-policy --key-id $_KEY_ID --policy-name $_POLICY_NAME --region
  $_REGION --output json
output: null
created_at: '2023-04-06T03:56:12.429535+00:00'
updated_at: '2023-04-10T20:20:53.424763+00:00'
platforms:
  - AWS
tags:
  - kms
  - policy
  - discovery
verified: true
validated: true
---

# AWS KMS Get Key Policy

## Command

```bash
aws kms get-key-policy --key-id $_KEY_ID --policy-name $_POLICY_NAME --region $_REGION --output json
```

## Description

This command retrieves the named policy for the specified KMS key in JSON format. It is used to inspect access controls on encryption keys, helping identify permissions for users, roles, or services. Run this after identifying a key ID via listing commands.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --key-id $_KEY_ID | The unique ID or ARN of the KMS key (e.g., 1234abcd-12ab-34cd-56ef-1234567890ab) | Yes |
| --policy-name $_POLICY_NAME | The name of the policy (default: 'default') | Yes |
| --region $_REGION | The AWS region where the key resides (e.g., us-east-1) | Yes |
| --output json | Format the output as JSON for easy parsing | No |

## Examples

### Basic Usage

```bash
aws kms get-key-policy --key-id 1234abcd-12ab-34cd-56ef-1234567890ab --policy-name default --region us-east-1
```

### Advanced Usage (with JSON Parsing)

```bash
aws kms get-key-policy --key-id 1234abcd-12ab-34cd-56ef-1234567890ab --policy-name default --region us-east-1 --output json | jq '.Policy'
```

## Expected Output

Successful execution returns a JSON object with KeyId, PolicyName, and Policy (a JSON string of the policy document). Example:

```json
{
  "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
  "PolicyName": "default",
  "Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"Enable IAM User Permissions\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::123456789012:root\"},\"Action\":\"kms:*\",\"Resource\":\"*\"}]}"
}
```

Parse the Policy field to view statements granting permissions like kms:Decrypt to specific IAM roles.

## Related

- [[commands/aws-kms-list-keys]]
- [[procedures/retrieve-aws-kms-key-policy]]
