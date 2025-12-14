---
id: proc-uuid-2
tags:
  - app-creation
  - twitter
  - web
type: procedure
tools:
  - '[[tools/Internet-Explorer-11]]'
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:47:12.792Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-New-Twitter-App-with-Valid-Details

## Summary

This procedure creates a new application in the Twitter developer portal using valid input to establish a base for later vulnerability exploitation.

## Description

After logging in, users can create apps by providing details like name, description, and a valid website URL. This step ensures the app is created successfully, generating an app ID for settings access. It bypasses any strict validation during creation, setting up for the edit-phase injection. The target environment is the web-based portal, with outcomes including app approval for editing.

## Requirements

1. Authenticated session in Twitter developer portal
2. Valid app details (e.g., unique name, description, legitimate website like https://example.com)
3. Web browser for form submission

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on app creation
- Validate all input fields server-side during creation
- Log and review new app registrations for anomalies

## Objectives

1. Generate a new app ID for manipulation
2. Ensure initial validation passes
3. Prepare settings page for editing

## Instructions

### Step 1: Initiate Creation

**Context**: Access the creation interface from the dashboard.

Click the 'new app' or 'Create App' button.

> Form fields appear for input. Expected output: Required fields highlighted.

### Step 2: Fill and Submit

**Context**: Provide valid data to complete creation.

Enter app name, description, and a valid website URL (e.g., https://example.com), then submit.

> App creates with success message. Expected output: App ID assigned and listed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Internet-Explorer-11]]
- [[tools/Google-Chrome]]

## Tags

- [[app-creation]]
- [[twitter]]
- [[web]]
