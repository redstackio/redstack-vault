---
id: proc-uuid-4
tags:
  - xss
  - chained
  - cookie-theft
  - javascript
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:31.680Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Chained-XSS-via-Redirect-Response

## Summary

This procedure chains the open redirect to a reflected XSS by viewing the redirect response in a browser, executing JavaScript in the context of the original domain to steal cookies.

## Description

The redirect response, when pasted or viewed in the browser, executes in the www.localizestaging.com context due to the original request's domain. The malicious site (evil.com) embeds JavaScript like alert(document.cookie), allowing cookie access and potential exfiltration.

## Requirements

1. Captured 302 redirect response from Burp
2. Browser without strict CSP
3. Attacker domain with XSS payload

## Defense

Defensive measures and detection strategies:

- Sanitize and escape outputs in redirect responses
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous JavaScript execution in web logs

## Objectives

1. Execute arbitrary JS in victim domain context
2. Steal session cookies for account takeover
3. Demonstrate impact of unvalidated redirects

## Instructions

### Step 1: Copy Response

**Context**: Extract the raw HTTP response containing the redirect.

In Burp's Response tab, copy the entire response body, including headers and HTML with script.

### Step 2: View in Browser

**Context**: Trigger execution by loading the response as HTML.

Save the response as .html file or paste into browser console/address bar (data: URI). The redirect fires, loading evil.com and running <script>alert(document.cookie)</script>.

**Expected Output**: Alert box showing cookies from www.localizestaging.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[chained]]
- [[cookie-theft]]
- [[JavaScript]]
