---
tags:
  - xss-execution
  - victim-trigger
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.369Z'
sub_techniques: []
id: 34d9833d-792d-4e22-b1ee-a967ed96c221
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-via-Victim-Interaction

## Summary

This procedure describes how the stored XSS payload executes arbitrary JavaScript in the victim's browser when they visit the malicious Mapbox share URL or view an embedded iframe, leading to potential data theft or session hijacking.

## Description

The final exploitation phase occurs when a victim loads the share page on *.tiles.mapbox.com. The payload, stored in marker titles, is processed by share.js's stripHTML, decoding to executable <img> tags that fire onerror events, running alert(1) or custom JS. This runs in the victim's browser context, independent of the editor. No attacker action needed post-sharing; relies on social engineering for delivery. Outcomes: Full JS control over victim session.

## Requirements

1. Distributed share URL or iframe embed code
2. Victim with browser access to the URL
3. No additional tools; execution is client-side

## Defense

Defensive measures and detection strategies:

- Deploy Content Security Policy (CSP) on share pages
- Sanitize all user-generated content before DOM insertion
- Educate users on phishing via map shares

## Objectives

1. Achieve code execution in victim context
2. Enable follow-on attacks like cookie theft
3. Demonstrate impact of stored XSS

## Instructions

### Step 1: Distribute Malicious URL

**Context**: Send the share URL to the target via email, link, or embed in a controlled page.

Share the URL: https://a.tiles.mapbox.com/v4/[map-id]/page.html?access_token=....

> Victim clicks and loads the page; no visible malice initially.

### Step 2: Observe Execution

**Context**: Upon page load, the payload executes automatically in the DOM.

Monitor for alert(1) or replace with payload like document.cookie for theft.

> JS runs on image onerror; network logs show failed src=x request triggering code.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Execution]]
- [[browser]]
