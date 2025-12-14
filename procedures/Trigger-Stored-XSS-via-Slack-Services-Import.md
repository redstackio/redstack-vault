---
tags:
  - xss-trigger
  - javascript-execution
  - slack
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.714Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 82ffa792-8a3f-4e5e-86eb-19144790fc88
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-Slack-Services-Import

## Summary

This procedure triggers the stored XSS by visiting the Slack services import page, where the unsanitized team name is rendered, leading to JavaScript execution in the victim's context.

## Description

The /services/import page displays the team name without proper encoding, executing the injected payload. This affects any user viewing the page in web-based Slack; prerequisites include successful payload injection. Outcomes: Arbitrary JS execution, enabling session hijacking or phishing.

## Requirements

1. Injected payload from previous procedure
2. Access to the Slack workspace (any user role)
3. Web browser session

## Defense

Defensive measures and detection strategies:

- Output encode all rendered content, especially dynamic fields like team names
- Deploy XSS auditors or WAF rules to detect payload execution
- Monitor for unexpected JS prompts or errors on pages

## Objectives

1. Render the vulnerable page to execute the payload
2. Confirm JS execution
3. Demonstrate potential for further attacks

## Instructions

### Step 1: Navigate to Import Page

**Context**: Visit the services import page to force rendering of the team name.

Open `https://hunter22.slack.com/services/import` (replace `hunter22` with the workspace subdomain).

> The page loads and renders the team name, triggering the onerror event in the injected <img> tag.

### Step 2: Observe Execution

**Context**: Verify the payload runs by checking for the prompt.

A dialog should appear prompting the document domain (e.g., "hunter22.slack.com").

> Expected: JS alert/prompt confirms execution; extend payload for real attacks like cookie theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[javascript-execution]]
- [[slack]]
