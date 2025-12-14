---
tags:
  - verification-link
  - endpoint-access
  - web-request
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:26:06.259Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 57abb908-d757-4d33-8bc6-767b1f5ae67b
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Access-Verification-Link

## Summary

This procedure accesses the email verification URL to interact with the vulnerable endpoint, potentially triggering errors that disclose server information.

## Description

Using the link from the verification email, such as http://www.localize.io/verify/e6be646b24pdd3w6d5c27ppa9a267ee7, this step sends a request to the /verify/ endpoint. In a vulnerable setup, it may cause a PHP fatal error due to improper error handling. Prerequisites include having the verification token; outcomes include observing the response for anomalies.

## Requirements

1. Valid verification URL from email
2. Web browser or command-line tool like curl
3. Network access to the target domain

## Defense

Defensive measures and detection strategies:

- Validate verification tokens server-side before processing
- Disable display_errors in PHP production environments
- Log all verification attempts and alert on failures

## Objectives

1. Trigger the verification process
2. Capture any error responses
3. Confirm endpoint behavior

## Instructions

### Step 1: Prepare the URL

**Context**: Ensure the verification link is ready for access.

Copy the full URL from the email, e.g., http://www.localize.io/verify/e6be646b24pdd3w6d5c27ppa9a267ee7.

### Step 2: Access via Browser

**Context**: Use a browser to visit the link and observe the page.

Paste the URL into the browser address bar and press enter.

> Expected output: Page load or error display in the browser.

### Step 3: Access via Curl (Optional)

**Context**: For scripted or logged access, use curl to fetch the response.

Execute [[commands/curl-access-url]] to verify:

```bash
curl -i "http://www.localize.io/verify/e6be646b24pdd3w6d5c27ppa9a267ee7"
```

> Explanation: This sends a GET request and displays headers and body. Expected output: HTTP 200 or 500 with error details.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used


## Tags

- url-access
- http-request
