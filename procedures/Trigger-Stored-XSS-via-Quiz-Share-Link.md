---
id: proc-trigger-stored-xss-quiz-link
tags:
  - xss-execution
  - client-side
  - data-theft
  - polldaddy
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
updated_at: '2025-12-14T03:46:31.436Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-Quiz-Share-Link

## Summary

This procedure demonstrates sharing a Polldaddy quiz containing a stored XSS payload and accessing the link to execute the injected JavaScript in the victim's browser context.

## Description

Once the payload is stored in the quiz's Media Embed, sharing the quiz via a public link renders the content in viewers' browsers, triggering the XSS. The onerror attribute executes when the img src fails, allowing arbitrary JS like cookie theft. This targets unsuspecting users who click the link. Prerequisites: Quiz with payload saved. Outcome: Script runs client-side, potentially exfiltrating data.

## Requirements

1. Saved Polldaddy quiz with XSS payload
2. Ability to generate public share links
3. Test browser or victim simulation (e.g., incognito mode)

## Defense

Defensive measures and detection strategies:

- Content Security Policy (CSP) to block inline scripts and unsafe attributes
- Server-side rendering with output encoding for all user inputs
- Monitor quiz views for anomalous JavaScript errors or exfiltration attempts

## Objectives

1. Distribute the quiz to potential victims
2. Execute the stored payload in browser context
3. Collect sensitive data via JS (e.g., cookies, tokens)

## Instructions

### Step 1: Generate Share Link

**Context**: From the quiz dashboard, create a public link for distribution.

In Polldaddy, go to the quiz overview, click "Share" or "Publish", and generate a link (e.g., https://polldaddy.com/quiz/12345). Copy the URL.

> Web UI action. Expected output: Shareable URL provided.

### Step 2: Access Link to Trigger Payload

**Context**: Open the link in a browser to simulate victim interaction.

Paste the URL into a new browser tab or send to a test user. The quiz loads, rendering the Media Embed, which includes the img tag. The invalid src triggers onerror, executing the JS.

> Browser access. Expected output: Alert pops (for test payload) or network request for exfiltration.

### Step 3: Validate Execution

**Context**: Confirm the XSS fired using browser tools.

Open developer console (F12) before loading. Look for script execution logs or network tabs for any outbound requests from the payload.

> Dev tools check. Expected output: Console shows JS run; potential data sent if payload modified.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[client-side]]
