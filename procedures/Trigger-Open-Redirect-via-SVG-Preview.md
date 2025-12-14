---
tags:
  - open-redirect
  - javascript
  - xss
  - phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 590de3c7-6742-40f3-b815-317d22a68bce
created_at: '2025-12-14T05:32:10.321Z'
updated_at: '2025-12-14T05:32:10.321Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Trigger-Open-Redirect-via-SVG-Preview

## Summary

This procedure exploits the generated preview URL from a malicious SVG upload in Rocket.Chat to execute embedded JavaScript in a victim's browser, enabling open redirects to phishing sites or other malicious behaviors like malware downloads.

## Description

After uploading an SVG with JS, Rocket.Chat serves it via a domain-trusted URL pointing to storage.googleapis.com. Visiting this URL loads the SVG inline, executing the script in the browser's context. This can redirect users to attacker-controlled sites for credential harvesting or deliver payloads. The attack relies on social engineering to lure victims to the link within chats. Prerequisites include the uploaded file's URL; outcomes involve arbitrary JS execution without direct server compromise.

## Requirements

1. Generated preview URL from prior SVG upload
2. Victim interaction via chat or external sharing
3. Attacker-controlled phishing or payload site
4. Web browser for testing

## Defense

Defensive measures and detection strategies:

- Implement strict CSP to prevent inline script execution on file previews
- Block or strip <script> tags from uploaded SVGs
- Log and alert on redirects from file preview URLs
- Educate users on suspicious file links in chats

## Objectives

1. Execute JS via SVG preview access
2. Redirect victim to malicious site
3. Enable social engineering for phishing or malware

## Instructions

### Step 1: Share Preview URL

**Context**: Distribute the URL to potential victims through the chat or other means to initiate the attack.

Copy the generated URL (e.g., `https://open.rocket.chat/file-upload/6ksXL2Mk4MonCcTpx/svgxss.svg`) and send it in the chat with enticing text like "Check this diagram I uploaded."

> Social engineering increases click-through rates.

### Step 2: Victim Access and Execution

**Context**: When the victim visits the URL, the browser fetches and renders the SVG, triggering JS.

Victim navigates to the URL; the SVG loads from storage.googleapis.com, and the embedded script executes (e.g., `window.location = 'https://phishingsite.com';`).

> Confirm execution by monitoring the phishing site for visits or using network tools to observe redirects.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[JavaScript]]
- [[xss]]
- [[Phishing]]
