---
id: proc-query-contentdocument
tags:
  - bac
  - aura
  - query
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Cloud (Salesforce)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:43.138Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Query-ContentDocument-Records-Aura

## Summary

Modify the Aura payload in Burp Suite to unauthenticatedly query up to 2000 ContentDocument records, exploiting Broken Access Control in Salesforce configuration.

## Description

By altering the Aura action to use the SelectableListDataProvider controller, this procedure fetches file metadata without authentication, revealing IDs for subsequent IDOR exploitation and enabling mass PII exposure.

## Requirements

1. Intercepted request in Burp Repeater
2. Knowledge of Salesforce Aura JSON structure
3. No auth tokens in request

## Defense

Defensive measures and detection strategies:

- Restrict ContentDocument object permissions to authenticated users only
- Implement rate limiting on Aura endpoint queries
- Audit sharing settings in Salesforce setup

## Objectives

1. Craft payload for unauthorized entity query
2. Retrieve file records en masse
3. Identify exploitable ContentDocument IDs

## Instructions

### Step 1: Edit Message Payload

**Context**: Replace the original action with a query action.

No command; in Repeater, modify the 'message' JSON to {"actions":[{"action":"serviceComponent://ui.force.components.controllers.lists.selectableListDataProvider.SelectableListDataProviderController/ACTION$getItems","params":{"entityNameOrId":"ContentDocument","pageSize":2000,"currentPage":0}}]}.

> Ensure the request method remains POST to /s/sfsites/aura.

### Step 2: Send Modified Request

**Context**: Execute the altered request to fetch data.

No command; click "Send" in Repeater.

> Response should be JSON with 'items' array containing file objects; check for errors like "Insufficient privileges".

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[bac]]
- [[aura]]
