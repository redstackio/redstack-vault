---
id: proc-uuid-navigate-uzbey-invites
tags:
  - web
  - navigation
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:36.113Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Navigate-to-Uzbey-Invites-Section

## Summary

This procedure guides navigation within the Uzbey web application to the Invites section, where the Gmail integration vulnerability can be accessed for exploitation.

## Description

The Uzbey application features an Invites page that integrates with Gmail to pull contacts for friend invitations. Due to insufficient sanitization, this section is the entry point for XSS attacks via malicious contacts. This procedure assumes a logged-in user session and focuses on reaching the vulnerable interface. Expected outcomes include loading the Invites page without errors, setting the stage for further steps.

## Requirements

1. Valid Uzbey account credentials
2. Active browser session
3. Internet access to the Uzbey web app

## Defense

Defensive measures and detection strategies:

- Require authentication for sensitive sections like Invites
- Log navigation patterns to detect unusual access to integration features
- Use rate limiting on page loads to prevent automated probing

## Objectives

1. Reach the Gmail-integrated Invites functionality
2. Prepare for contact pulling without triggering alerts
3. Ensure session remains active

## Instructions

### Step 1: Log into Uzbey

**Context**: Establish a user session to access application features.

No command; enter credentials at login page.

> Dashboard loads upon successful authentication.

### Step 2: Locate Invites Section

**Context**: Use the application's navigation to find the Invites area.

No command; click on 'Invites' in the menu or sidebar.

> Invites page renders, displaying invitation options including Gmail.

### Step 3: Verify Page Load

**Context**: Confirm the section is functional and Gmail option is present.

Inspect the page source or UI elements.

> Gmail 'Invite Friends' button is visible and clickable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[navigation]]
