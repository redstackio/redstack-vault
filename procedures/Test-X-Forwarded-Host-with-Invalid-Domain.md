---
id: proc-test-invalid-xforwardedhost
tags:
  - ssrf
  - header-test
  - validation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:46.894Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test X-Forwarded-Host with Invalid Domain

## Summary

This procedure tests the server's host validation by adding an invalid X-Forwarded-Host header, expecting a failure to confirm the prioritization of this header over the standard Host header in Slack's backend.

## Description

Using Burp Repeater, the request is modified to include `X-Forwarded-Host: xxx.com`, simulating a mismatch. The server, honoring this header for internal forwarding, returns a 500 error due to invalid host resolution. This step validates the vulnerability's root cause: improper header prioritization allowing bypasses. It requires an intercepted request and focuses on AWS-hosted Slack services.

## Requirements

1. Intercepted request in Burp Repeater
2. Knowledge of target domain (files.slack.com)
3. Burp Suite active session

## Defense

Defensive measures and detection strategies:

- Strictly validate and sanitize all forwarded headers
- Log and alert on mismatched Host/X-Forwarded-Host values
- Use allowlists for permitted hosts in forwarding logic

## Objectives

1. Confirm header prioritization and validation enforcement
2. Identify error responses for invalid hosts
3. Set baseline for bypass testing

## Instructions

### Step 1: Add Invalid Header

**Context**: Modify the request to include the test header.

No command required; edit in Burp:

- In Repeater, add header: X-Forwarded-Host: xxx.com
- Ensure original Host remains files.slack.com
- Click Send

> Expected output: 500 Internal Server Error response indicating host mismatch.

### Step 2: Analyze Response

**Context**: Verify the error confirms validation.

No command required; inspect in Burp:

- Review response body for error details (e.g., host not found)

> Expected output: Error message related to invalid host resolution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ssrf]]
- [[header-test]]
- [[validation]]
