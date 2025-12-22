---
id: proc-uuid-2
tags:
  - execution
  - intercept
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/send-temp-password-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:18.046Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-and-Intercept-Temp-Password-Request

## Summary

This procedure triggers a temporary password request for an arbitrary user on the UPS site and intercepts it using a proxy tool, setting up for response manipulation.

## Description

The UPS support site's /api/Account/SendTempPassword endpoint handles temp password requests without strong server-side auth, relying on client-side JS. For non-existent users, it returns status false, but interception allows bypass. Target environment is a web app over HTTP/2 with Angular frontend.

## Requirements

1. Burp Suite configured as proxy
2. Arbitrary username/email (non-existent)
3. Access to login page

## Defense

Defensive measures and detection strategies:

- Enforce server-side validation on all API responses
- Log and alert on intercepted/modified traffic patterns

## Objectives

1. Trigger the vulnerable endpoint
2. Capture the failing response for modification
3. Maintain session cookies for continuity

## Instructions

### Step 1: Submit Temp Password Request

**Context**: From the login page, enter arbitrary username and submit to initiate the POST request.

**Command** ([[commands/send-temp-password-request]]):
```bash
curl -X POST "https://█████████/api/Account/SendTempPassword/?userName=test@example.com" -H "Host: ██████████" -H "Cookie: ████████" -H "Content-Length: 0" -H "Sec-Ch-Ua: \"\")" -H "Sec-Ch-Ua-Mobile: ?0" -H "Sec-Ch-Ua-Platform: \"Windows\"" --http2
```

> Request sent; response intercepted in Burp showing {"status":false,...}.

### Step 2: Confirm Interception

**Context**: Verify the request is held in Burp Proxy for editing.

No command; inspect in Burp UI.

> Intercepted request visible with headers and empty body.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/send-temp-password-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[Execution]]
- [[intercept]]
- [[web]]
