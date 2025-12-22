---
tags:
  - xss-trigger
  - admin-compromise
  - concrete-cms
type: procedure
tools: []
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
id: 5b9e26d3-35cb-48a0-b64e-055da7d2584b
created_at: '2025-12-14T03:46:38.216Z'
updated_at: '2025-12-14T03:46:38.216Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-as-Administrator

## Summary

This procedure logs in as an administrator and interacts with the injected message to execute the stored XSS payload in Concrete CMS.

## Description

Following payload injection, this step switches to an admin session to view the private message. The vulnerability causes the unsanitized msgBody to render as HTML, executing JS on events like hover. Target environment is the same CMS instance. Prerequisites include admin credentials and the stored payload. Expected outcome is script execution, enabling attacks like redirects or alerts in the admin's browser.

## Requirements

1. Valid administrator credentials
2. Stored XSS payload in a private message
3. Web browser session separate from low-priv

## Defense

Defensive measures and detection strategies:

- Render user content in isolated iframes or text-only mode for admins
- Monitor for unexpected JS execution via browser dev tools or CSP logs
- Implement Content Security Policy (CSP) to block inline scripts

## Objectives

1. Authenticate as high-priv user to access injected content
2. Trigger payload execution via UI interaction
3. Demonstrate impact like session theft or phishing

## Instructions

### Step 1: Login as Administrator

**Context**: Switch to admin session for viewing.

Log out of the low-priv account, then navigate to the login page and enter admin credentials.

> Dashboard loads with elevated privileges; private messages remain accessible.

### Step 2: View and Interact with Message

**Context**: Open the conversation and trigger the event.

Go to private messages, open the targeted conversation, and hover the mouse over the injected message body.

> Payload executes: alert shows or browser redirects to the malicious URL.

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
- [[admin-compromise]]
