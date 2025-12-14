---
tags:
  - xss-trigger
  - demo-site
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/javascript-alert-document-domain-semicolon]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:20.261Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: c29f4d54-1132-447d-a014-87522555cee4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Navigate-to-Published-Site-and-Trigger-Demo-Domain-XSS

## Summary

This procedure accesses the published site view and triggers the stored XSS from the Demo Domain field by clicking 'view' on the demo, affecting admins who interact with published previews.

## Description

With the payload stored, navigating to /sites/<siteid>/published and selecting the demo executes the javascript: payload in the same domain context. This second vector targets other admins viewing the site, enabling hijacking or data exfiltration without the attacker's presence.

## Requirements

1. Settings saved with Demo Domain payload
2. Access to published site page
3. Browser for interaction

## Defense

Defensive measures and detection strategies:

- Validate demo domain outputs to prevent URI scheme execution
- Monitor published site views for anomalous behavior
- Deploy XSS auditors or WAF rules to block javascript: in URLs

## Objectives

1. Load the published site management page
2. Execute the Demo Domain payload via demo view
3. Confirm cross-admin impact potential

## Instructions

### Step 1: Access Published Site Page

**Context**: Navigate to the page listing published versions.

No command; manual navigation.

> Go to http://localhost:1337/sites/<siteid>/published. Expected output: List of published sites including demo.

### Step 2: Trigger XSS on Demo View

**Context**: Click to view the demo, executing the stored payload.

**Command** ([[commands/javascript-alert-document-domain-semicolon]]):

The payload executes on click:

```javascript
javascript:alert(document.domain);
```

> Click 'view' on the demo site entry. Expected output: Alert box showing the document domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/javascript-alert-document-domain-semicolon]]

## Tools Used


## Tags

- xss-trigger
- demo-site
