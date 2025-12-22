---
tags:
  - xss
  - trigger
  - published-sites
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/javascript-alert-domain-semicolon]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.657Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: d5024a43-2c68-4daf-b752-dfe9137662f9
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Demo-XSS-via-Published-Sites

## Summary

This procedure navigates to the published sites view and triggers the stored XSS from the Demo Domain payload by clicking 'view' on the demo site, confirming execution in the admin context.

## Description

The Demo Domain payload, stored after save, affects the published sites listing (/sites/<siteid>/published). Clicking 'view' executes the javascript: URI, similar to Custom Domain, but targets demo interactions. This broadens the attack to any admin reviewing publications.

## Requirements

1. Settings saved with Demo payload.
2. Published sites page accessible.
3. Admin session active.

## Defense

Defensive measures and detection strategies:

- Sanitize demo domain outputs in published views.
- Use URL validation to block non-http/https schemes.
- Monitor for repeated JS executions in admin traffic.

## Objectives

1. Verify second payload persistence.
2. Execute JS in published context.
3. Highlight multi-vector XSS impact.

## Instructions

### Step 1: Access Published Sites

**Context**: Load the page listing published demos.

Navigate to http://localhost:1337/sites/<siteid>/published.

> Expected output: List of published sites with 'view' buttons.

### Step 2: Trigger via Demo View

**Context**: Interact with the affected demo entry.

**Command** ([[commands/javascript-alert-domain-semicolon]]):
```javascript
javascript:alert(document.domain);
```

Click 'view' on the demo site.

> Expected output: Alert displaying the domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/javascript-alert-domain-semicolon]]

## Tools Used


## Tags

- [[xss]]
- [[trigger]]
- [[published-sites]]
