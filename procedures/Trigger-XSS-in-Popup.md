---
tags:
  - xss-execution
  - trigger
  - browser
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.239Z'
sub_techniques: []
id: 7e3c06d7-faaf-4a57-a2d5-6b38f41094f4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS in Popup

## Summary

This procedure triggers the stored XSS by displaying the embedded Infogram content in the WordPress popup, executing the JavaScript payload in the authenticated user's browser context.

## Description

Viewing or re-interacting with the 'Add from Infogram' interface causes the plugin to render the project name in the popup, executing the onerror handler due to lack of escaping. This leads to arbitrary JS execution, such as prompt(0), and can escalate to session theft or site compromise. Targets browsers of WordPress users; outcomes include confirmed payload execution via alert.

## Requirements

1. Embedded malicious graphic in WordPress post
2. Victim browser session on the site
3. No CSP blocking inline scripts

## Defense

Defensive measures and detection strategies:

- Implement strict output escaping in plugin popups
- Monitor browser console for unauthorized script execution
- Use browser extensions or policies to block XSS prompts

## Objectives

1. Execute stored JavaScript in victim context
2. Demonstrate impact like data exfiltration
3. Highlight vulnerability for remediation

## Instructions

### Step 1: View Embedded Content

**Context**: Load the post to initiate popup rendering.

Publish or preview the WordPress post with the embedded graphic. Ensure the page loads fully.

### Step 2: Interact with Popup

**Context**: Force reflection of the malicious name.

Click the 'Add from Infogram' button or refresh the embed interface. Observe the popup where the project name is displayed, triggering `<img src=x onerror=prompt(0);>` to execute and show a prompt dialog.

> Inspect the popup HTML to confirm the unsanitized reflection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-execution
- trigger
- browser
