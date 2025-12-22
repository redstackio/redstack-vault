---
tags:
  - xss
  - self-xss
  - injection
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.288Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 2917ba2b-c685-42aa-95b2-ff9a2bad7bba
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Configure-Malicious-Editor-Link-in-Weblate-Profile

## Summary

This procedure injects a malicious JavaScript URI payload into the Editor link field of a Weblate user profile, exploiting lack of server-side sanitization to store executable code for later self-XSS triggering.

## Description

In Weblate, the user profile preferences allow setting an Editor link, which is intended for external editor integration but accepts unsanitized input. By entering a JavaScript URI like 'javaScript:alert(document.cookie);//confirm(1);', the payload is saved without validation. When later invoked (e.g., via source file links on translation pages), it executes in the user's browser context, potentially stealing cookies or performing other client-side actions. This is self-XSS, affecting only the attacker unless shared, and requires an authenticated session.

## Requirements

1. Authenticated access to Weblate account
2. Web browser with JavaScript enabled
3. No additional tools; performed via UI

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation to strip or block JavaScript URIs in link fields
- Use Content Security Policy (CSP) to restrict script execution from user-controlled sources
- Monitor for anomalous alert or confirm dialogs in browser logs

## Objectives

1. Store executable JavaScript payload in user profile
2. Prepare for self-XSS execution without server errors
3. Demonstrate unsanitized input persistence

## Instructions

### Step 1: Access Profile Preferences

**Context**: Load the profile settings to reach the vulnerable field.

Navigate to https://demo.weblate.org/accounts/profile/#preferences in your browser.

> The page should display the preferences form with the Editor link input.

### Step 2: Enter and Save Payload

**Context**: Inject the JavaScript URI to exploit the lack of sanitization.

In the Editor link field, input: `javaScript:alert(document.cookie);//confirm(1);` and click Save.

> Saving succeeds without errors, storing the payload for later use. The payload alerts cookies and shows a confirm dialog upon execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- self-xss
- weblate
