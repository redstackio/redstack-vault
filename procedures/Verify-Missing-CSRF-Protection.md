---
tags:
  - csrf
  - verification
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-add-coupon-csrf]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.817Z'
sub_techniques: []
id: 1ea183fa-9c5d-41c5-bd93-116f88eeb29d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify Missing CSRF Protection

## Summary

This procedure inspects the coupon addition request to confirm the lack of CSRF token requirements, enabling cross-origin forgery attacks.

## Description

CSRF vulnerabilities occur when state-changing endpoints like the Teavana coupon adder do not validate origin or include anti-forgery tokens. By examining the captured POST request for absent tokens (e.g., no `__csrf` param or `X-CSRF-Token` header) and testing replay from a non-origin context, the flaw is confirmed. This applies to web applications on Demandware, where the endpoint `/Home-AddCouponToBasket` processes `couponcode` and `format=ajax` without protection, allowing unauthorized actions on authenticated sessions.

## Requirements

1. Captured legitimate request from previous step
2. Browser developer tools or proxy like Burp Suite
3. Valid session cookie

## Defense

Defensive measures and detection strategies:

- Enforce SameSite cookies and strict origin checks
- Log and alert on cross-origin POSTs to sensitive endpoints
- Require CSRF tokens for all non-GET requests

## Objectives

1. Confirm absence of CSRF mitigations
2. Test request replayability
3. Assess potential for forgery

## Instructions

### Step 1: Inspect Request Details

**Context**: Analyze headers and parameters for token presence.

In developer tools, review the POST request: Check body (`couponcode=BOGO50&format=ajax`) and headers—no CSRF elements should be found.

### Step 2: Replay Request Cross-Origin

**Context**: Simulate a forged request to validate vulnerability.

Use [[commands/curl-add-coupon-csrf]] from a terminal, omitting origin headers to mimic cross-site submission:

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Home-AddCouponToBasket' -d 'couponcode=BOGO50&format=ajax' -H 'Cookie: session=your_cookie_here' -H 'Origin: http://evil.com'
```

> If the request succeeds (basket updated), CSRF protection is missing; response should be AJAX format confirming addition.

**Expected Output**: Successful basket modification without token.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-add-coupon-csrf]]

## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[verification]]
