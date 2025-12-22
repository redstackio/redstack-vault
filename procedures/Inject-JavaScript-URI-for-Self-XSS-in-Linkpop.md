---
id: proc-uuid-placeholder
tags:
  - xss
  - self-xss
  - javascript-uri
  - linkpop
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.954Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-JavaScript-URI-for-Self-XSS-in-Linkpop

## Summary

This procedure exploits a lack of validation in the Linkpop dashboard's add links URL input field, allowing injection of javascript: URIs to execute arbitrary JavaScript in the attacker's own browser upon preview interaction, resulting in self-XSS with limited impact to the user's session.

## Description

The vulnerability occurs in the Linkpop dashboard at https://linkpop.com/dashboard/admin during the addition of new links. The URL field accepts javascript: protocols without sanitization, leading to reflected self-XSS. When a payload like `javascript:alert(document.cookie)` is entered, the generated phone preview includes a clickable link that triggers the URI, executing JavaScript client-side. This can potentially access cookies or perform other actions but only affects the authenticated user themselves, with no cross-user propagation.

## Requirements

1. Authenticated access to the Linkpop dashboard with permissions to add links
2. Modern web browser capable of executing JavaScript URIs
3. Standard internet connection to reach https://linkpop.com

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation to block javascript: and other dangerous protocols in input fields
- Use Content Security Policy (CSP) to restrict script execution from untrusted sources
- Sanitize all user inputs on the client and server side to prevent URI scheme abuse
- Monitor for unusual JavaScript execution patterns in browser logs or via client-side monitoring tools

## Objectives

1. Inject and execute arbitrary JavaScript in the attacker's browser session
2. Demonstrate potential for self-impacting actions like cookie theft
3. Highlight the need for protocol validation in URL inputs

## Instructions

### Step 1: Access and Navigate to Add Links

**Context**: Log in and reach the add links interface to access the vulnerable URL field.

Navigate to https://linkpop.com/dashboard/admin and ensure you are authenticated. Click on "Links" then "Add Links" to open the form.

### Step 2: Enter Malicious Payload

**Context**: Input the javascript: URI to bypass validation and prepare for execution.

In the URL field, enter:

```text
javascript:alert(document.cookie)
```

Submit or allow the form to generate the preview without saving if possible.

### Step 3: Interact with Preview to Execute

**Context**: Trigger the payload by clicking the previewed link, confirming self-XSS.

Locate the phone image preview and click the generated link within it. Observe the alert dialog for execution confirmation.

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
- [[self-xss]]
- [[javascript-uri]]
