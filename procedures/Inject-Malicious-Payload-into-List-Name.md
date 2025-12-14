---
id: p-inject-xss-payload-instacart
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:23.485Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-List-Name

## Summary

This procedure involves creating a new shopping list in Instacart and injecting a malicious JavaScript payload into the list name field, which is stored server-side without proper sanitization, setting up for stored XSS execution.

## Description

The Instacart list creation form accepts arbitrary input in the name field, failing to escape HTML or JavaScript. The payload `'</script></title><script>alert(document.domain)</script>` breaks out of existing tags and injects executable code. This stored payload persists and executes when the list is previewed by any authenticated user, potentially leading to session theft.

## Requirements

1. Authenticated session with access to lists
2. Knowledge of XSS payloads
3. Web browser developer tools for testing (optional)

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs, especially in stored fields like names
- Implement Content Security Policy (CSP) to restrict script execution
- Scan for anomalous payloads in database-stored content using WAF or backend validation

## Objectives

1. Store unsanitized JavaScript in the list name
2. Confirm list creation without rejection
3. Enable execution in subsequent views

## Instructions

### Step 1: Initiate List Creation

**Context**: Access the add list functionality to open the input form.

Click the 'Add List' button on the lists page.

> Expected output: Modal or form appears with a name input field.

### Step 2: Enter Payload and Save

**Context**: Inject the payload to exploit lack of sanitization.

In the list name field, enter `'</script></title><script>alert(document.domain)</script>` and click 'Create' or 'Save'.

> The payload is stored. Expected output: List added to the user's lists; no validation errors.

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
