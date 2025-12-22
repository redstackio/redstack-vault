---
tags:
  - csrf
  - recon
  - api
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-with-origin]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.605Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: cdf10d22-31e5-4400-954b-c9020e110a07
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify CSRF Protection Mechanism on Webcast Endpoints

## Summary

This procedure involves analyzing TikTok's Webcast API endpoints to identify the CSRF protection mechanism, which validates requests only when the Origin header is present but fails to reject those without it.

## Description

In the context of testing TikTok's Webcast API, this step uncovers the reliance on the Origin header for CSRF prevention. By inspecting requests, testers can confirm that protection is incomplete, setting the stage for bypass exploitation. This is typically done in a controlled environment with authenticated access to observe header validation behavior.

## Requirements

1. Access to TikTok account for authentication
2. Tool like curl or Burp Suite for HTTP requests
3. Knowledge of Webcast API endpoints (e.g., from documentation or prior recon)

## Defense

Defensive measures and detection strategies:

- Implement strict Origin header checks, rejecting requests without it
- Use CSRF tokens in addition to header validation
- Monitor for anomalous API calls lacking Origin from unexpected sources

## Objectives

1. Confirm CSRF protection mechanism details
2. Identify weaknesses in header validation
3. Prepare for bypass testing

## Instructions

### Step 1: Inspect API Endpoints

**Context**: Review the Webcast API to locate endpoints handling user actions.

No specific command; use browser dev tools or proxy to capture requests.

### Step 2: Send Request with Origin Header

**Context**: Test normal validation by including the Origin header.

**Command** ([[commands/curl-test-with-origin]]):
```bash
curl -X POST https://api.tiktok.com/webcast/endpoint \
  -H "Origin: https://www.tiktok.com" \
  -H "Cookie: session=valid_session" \
  -d "data=test_payload"
```

> This command sends a POST request with Origin, expecting successful processing and validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-with-origin]]

## Tools Used

- [[curl]]

## Tags

- [[csrf]]
- [[api]]
- [[recon]]
