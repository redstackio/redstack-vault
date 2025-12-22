---
id: 8bdd9ade-059b-40f8-930f-e22ac8355354
name: AWS-Credential-Testing
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.690027+00:00'
updated_at: '2023-04-10T20:20:56.173241+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
tags:
  - '[[tags/5. Exploitation Scenario]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Persistence & Backdooring]]'
  - '[[tags/Testing the credential]]'
commands:
  - '[[commands/aws-sts-get-caller-identity]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS-Credential-Testing

## Summary

The AWS Credential Testing procedure validates the authenticity of AWS access keys or IAM role credentials by querying the Security Token Service (STS) for caller identity information. This technique is commonly used by attackers to confirm the usability of stolen or brute-forced credentials before escalating to further exploitation, such as enumerating resources or assuming roles within the AWS environment.

## Description

In an attack scenario, credentials may be obtained through phishing, misconfigurations, or brute-force attempts against exposed endpoints. This procedure leverages the 'aws sts get-caller-identity' command to retrieve metadata about the authenticated IAM user or role, including the account ID, ARN, and user ID. A successful response indicates valid credentials, enabling the attacker to proceed with actions like listing S3 buckets or launching EC2 instances. The process can be automated in scripts to test batches of credentials efficiently. This is particularly effective in cloud environments where credentials are long-lived and often over-privileged, leading to potential data exfiltration or persistence.

## Requirements

1. AWS CLI installed and configured with the credentials to test (via environment variables, ~/.aws/credentials file, or IAM role assumption).
2. Network access to AWS STS endpoints (typically over HTTPS on port 443).
3. Basic knowledge of AWS IAM concepts, such as access keys and profiles.

## Defense

- Implement least-privilege access for IAM users and roles to limit damage from compromised credentials.
- Enable AWS CloudTrail logging to monitor STS API calls and detect anomalous credential usage patterns.
- Use credential rotation policies and integrate with identity federation to avoid static long-term keys.
- Monitor for unusual 'GetCallerIdentity' calls from unexpected IP addresses or user agents via AWS GuardDuty.

## Objectives

1. Verify if provided AWS credentials are valid and active.
2. Retrieve identity metadata to assess the scope of access (e.g., user vs. role, account details).
3. Identify viable credentials for subsequent AWS resource enumeration or exploitation.

## Instructions

### Step 1: Configure AWS CLI with Credentials to Test

**Context**: Set up the AWS CLI environment with the target credentials. This can be done by exporting environment variables (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY) or using a named profile in the credentials file. This step ensures the CLI authenticates correctly before querying STS.

If using environment variables:

```bash
export AWS_ACCESS_KEY_ID=$_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=$_SECRET_ACCESS_KEY
```

If using a profile, edit ~/.aws/credentials:

```ini
[example_profile]
aws_access_key_id = $_ACCESS_KEY_ID
aws_secret_access_key = $_SECRET_ACCESS_KEY
```

> This isolates the test to specific credentials without affecting the default profile. Verify configuration with 'aws configure list' if needed.

### Step 2: Execute Get Caller Identity Command

**Context**: Run the STS command to test credential validity. The command queries the STS service and returns identity details if authenticated successfully. Use the --profile flag for named profiles to test isolated credentials.

**Command** ([[commands/aws-sts-get-caller-identity]]):

```bash
aws sts get-caller-identity --profile $_PROFILE_NAME
```

> This command performs the core validation. If credentials are invalid, it will error with an 'InvalidClientTokenId' or 'SignatureDoesNotMatch' message. Successful execution provides JSON output confirming access. For automation, wrap in a loop over a credential list and parse the response for 'UserId' presence to flag valid ones.

### Step 3: Parse and Validate Response

**Context**: Review the output to confirm success and extract key details. Look for the presence of 'Account', 'Arn', and 'UserId' fields in the JSON response. Invalid credentials will lack these or return an error.

Use jq for parsing if available:

```bash
aws sts get-caller-identity --profile $_PROFILE_NAME | jq '.Account'
```

> Extract the account ID to understand the target environment. If valid, proceed to further reconnaissance like 'aws iam list-users'. Log valid credentials for later use in attack chains.
