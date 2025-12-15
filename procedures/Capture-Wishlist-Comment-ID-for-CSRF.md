---
id: proc-uuid-004
tags:
  - id-capture
  - proxy-intercept
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/submit-wishlist-comment]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:27:43.168Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Capture Wishlist Comment ID for CSRF

## Summary

This procedure intercepts a legitimate comment submission to extract the dynamic :id parameter required for crafting the CSRF PoC.

## Description

The endpoint uses a dynamic :id in the URL path. By submitting a benign comment and proxying the request, the :id is captured. This enables targeting specific wishlists in the CSRF attack. Uses tools like Burp Suite; assumes authenticated access.

## Requirements

1. Proxy tool configured (e.g., Burp)
2. Authenticated session
3. Valid wishlist item

## Defense

Defensive measures and detection strategies:

- Use non-predictable IDs or sessions
- Rate-limit comment submissions
- Proxy detection via headers

## Objectives

1. Obtain :id from legitimate POST
2. Enable CSRF targeting
3. Avoid direct exposure

## Instructions

### Step 1: Submit Benign Comment

**Context**: Trigger a request to capture.

**Command** ([[commands/submit-wishlist-comment]]):
```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/[ID]' -d 'wishlistComment=Test' -H 'Cookie: [AUTH_COOKIE]'
```

> Proxy intercepts; note :id in URL.

### Step 2: Extract ID

**Context**: Analyze proxy log.

**Command**:
```bash
# In Burp: View request history for POST URL
```

> :id like /Wishlist-Comments/12345 captured.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Sniffing]] Network Sniffing

### Sub-Techniques


## Commands Used

- [[commands/submit-wishlist-comment]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- id-capture
- proxy-intercept
