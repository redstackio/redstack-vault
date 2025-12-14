---
id: proc-slack-trigger-xss-001
tags:
  - xss
  - slack
  - execution
  - client-side
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
updated_at: '2025-12-13T23:56:19.753Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Slack-Gist-View

## Summary

This procedure triggers the XSS payload by accessing vulnerable views of the shared Gist in Slack, leading to arbitrary JavaScript execution under Slack's domain.

## Description

Once the Gist is shared, Slack creates views like 'raw' or 'new window' on its subdomain (e.g., outpost.slack.com). These views render the unsanitized filename in an HTML/SVG context, executing the onload script. This can lead to session hijacking or data theft. The procedure assumes the Gist is shared and focuses on victim-side interaction simulation.

## Requirements

1. Shared Gist in accessible Slack channel
2. Victim browser session on Slack
3. No additional tools; browser interaction suffices

## Defense

Defensive measures and detection strategies:

- Escape filenames and user inputs in all rendered contexts
- Deploy strict CSP headers to prevent JavaScript from SVG/onload
- Log and alert on unexpected script execution in client-side views

## Objectives

1. Execute the injected JavaScript payload
2. Demonstrate impact like alert or cookie access
3. Highlight potential for broader client-side attacks

## Instructions

### Step 1: Locate the Shared Gist in Slack

**Context**: Identify the entry point for vulnerable views.

Open the Slack channel and find the posted Gist message.

### Step 2: Access Vulnerable View

**Context**: Navigate to the rendering that triggers the payload.

Click the 'raw' button or 'open in new window' on the Gist embed. This loads a URL like https://outpost.slack.com/files/username/abc123/___svg_onload_alert_1.

**Expected Output**: Page loads with the filename rendered, triggering the SVG onload.

### Step 3: Observe Execution

**Context**: Validate the XSS impact.

Look for the alert(1) popup or inspect console for script execution.

**Expected Output**: JavaScript runs in Slack's context, e.g., alert box appears.

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
- [[slack]]
- [[Execution]]
