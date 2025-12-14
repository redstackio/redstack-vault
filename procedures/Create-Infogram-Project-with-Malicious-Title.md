---
tags:
  - xss-injection
  - malicious-payload
  - infogram
  - project-creation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.295Z'
sub_techniques: []
id: de2bfb2b-62ab-455b-9932-16bf72cf5806
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Infogram-Project-with-Malicious-Title

## Summary

This procedure involves creating a new project on Infogram and setting its title to a malicious string containing JavaScript code, such as a script tag, which will later be exploited in the embed generation step.

## Description

After logging in, users can create projects like charts or infographics. The title field accepts user input without immediate sanitization. By entering '<script>alert(1);</script>', the payload is stored and will be reflected unsanitized in share embeds. This targets the lack of HTML entity encoding in title handling. Prerequisites include an active Infogram account. Expected outcome: a saved project with the injected payload.

## Requirements

1. Active Infogram account from previous procedure
2. Web browser session logged into dashboard
3. Basic understanding of JavaScript payloads for XSS

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs, especially titles, with HTML entity encoding
- Implement Content Security Policy (CSP) to block inline scripts
- Log and review project titles for suspicious patterns like <script> tags

## Objectives

1. Inject executable JavaScript into project metadata
2. Prepare payload for reflection in embed code
3. Set up conditions for XSS execution

## Instructions

### Step 1: Initiate New Project

**Context**: Start a new project to access the title input field.

From the dashboard, click 'Create New' and select a project type (e.g., blank infographic). Proceed to the editor.

### Step 2: Set Malicious Title

**Context**: Enter the XSS payload as the project title to store it unsanitized.

In the project settings or title field, input '<script>alert(1);</script>' and save the project.

> The platform accepts the input without escaping, storing it for later use in embeds.

### Step 3: Verify Project Save

**Context**: Confirm the project is saved with the payload intact.

Return to the project list or preview; the title should display the raw input.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-injection]]
- [[malicious-payload]]
