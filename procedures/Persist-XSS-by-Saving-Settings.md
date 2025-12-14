---
id: proc-uuid-5
tags:
  - xss
  - persistence
  - save
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.936Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Persist-XSS-by-Saving-Settings

## Summary

This procedure saves the modified settings to store the XSS payload persistently in the Judge.me app configuration.

## Description

Saving the Widget Form settings commits the injected payload to the backend, making it available for all future previews by any user accessing the settings, including store admins or staff. This turns the XSS into a stored variant, broadening the attack surface beyond the initial injector.

## Requirements

1. Payload injected and previewed successfully
2. No unsaved changes conflicts
3. Admin write permissions in Judge.me

## Defense

Defensive measures and detection strategies:

- Validate inputs server-side before saving configurations
- Alert on saves containing HTML tags or script-like patterns
- Periodic scans of app settings for malicious content

## Objectives

1. Commit changes to persist the payload
2. Ensure retrievability on reload
3. Impact multiple user sessions

## Instructions

### Step 1: Confirm Changes

**Context**: Verify the payload is still in the field before saving.

Review the success message field to ensure the payload remains.

> Expected: Injected content visible and unmodified.

### Step 2: Save Settings

**Context**: Submit the configuration to the app backend.

Click the 'Save' or 'Update' button at the bottom of the Widget Form page.

> Expected: Success message or confirmation; settings reload without errors. Re-preview to confirm persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Persistence]]
- [[save]]
