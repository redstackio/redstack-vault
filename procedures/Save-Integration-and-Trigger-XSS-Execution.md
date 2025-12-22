---
id: proc-save-trigger-xss-001
name: Save-Integration-and-Trigger-XSS-Execution
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:16:37.458Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - execution-trigger
  - stored-xss
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Save-Integration-and-Trigger-XSS-Execution

## Summary

This procedure finalizes the GitHub integration in Slack by saving the configuration, causing the stored XSS payload in the Branches field to render and execute arbitrary JavaScript in the browser context.

## Description

Upon saving, Slack stores the unsanitized Branches input in its backend and re-renders the integration settings page, executing the injected script. This can lead to alerts, cookie theft, or other client-side attacks for any user viewing the settings. The vulnerability stems from lack of output escaping during rendering.

## Requirements

1. Completed integration form with injected payload
2. Slack permissions to save integrations
3. Victim or tester viewing the settings page post-save

## Defense

Defensive measures and detection strategies:

- Escape all stored data before rendering (e.g., use htmlspecialchars)
- Deploy Web Application Firewall (WAF) rules to detect XSS patterns in configs
- Regularly scan integrations for malicious content via automated tools

## Objectives

1. Persist the malicious payload in Slack's storage
2. Trigger JS execution on render
3. Demonstrate impact like domain alert or data exfil

## Instructions

### Step 1: Submit the Form

**Context**: Save the integration to store the payload.

Click the 'Save integration' button at the bottom of the form.

### Step 2: Observe Execution

**Context**: Verify XSS by checking for immediate or post-render effects.

After saving, the page reloads or updates, triggering the onerror event and displaying an alert with the document domain.

> Success is confirmed by the alert box popping up, proving arbitrary JS execution.

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
- [[execution-trigger]]
- [[stored-xss]]
