---
id: c787ad8a-31a8-4cbc-9c44-48f9c1dc85e6
name: Enumerate-AWS-Key-Owner-and-Gain-Initial-Access
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.403953+00:00'
updated_at: '2023-04-10T20:20:31.956911+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud-Service-Dashboard|T1538 - Cloud Service Dashboard]]'
sub_techniques: []
tags:
  - '[[tags/5. Exploitation Scenario]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumerating the owner of the key and initial compromise]]'
  - aws
  - cloud
  - discovery
commands:
  - '[[commands/aws-sts-get-caller-identity]]'
platforms:
  - AWS
  - Cloud
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Enumerate-AWS-Key-Owner-and-Gain-Initial-Access

## Summary

This procedure enumerates the owner and account details associated with a compromised AWS access key using the AWS Security Token Service (STS) API, then uses the obtained credentials to access the AWS Management Console for initial compromise. It allows attackers to identify the target account, verify permissions, and establish a foothold in the cloud environment by logging into the console to perform further actions like resource enumeration or modification.

## Description

In cloud environments like AWS, attackers often obtain access keys through misconfigurations, leaks, or prior compromises. This procedure starts by querying the STS GetCallerIdentity API to retrieve the AWS account ID, user ARN, and associated identity details, revealing the key's owner without alerting typical monitoring if permissions allow. If the key has console access permissions, the attacker can then authenticate to the AWS Management Console using the identified credentials. This technique targets the AWS dashboard for discovery and initial access, enabling subsequent actions such as creating backdoor resources or exfiltrating data. It assumes the attacker has valid AWS credentials (access key ID and secret access key) and is applicable in scenarios where keys are exposed in code repositories, logs, or unsecured applications.

## Requirements

1. Valid AWS access key ID and secret access key (compromised or leaked).
2. Network access to AWS API endpoints (e.g., sts.amazonaws.com) over HTTPS.
3. AWS CLI installed and configured with the target credentials, or equivalent SDK/tool for API interaction.
4. For console access: The key must be associated with an IAM user or role that has console login permissions (e.g., no MFA required initially).

## Defense

- Implement least privilege access for IAM users and keys, revoking unused or overly permissive credentials.
- Enable AWS CloudTrail logging for STS API calls and console sign-ins to detect anomalous identity queries.
- Enforce multi-factor authentication (MFA) for all console logins and monitor for failed or unusual access patterns.
- Use key rotation policies and avoid embedding keys in code or public repositories; leverage IAM roles instead of long-term keys.

## Objectives

1. Retrieve the AWS account ID, user ARN, and identity details tied to the access key.
2. Verify if the credentials allow access to the AWS Management Console.
3. Establish initial interactive access to the AWS account for further compromise.
4. Identify opportunities for persistence or lateral movement within the cloud environment.

## Instructions

### Step 1: Query AWS STS for Caller Identity

**Context**: Use the AWS CLI to call the STS GetCallerIdentity API, which returns details about the account and principal associated with the current credentials. This step enumerates the key owner without requiring additional permissions beyond the key itself. Ensure AWS CLI is configured with the target access key and secret via environment variables or profile.

**Command** ([[commands/aws-sts-get-caller-identity]]):
```bash
aws sts get-caller-identity --profile target-profile
```

> This command outputs a JSON response with the Account field (account ID), UserId, and Arn (including the IAM user or role name). Review the Arn to identify the key owner, such as an IAM user in a specific account. If the response includes a role ARN, note potential assumed role scenarios. Success is indicated by a 200 OK response without permission errors; errors like InvalidClientTokenId suggest invalid keys.

### Step 2: Verify Console Access Permissions

**Context**: Based on the identity details from Step 1, check if the credentials support console login by attempting authentication. This involves manual steps but confirms if the enumerated user/role has the necessary policies (e.g., aws-portal:ViewBilling). If MFA is enabled, additional tokens may be required, but for initial compromise, assume no MFA or bypassed.

**Instructions**: Export the access key and secret to AWS CLI profile if not already done:
```bash
aws configure set aws_access_key_id AKIA... --profile target-profile
aws configure set aws_secret_access_key ... --profile target-profile
```
Then, generate a sign-in token using the CLI (if supported) or proceed to manual login.

> Expected: No errors in credential setup. If the user has console permissions, proceed to login; otherwise, the procedure stops here, and alternative API-only access is used for further enumeration.

### Step 3: Access AWS Management Console

**Context**: Use the enumerated credentials to log into the AWS Console, establishing an interactive session for dashboard access. This step compromises the account by allowing navigation to services like EC2, S3, or IAM for deeper exploitation.

**Instructions**: 
1. Navigate to https://signin.aws.amazon.com/console in a web browser.
2. Select 'Security credentials' or 'IAM user' sign-in (based on ARN from Step 1).
3. Enter the account ID (from Step 1), IAM username (parsed from ARN), and prefix 'AWS'.
4. Use the access key ID as username and secret as password (for programmatic access keys with console perms).
5. If successful, you'll land on the console dashboard.

> Expected: Redirect to the AWS Management Console with access to services based on the user's policies. Look for the console URL in the address bar confirming the account ID. Success indicators include viewing resources without access denied errors.
