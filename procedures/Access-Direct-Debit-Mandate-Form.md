---
id: uuid-access-form
tags:
  - web
  - access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:35.839Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Direct-Debit-Mandate-Form

## Summary

This procedure involves navigating to the direct debit mandate creation or editing form on the Mobile Vikings website to gain access to vulnerable input fields.

## Description

In the context of exploiting a stored XSS vulnerability, the attacker first needs authenticated access to the account management section. This step targets the form at endpoints like /en/account/easypay/correct-direct-debit-mandate/, where the owner's name field lacks proper sanitization. Prerequisites include a valid login session.

## Requirements

1. Authenticated session on Mobile Vikings website
2. Web browser with developer tools for inspection
3. Network access to https://mobilevikings.be

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit form access
- Monitor for unusual navigation patterns in account management logs

## Objectives

1. Load the editable direct debit mandate form
2. Identify the owner's name input field
3. Prepare for payload injection

## Instructions

### Step 1: Log In and Navigate

**Context**: Authenticate and reach the easypay section to access the mandate form.

**Instructions**: Open a browser, navigate to https://mobilevikings.be, log in with valid credentials, and go to the direct debit management page, e.g., https://mobilevikings.be/en/account/easypay/correct-direct-debit-mandate/111366/.

> The form should display fields for mandate details, including the owner's name.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- access
