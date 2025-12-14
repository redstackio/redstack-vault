---
id: proc-initiate-respondly-gmail-import
tags:
  - xss
  - respondly
  - gmail-import
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
updated_at: '2025-12-14T03:15:36.233Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Respondly-Gmail-Import

## Summary

This procedure triggers the contact import feature in Respondly, fetching unsanitized data from Gmail and setting up the conditions for XSS execution.

## Description

The attacker or victim (via social engineering) uses Respondly's Gmail integration to import contacts. The feature pulls names via the Gmail API without proper escaping, rendering them directly in the browser. This step requires a Respondly account and Gmail access; outcomes include the display of contact data ripe for payload triggering.

## Requirements

1. Valid Respondly user account
2. Gmail account permissions for the integration
3. Victim tricked into performing the import (e.g., via phishing email)

## Defense

Defensive measures and detection strategies:

- Validate and escape all API-fetched data before rendering
- Log and alert on import attempts from untrusted sources
- Use OAuth scopes minimally for Gmail access

## Objectives

1. Authenticate and grant Respondly access to Gmail contacts
2. Fetch the contact list including the malicious entry
3. Render the contacts in the Respondly UI without sanitization

## Instructions

### Step 1: Log into Respondly

**Context**: Access the account where the import will occur.

Open respondly.com in a browser and log in with the victim's credentials.

### Step 2: Navigate to Import Feature

**Context**: Locate the Gmail contact import option.

Go to settings or the contacts/dashboard section. Select 'Import from Gmail' or similar button.

### Step 3: Authenticate with Gmail

**Context**: Allow Respondly to read contacts via API.

Click 'Connect to Gmail' and authenticate, granting necessary permissions. Confirm the import to start fetching contacts.

> The API call retrieves names directly; inspect network requests in dev tools to see raw data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[respondly]]
- [[gmail-import]]
