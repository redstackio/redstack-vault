---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - phabricator
  - settings-access
type: procedure
tools:
  - '[[tools/Browser-Network-Inspector]]'
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
updated_at: '2025-12-14T03:16:31.206Z'
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
# Navigate-to-Phabricator-Settings

## Summary

This procedure accesses the Phabricator display settings panel to prepare for injecting a malicious editor link configuration, enabling the setup for a persistent XSS attack.

## Description

In Phabricator, user settings are managed via a web interface at /settings/panel/display/. This procedure involves navigating to this endpoint while authenticated, allowing subsequent steps to capture and modify save requests. The target environment is a standard Phabricator installation running on PHP with libphutil. Expected outcomes include loading the settings form without errors, confirming the editor link field is present and editable.

## Requirements

1. Authenticated session in Phabricator (valid cookies or session token)
2. Direct network access to the Phabricator web server
3. Modern web browser for navigation

## Defense

Defensive measures and detection strategies:

- Implement session timeouts and monitor unusual settings access patterns
- Use CSP headers to restrict script execution in settings pages

## Objectives

1. Access the vulnerable settings panel
2. Verify editor link configuration is available
3. Prepare for request capture without triggering alerts

## Instructions

### Step 1: Open Phabricator in Browser

**Context**: Launch the browser and ensure you are logged in to establish a valid session.

No command required; manually navigate to the Phabricator dashboard.

> Log in if necessary and confirm session is active by viewing any page.

### Step 2: Navigate to Settings

**Context**: Directly access the display settings endpoint to load the form.

No command required; enter the URL in the browser address bar.

> Go to 'https://phabricator.example.com/settings/panel/display/'. The page should load with user preferences, including the 'External Editor' link field.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Network-Inspector]]

## Tags

- [[phabricator]]
- [[settings-access]]
