---
tags:
  - xss
  - svg
  - payload-creation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 41fb2751-0d30-4820-93e4-9ff1eda18972
created_at: '2025-12-14T05:32:13.286Z'
updated_at: '2025-12-14T05:32:13.286Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-SVG-Payload-for-XSS

## Summary

This procedure crafts an SVG file embedding HTML and JavaScript to exploit file upload vulnerabilities, enabling stored XSS in systems like Concrete CMS that whitelist .svg without content validation.

## Description

SVG files, per W3C SVG2 specifications, can include foreign elements like HTML, allowing script tags. This payload is created offline and uploaded to bypass restrictions on direct HTML/JS files. In the attack scenario, an admin crafts and uploads it, leading to execution when embedded. Prerequisites include a text editor; expected outcome is a file that triggers JS on render.

## Requirements

1. Text editor capable of saving XML/SVG files
2. Knowledge of basic HTML/JS for payload customization
3. Target system with SVG upload support

## Defense

Defensive measures and detection strategies:

- Validate and sanitize uploaded file contents, stripping script tags from SVGs
- Use Content Security Policy (CSP) to block inline scripts
- Monitor admin uploads for anomalous file patterns

## Objectives

1. Generate a bypass-capable payload for file upload vulns
2. Test XSS execution in whitelisted formats
3. Enable further chain to stored XSS

## Instructions

### Step 1: Draft Payload Content

**Context**: Define the SVG structure with embedded HTML to include executable JS.

Create a new file in a text editor and insert:

```xml
<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 96 105'><html><head><title>test</title></head><body><script>alert('xss');</script></body></html></svg>
```

> This creates a minimal SVG that embeds an HTML body with a script. The alert serves as a proof-of-concept; replace with malicious JS for real attacks.

### Step 2: Save and Validate File

**Context**: Ensure the file is properly formatted as .svg for upload compatibility.

Save as `malicious.svg`. Open in a browser to confirm SVG renders without immediate JS execution (it needs embedding).

> Expected: Visual SVG box appears; no alert yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[svg]]
- [[payload-creation]]
