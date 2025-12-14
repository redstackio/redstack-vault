---
tags:
  - xss
  - injection
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 84d13b40-dae5-44b7-b528-1271c47bcb9c
created_at: '2025-12-14T03:15:47.193Z'
updated_at: '2025-12-14T03:15:47.193Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-User-Full-Name

## Summary

This procedure involves logging in as a non-admin attacker user and modifying the full name field to inject a stored XSS payload, which is then persisted in the Nextcloud database and rendered unsanitized in the chat module.

## Description

In Nextcloud Server 9.0.51 with JavaScript XMPP Chat 3.0.0, the user full name is not properly escaped when displayed in the chat information panel. By setting the full name to a payload like 'elamaran\"\"><script>alert(document.domain)</script>', an attacker can break out of HTML attributes and inject executable JavaScript. This stored payload executes in the context of any victim's browser when they view the attacker's profile, potentially leading to session cookie theft or other client-side exploits on the Nextcloud domain.

## Requirements

1. Valid non-admin attacker account in Nextcloud
2. Access to user profile settings via web interface
3. Target Nextcloud instance running version 9.0.51

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output escaping for user profile fields using libraries like DOMPurify
- Enable Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript alerts or network requests from chat module

## Objectives

1. Persist malicious JavaScript in the attacker's full name field
2. Ensure payload survives storage and retrieval without sanitization
3. Set up for execution in victim sessions

## Instructions

### Step 1: Log In as Attacker

**Context**: Authenticate as the non-admin user to gain access to profile modification.

Log in to the Nextcloud web interface using attacker credentials.

> Navigate to the dashboard and confirm successful login.

### Step 2: Modify Full Name

**Context**: Update the profile to inject the XSS payload, escaping quotes to break out of any attribute contexts.

In user settings, set the full name to:

```html
elamaran\"\"><script>alert(document.domain)</script>
```

> Save the changes. The payload includes escaped backslashes and quotes to close HTML attributes, followed by a script tag that executes on render.

### Step 3: Verify Injection

**Context**: Confirm the payload is stored by viewing the profile as the attacker.

Refresh the profile page and check if the full name displays the injected content without immediate execution (execution occurs only in chat view).

> Expected: No errors on save; payload visible in raw form.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
- [[nextcloud]]
