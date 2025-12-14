---
id: proc-concretecms-inject-xss-city
tags:
  - xss-injection
  - payload
  - concrete-cms
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
updated_at: '2025-12-14T03:16:14.651Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-City-Field

## Summary

This procedure details the injection of a reflected XSS payload into the City textbox of a Concrete CMS user profile, exploiting lack of input sanitization to close HTML attributes and insert executable JavaScript.

## Description

The City field in Concrete CMS profiles accepts user input without proper escaping, allowing attackers to inject HTML and JS. The payload `"><img src=x onerror=alert(document.cookie)>` breaks out of the attribute context (e.g., value="input") and adds an <img> tag that executes JS on error, alerting cookies. This stored payload reflects in the member list view.

## Requirements

1. Access to the profile edit form from the previous procedure
2. Knowledge of basic HTML/JS for payload crafting
3. Target Concrete CMS version vulnerable to unsanitized profile output

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding (e.g., htmlspecialchars)
- Validate input length and content in the City field
- Log and alert on suspicious inputs containing script tags or event handlers

## Objectives

1. Insert payload to escape HTML context
2. Store malicious input in the profile
3. Enable reflection in downstream views like member lists

## Instructions

### Step 1: Prepare the Payload

**Context**: Craft the XSS payload to break out and execute JS.

Use the string: `"><img src=x onerror=alert(document.cookie)>`

This closes the quote, adds a broken img src, and uses onerror to run alert(document.cookie).

**Expected Output**: Payload ready for input.

### Step 2: Enter and Save Payload

**Context**: Inject into the City field and persist the change.

In the City textbox, paste the payload and submit the form to save the profile.

**Expected Output**: Profile updates successfully; no errors from the CMS.

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
- [[payload]]
- [[concrete-cms]]
