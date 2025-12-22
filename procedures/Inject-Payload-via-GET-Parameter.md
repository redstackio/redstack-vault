---
tags:
  - xss
  - content-sniffing
  - get-injection
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-get-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:30.912Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 3ec15604-422a-43ff-823f-7917cc660c3c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Payload-via-GET-Parameter

## Summary

This procedure tests for reflected XSS vulnerabilities by injecting a URL-encoded malicious payload into the sign-in.currency query parameter of the Liberapay /about/me/edit endpoint, aiming to exploit content-sniffing in browsers to execute JavaScript.

## Description

In the Liberapay application, the sign-in.currency parameter is reflected in text elements without proper escaping, potentially allowing browsers to misinterpret the content as executable script via MIME-type sniffing. The payload USD<WDILR9>G8OAI[ !+! ]</WDILR9> is encoded and sent via GET to observe reflection. Although mitigations like X-Content-Type-Options: nosniff and application/json Content-Type prevent execution, this tests the vector for cookie theft or session hijacking in vulnerable setups. Prerequisites include access to the public Liberapay site; no authentication is required for basic testing.

## Requirements

1. Internet access to https://liberapay.com
2. curl or a browser for sending requests
3. Basic knowledge of URL encoding and HTML inspection

## Defense

Defensive measures and detection strategies:

- Set X-Content-Type-Options: nosniff header to prevent MIME sniffing
- Use strict Content-Type: application/json for API responses
- Implement CSRF tokens to block unauthorized POSTs
- Monitor for anomalous query parameters in logs

## Objectives

1. Confirm payload reflection in response
2. Assess potential for browser-based script execution
3. Evaluate mitigation effectiveness

## Instructions

### Step 1: Encode and Send GET Request

**Context**: Construct a GET request to the edit endpoint with the encoded payload in sign-in.currency to trigger reflection.

**Command** ([[commands/curl-get-payload]]):
```bash
curl -G "https://liberapay.com/about/me/edit" --data-urlencode "sign-in.currency=USD<WDILR9>G8OAI[ !+! ]</WDILR9>"
```

> This command sends the URL-encoded payload and returns the HTML response. Inspect the output for the decoded payload in text elements, such as <span>USD<WDILR9>G8OAI[ !+! ]</WDILR9></span>. Expect no execution due to headers.

### Step 2: Inspect Response

**Context**: Analyze the response body for unescaped reflection.

**Command** ([[commands/curl-get-payload]] with verbose):
```bash
curl -v -G "https://liberapay.com/about/me/edit" --data-urlencode "sign-in.currency=USD<WDILR9>G8OAI[ !+! ]</WDILR9>"
```

> Look for headers like X-Content-Type-Options: nosniff and Content-Type: text/html; check body for payload. Success if reflected but not executed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-payload]]

## Tools Used

- [[tools/curl]]

## Tags

- xss
- content-sniffing
