---
tags:
  - interception
  - request-analysis
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-waitlist-lookup]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:45.235Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 702f42cf-bebc-4043-8fbc-c054809b9f49
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Intercept-Waitlist-Track-Position-Request

## Summary

Intercept and analyze the HTTP POST request from Curve's 'Track my position' form using a proxy tool to identify the API endpoint, request format, and initial response containing partial user data.

## Description

This procedure captures the client-side request to the waitlist API, which is triggered by form submission. The request targets https://website-api.production.curve.app/api/waitlist/us with a JSON body including the email. Analysis reveals the unauthenticated disclosure of user objects. Use in web vulnerability assessments; requires proxy setup.

## Requirements

1. Burp Suite configured as browser proxy
2. Test email address
3. Knowledge of HTTP/JSON structures

## Defense

Defensive measures and detection strategies:

- Log all API requests and alert on proxy-like user agents
- Enforce HTTPS and validate request origins
- Use WAF to block interception attempts

## Objectives

1. Capture the exact request payload and headers
2. Replay and observe response for data leakage
3. Confirm vulnerability parameters

## Instructions

### Step 1: Configure Proxy and Submit Form

**Context**: Set up interception to capture the live request.

Configure browser to use Burp proxy, then submit the form with a test email.

> Intercepted request shows POST with {"email":"test@example.com"}.

### Step 2: Replay Request with curl for Verification

**Context**: Use [[commands/curl-waitlist-lookup]] to manually test the endpoint outside the browser.

Execute [[commands/curl-waitlist-lookup]] to verify:

```bash
curl -X POST https://website-api.production.curve.app/api/waitlist/us \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com"}'
```

> Expected output: JSON with user details if email exists, or error.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/curl-waitlist-lookup]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[interception]]
- [[request-analysis]]
