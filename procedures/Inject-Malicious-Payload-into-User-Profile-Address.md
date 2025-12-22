---
tags:
  - xss
  - injection
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/xss-payload-alert-injection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.509Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6974e320-17b2-4498-8bbf-672aaf47dd58
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-User-Profile-Address

## Summary

This procedure involves logging into the Uber Partners portal and injecting a malicious XSS payload into the user profile's address field, which is stored server-side without proper sanitization.

## Description

In the context of Uber's partners.uber.com, the address field in the user profile accepts arbitrary input, including HTML and JavaScript, which is later reflected on other pages like the fuel cards enrollment. This stored XSS allows persistence of the payload for execution when victims (including the attacker in self-XSS scenarios) visit affected pages. Prerequisites include valid credentials and access to the profile edit functionality.

## Requirements

1. Authenticated session to https://partners.uber.com
2. Web browser for form submission
3. Knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and sanitization for address fields (e.g., strip HTML tags)
- Use Content Security Policy (CSP) to block inline scripts and iframes
- Monitor for anomalous JavaScript execution in browser logs

## Objectives

1. Store malicious payload in the profile address field
2. Ensure payload breaks out of HTML context for execution
3. Prepare for reflection on downstream pages

## Instructions

### Step 1: Access Profile Settings

**Context**: Log in and navigate to the user profile to reach the editable address field.

**Command** ([[No Command]]):

No specific command; use the web interface to log in at https://partners.uber.com and go to profile settings.

> Expected: Profile edit form loads with address input.

### Step 2: Inject Payload

**Context**: Modify the address field to include the XSS payload, closing any surrounding tags to inject script.

**Command** ([[commands/xss-payload-alert-injection]]):
```html
#><img src=x onerror=prompt(1);>
```

> Insert this into the address field and save. The '#' comments out preceding content, '><' closes tags, and the img onerror executes JS. Expected: Profile saves without error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/xss-payload-alert-injection]]

## Tools Used


## Tags

- xss
- injection
