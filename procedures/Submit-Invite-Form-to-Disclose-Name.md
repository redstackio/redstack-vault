---
tags:
  - disclosure
  - information-leak
  - shopify
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:24:56.656Z'
skill_level: basic
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 3177bab2-0baa-4b0c-a842-bdb0fe5c17e8
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Submit-Invite-Form-to-Disclose-Name

## Summary

This procedure submits the invitation form after entering an existing email, exploiting the Shopify Plus flow to prematurely reveal the full name of the account holder, enabling privacy breaches or social engineering.

## Description

Upon submission, the system queries the Shopify ID database and displays user details if a match is found, bypassing standard flows that wait for acceptance. This information disclosure allows any authorized user to enumerate PII, potentially chaining with other attacks like phishing.

## Requirements

1. Populated email field with existing account email
2. Selected role in the form
3. Active session with user management permissions

## Defense

Defensive measures and detection strategies:

- Modify invite flow to hide names until post-acceptance
- Implement CAPTCHA or secondary verification for invites
- Alert on bulk or suspicious invite submissions

## Objectives

1. Force the backend to return and display full user name
2. Capture the disclosed PII for enumeration
3. Validate the vulnerability without completing the invite

## Instructions

### Step 1: Complete and Submit Form

**Context**: Select a role and submit to trigger the disclosure.

No specific command required; perform via browser UI:

- From the role dropdown, select any option (e.g., 'Viewer' or 'Staff').
- Click the 'Send invite' button.
- Inspect the resulting user page or response for displayed details.

> If the email matches an existing Shopify ID, the full name (first and last) will appear on the page. For non-matches, a generic error or new user prompt shows, confirming the technique.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- disclosure
- information-leak
- shopify
