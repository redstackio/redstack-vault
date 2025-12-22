---
tags:
  - ssrf-trigger
  - xapi-test
  - internal-request
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-post-xapi-to-metadata]]'
  - '[[commands/curl-get-xapi-from-metadata]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:10.043Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 15c10210-1a79-4b79-8144-77c56ef44bcb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-LRS-Configuration-to-Trigger-SSRF

## Summary

This procedure triggers the SSRF by testing the malicious LRS configuration, causing the server to send xAPI requests to the AWS metadata endpoint and potentially exfiltrate internal data.

## Description

The 'Test' function in LRS Configurations sends sample xAPI statements (POST and GET) to the configured URL using server-side HTTP clients. With the URL set to the metadata service, this results in unauthorized access to instance details. The app logs the full HTTP exchange, including responses, for later retrieval. This exploits trust in user-provided endpoints in AWS environments, leading to metadata exposure.

## Requirements

1. Malicious LRS configuration created
2. Access to the product's LRS test button
3. Server-side HTTP client without internal restrictions

## Defense

Defensive measures and detection strategies:

- Disable or sandbox LRS test requests to external proxies
- Monitor server logs for requests to 169.254.169.254
- Use VPC endpoints or security groups to block metadata access from app servers

## Objectives

1. Force server to request internal AWS resources
2. Capture metadata response in test logs
3. Demonstrate full read access to instance info

## Instructions

### Step 1: Initiate LRS Test

**Context**: Execute the test to send requests via SSRF.

Click the 'Test' button beside the malicious configuration name. This triggers POST /latest/meta-data?/statements and GET /latest/meta-data?/statements?statementId=... using Basic Auth 'test:test' and xAPI headers.

To simulate locally for validation, execute [[commands/curl-post-xapi-to-metadata]]:

```bash
curl -X POST "http://169.254.169.254/latest/meta-data?/statements" \
  -H "X-Experience-API-Version: 1.0.3" \
  -H "Authorization: Basic dGVzdDp0ZXN0" \
  -H "Host: 169.254.169.254" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"actor":{"objectType":"Agent","name":"xAPI mbox","mbox":"mailto:████"},"verb":{"id":"http://███","display":{"en-GB":"attended","en-US":"attended"}},"object":{"objectType":"Activity","id":"http://www.example.com/meetings/occurances/34534"},"id":"3b9e4565-07ac-475f-be1f-d5f590f40779"}'
```

> This command sends the xAPI POST; expect 200 OK with metadata paths if on an AWS instance.

### Step 2: Handle Post-Test Redirect

**Context**: Return to the product after the test completes.

User is redirected to the homepage; manually navigate back to the product page to check results.

**Expected Output**: Test entry in 'Past Results'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-post-xapi-to-metadata]]
- [[commands/curl-get-xapi-from-metadata]]

## Tools Used


## Tags

- ssrf-trigger
- xapi-test
- internal-request
