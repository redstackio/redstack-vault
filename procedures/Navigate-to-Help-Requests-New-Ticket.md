---
id: proc-uuid-2
tags:
  - xss
  - navigation
  - slack
  - zendesk
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
updated_at: '2025-12-14T03:16:14.592Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Navigate to Help Requests New Ticket Page

## Summary

This procedure accesses the Slack help requests new ticket creation page, positioning the user to create a ticket that will incorporate the injected profile name.

## Description

Slack integrates with Zendesk for help requests, accessible via a specific URL. This step is preparatory, ensuring the interface is reachable. No payload execution occurs here. Target environment: Authenticated Slack web app. Expected outcome: Form page loaded, ready for ticket submission.

## Requirements

1. Active Slack session.
2. Access to help requests feature (standard for most workspaces).
3. Web browser.

## Defense

Defensive measures and detection strategies:

- Rate-limit access to help request pages to prevent abuse.
- Log navigation to sensitive forms for anomaly detection.
- Ensure all user data pulled into forms is encoded.

## Objectives

1. Reach the ticket creation interface.
2. Confirm integration with Zendesk is active.
3. Set stage for ticket submission.

## Instructions

### Step 1: Locate Help Requests

**Context**: Use Slack's UI or direct URL to access the form.

No command; manual navigation:

- In Slack sidebar, click "Help" or directly enter URL: `https://yourworkspace.slack.com/help/requests/new`.

> Page loads with form fields for subject, description, etc.

### Step 2: Verify Page Accessibility

**Context**: Ensure no blocks or errors prevent access.

- Check for form elements; if redirected, confirm authentication.

> Expected: Clean form interface without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- zendesk
- help-requests
- navigation
