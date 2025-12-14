---
id: 123e4567-e89b-12d3-a456-426614174001
name: Trigger-Share-Endpoint-to-Leak-Config-Token
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.204Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - authorization-bypass
  - token-leak
commands: []
platforms:
  - Web
tools:
  - '[[tools/videoLeak-php]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Trigger-Share-Endpoint-to-Leak-Config-Token

## Summary

This procedure sends an unauthorized AJAX request to Vimeo's share endpoint for a private video, triggering an error response that leaks a secret token in an embedded config URL, enabling further unauthorized access.

## Description

In the context of Vimeo's web application, the share endpoint at https://vimeo.com/[VIDEO_ID]?action=share fails to properly sanitize error responses for unauthorized users, including sensitive config details. This step simulates an AJAX call to provoke the leak, targeting private videos where the user has no access. Prerequisites include knowing the video ID and basic HTTP request tools. Expected outcome is receipt of an error containing the token.

## Requirements

1. Public internet access to Vimeo's endpoints
2. Target private video ID (e.g., from shared link or enumeration)
3. HTTP client like curl or browser developer tools

## Defense

Defensive measures and detection strategies:

- Implement proper error handling to exclude sensitive tokens from responses
- Rate-limit AJAX endpoints and monitor for anomalous unauthorized requests
- Log and alert on access attempts to private video shares

## Objectives

1. Provoke leakage of secret token via error response
2. Obtain config URL for subsequent steps
3. Establish initial unauthorized access vector

## Instructions

### Step 1: Prepare and Send AJAX Request

**Context**: Simulate an authenticated AJAX call without credentials to trigger the vulnerable error.

**Command** (curl-trigger-share):
```bash
curl -X GET "https://vimeo.com/[VIDEO_ID]?action=share" -H "X-Requested-With: XMLHttpRequest" -v
```

> This command sends a GET request mimicking XMLHttpRequest, replacing [VIDEO_ID] with the target. Expected output includes a 403-like error body with the config URL and s=[SECRET] parameter.

### Step 2: Capture Response

**Context**: Inspect the full response to confirm leak.

No specific command; use -v flag in curl for verbose output or browser network tab.

> Verify the response body contains the leaked URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/videoLeak-php]]

## Tags

- [[authorization-bypass]]
- [[token-leak]]
