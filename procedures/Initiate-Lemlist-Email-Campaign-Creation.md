---
id: proc-938683-step1
tags:
  - initial-access
  - web-app
  - campaign-setup
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.674Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate Lemlist Email Campaign Creation

## Summary

This procedure outlines logging into lemlist and starting a new email campaign to access the vulnerable Froala editor interface, serving as the entry point for subsequent XSS exploitation.

## Description

In the context of exploiting a DOM-based XSS in lemlist, this step establishes access to the campaign creation workflow. It requires an authenticated session and navigates to the editor where payloads can be injected. Expected outcome is the loaded campaign form, enabling further steps without alerting defenses.

## Requirements

1. Valid lemlist account credentials for authentication
2. Web browser with JavaScript enabled
3. Direct internet access to app.lemlist.com

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on campaign creation to detect automated abuse
- Monitor login and campaign initiation logs for anomalous user behavior

## Objectives

1. Gain access to the email campaign editor
2. Position for payload injection without triggering UI validations
3. Validate authenticated session integrity

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Log in to establish a session and reach the campaigns dashboard.

Open a web browser and navigate to https://app.lemlist.com. Enter credentials and submit the login form.

> Upon success, the dashboard loads, confirming session establishment.

### Step 2: Start New Campaign

**Context**: Initiate the creation process to load the editor.

From the dashboard, click "New Campaign" or equivalent button to open the setup interface.

> The campaign form appears, ready for field input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- initial-access
- web-app
