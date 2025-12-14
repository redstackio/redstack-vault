---
id: proc-uber-xss-trigger-001
name: Trigger-XSS-via-Uber-App-Deletion
tags:
  - xss
  - trigger
  - javascript-execution
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.807Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Uber-App-Deletion

## Summary

This procedure triggers the stored XSS payload in Uber's developer portal by attempting to delete the maliciously named application, causing the unsanitized name to render and execute JavaScript in the current browser context.

## Description

Once the payload is stored via the application name, interacting with the app—such as selecting it for deletion—causes the backend to render the name without proper escaping, injecting the malicious script into the page. This executes in the context of the viewing user (e.g., admin), allowing arbitrary JS like prompts or cookie theft. The attack relies on the victim (another developer) accessing the app list or deletion flow.

## Requirements

1. Pre-injected malicious application from prior procedure
2. Access to the applications list in Uber developer portal
3. Browser capable of executing JavaScript (e.g., Firefox or Chrome)

## Defense

Defensive measures and detection strategies:

- Sanitize all outputs when rendering user input in HTML contexts
- Implement rate limiting on app creation/deletion to detect abuse
- Use browser security features like XSS auditors and monitor for unexpected JS execution via error logs

## Objectives

1. Execute the stored payload in a victim's browser
2. Demonstrate impact through visible JS effects (e.g., alert)
3. Facilitate escalation to data theft or account takeover

## Instructions

### Step 1: Navigate to Applications List

**Context**: Access the list where the malicious app is displayed to prepare for interaction.

Log in to https://login.uber.com/applications and view the full list of applications.

> Expected output: Malicious app name visible in the list, potentially showing raw HTML if not escaped.

### Step 2: Initiate Deletion

**Context**: Select the malicious app for deletion to trigger rendering of the name in the confirmation UI.

Click on the malicious app and choose the 'Delete' option. Confirm the deletion if prompted.

> Expected output: XSS payload executes, displaying a prompt(1) dialog or equivalent JS alert in the browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- xss
- trigger
- deletion-exploit
