---
tags:
  - exfiltration
  - rendering
type: procedure
tools:
  - '[[tools/ImageMagick]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/upload-svg-payload]]'
platforms:
  - Web
  - Windows
techniques:
  - '[[Unsecured Credentials]]'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
id: 109e24a3-cf24-45ec-b7b9-8bc15d3621f6
created_at: '2025-12-13T09:00:28.098Z'
updated_at: '2025-12-13T09:00:28.098Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Render Extracted Data on Emblem

## Summary

This procedure renders extracted sensitive data within the SVG, converting it to PNG for visual exfiltration on the crew emblem.

## Description

After extraction via XXE or XIncludes, the data is embedded in SVG elements like patterns or text, then converted to PNG by ImageMagick, making it visible on the emblem.

## Requirements

1. Extracted data from prior steps
2. Access to emblem viewer
3. SVG with embedded data

## Defense

Defensive measures and detection strategies:

- Monitor emblem creations for anomalous content
- Rate-limit conversions and audit outputs

## Objectives

1. Embed extracted data in SVG
2. Convert to PNG
3. Exfiltrate via visual inspection

## Instructions

### Step 1: Finalize and Upload SVG

**Context**: Upload SVG with extracted content for rendering.

**Command** ([[commands/upload-svg-payload]]):
```bash
curl -X POST -F 'file=@final-malicious.svg' https://emblem-editor-endpoint
```

> Converts SVG to PNG, rendering data on emblem.

### Step 2: View Emblem

**Context**: Check the generated emblem for exfiltrated data.

> Access the crew emblem in the game or editor to view the PNG.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques



## Commands Used

- [[commands/upload-svg-payload]]

## Tools Used

- [[tools/ImageMagick]]

## Tags

- [[Exfiltration]]
- [[rendering]]
