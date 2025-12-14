---
id: proc-add-contacts-acronis-001
tags:
  - data-modification
  - contact-add
  - csrf-setup
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:27:57.622Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Add Contact Details to Victim Account

## Summary

This procedure describes adding contact information to the victim's Acronis Academy account to create exploitable data points for the CSRF deletion attack.

## Description

To demonstrate the vulnerability, contacts must exist to delete. The edit interface allows input of email, telephone, fax, address, or Skype details via form submission, likely POST requests with session validation. This step populates the account, generating contact IDs observable in subsequent requests. Prerequisites include edit page access; outcomes include persisted data verifiable in the profile.

## Requirements

1. Access to the account edit page
2. Fictional or test contact data
3. Active session

## Defense

Defensive measures and detection strategies:

- Validate input sanitization to prevent malicious data injection
- Rate-limit account modifications to detect bulk changes
- Audit logs for unusual data additions

## Objectives

1. Insert new contact records
2. Generate unique contact IDs
3. Confirm persistence of added data

## Instructions

### Step 1: Locate Contact Fields

**Context**: Identify input areas on the edit page.

Scroll to sections for email, phone, etc.

> Fields should be text inputs or dropdowns.

### Step 2: Fill and Submit Data

**Context**: Enter details and save.

Input values like email: test@example.com, phone: 123-456-7890, then click save or update button.

> Submission sends a POST request; watch for success response in DevTools.

### Step 3: Verify Addition

**Context**: Check if data is saved.

Refresh the page or view profile summary.

> Added contacts listed with new IDs (e.g., contact_id=123).

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- contact-add
- data-input
