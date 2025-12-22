---
id: proc-inject-bandcamp-url
tags:
  - xss
  - payload-injection
  - bandcamp
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
updated_at: '2025-12-14T03:47:12.761Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Bandcamp-URL

## Summary

This procedure details crafting and injecting a malicious URL into the Discourse topic title field, exploiting the permissive Bandcamp preview regex to fetch unsanitized OpenGraph metadata from an attacker-controlled server.

## Description

The Bandcamp preview engine uses a regex `^https?://.*bandcamp\.com\/album\/` that matches any domain ending in bandcamp.com/album/, allowing evasion via IP addresses with path mimicking the structure (e.g., /bandcamp.com/album/). The injected URL points to a server hosting HTML with OpenGraph tags containing XSS payloads, which are rendered without escaping, leading to JavaScript execution.

## Requirements

1. Attacker-controlled web server hosting the malicious page
2. Malicious HTML with OpenGraph metadata like `<meta property="og:title" content="<script>alert('XSS')</script>">`
3. Access to Discourse composer title field

## Defense

Defensive measures and detection strategies:

- Tighten URL regex to exact domain matching (e.g., ^https?://(?:[^/]+\.)*bandcamp\.com\/album\/)
- Sanitize all fetched OpenGraph data with HTML escaping
- Validate external fetches against allowlists

## Objectives

1. Bypass URL validation for preview triggering
2. Deliver XSS payload via metadata
3. Persist injection in stored topic

## Instructions

### Step 1: Craft Malicious URL

**Context**: Create a URL that evades the regex while directing to your server.

Construct URL: https://<your-ip>/bandcamp.com/album/index.html?XSSa2

> Ensure the server at <your-ip> serves HTML with injected OpenGraph tags.

### Step 2: Paste into Title Field

**Context**: Inject the URL into the composer to queue preview fetch.

Paste the crafted URL into the title field placeholder 'Type title or paste a link here'.

> The field accepts the input; no validation blocks the IP-based path.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[url-injection]]
