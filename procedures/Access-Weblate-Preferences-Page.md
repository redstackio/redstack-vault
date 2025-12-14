---
tags:
  - weblate
  - preferences
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques: []
updated_at: '2025-12-14T03:15:47.097Z'
sub_techniques: []
id: fc3ac420-5479-4847-b391-a43a840c0b89
validated: true
---
# Access Weblate Preferences Page

## Summary

This procedure outlines how to navigate to the user preferences page in Weblate to access the vulnerable Editor Link field, setting the stage for payload injection in a stored self-XSS attack.

## Description

In Weblate, user preferences are accessible via the profile section, where customizable fields like Editor Link are stored without proper validation. This step requires authentication and targets web-based instances like demo.weblate.org. The outcome is visibility of the input field for further exploitation.

## Requirements

1. Authenticated session in Weblate
2. Web browser with JavaScript enabled
3. Direct access to the Weblate URL (e.g., https://demo.weblate.org)

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit preference modifications
- Log all profile updates for anomaly detection in input patterns

## Objectives

1. Gain access to the Editor Link configuration field
2. Verify the field's editability
3. Prepare for payload insertion

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Ensure you are logged in and direct your browser to the profile section to load preferences.

Manually navigate to `https://demo.weblate.org/accounts/profile/#preferences`.

> This loads the preferences tab, where the Editor Link field is located as a text input.

### Step 2: Locate Vulnerable Field

**Context**: Identify the specific field targeted for XSS injection.

Scan the page for the 'Editor Link' input field, typically under editor or external tool configurations.

> Successful location confirms the field is present and lacks visible restrictions on input type.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- weblate
- preferences
- access
