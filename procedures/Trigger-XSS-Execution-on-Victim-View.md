---
id: proc-trigger-xss-victim-view
tags:
  - xss
  - execution
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Desktop (Electron)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:38.755Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Trigger-XSS-Execution-on-Victim-View

## Summary

This procedure describes luring a victim to view the stored malicious message in Rocket.Chat, causing their browser to parse and execute the injected JavaScript, such as loading external scripts.

## Description

When a victim loads the chat containing the stored message, their browser renders the pre-parsed HTML from the server. The malformed <a> tag triggers event handlers like onanimationiteration, which overrides prototypes or evals code, leading to arbitrary JS execution in the victim's context. This can include fetching and running remote scripts.

## Requirements

1. Victim with access to the channel
2. Social engineering to encourage viewing (e.g., mention in message)
3. Vulnerable browser without XSS protections

## Defense

Defensive measures and detection strategies:

- Enable Content Security Policy (CSP) to block inline scripts and eval
- Use browser extensions like NoScript
- Monitor for unexpected network requests from chat pages

## Objectives

1. Cause rendering of malicious HTML in victim browser
2. Execute injected JS for payload delivery
3. Confirm execution via alerts or beacons

## Instructions

### Step 1: Lure Victim

**Context**: Use social engineering to direct the victim to the channel.

Send a follow-up message mentioning the victim or use notifications.

> Expected: Victim opens the chat.

### Step 2: Observe Execution

**Context**: As the victim views the message, the browser parses the attributes.

The payload executes automatically on render, e.g., triggering animationiteration to run eval('alert("XSS")').

> Explanation: Network tab shows fetch to external script like sectex.dev/files/cswsh.js.

### Step 3: Validate Trigger

**Context**: Check for execution indicators remotely.

Monitor attacker server for callback from loaded script.

**Expected Output**: Alert popup or console log in victim browser; remote beacon received.

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
- [[JavaScript]]

