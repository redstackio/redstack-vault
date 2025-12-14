---
tags:
  - clickjacking
  - ui-redressing
  - html
  - iframe
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.873Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: fb2df615-ebac-4595-8371-c733711909a6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Clickjacking-HTML-Page-with-Embedded-Twitter-Card

## Summary

This procedure constructs a simple HTML page that embeds a vulnerable Twitter card URL in an iframe, setting up the infrastructure for UI redressing to capture user interactions without detection.

## Description

The attacker creates a webpage hosted on their domain that loads the Twitter card in an invisible or overlaid iframe. When victims interact, it appears as a normal page action but triggers data submission to the attacker. This targets web browsers and requires no special privileges, with outcomes being a deployable malicious page ready for distribution.

## Requirements

1. Text editor for HTML creation
2. Web hosting service for the malicious page
3. Identified vulnerable Twitter card URL from prior reconnaissance

## Defense

Defensive measures and detection strategies:

- Enforce Content-Security-Policy (CSP) frames to restrict iframing
- Scan hosted content for suspicious iframes using security tools
- Browser extensions that detect clickjacking overlays

## Objectives

1. Embed vulnerable content seamlessly
2. Position iframe for deceptive clicks
3. Host page for victim access

## Instructions

### Step 1: Author HTML File

**Context**: Write basic HTML to include an iframe sourcing the Twitter URL.

Create a file named index.html with the following content:

```html
<html>
<iframe src="https://twitter.com/i/cards/tfw/v1/759046372544741376?cardname=promotion&autoplay_disabled=true&earned=true&lang=en&card_height=357" width="100%" height="400"></iframe>
</html>
```

> This embeds the page without restrictions due to missing headers.

### Step 2: Host and Test Page

**Context**: Upload to a server and verify embedding works.

Host the file on a web server (e.g., via GitHub Pages or a VPS). Visit the hosted URL in a browser to confirm the iframe loads the Twitter content.

> Ensure no console errors and that interactions are possible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[clickjacking]]
- [[ui-redressing]]
- [[html]]
- [[iframe]]
