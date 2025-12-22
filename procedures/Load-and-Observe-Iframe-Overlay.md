---
tags:
  - iframe
  - overlay
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:44.944Z'
sub_techniques: []
id: 33fbd45e-47aa-4cba-af62-027ff7b622bd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Load-and-Observe-Iframe-Overlay

## Summary

This procedure describes delivering and opening the malicious HTML to the victim, observing the iframe as it overlays the profile page for clickjacking setup.

## Description

The victim is tricked into opening the attacker's HTML file in their browser while maintaining the UPchieve session. The small iframe displays the profile page, positioned over decoy elements, allowing the attacker to confirm the embedding works before adjustment. This step relies on the vulnerability's lack of frame protection, enabling seamless integration.

## Requirements

1. Victim's browser with active UPchieve session
2. Malicious HTML file delivered (e.g., download or link)
3. Same-origin browser context for session persistence

## Defense

Defensive measures and detection strategies:

- Browser extensions like NoScript or uBlock Origin to block iframes
- User training on phishing via file downloads
- Web Application Firewall (WAF) rules to detect anomalous iframe requests

## Objectives

1. Load the malicious page with embedded profile
2. Confirm iframe visibility and positioning
3. Observe victim interaction potential

## Instructions

### Step 1: Deliver Malicious File

**Context**: Send the HTML to the victim via social engineering.

Attach iframe.html to an email or host it and share a link, prompting the victim to open it.

> Victim downloads and runs the file in their browser.

### Step 2: Observe Iframe Display

**Context**: Verify the overlay in the victim's session.

Upon opening, the small iframe shows the profile page overlaid on the decoy content.

> Check for profile elements rendering correctly within the iframe bounds.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- iframe
- overlay
- web
