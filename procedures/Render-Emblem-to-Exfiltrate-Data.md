---
id: proc-uuid-5
tags:
  - render
  - exfil
  - png
type: procedure
tools:
  - '[[tools/ImageMagick]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:27.528Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Render-Emblem-to-Exfiltrate-Data

## Summary

This final procedure submits the manipulated SVG for PNG conversion, causing ImageMagick to process XXE/XInclude and embed exfiltrated data in the output image for attacker access.

## Description

The emblem editor converts user SVG to PNG using vulnerable ImageMagick, triggering all prior payloads. Leaked data (files, HTTP responses) renders as text in the PNG, which the attacker downloads. This completes the chain; high impact as it reveals sensitive info without further interaction.

## Requirements

1. Manipulated SVG submitted
2. Access to download rendered PNG
3. Image viewer to extract text

## Defense

Defensive measures and detection strategies:

- Render images in isolated environments without network
- OCR scan outputs for sensitive data leaks
- Rate-limit SVG submissions

## Objectives

1. Trigger full payload execution
2. Obtain exfiltrated data in PNG
3. Achieve LFI/SSRF impact

## Instructions

### Step 1: Submit SVG

**Context**: Input the payload into emblem editor.

Paste the SVG with bypass and XXE/XInclude.

### Step 2: Convert to PNG

**Context**: Initiate rendering.

Click convert; download the resulting PNG.

**Expected Output**: PNG file with embedded text (e.g., hosts file contents).

### Step 3: Extract Data

**Context**: View or OCR the image.

Open PNG; leaked data visible as rendered text.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ImageMagick]]

## Tags

- render
- exfil
- png
