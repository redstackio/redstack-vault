---
tags:
  - xss-trigger
  - execution
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
updated_at: '2025-12-13T23:52:25.324Z'
sub_techniques: []
id: c78f4608-2c53-4907-8631-ab0bf54c3d0b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Webhooks-User-Selection

## Summary

This procedure triggers the stored XSS payload by interacting with the webhooks configuration interface in SMTP2GO, causing JavaScript execution in the victim's browser and demonstrating potential for session theft or further exploitation.

## Description

The webhooks setup renders the stored username in a selectable dropdown without escaping, focusing the malicious input element and firing the onfocus event. This affects administrators or other users viewing the list, leading to arbitrary code execution in their context. Prerequisites: Payload already stored; outcomes include alert popups or advanced payloads for cookie exfiltration.

## Requirements

1. Malicious user present in the SMTP users list
2. Access to webhooks configuration (authenticated session)
3. Victim context (e.g., admin privileges or shared view)

## Defense

Defensive measures and detection strategies:

- Output encoding for all user-controlled data in UI renders
- Client-side event handlers sanitized or disabled
- Monitoring for unexpected JavaScript errors or alerts in logs

## Objectives

1. Execute the stored payload in a browser context
2. Confirm impact like alert or data theft
3. Highlight cross-user execution risks

## Instructions

### Step 1: Access Webhooks Section

**Context**: Navigate to the interface that renders the vulnerable user list.

From the dashboard, click on "Webhooks" and proceed to the add webhook setup.

### Step 2: Select Malicious User

**Context**: Interact with the dropdown to focus and trigger the payload.

In the user selection dropdown, choose the malicious SMTP user, causing the onfocus event to fire and execute alert(1).

### Step 3: Observe Execution

**Context**: Validate the XSS trigger and assess potential impact.

Look for the alert popup; in a real attack, replace with payload to steal document.cookie or perform actions.

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
- [[web]]

