---
tags:
  - csrf
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:42.959Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 9f096fa3-8647-42be-bd5b-68e7640cc966
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-CSRF-in-Unsubscribe-Endpoints

## Summary

This procedure involves analyzing ExpressionEngine's comment and channel unsubscribe functionality to detect the absence of CSRF protection, confirming that state-changing actions use unprotected GET requests.

## Description

In ExpressionEngine CMS, unsubscribe actions for comments and channels are handled via GET requests to endpoints like `/member/unsubscribe?entry_id=ID`, without CSRF tokens or validation. This allows attackers to forge requests from authenticated users. The procedure requires access to a test instance or the target site, using browser tools to inspect requests. Expected outcome is verification of the vulnerability, enabling further exploitation without leading to immediate impact.

## Requirements

1. Access to an ExpressionEngine instance with comment/channel subscriptions enabled
2. Browser with developer tools (e.g., Chrome DevTools)
3. Basic knowledge of HTTP requests and CSRF concepts

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Enforce POST for sensitive actions and validate referer headers
- Monitor for anomalous unsubscribe requests from unusual sources

## Objectives

1. Confirm lack of CSRF protection in unsubscribe endpoints
2. Document vulnerable URLs and parameters
3. Assess potential for exploitation

## Instructions

### Step 1: Inspect Unsubscribe Functionality

**Context**: Log in as a test user and subscribe to a comment or channel to trigger unsubscribe options.

Navigate to a comment or channel page and locate the unsubscribe link. Right-click and inspect the element to view the href attribute, confirming it's a GET request without tokens.

**Expected Output**: URL like `https://target.com/member/unsubscribe?entry_id=123` with no CSRF parameter.

### Step 2: Test for CSRF Validation

**Context**: Attempt to trigger the unsubscribe via a crafted link from another domain to verify bypass.

Create a simple test page on a different domain with an img tag pointing to the unsubscribe URL. Visit it while authenticated and check if unsubscription occurs.

Example test HTML:

```html
<img src="https://target.com/member/unsubscribe?entry_id=123" onload="alert('Triggered')">
```

**Expected Output**: Unsubscription succeeds without additional prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[recon]]
