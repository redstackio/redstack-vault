---
id: proc-uuid-004
tags:
  - execution
  - privilege-escalation
  - csrf-trigger
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/xmlhttprequest-csrf-add-group]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:27:03.311Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Trigger-CSRF-via-Admin-Page-Visit

## Summary

This procedure executes the CSRF attack by having an admin visit the compromised page, triggering the JavaScript to forge group membership changes.

## Description

The injected script runs on window.onload, using the admin's session to POST to unprotected endpoints. No CSRF token is checked, allowing the escalation. Prerequisites: Published page with payload. Outcome: Non-admin added to admin group, gaining site control.

## Requirements

1. Admin user visits the page (social engineering)
2. Valid session cookie for admin
3. Vulnerable endpoints without token validation

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Monitor for anomalous group membership changes
- Educate admins on phishing and suspicious links

## Objectives

1. Execute forged POST using admin credentials
2. Escalate privileges silently
3. Verify elevation post-execution

## Instructions

### Step 1: Lure Admin to Page

**Context**: Trick admin into loading the page.

**Command** (Social Engineering):

Send link via email or chat: 'Review this new blog post.'

> Admin browses to page; script loads.

### Step 2: Script Execution

**Context**: JavaScript sends POST on load.

**Command** ([[commands/xmlhttprequest-csrf-add-group]]):
```javascript
// As embedded in header; executes automatically
XHR.open('POST', 'http://<<site>>/concrete5/index.php/ccm/system/user/add_group');
XHR.send(urlEncodedData);
```

> Silent request; check dashboard for user in group 3.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques

- None

## Commands Used

- [[commands/xmlhttprequest-csrf-add-group]]

## Tools Used

- None

## Tags

- [[Execution]]
- [[privilege-escalation]]
- [[csrf-trigger]]
