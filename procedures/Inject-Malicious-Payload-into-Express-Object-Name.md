---
tags:
  - xss
  - injection
  - payload
  - concrete-cms
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.117Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 285a0ba2-093c-4e53-a2ea-027a2d542673
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Express-Object-Name

## Summary

This procedure exploits the lack of input sanitization in the 'name' parameter of the Express Objects creation form in Concrete CMS v8.1.0 by submitting a malicious HTML/JavaScript payload, which is stored in the database for later execution.

## Description

The vulnerability stems from improper sanitization of user input in the POST request to /index.php/dashboard/system/express/entities/add. By injecting a payload like "><svg/onload=confirm(document.domain)>, the attacker closes the HTML attribute and injects executable script. This stored XSS affects all users viewing the entries page. Prerequisites: Authenticated access to the add form; outcomes: Payload persistence in the database.

## Requirements

1. Authenticated session with Express creation permissions
2. Access to the add object form
3. Knowledge of the ccm_token for form submission
4. Web browser for form manipulation

## Defense

Defensive measures and detection strategies:

- Input validation and HTML escaping on the server-side for all user inputs
- Content Security Policy (CSP) to restrict script execution
- Database monitoring for suspicious stored content (e.g., script tags)

## Objectives

1. Bypass input sanitization to store malicious code
2. Persist the payload in the Express Objects database
3. Set up for cross-user execution

## Instructions

### Step 1: Initiate Add Object Form

**Context**: Open the form to access input fields.

Click 'Add Object' on /index.php/dashboard/express/entries.

> Expected output: Form loads with fields including 'name', 'handle', 'plural_handle', and ccm_token.

### Step 2: Craft and Submit Payload

**Context**: Insert the XSS payload into the 'name' field and complete submission.

Enter "><svg/onload=confirm(document.domain)> as the name value, fill handle=blah, plural_handle=blah, include ccm_token, and submit POST to /index.php/dashboard/system/express/entities/add.

> Browser handles the POST request. Expected output: Success message; object created with payload stored.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- xss
- injection
