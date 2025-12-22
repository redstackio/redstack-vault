---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - profile-editing
  - wordpress
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques: []
updated_at: '2025-12-14T03:47:12.719Z'
sub_techniques: []
validated: true
---
# Edit-Account-Details

## Summary

This procedure updates basic account information such as first and last name on the WordPress Mercantile profile, preparing the account for address field manipulation without triggering early defenses.

## Description

Authenticated users can edit non-sensitive details via the /my-account/edit-account/ endpoint. This step ensures the profile is active and editable, serving as a precursor to injecting payloads into address fields. No technical exploitation occurs here, but it confirms form submission works as expected.

## Requirements

1. Active user session on https://mercantile.wordpress.org/my-account/
2. Web browser for form interaction

## Defense

Defensive measures and detection strategies:

- Log all profile edits and alert on rapid successive changes
- Implement rate limiting on edit endpoints

## Objectives

1. Confirm editable profile access
2. Populate basic fields to avoid incomplete profile errors
3. Transition to address editing

## Instructions

### Step 1: Access Edit Page

**Context**: Log in and navigate to the account details editor.

Visit https://mercantile.wordpress.org/my-account/edit-account/.

> Locate first name and last name fields.

### Step 2: Update and Save

**Context**: Enter valid names and submit to test form handling.

Fill fields with arbitrary but valid names (e.g., 'Test First', 'Test Last') and click save.

> Expected: Success message and updated profile view.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[profile-editing]]
- [[wordpress]]
