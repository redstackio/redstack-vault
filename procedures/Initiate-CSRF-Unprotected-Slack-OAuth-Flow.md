---
id: proc-csrf-slack-oauth-init
tags:
  - csrf
  - oauth
  - slack
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/get-hackerone-slack-auth]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.815Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-CSRF-Unprotected-Slack-OAuth-Flow

## Summary

This procedure exploits the absence of CSRF protection in HackerOne's Slack integration OAuth initiation, allowing an attacker to force a logged-in user's browser to start the flow via a malicious link or form submission, redirecting to Slack without validation.

## Description

The vulnerability stems from the `/auth/slack` endpoint relying solely on Slack's state parameter for security, without server-side CSRF token checks. An attacker can embed a simple GET request in a webpage, tricking the victim into loading it while authenticated on HackerOne. This initiates the OAuth redirect to Slack, setting up for further exploitation. Prerequisites include victim authentication on HackerOne and delivery of the malicious payload (e.g., via email or another site). Expected outcome: Unprotected OAuth start, exposing the flow to manipulation.

## Requirements

1. Victim logged into HackerOne at `https://hackerone.com`
2. Attacker-controlled webpage or link to deliver the CSRF payload
3. Browser access to internet for redirects to slack.com

## Defense

Defensive measures and detection strategies:

- Implement server-side CSRF token generation and validation on OAuth initiation endpoints
- Monitor for anomalous OAuth starts from unusual referers or without tokens
- Use Content-Security-Policy (CSP) to block unauthorized form submissions

## Objectives

1. Force initiation of Slack OAuth without protection
2. Redirect victim to Slack authorize endpoint with controllable parameters
3. Position for callback forgery in subsequent steps

## Instructions

### Step 1: Craft Malicious Payload

**Context**: Create an HTML page that automatically submits the CSRF request to bypass user interaction.

**Command** ([[commands/get-hackerone-slack-auth]]):
```bash
GET https://hackerone.com/auth/slack HTTP/1.1
```

> This command simulates the request; in practice, embed it in an auto-submitting form: `<form action="https://hackerone.com/auth/slack" method="GET"></form><script>document.forms[0].submit();</script>`. Expected output: 302 redirect to Slack's OAuth URL with client_id, redirect_uri, etc.

### Step 2: Deliver to Victim

**Context**: Host the HTML on an attacker site and phish the victim to visit it while logged into HackerOne.

No command needed; use social engineering. Expected output: Victim's browser follows the redirect to Slack.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/get-hackerone-slack-auth]]

## Tools Used


## Tags

- [[csrf]]
- [[oauth]]
- [[slack]]
