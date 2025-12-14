---
tags:
  - xss-trigger
  - persistence
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
updated_at: '2025-12-14T03:47:18.398Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 82a5542e-2a21-4ea9-95e1-a6a9c7b6c5d3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Client-and-Trigger-XSS

## Summary

This procedure involves saving the client with the injected XSS payload and then triggering its execution by viewing the details page and expanding the custom attributes section in the Ubiquiti UCRM demo.

## Description

After injection, submitting the form stores the payload in the database without sanitization. Viewing the client at /client/{id} and clicking 'Show more' renders the payload, executing JavaScript in the browser context, demonstrating alerts like prompt(1) and confirm(3).

## Requirements

1. Admin session with the client form submitted.
2. Client ID from creation (e.g., 24).
3. Victim or test browser to trigger execution.

## Defense

Defensive measures and detection strategies:

- Output encode all dynamic content with context-aware escaping (e.g., HTML escaping for attributes).
- Log and monitor unusual JavaScript errors or alert executions in browsers.
- Implement client-side validation to prevent payload rendering.

## Objectives

1. Persist the XSS in the backend.
2. Execute the payload in a browser context.
3. Confirm arbitrary code execution.

## Instructions

### Step 1: Submit Form

**Context**: Save the client to store the payload.

Click 'Save' or 'Create Client' on the form.

> Form submission. Expected output: Success message and new client ID.

### Step 2: Navigate to Details

**Context**: Load the page where attributes are displayed.

Visit https://dev-ucrm-billing-demo.ubnt.com/client/24.

> Page loads. Expected output: Client info with collapsed custom attributes.

### Step 3: Expand and Trigger

**Context**: Interact to render the payload.

Click 'Show more' under Custom Attribute 1.

> Click action. Expected output: JavaScript alerts pop up (prompt(1), confirm(3)).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[Persistence]]
