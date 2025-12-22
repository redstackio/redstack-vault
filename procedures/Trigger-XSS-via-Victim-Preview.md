---
tags:
  - xss
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/xss-trigger-preview]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:44.187Z'
sub_techniques: []
id: 8dc1e0fe-c62c-46e3-9228-49056f3d2686
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Victim-Preview

## Summary

Lure the victim to click the HMAC URL, authenticate them to the attacker's session, and execute the XSS payload during template preview.

## Description

The URL logs the victim in as the attacker without credentials. Previewing the template parses the payload in the browser, executing JS on www.judge.me subdomain due to parsing mismatch.

## Requirements

1. Valid HMAC URL
2. Victim interaction
3. Attacker's session active

## Defense

- Disable auto-login via HMAC for sensitive actions
- Warn on external links in emails
- Log preview accesses

## Objectives

1. Victim authentication
2. Payload execution
3. JS context on domain

## Instructions

### Step 1: Victim Access

**Context**: Victim clicks URL and logs in.

No command; social engineering to send URL.

> Expected: Redirect to edit page with auth.

### Step 2: Preview Trigger

**Context**: Victim previews template, firing onload.

**Command** ([[commands/xss-trigger-preview]]):
```javascript
// Payload executes: <img src=1 onerror='alert(1)'/>
```

> JS runs in judge.me context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/xss-trigger-preview]]

## Tools Used


## Tags

- [[xss]]
- [[Execution]]
