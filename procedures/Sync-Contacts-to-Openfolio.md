---
tags:
  - xss
  - sync
  - openfolio
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:36.317Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8b1da64c-83b8-4810-b6f5-1765d1af34fc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Sync-Contacts-to-Openfolio

## Summary

This procedure synchronizes contacts from Google Contacts to Openfolio, importing the malicious contact with its unsanitized XSS payload for subsequent exploitation.

## Description

Openfolio's sync feature pulls contacts directly from the linked Google account via API or OAuth integration. By initiating the sync after creating the malicious contact, the payload is transferred without sanitization, setting up the vulnerability. This targets web applications with external data imports. Prerequisites include an Openfolio account linked to Google. Outcomes include the payload appearing in Openfolio's contact list, ready for triggering.

## Requirements

1. Openfolio account with Google integration enabled
2. Malicious contact already created in Google Contacts
3. Access to Openfolio dashboard

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all imported fields during sync process
- Rate-limit sync operations to detect bulk anomalous imports
- Log sync events for review of imported data sources

## Objectives

1. Transfer malicious payload to target application
2. Preserve payload integrity during import
3. Position for execution in browsing interface

## Instructions

### Step 1: Log in to Openfolio

**Context**: Access the account to reach the sync functionality.

Navigate to https://openfolio.com and log in with the linked Google account.

### Step 2: Initiate Sync

**Context**: Trigger the import of contacts from Google to pull in the malicious entry.

Go to the settings or contacts section and click the "Sync with Google Contacts" button to start the import process.

> The sync fetches contacts via Google's API, importing names and other fields without escaping HTML/JS in this vulnerable version.

**Expected Output**: Sync completes, showing updated contact count.

### Step 3: Verify Import

**Context**: Check that the malicious contact has been added.

Review the contacts list in Openfolio to confirm the payload name is present.

**Expected Output**: Malicious contact listed with intact payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[sync]]
- [[openfolio]]
