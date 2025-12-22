---
tags:
  - xss
  - stored-xss
  - persistence
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 62cdfc3b-2555-490d-a303-8b7ae9efb4d6
created_at: '2025-12-14T03:16:31.142Z'
updated_at: '2025-12-14T03:16:31.142Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Malicious-Slack-File-Post

## Summary

This procedure submits the form containing the injected XSS payload to store it persistently in Slack's backend.

## Description

After injecting the payload, submitting the post form causes Slack to save the content without neutralizing the JavaScript. This stored content becomes part of the file post record, ready for public linking. The lack of server-side sanitization allows the payload to survive storage and be retrieved later for execution.

## Requirements

1. Payload already entered in the post creation form
2. Valid Slack session
3. No additional tools beyond the browser

## Defense

Defensive measures and detection strategies:

- Enforce server-side validation to strip or escape JavaScript from post content before storage
- Log and alert on submissions containing script-like patterns (e.g., 'onerror', 'alert')
- Rate-limit post creations to prevent abuse

## Objectives

1. Persist the XSS payload in Slack's database
2. Confirm storage without loss of malicious functionality
3. Set up for public exposure

## Instructions

### Step 1: Submit the Form

**Context**: Finalize the post creation to trigger backend storage.

Click the submit button on the `https://subdomain.slack.com/files/create/post` form.

### Step 2: Confirm Save

**Context**: Verify the post is created and accessible in the workspace.

Check your Slack files or posts list for the new entry containing the payload.

### Step 3: Inspect Stored Content

**Context**: Ensure the payload remains intact post-save.

If possible, preview the post within Slack to see if the payload renders without immediate execution (it should not execute in authenticated context).

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
- [[stored-xss]]
- [[slack]]
