---
tags:
  - enumeration
  - email-lookup
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
updated_at: '2025-12-14T17:24:56.667Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
id: ae6bc250-4438-42fd-83b9-a1414606e1fe
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enter-Existing-Email-for-Lookup

## Summary

This procedure involves inputting an email address associated with an existing Shopify account into the invitation form, initiating a backend check that sets up the disclosure upon submission.

## Description

The email field in the Shopify Plus 'Add users' form performs a lookup against existing Shopify IDs. Unlike standard invitation flows, this Plus-specific behavior allows enumeration by testing arbitrary emails. The attacker can use known or guessed emails to probe for account existence without sending actual invites.

## Requirements

1. Loaded 'Add users' form
2. Target email address (e.g., from external sources or guesses)
3. Authenticated session with user management access

## Defense

Defensive measures and detection strategies:

- Rate-limit email lookups in invitation forms
- Anonymize or suppress user details until invitation acceptance
- Log repeated email probes as potential enumeration attempts

## Objectives

1. Populate the email field with a valid existing account email
2. Trigger initial validation without submission
3. Prepare for name disclosure on form submit

## Instructions

### Step 1: Input Target Email

**Context**: Enter the email to initiate the lookup process.

No specific command required; perform via browser UI:

- Locate the email input field on the form.
- Type or paste an email like `francisbeaudoin+h1-2101@wearehackerone.com`.
- Do not submit yet; observe if any auto-complete or error appears (none expected for existing accounts).

> The field should accept the input. This step alone does not disclose info but enables the vulnerable response on submission.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- enumeration
- email-lookup
- shopify
