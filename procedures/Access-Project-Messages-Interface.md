---
tags:
  - messages-access
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T03:46:37.192Z'
sub_techniques: []
id: 1507cfb7-aaec-4e1e-a99c-b4d534ddbf83
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-Project-Messages-Interface

## Summary

This procedure involves navigating to the messages section of a created project on TopCoder Connect, where the stored XSS vulnerability resides in the message content input.

## Description

Once a project is approved, its messages page becomes accessible at https://connect.topcoder.com/projects/<project_id>/messages. This interface allows chat-like interactions among project members. The vulnerability stems from unsanitized user input here, enabling stored XSS. Expected outcome is loading the vulnerable form for payload injection.

## Requirements

1. Approved project with known ID
2. Authenticated browser session
3. Internet connectivity

## Defense

Defensive measures and detection strategies:

- Sanitize all message inputs server-side
- Use Content Security Policy (CSP) to block inline scripts
- Monitor access logs for repeated project visits

## Objectives

1. Reach the vulnerable messages endpoint
2. Identify input fields for exploitation
3. Prepare for payload submission

## Instructions

### Step 1: Navigate to Messages

**Context**: Use the project ID to access the chat.

In [[tools/Chrome-Browser]], enter https://connect.topcoder.com/projects/<your_project_id>/messages.

> Ensure the page loads without errors, showing the messages interface.

### Step 2: Verify Access

**Context**: Confirm chat functionality is available.

Attempt to view existing messages or the input form.

> Success if the content field is editable.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- messages-access
