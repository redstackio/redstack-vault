---
id: proc-uuid-3
tags:
  - xss
  - poc
  - jetpack
type: procedure
tools:
  - '[[tools/publicwww-com]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:20.877Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Jetpack-XSS-via-PoC-Link

## Summary

This procedure delivers the chained exploit via a proof-of-concept HTML link that automates the widgets.wp.com XSS and postMessage to execute arbitrary JS on the target Jetpack site.

## Description

A simple HTML page hosts a clickable link that loads the malicious preview URL and handles the cross-origin communication. When clicked, it triggers the full chain, inserting the payload into the Jetpack Likes DOM via innerHTML. Use [[tools/publicwww-com]] to find vulnerable sites. Outcomes: JS execution like alerts or data exfiltration on the target domain.

## Requirements

1. Hosted PoC HTML accessible via URL
2. Target site with Jetpack Likes feature
3. Victim interaction (clicking the link)

## Defense

Defensive measures and detection strategies:

- Patch Jetpack to encode postMessage payloads
- Disable or audit third-party widgets like sharing buttons
- Educate users on phishing links

## Objectives

1. Automate exploit delivery for realism
2. Execute JS on target without direct access
3. Demonstrate impact on multiple domains

## Instructions

### Step 1: Prepare PoC HTML

**Context**: Create or use an HTML file that embeds the exploit logic.

Example PoC content: `<a href="https://widgets.wp.com/sharing-buttons-preview/?custom[0][name]=..." target="_blank" onclick="postMessageToTarget(this.href)">Click for Preview</a>`, with JS to send message on load.

> Host at e.g., https://0-a.nl/jetpackxssclick.html?url=https://wordpress.com/blog/2024/01/31/http3/. Expected: Link ready for sharing.

### Step 2: Trigger and Validate

**Context**: Click the link to chain the attack and confirm execution.

Navigate to PoC, click link; new window opens widgets.wp.com, sends message, triggers alert on target.

> Success: Alert fires on target domain. Use [[tools/publicwww-com]] to search for more targets: query for Jetpack Likes code snippets.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/publicwww-com]]

## Tags

- xss
- poc
