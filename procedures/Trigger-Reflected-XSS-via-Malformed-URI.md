---
tags:
  - xss
  - reflected-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 006a9af1-30e6-4c3a-8eed-03027598d197
created_at: '2025-12-13T23:52:55.769Z'
updated_at: '2025-12-13T23:52:55.769Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Reflected-XSS-via-Malformed-URI

## Summary

This procedure triggers a reflected XSS on dev.twitter.com by using malformed URIs with invalid ports and null bytes, causing the redirect page to render a clickable javascript: link instead of auto-redirecting, particularly effective in Firefox for executing arbitrary JavaScript.

## Description

Due to differences in how the Location header and the page-rendered link process malformed URIs (e.g., :1/ for invalid port and %01 for null byte), the server sends a 302 but the browser blocks auto-redirect, displaying a page with the raw URI as a hyperlink. Clicking it executes the JavaScript in the site's context, enabling attacks like cookie theft or session hijacking.

## Requirements

1. Firefox browser for optimal blocking of invalid port redirects
2. Access to dev.twitter.com
3. Understanding of URI encoding

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all URIs to reject invalid ports and control characters
- Use strict output encoding for links in HTML responses
- Deploy WAF rules to block payloads with %01 or javascript: schemes

## Objectives

1. Render a non-auto-redirecting page with XSS payload
2. Enable user-triggered JavaScript execution
3. Escalate to data exfiltration

## Instructions

### Step 1: Craft XSS-Triggering URL

**Context**: Build a URL exploiting URI parsing flaws to embed a javascript: payload.

Access the following URL:

```url
https://dev.twitter.com//x:1/:///%01javascript:alert(document.cookie)/
```

> The server processes this as a 302 to the malformed target, but Firefox renders the page with the link due to invalid :1 port.

### Step 2: Observe Rendered Page

**Context**: Verify the intermediate page shows the clickable malicious link.

The page text: 'You should be redirected automatically to target URL: <a href="\x01javascript:alert(document.cookie)">\x01javascript:alert(document.cookie)</a>'.

> No auto-redirect occurs; the link is ready for clicking.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
