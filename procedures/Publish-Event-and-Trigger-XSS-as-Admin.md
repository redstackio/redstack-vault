---
tags:
  - xss
  - trigger
  - concrete-cms
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a036cae4-a6a7-4f11-843d-2ce598285365
created_at: '2025-12-14T03:16:20.407Z'
updated_at: '2025-12-14T03:16:20.407Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Publish-Event-and-Trigger-XSS-as-Admin

## Summary

This procedure publishes the malicious event to make it visible to other users and triggers the stored XSS payload when an admin views the Calendar & Events page, executing JavaScript in their browser context.

## Description

After injecting the payload, edit the event to publish it, ensuring it's listed publicly in the calendar. Switch to an admin session and navigate to the dashboard to view events. The unsanitized event name renders the payload, executing arbitrary JavaScript against the viewer, enabling attacks like phishing within the authenticated context.

## Requirements

1. Previously created event with stored XSS payload
2. Separate admin session
3. Permissions to publish events and view calendars

## Defense

Defensive measures and detection strategies:

- Escape output when rendering event names in HTML contexts
- Scan for XSS patterns in stored data using automated tools
- Monitor browser console for unexpected script executions in dashboards

## Objectives

1. Make the payload accessible to target users
2. Execute JS in victim's browser upon page load
3. Demonstrate cross-session impact

## Instructions

### Step 1: Edit and Publish Event

**Context**: Activate the event for visibility to other users.

As user2, click on the event, select Edit, then 'Publish Event'.

**Expected Output**: Event status changed to published.

### Step 2: Switch to Admin Session

**Context**: Simulate a victim user viewing the calendar.

Return to the main browser window logged in as admin.

**Expected Output**: Admin dashboard accessible.

### Step 3: View Calendar Events

**Context**: Load the page containing the malicious event name.

Navigate to Dashboard > Calendar & Events.

**Expected Output**: Event list renders, triggering the payload.

### Step 4: Observe XSS Trigger

**Context**: Confirm execution in the admin's browser.

View the event; the payload should execute.

**Expected Output**: Prompt box appears showing the domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- [[xss]]
- [[trigger]]
