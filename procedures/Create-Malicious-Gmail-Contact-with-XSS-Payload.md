---
id: proc-uuid-create-gmail-xss
tags:
  - xss
  - injection
  - gmail
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
updated_at: '2025-12-14T03:15:36.120Z'
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
# Create-Malicious-Gmail-Contact-with-XSS-Payload

## Summary

This procedure involves creating a contact in Gmail with a specially crafted email address containing an XSS payload, which will later be pulled into the Uzbey application during the invitation process, enabling JavaScript injection without proper sanitization.

## Description

In the context of exploiting the Uzbey application's lack of input sanitization in its Gmail friends invitation feature, this procedure prepares the attack by embedding HTML and JavaScript in a Gmail contact's email field. The payload `a"><img src=y onerror=prompt(document.domain);>` closes any open tags, injects an image element, and triggers a JavaScript alert on error, demonstrating arbitrary code execution. This targets web applications integrated with Gmail APIs that render contact data unsafely. Prerequisites include a Gmail account; expected outcomes are a saved contact ready for exploitation, with no immediate execution until rendered in the vulnerable app.

## Requirements

1. Active Gmail account with contact creation permissions
2. Web browser for accessing Gmail
3. Knowledge of basic XSS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize all user-supplied inputs, especially from external sources like email fields, using HTML entity encoding or libraries like DOMPurify
- Implement Content Security Policy (CSP) to restrict inline scripts and image sources
- Monitor for anomalous JavaScript execution in browser consoles or server logs during API integrations

## Objectives

1. Prepare a vector for XSS injection via Gmail contacts
2. Ensure payload survives contact storage and retrieval
3. Set up for execution in the target application

## Instructions

### Step 1: Access Gmail Contacts

**Context**: Log into Gmail to reach the contacts management interface where new entries can be created.

No command required; navigate to contacts.google.com or via Gmail sidebar.

> Browser navigation leads to the contacts page.

### Step 2: Create New Contact

**Context**: Add a new contact and focus on the email field to insert the payload.

No command; click 'Create contact' and enter details.

> Contact form opens; set name to something innocuous like 'Test User'.

### Step 3: Inject Payload in Email Field

**Context**: Enter the XSS payload directly into the email field to bypass any client-side validation in Gmail.

Payload example:

```html
a"><img src=y onerror=prompt(document.domain);>
```

> Gmail saves the contact without executing the payload, storing it as plain text for later retrieval.

### Step 4: Save and Verify

**Context**: Confirm the contact is saved and the payload is intact.

No command; click 'Save' and search for the contact.

> Contact appears in list with payload visible in email field.

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
- [[gmail]]
- [[injection]]
