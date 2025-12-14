---
tags:
  - phishing
  - social-engineering
  - clickjacking
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:05.078Z'
sub_techniques: []
id: 7c7da860-9823-41cc-9d61-080420c90f66
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trick-Victim-into-Clickjacking-Interaction

## Summary

This procedure involves luring an authenticated Crossclip user to the malicious clickjacking page, inducing interactions that lead to unintended clip deletions or privacy changes via overlaid iframe elements.

## Description

With the victim logged into Crossclip, the attacker distributes the malicious page via phishing (e.g., email link disguised as a clip share). The page uses visual deception or prompts (e.g., "Click to view") over transparent divs aligned with iframe buttons. No confirmation dialogs appear, enabling stealthy actions like two clicks to toggle privacy or delete. Prerequisites: Victim's authentication and social engineering vector. Outcomes: Data loss (deleted clips) or exposure control (privacy alterations), impacting user trust and data integrity.

## Requirements

1. Hosted malicious HTML page
2. Phishing delivery method (email, social media)
3. Victim authenticated to Crossclip

## Defense

Defensive measures and detection strategies:

- User training on suspicious links and unexpected interactions
- Browser warnings for cross-origin iframes (if CSP implemented)
- Application logging of rapid data changes for anomaly detection
- Rate limiting on sensitive actions like deletes

## Objectives

1. Induce victim to visit and interact with the malicious page
2. Execute unauthorized actions via click hijacking
3. Achieve data manipulation without detection

## Instructions

### Step 1: Prepare Phishing Lure

**Context**: Craft a deceptive message to direct victim to the page.

Create an email or message: "Check out this clip: [malicious-link]" where malicious-link points to the hosted HTML.

> Manual creation. Expected output: Convincing lure ready for distribution.

### Step 2: Distribute to Victim

**Context**: Send the link to the target user.

Deliver via email, chat, or social platform, ensuring the victim is logged into Crossclip (e.g., recent session).

> Manual sending. Expected output: Victim clicks and loads the page; iframe authenticates via cookies.

### Step 3: Induce and Verify Interaction

**Context**: Prompt clicks on overlays to trigger actions.

The page may show a button like "Play Video" over the delete button. Victim clicks 1-2 times; actions occur in iframe.

> As demonstrated in POC video. Expected output: Clips deleted or privacy changed; verify via app or notifications.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- Phishing tools (optional, e.g., email client)

## Tags

- [[Phishing]]
- [[user-execution]]
