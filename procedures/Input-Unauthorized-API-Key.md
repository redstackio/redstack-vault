---
id: proc-unauthorized-api-key-input-001
tags:
  - api-key
  - unauthorized-access
  - bypass
  - dropcontact
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:01.867Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Input-Unauthorized-API-Key

## Summary

This procedure involves entering a Pipedrive API key from another user into the Dropcontact integration form, exploiting the lack of ownership validation.

## Description

The Dropcontact Pipedrive integration fails to verify if the provided API key belongs to the logged-in user, allowing arbitrary keys to be used. This step occurs in the web form after accessing the integration page, with the expected outcome being acceptance of the input without rejection. The API key must be obtained separately (e.g., via phishing or leak).

## Requirements

1. Target Pipedrive API key string (e.g., from another user's account)
2. Loaded Pipedrive integration form in Dropcontact
3. No client-side validation blocking input

## Defense

Defensive measures and detection strategies:

- Server-side validation of API key ownership against user ID
- Log all API key submissions with user context
- Integrate with Pipedrive's API to verify key permissions

## Objectives

1. Submit foreign API key without detection
2. Bypass ownership checks in integration setup
3. Set up for unauthorized connection or trial

## Instructions

### Step 1: Locate API Key Field

**Context**: Identify the input area for the Pipedrive credential.

On the integration page, find the 'API Key' or 'Pipedrive Key' text field.

### Step 2: Enter the Key

**Context**: Input the unauthorized key to test validation.

Paste or type the target user's Pipedrive API key into the field.

> The form should not display ownership errors; if it does, the vulnerability may be patched.

### Step 3: Prepare Submission

**Context**: Ensure the form is ready to proceed.

Review other fields (if any) and hover over the submit button to confirm no immediate validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[credential-misuse]]
- [[api-bypass]]
- [[pipedrive]]
