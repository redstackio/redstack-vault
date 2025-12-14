---
tags:
  - web
  - data-creation
  - weblate
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques: []
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: ff3eac6c-8dbf-4040-8d4e-d5007a15593e
created_at: '2025-12-14T17:27:22.509Z'
updated_at: '2025-12-14T17:27:22.509Z'
validated: true
---
# Add-Dictionary-Entry-in-Weblate

## Summary

This procedure creates a new entry in a Weblate dictionary to provide a target for deletion in the CSRF POC, simulating normal user activity.

## Description

Weblate dictionaries store translation terms. Adding an entry via the web interface generates an ID used in the delete endpoint. This step requires an authenticated session and targets a specific project/language (e.g., 'hello' project in Slovenian 'sl'). The outcome is a new entry with a trackable ID, essential for demonstrating the vulnerability.

## Requirements

1. Active authenticated session from login procedure
2. Access to the dictionaries page (e.g., https://demo.weblate.org/dictionaries/hello/sl/)
3. Basic knowledge of the translation interface

## Defense

Defensive measures and detection strategies:

- Rate-limit dictionary modifications to prevent abuse
- Log all entry creations with user IP and timestamp for auditing

## Objectives

1. Create a testable dictionary entry
2. Obtain the entry's unique ID for exploitation
3. Mimic legitimate user behavior

## Instructions

### Step 1: Access Dictionaries Page

**Context**: Load the management interface for the target dictionary.

After login, navigate to https://demo.weblate.org/dictionaries/hello/sl/.

> The page should display the dictionary list. If empty, proceed to add.

### Step 2: Create New Entry

**Context**: Input and save a new term to generate an ID.

Click the 'Add term' or similar button, enter source text (e.g., 'test') and target translation (e.g., 'test'), then submit.

> Expected output: The entry appears in the list with an ID (e.g., 5545). Note the ID from the entry's detail URL.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[data-creation]]
