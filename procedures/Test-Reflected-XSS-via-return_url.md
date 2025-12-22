---
id: proc-adobe-xss-test
tags:
  - xss
  - reflected-xss
  - session-theft
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-test-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:52.943Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test Reflected XSS via return_url

## Summary

This procedure exploits insufficient sanitization in the return_url parameter to inject and execute JavaScript post-login/registration, allowing theft of session tokens or sensitive data from the victim's browser.

## Description

The return_url at http://youthvoices.adobe.com/community?return_url= accepts JavaScript schemes like javascript:alert(1) without escaping, leading to reflected XSS after authentication. This executes in the context of the authenticated session, enabling attackers to steal cookies or keylog. The attack requires victim interaction via a crafted link; outcomes include full account compromise.

## Requirements

1. Web browser with JavaScript enabled.
2. Target site access.
3. Knowledge of payload crafting for data exfiltration.

## Defense

Defensive measures and detection strategies:

- Sanitize and escape return_url to block JavaScript schemes.
- Implement strict CSP to prevent inline script execution.
- Detect anomalous JavaScript in URL parameters via WAF.

## Objectives

1. Verify XSS execution post-authentication.
2. Enable session token exfiltration.
3. Highlight data theft risks.

## Instructions

### Step 1: Craft XSS Payload

**Context**: Inject JavaScript scheme into return_url.

Execute [[commands/curl-test-xss]] to probe:

```bash
curl "http://youthvoices.adobe.com/community?return_url=javascript:alert(1)" -v
```

> Use -v for verbose output; in practice, deliver via link to victim.

### Step 2: Trigger Execution

**Context**: Victim authenticates, triggering the payload.

Send URL to victim; after login, confirm alert(1) or replace with alert(document.cookie) for session theft.

> Expected: Script runs, displaying alert with cookies or other data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[session-theft]]
