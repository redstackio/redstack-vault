---
id: cddcc066-c1fc-4d5b-af91-3f37bf6abcc4
name: Retrieve-EC2-User-Data-With-IMDSv2-Token
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:13.398633+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
  - Linux
tags:
  - cloud-metadata
  - aws-imds
validated: true
---

# Retrieve-EC2-User-Data-With-IMDSv2-Token

## Code

```bash
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/user-data/
```

## Description

This bash code snippet retrieves a session token from the AWS IMDSv2 endpoint and uses it to fetch user data from an EC2 instance. It handles the two-step authentication process required for secure metadata access, preventing token replay attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $TOKEN | Auto-generated session token from first curl | 1234567890abcdef... (opaque string) |
| 21600 | Token TTL in seconds (6 hours max) | 21600 |

## Usage

Execute directly in a shell on the compromised EC2 instance after gaining foothold. Ideal for post-exploitation to extract launch-time secrets. Can be chained with other metadata queries using the same token for efficiency. Save as a script for automation in larger engagements.

## Detection

- CloudTrail logs for unusual instance metadata API calls or token requests.
- VPC Flow Logs showing traffic to 169.254.169.254 from unexpected processes.
- Process monitoring for curl invocations with IMDS endpoints; enable AWS Config rules for IMDSv2 enforcement.
- Anomalous user data access patterns in GuardDuty alerts.

## Related

- [[procedures/Retrieve-AWS-EC2-User-Data-via-Instance-Metadata-Service]]
- [[tools/cURL]]
