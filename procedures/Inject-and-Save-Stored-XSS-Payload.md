---
tags:
  - xss-injection
  - payload-storage
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:38.046Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: ede67f82-09fe-44c8-b46a-3c86ae22ae3c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-and-Save-Stored-XSS-Payload

## Summary

This procedure involves editing an existing promo code in the Acronis admin interface to inject and store a malicious JavaScript payload, which persists in the database and executes on subsequent page views.

## Description

The promo code field in the admin interface at http://www.grouplogic.com/ADMIN/store/index.cfm?fa=disprocode does not sanitize or encode user input, allowing HTML and JavaScript to be stored. Payloads like event-based scripts (e.g., onmouseover or onerror) are rendered directly when the page reloads, leading to XSS execution. This targets ColdFusion web apps and requires prior access to the edit form.

## Requirements

1. Access to the unauthenticated admin promo codes page
2. Web browser for form interaction
3. Knowledge of basic XSS payloads

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., HTML entity encoding) when rendering promo codes
- Validate and sanitize input to reject script tags or event handlers
- Implement Content Security Policy (CSP) to block inline JavaScript execution
- Log and alert on suspicious input patterns in admin forms

## Objectives

1. Insert executable JavaScript into the promo code field
2. Persist the payload via form submission
3. Set up for execution on page render

## Instructions

### Step 1: Locate and Edit Promo Code

**Context**: Select an existing promo code to modify, opening the input field for payload insertion.

**Action**:

Navigate to the promo codes section and click edit on any entry.

```plaintext
URL: http://www.grouplogic.com/ADMIN/store/index.cfm?fa=disprocode
```

> The edit form loads with the Promo Code field populated; clear or append to it.

### Step 2: Insert Malicious Payload

**Context**: Replace the field value with a stored XSS payload to ensure it renders and executes later.

**Action**:

Enter one of the following payloads into the Promo Code field:

```html
<h1 onmouseover=alert(document.domain)>XSS</h1>
```

or

```html
<img src=x onerror=alert(1)>
```

> Payloads are chosen for persistence: the first triggers on interaction, the second on load.

### Step 3: Submit and Save

**Context**: Persist the payload by submitting the form, storing it without validation.

**Action**:

Click the 'Edit Promo Code' button to save.

> The form submits successfully, updating the database with the unsanitized input.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-injection]]
- [[payload-storage]]
- [[stored-xss]]

