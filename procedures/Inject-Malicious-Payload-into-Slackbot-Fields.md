---
id: proc-slack-payload-injection-4561
tags:
  - xss
  - stored-xss
  - payload-injection
  - slack
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
updated_at: '2025-12-14T03:16:31.233Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Slackbot-Fields

## Summary

This procedure involves responding to Slackbot's profile prompts with a malicious JavaScript payload, exploiting the lack of input sanitization to store XSS in direct messages.

## Description

Slackbot's profile completion process accepts user inputs for fields like first name or Skype account and stores them in DM threads. By entering a javascript: URI scheme payload such as `<javascript:alert(document.cookie);>`, the input is rendered as an unsafe anchor tag (`<a href="javascript:alert(document.cookie);">...</a>`) in the web client. This stored XSS persists in the conversation history, affecting any user viewing the thread. Prerequisites include active Slackbot prompts from team creation. Outcomes enable client-side execution upon interaction.

## Requirements

1. Ongoing Slackbot DM session from team onboarding
2. Knowledge of javascript: URI payloads
3. Web browser for input submission

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs before rendering in HTML attributes, especially href
- Escape special characters in anchor tags to block javascript: schemes
- Scan stored messages for suspicious URI patterns in logs

## Objectives

1. Store unsanitized payload in Slackbot DMs
2. Render payload as executable link in web view
3. Enable persistence for victim interaction

## Instructions

### Step 1: Respond to Profile Prompts

**Context**: Enter the malicious payload in response to Slackbot's questions to ensure storage.

No specific command; type directly in chat:

- When prompted for first name or Skype: Input `<javascript:alert(document.cookie);>`
- Submit the response.

> Slackbot echoes the input back, storing it in the thread.

### Step 2: Verify Storage and Rendering

**Context**: Check the DM thread to confirm the payload is rendered as a link.

No command; refresh the Slack web page and inspect the message HTML (via dev tools).

> Expected: Anchor tag with href="javascript:alert(document.cookie);" visible in source.

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
- [[stored-xss]]
