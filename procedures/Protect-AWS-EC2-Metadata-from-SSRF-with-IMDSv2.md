---
id: 78d0d9dc-6454-4c34-b17b-9fae700d7a65
name: Protect-AWS-EC2-Metadata-from-SSRF-with-IMDSv2
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.208841+00:00'
updated_at: '2023-04-10T20:19:51.003851+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Cloud Instance Metadata API]]'
sub_techniques: []
tags:
  - '[[tags/AWS - Metadata SSRF]]'
  - '[[tags/Cloud - AWS]]'
  - defense
  - ssrf
commands:
  - '[[commands/aws-modify-instance-metadata-options-enable-imdsv2]]'
platforms:
  - AWS
tools: []
validated: true
---

# Protect-AWS-EC2-Metadata-from-SSRF-with-IMDSv2

## Summary

This procedure enables Instance Metadata Service Version 2 (IMDSv2) on AWS EC2 instances to protect against Server-Side Request Forgery (SSRF) attacks targeting the instance metadata endpoint. By requiring session tokens for metadata requests, it prevents unauthorized access to sensitive credentials and instance details that could lead to privilege escalation.

## Description

The AWS instance metadata service provides temporary credentials and configuration data to EC2 instances via the link-local address 169.254.169.254. SSRF vulnerabilities in applications running on these instances can be exploited to read this metadata, potentially exposing IAM roles and enabling lateral movement. This procedure mitigates such risks by switching from IMDSv1 (which uses simple HTTP GET requests) to IMDSv2, which mandates a session token obtained via a PUT request with mutual TLS-like protections. It includes steps to enable IMDSv2 on an instance and demonstrate token generation and usage for secure metadata access. This is particularly useful in cloud environments where applications may inadvertently allow SSRF, ensuring only authorized processes can query metadata.

## Requirements

1. AWS account with EC2 permissions to modify instance metadata options (e.g., ec2:ModifyInstanceMetadataOptions).
2. Access to the AWS CLI configured with appropriate credentials or the AWS Management Console.
3. The target EC2 instance must be running and accessible via the AWS API.
4. Basic knowledge of AWS networking and the instance metadata service.

## Defense

- Use AWS IAM policies to restrict metadata access and monitor API calls via CloudTrail for suspicious ModifyInstanceMetadataOptions activity.
- Implement network ACLs or security groups to limit traffic to the metadata endpoint (169.254.169.254) from untrusted sources.
- Enable AWS Config rules to audit IMDSv1 usage and alert on non-compliant instances.
- Regularly scan applications for SSRF vulnerabilities using tools like AWS Inspector or static analysis.

## Objectives

1. Enable IMDSv2 on EC2 instances to require tokens for metadata requests, blocking unauthenticated SSRF attempts.
2. Generate and utilize IMDSv2 session tokens to ensure secure, authorized access to instance metadata.
3. Verify the configuration to confirm protection against unauthorized metadata exfiltration.

## Instructions

### Step 1: Enable IMDSv2 on the EC2 Instance

**Context**: This step modifies the instance metadata options to enable the HTTP endpoint and require a session token, upgrading from IMDSv1 to IMDSv2. This prevents SSRF attacks that rely on simple GET requests to access metadata without authentication.

**Command** ([[commands/aws-modify-instance-metadata-options-enable-imdsv2]]):
```bash
aws ec2 modify-instance-metadata-options --instance-id <INSTANCE-ID> --profile <AWS_PROFILE> --http-endpoint enabled --http-token required
```

> This command updates the specified EC2 instance to use IMDSv2. The --http-endpoint enabled allows HTTP requests to metadata, while --http-token required enforces token usage. Replace <INSTANCE-ID> with the actual instance ID (e.g., i-1234567890abcdef0) and <AWS_PROFILE> with your CLI profile name. The command returns a JSON response confirming the modification if successful.

### Step 2: Generate and Use an IMDSv2 Session Token

**Context**: After enabling IMDSv2, all metadata requests must include a session token. This step demonstrates how to obtain a token (valid for up to 6 hours) and use it to query metadata securely, verifying the protection works and providing a template for legitimate applications.

**Code** ([[codes/generate-and-use-imdsv2-token]]):
```bash
export TOKEN=`curl -X PUT -H "X-aws-ec2-metadata-token-ttl-seconds: 21600" "http://169.254.169.254/latest/api/token"`
curl -H "X-aws-ec2-metadata-token:$TOKEN" -v "http://169.254.169.254/latest/meta-data"
```

> Execute this from within the EC2 instance. The first curl command performs a PUT request to generate a token with a 21600-second (6-hour) TTL. The second curl uses the token in the header to fetch basic metadata. If IMDSv2 is properly enabled, requests without the token will fail with a 401 Unauthorized error. Expected output includes instance details like instance ID and region upon success.
