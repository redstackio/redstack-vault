---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss
  - stored-xss
  - imageproxy
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/coursera-imageproxy-fetch-malicious-file]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.937Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Coursera-Imageproxy

## Summary

This procedure uses Coursera's imageproxy endpoint to fetch and render the malicious HTML from S3, executing the stored JavaScript payload in the victim's browser context.

## Description

Coursera's imageproxy trusts content from its S3 bucket without validating content-type or rendering it as an image, instead serving it as HTML. This leads to execution of embedded JavaScript when viewed, such as stealing cookies via alert(document.cookie).

## Requirements

1. S3 URL from previous retrieval step
2. Browser access to coursera.org (for execution)
3. HTTP client for testing

## Defense

Defensive measures and detection strategies:

- Validate and sanitize proxied content (e.g., force image rendering or content-type checks)
- Implement CSP to block inline scripts
- Monitor proxy logs for non-image responses

## Objectives

1. Execute arbitrary JavaScript in victim browsers
2. Collect sensitive data like cookies
3. Demonstrate impact of stored malicious content

## Instructions

### Step 1: Construct Proxy URL

**Context**: Build the imageproxy URL with the S3 path as parameter.

No command; example URL: https://www.coursera.org/api/utilities/v1/imageproxy/http://coursera-profile-photos.s3.amazonaws.com/[redacted]/stored_xss.html

### Step 2: Fetch and Execute

**Context**: Access the URL in a browser or via curl to trigger rendering.

**Command** ([[commands/coursera-imageproxy-fetch-malicious-file]]):

```bash
curl "https://www.coursera.org/api/utilities/v1/imageproxy/http://coursera-profile-photos.s3.amazonaws.com/[redacted]/stored_xss.html"
```

> In browser, this renders HTML and runs JS. Curl shows raw HTML for verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

-

## Commands Used

- [[commands/coursera-imageproxy-fetch-malicious-file]]

## Tools Used

-

## Tags

- xss
- stored-xss
- imageproxy
