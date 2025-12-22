---
tags:
  - xss
  - payload-injection
type: procedure
tools:
  - '[[tools/Meyerweb-Dencoder-URL-Encoder]]'
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
updated_at: '2025-12-14T03:15:47.380Z'
sub_techniques: []
id: 71f329e1-47fa-4464-a939-5dfff2e4c474
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Mapbox-Marker-Titles

## Summary

This procedure details injecting a stored XSS payload into Mapbox classic map marker titles, exploiting the flawed stripHTML function that decodes HTML entities, allowing executable tags to persist and execute later on the share page.

## Description

Targeting the Mapbox online classic editor, this step involves crafting and inserting an XSS payload like '<img src=x onerror=alert(1) "' into a marker's title field. The editor's sanitization uses L.mapbox.sanitize followed by textContent, which inadvertently decodes entities like &lt; back to <, storing the payload. Upon sharing, it renders executable in the victim's DOM via /v3/embed/share.js or /v4/embed/share.js. Prerequisites include a created map from prior steps. Outcomes: Payload stored without editor execution, ready for victim triggering.

## Requirements

1. Access to an existing Mapbox classic map with markers
2. [[tools/Meyerweb-Dencoder-URL-Encoder]] for payload preparation
3. Knowledge of basic HTML/JS for payload crafting

## Defense

Defensive measures and detection strategies:

- Enhance sanitization to prevent entity decoding (e.g., use proper HTML escaping)
- Validate and strip executable tags in marker titles server-side
- Monitor for suspicious strings like 'onerror' in editor inputs

## Objectives

1. Store malicious JavaScript in map metadata
2. Evade client-side sanitization flaws
3. Enable execution on share page load

## Instructions

### Step 1: Prepare XSS Payload

**Context**: Encode the payload to bypass initial input rejection in the editor.

Use [[tools/Meyerweb-Dencoder-URL-Encoder]] at http://meyerweb.com/eric/tools/dencoder/ to handle the raw payload '<img src=x onerror=alert(1) "'.

> Encoded version ensures acceptance; example input yields URL-safe string for pasting.

### Step 2: Insert Payload into Marker Title

**Context**: Edit a marker's title field in the Mapbox editor and save the changes.

Paste the prepared payload into the title input and save the map.

> No immediate alert in editor; payload stored as text, decodes later in share.js.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Meyerweb-Dencoder-URL-Encoder]]

## Tags

- [[xss]]
- [[JavaScript]]
