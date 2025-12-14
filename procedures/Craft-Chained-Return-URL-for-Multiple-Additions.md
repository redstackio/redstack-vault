---
tags:
  - csrf
  - chaining
  - web
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/csrf-chained-stock-alert-get]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:42.559Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 3f34161a-1a3b-4eea-a129-b52ff695367f
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Chained-Return-URL-for-Multiple-Additions

## Summary

This procedure crafts nested return_url parameters in Lyst's stock alert endpoint to chain multiple item additions in a single GET request, amplifying the CSRF impact by triggering sequential saved list modifications.

## Description

The endpoint supports a return_url parameter for redirects post-alert signup. By nesting these (e.g., return_url pointing to another stock-alert URL), a single request cascades into multiple additions. This exploits the lack of depth limits or CSRF checks. Target environment is Lyst's web app; expected outcome is multiple unauthorized additions. Requires product IDs and basic URL encoding knowledge.

## Requirements

1. Multiple Lyst product IDs
2. URL encoding tool or manual crafting
3. Proxy like Burp for testing chains
4. Authenticated session for validation

## Defense

Defensive measures and detection strategies:

- Limit redirect depth and validate return_url origins
- Use CSRF tokens in all chained requests
- Log and alert on high-volume additions from single IPs

## Objectives

1. Create a chain adding 3+ items per request
2. Test for redirect success without breaks
3. Scale for larger floods

## Instructions

### Step 1: Build Nested URL

**Context**: Manually construct the chained URL starting from the innermost endpoint.

**Command** (Manual):
```bash
# Example chain: /stock-alert/ID1/?return_url=/stock-alert/ID2/?return_url=/stock-alert/ID3/
```

> Start with innermost: /email-capture/stock-alert/89201857/. Then nest: /email-capture/stock-alert/91703404/?return_url=previous. Full: /email-capture/stock-alert/93543518/?return_url=/email-capture/stock-alert/91703404/?return_url=/email-capture/stock-alert/89201857/.

### Step 2: Test Chained Request

**Context**: Send the crafted URL to verify sequential additions.

**Command** ([[commands/csrf-chained-stock-alert-get]]):
```bash
curl -X GET "https://www.lyst.com/email-capture/stock-alert/93543518/?return_url=/email-capture/stock-alert/91703404/?return_url=/email-capture/stock-alert/89201857/" -v
```

> Expect multiple 302 redirects; check saved list for all three items added.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/csrf-chained-stock-alert-get]]

## Tools Used


## Tags

- [[csrf]]
- [[chaining]]
- [[web]]
