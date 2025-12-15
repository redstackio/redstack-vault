---
id: proc-uuid-004
tags:
  - clickjacking
  - framing
  - ui-redress
type: procedure
tools:
  - '[[tools/Burp-Clickbandit]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:24:31.728Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Demonstrate-Clickjacking-on-dev-twitter-com

## Summary

This procedure demonstrates clickjacking by embedding the XSS-vulnerable page in an iframe without X-Frame-Options, overlaying invisible elements to force clicks on the malicious link.

## Description

Absence of frame-busting headers allows iframe embedding. Combine with XSS page to trick users. Scenario: Host PoC HTML that loads dev.twitter.com XSS URL in iframe, overlay button labeled 'Click Here' over the link. Outcome: User clicks trigger XSS without awareness.

## Requirements

1. [[tools/Burp-Clickbandit]] or manual HTML crafting
2. Local web server for PoC
3. Browser for testing

## Defense

Defensive measures and detection strategies:

- Add X-Frame-Options: DENY or SAMEORIGIN
- Use frame-ancestors in CSP
- Monitor for iframe embeddings in logs

## Objectives

1. Embed vulnerable page in iframe
2. Overlay deceptive UI
3. Trigger XSS via forced click

## Instructions

### Step 1: Confirm Framing Vulnerability

**Context**: Test if dev.twitter.com can be iframed.

Create simple HTML: <iframe src="https://dev.twitter.com//x:1/:///%01javascript:alert(document.cookie)/"></iframe> and load locally.

**Expected Output**: Iframe loads content.

### Step 2: Generate Clickjacking PoC

**Context**: Use tool to create overlay.

Run Burp Clickbandit to target the XSS URL, generating HTML with invisible overlay.

Host and access the PoC; simulate user interaction.

> PoC tricks click to execute javascript:alert.

**Expected Output**: XSS fires on 'innocent' click.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Clickbandit]]

## Tags

- [[clickjacking]]
- [[ui-redress]]
