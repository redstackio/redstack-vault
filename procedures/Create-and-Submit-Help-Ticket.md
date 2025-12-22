---
id: proc-uuid-3
tags:
  - xss
  - ticket-creation
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
updated_at: '2025-12-14T03:16:14.588Z'
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
# Create and Submit Help Ticket

## Summary

This procedure submits a new help ticket in Slack, embedding the user's profile name (with injected payload) into the ticket data for later display.

## Description

The help ticket form pulls the user's profile name automatically. Upon submission, the data is sent to the Zendesk backend. This step does not trigger XSS but prepares the payload for the view stage. Requires authenticated session. Expected outcome: Ticket created and queued for viewing.

## Requirements

1. Access to new ticket form.
2. Basic form-filling capability.
3. Slack/Zendesk integration enabled.

## Defense

Defensive measures and detection strategies:

- Validate and encode all user data before inclusion in tickets.
- Implement CAPTCHA or rate-limiting on submissions.
- Audit ticket creation logs for suspicious patterns.

## Objectives

1. Generate a ticket incorporating the profile name.
2. Successfully submit without errors.
3. Obtain access to the ticket view.

## Instructions

### Step 1: Fill Ticket Form

**Context**: Provide minimal details to create the ticket.

No command; UI interaction:

- Enter subject: e.g., "Test Request".
- Description: Any text.
- Attachments: Optional.
- Submit the form.

> Submission processes; profile name is included invisibly in metadata.

### Step 2: Confirm Submission

**Context**: Verify ticket is created.

- Look for success message or ticket ID.
- Note the URL for viewing.

> Expected: Confirmation; no immediate XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ticket-submission
- data-embedding
