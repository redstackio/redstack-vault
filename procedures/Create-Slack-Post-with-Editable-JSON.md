---
tags:
  - slack
  - html-injection
type: procedure
tools:
  - '[[tools/HTTP-Proxy]]'
  - '[[tools/HTTPS-Enabled-Server]]'
  - '[[tools/Developer-Tools]]'
  - '[[tools/Email-Client]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/open-calculator-macos]]'
  - '[[commands/open-calculator-windows]]'
  - '[[commands/exec-shell-command-nodejs]]'
  - '[[commands/alert-localstorage]]'
platforms:
  - Desktop
  - Electron
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d31f31e1-fa8f-4361-91b6-0fd639b6450d
created_at: '2025-12-11T06:10:22.538Z'
updated_at: '2025-12-11T06:10:22.538Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Create Slack Post with Editable JSON

## Summary

This procedure creates a new Slack Post, generating an editable JSON file on files.slack.com, setting the stage for HTML injection.

## Description

In Slack, Posts are stored as JSON files with 'full' and 'preview' fields containing HTML content. This allows direct editing for injection attacks, targeting the desktop app's rendering.

## Requirements

1. Access to a Slack workspace.
2. Slack desktop or web app.
3. No special tools required.

## Defense

Defensive measures and detection strategies:

- Monitor API calls for unusual file edits.
- Implement stricter HTML sanitization in Slack Posts.

## Objectives

1. Generate editable JSON structure.
2. Prepare for payload injection.
3. Enable subsequent exploitation steps.

## Instructions

### Step 1: Create New Post

**Context**: Use Slack UI to create a Post with title and content.

No specific command; perform via Slack interface.

> Expected: JSON structure {'full': '<p>content</p>', 'preview': '<p>content</p>'} generated on files.slack.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[slack]]
- [[html-injection]]
