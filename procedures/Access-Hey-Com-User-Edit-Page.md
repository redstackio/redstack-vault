---
id: proc-uuid-1
tags:
  - web-access
  - authentication
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
updated_at: '2025-12-14T17:26:56.457Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Hey-Com-User-Edit-Page

## Summary

This procedure outlines how to navigate to the user profile edit page in hey.com, serving as the entry point for username manipulation attacks.

## Description

In the hey.com email service, authenticated users can access a dedicated edit page for profile details, including the display name. This page lacks restrictions on subsequent input lengths, making it vulnerable to oversized data injection. The procedure requires a valid login and uses the user's unique ID to construct the URL. Expected outcomes include successful page load, enabling further exploitation steps like submitting long names.

## Requirements

1. Valid hey.com account credentials
2. Web browser with session persistence
3. Knowledge of user ID (obtainable from account URLs or dev tools)

## Defense

Defensive measures and detection strategies:

- Implement session timeouts and monitor unusual profile edit frequency
- Log access to edit endpoints and alert on anomalous patterns

## Objectives

1. Gain access to the username modification interface
2. Prepare for input validation bypass
3. Confirm authenticated access without errors

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Log in to establish a session and reach the contacts management area.

No specific command; use browser to visit https://app.hey.com and sign in, then go to contacts.

> Browser navigation loads the dashboard; success if no login prompts reappear.

### Step 2: Locate User Edit URL

**Context**: Construct the direct edit URL using the user ID.

Inspect network requests or account links to find %user_id_number%, then navigate to https://app.hey.com/contacts/%user_id_number%/user/edit.

> Page loads with editable form fields, including name input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web-access
- authentication
