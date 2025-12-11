---
tags:
  - cookie-leak
  - human-error
type: procedure
tools:
  - '[[tools/cURL]]'
  - '[[tools/Browser-Console]]'
  - '[[tools/Browser]]'
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Steal Web Session Cookie]]'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
id: 0e3d3c55-50e3-4fda-966d-de29ae2e9b18
created_at: '2025-12-10T05:55:44.993Z'
updated_at: '2025-12-10T05:55:44.993Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1539]]'
---
# Leak Session Cookie via Unsanitized cURL Paste

## Summary

This procedure describes how human error in sharing vulnerability reproduction steps can lead to the accidental disclosure of sensitive session cookies, enabling potential account takeovers.

## Description

In bug bounty platforms, analysts often copy cURL commands from browser consoles to document reproduction steps. Failing to sanitize these commands can expose session cookies in report comments, which attackers can exploit. This targets web session management without IP binding.

## Requirements

1. Access to a browser console for capturing requests.
2. A valid session on the target platform.
3. Tools: [[tools/cURL]] and [[tools/Browser-Console]].

## Defense

Defensive measures and detection strategies:

- Implement automated scanning for sensitive data in comments.
- Enforce IP-binding on sessions and train staff on data sanitization.

## Objectives

1. Disclose a session cookie inadvertently.
2. Enable potential reuse by attackers.
3. Demonstrate risks of unsanitized data sharing.

## Instructions

### Step 1: Capture cURL Command from Browser Console

**Context**: Use the browser console to copy a cURL command during vulnerability reproduction.

**Command** ([[commands/curl-reproduce-vulnerability]]):
```bash
curl -H "Cookie: session=leaked_session_cookie_value" https://target.endpoint
```

> This captures the HTTP request including the session cookie.

### Step 2: Paste Unsanitized Command into Report Comment

**Context**: Share the command in a report without removing the cookie header.

No specific command; paste directly into the platform's comment field.

> This exposes the cookie to anyone viewing the report.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques



## Commands Used

- [[commands/curl-reproduce-vulnerability]]

## Tools Used

- [[tools/cURL]]
- [[tools/Browser-Console]]

## Tags

- #cookie-leak
- #human-error
