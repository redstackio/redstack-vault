---
id: 1741c202-2e4b-4efb-a8bd-e47ff89a3e9a
name: Retrieve-AWS-EC2-User-Data-via-Instance-Metadata-Service
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.406705+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/AWS-User-Data]]'
  - '[[tags/Cloud-AWS]]'
  - '[[tags/Exploitation]]'
  - '[[tags/Cloud-Metadata-Retrieval]]'
commands:
  - '[[codes/curl-retrieve-ec2-user-data-imdsv1]]'
  - '[[commands/curl-retrieve-ec2-user-data-imdsv2]]'
platforms:
  - AWS
  - Linux
tools: []
validated: true
---

# Retrieve-AWS-EC2-User-Data-via-Instance-Metadata-Service

## Summary

This procedure demonstrates how to retrieve user data from an AWS EC2 instance using the Instance Metadata Service (IMDS). User data often contains sensitive configuration scripts, credentials, or API keys passed at launch, enabling attackers with instance access to escalate privileges, perform lateral movement, or exfiltrate data. It covers both IMDSv1 (unauthenticated) and IMDSv2 (token-based) methods for compatibility with different AWS configurations.

## Description

The Instance Metadata Service (IMDS) is a REST API accessible from within an EC2 instance at the link-local address 169.254.169.254. It provides instance-specific data, including user data (up to 16KB) supplied during launch for bootstrapping. Attackers can query this service to extract secrets without authentication in IMDSv1 mode or with a session token in IMDSv2 (default since 2019 for new instances). This technique is useful post-compromise for discovering embedded credentials in cloud environments, mapping to MITRE ATT&CK for cloud data collection and evasion. It requires shell access to the instance and assumes the metadata service is not blocked by Instance Metadata Service (IMDS) restrictions or network policies.

## Requirements

1. Shell access to a running AWS EC2 instance (e.g., via SSH or initial foothold).
2. curl utility installed on the instance (standard on most Linux AMIs; if missing, use wget or another HTTP client).
3. IMDS enabled on the instance (default; check via AWS console or describe-instance API).
4. For IMDSv2: Instance configured to require tokens (IMDSv2-required mode).

## Defense

- Avoid embedding sensitive data in user data; use AWS Secrets Manager or Parameter Store instead.
- Enforce IMDSv2-required mode via instance metadata options to prevent unauthenticated access.
- Implement network ACLs or security groups to block outbound traffic to 169.254.169.254 if unnecessary.
- Monitor CloudTrail for unusual API calls related to instance metadata and enable VPC Flow Logs for metadata endpoint traffic.
- Use tools like AWS GuardDuty to detect anomalous metadata queries.

## Objectives

1. Retrieve user data containing potential secrets like API keys or scripts from the EC2 instance.
2. Use extracted information for privilege escalation, lateral movement, or data exfiltration in the AWS environment.
3. Validate success by confirming the presence of configuration or credential data in the output.

## Instructions

### Step 1: Attempt Retrieval Using IMDSv1 (Unauthenticated)

**Context**: Test for legacy IMDSv1 support, which allows direct access without tokens. This is faster but may fail on modern instances requiring IMDSv2.

**Command** ([[codes/curl-retrieve-ec2-user-data-imdsv1]]):
```bash
curl http://169.254.169.254/latest/user-data/
```

> This sends a simple GET request to the metadata endpoint. If successful, it returns the raw user data (e.g., base64-encoded scripts or plain text configs). If IMDSv2 is enforced, expect a 401 Unauthorized response, indicating the need for a token.

### Step 2: Retrieve Token and Fetch User Data Using IMDSv2

**Context**: For secure instances, first obtain a session token (TTL up to 6 hours), then use it to authenticate the user data request. This method is required for IMDSv2 and provides better security.

**Command** ([[commands/curl-retrieve-ec2-user-data-imdsv2]]):
```bash
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600") && curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/user-data/
```

> The first curl retrieves a token via PUT request with TTL header. The second uses the token in the header for the GET, with -v for verbose output showing headers and response. Success yields the user data; failure (e.g., invalid token) returns 401 or 403. Reuse the token for multiple metadata queries within its TTL to avoid repeated requests.

### Step 3: Parse and Analyze Retrieved Data

**Context**: Once data is obtained, decode or inspect it for secrets. User data is often base64-encoded or script-based.

**Instructions**: Pipe output to base64 -d if encoded, or grep for keywords like 'AKIA' (AWS keys) or 'password'. For example:
```bash
curl http://169.254.169.254/latest/user-data/ | base64 -d | grep -i secret
```

> This verifies exploitable content. If no data, the instance may have empty user data—proceed to other metadata endpoints like /latest/meta-data/ for IAM roles.
