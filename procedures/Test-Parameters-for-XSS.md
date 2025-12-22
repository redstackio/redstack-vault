---
tags:
  - xss
  - testing
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-test-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.320Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 0e081b90-e8ac-462c-845d-c5c94ca42c16
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test Parameters for XSS

## Summary

This procedure tests query parameters in ASPX pages for reflected XSS by injecting special characters to detect lack of sanitization, confirming if HTML and JavaScript can be injected.

## Description

Reflected XSS occurs when user input from parameters is echoed back without escaping, allowing attackers to inject <script> or other HTML/JS. Target parameters like PId, CID, OprId on MyAccount.aspx. Use payloads with < > " / ' to break context. Successful tests show unencoded output, enabling further exploitation for session theft.

## Requirements

1. Identified endpoint from reconnaissance
2. HTTP client like curl or browser
3. Knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Enforce output encoding (e.g., HtmlEncode in ASP.NET)
- Use Content Security Policy (CSP) to block inline scripts
- Monitor for suspicious payloads in access logs

## Objectives

1. Confirm injection points in parameters
2. Verify lack of filtering for special characters
3. Identify context (e.g., attribute, text) for payload crafting

## Instructions

### Step 1: Inject Basic Special Characters

**Context**: Test if characters like < > " / ' are sanitized.

Execute [[commands/curl-test-xss]] to send a request with payload in OprId:

```bash
curl -s "https://videostore.mtnonline.com/GL/MyAccount.aspx?PId=126&CID=5&OprId=11%3Cscript%3Ealert(1)%3C/script%3E" | grep -i "<script"
```

> This checks if <script>alert(1)</script> appears unencoded in the response. If grep finds it, vulnerability confirmed.

**Expected Output**: Response contains unescaped <script> tag.

### Step 2: Test Context Breakout

**Context**: Determine if payload can break out of HTML attributes or text nodes.

Modify payload to %27%3E%3Cscript%3Ealert(1)%3C/script%3E in OprId and inspect response.

**Expected Output**: Alert triggers or HTML breaks, e.g., </input><script>.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss]]

## Tools Used


## Tags

- [[xss]]
- [[testing]]
- [[injection]]
