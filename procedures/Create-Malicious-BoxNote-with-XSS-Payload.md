---
id: proc-slack-boxnote-inject-001
tags:
  - xss
  - injection
  - javascript
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
updated_at: '2025-12-14T03:16:37.485Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-BoxNote-with-XSS-Payload

## Summary

This procedure involves crafting and injecting a malicious JavaScript payload into a Slack BoxNote snippet, exploiting poor sanitization to store executable code that persists for later team-wide exploitation.

## Description

In the context of Slack's BoxNote feature on files.slack.com, user-supplied content is not properly escaped when stored. By injecting a payload that includes script tags and event handlers, an attacker can embed JavaScript that executes in the browser of any authenticated user viewing the raw content. This targets web-based collaboration environments where team members share files, leading to potential arbitrary code execution, session theft, or data exfiltration. Prerequisites include authenticated access to a Slack workspace.

## Requirements

1. Authenticated Slack account with permission to create BoxNotes
2. Web browser for interacting with Slack's interface
3. Knowledge of XSS payloads to bypass basic filtering

## Defense

Defensive measures and detection strategies:

- Implement strict content sanitization using libraries like DOMPurify for all user inputs in shared files
- Disable or restrict 'view raw' features for untrusted content
- Monitor for anomalous JavaScript execution in browser consoles or via Content Security Policy (CSP) violations

## Objectives

1. Store malicious JavaScript in a BoxNote without immediate detection
2. Ensure payload survives storage and retrieval
3. Prepare for execution in victim browsers

## Instructions

### Step 1: Access BoxNote Creation

**Context**: Log into Slack and navigate to the BoxNote creation tool to begin inputting content.

Open Slack in your web browser, go to a channel, and start a new BoxNote via the '+' menu or search for BoxNote integration.

### Step 2: Inject the Payload

**Context**: Enter the malicious payload into the BoxNote content field to exploit sanitization flaws.

Input the following payload: `XSS") ;</script> <img src="<img src=search"/onerror=alert(document.domain)//"> "><marquee>`. This closes any open script contexts, injects an img tag with an onerror handler to execute `alert(document.domain)`, and adds a marquee for obfuscation.

### Step 3: Save the Snippet

**Context**: Save the BoxNote to store the payload on files.slack.com.

Click save or submit the BoxNote. Verify it appears in your Slack files without triggering alerts.

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
- [[injection]]
