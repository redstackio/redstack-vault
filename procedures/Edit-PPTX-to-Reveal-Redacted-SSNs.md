---
tags:
  - pii-leak
  - information-disclosure
  - redaction-bypass
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:24:56.461Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
id: d13f87d4-4ac3-4d35-8a61-3886ec9a5c08
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Edit-PPTX-to-Reveal-Redacted-SSNs

## Summary

This procedure demonstrates editing the PowerPoint file to remove or adjust redaction overlays, exposing full SSNs hidden in screenshots of health records.

## Description

PPTX files are ZIP archives with editable XML and image components. Attackers unzip the file, modify redaction elements (e.g., black rectangles over text), and repackage it. In the context of DoD documents, this bypasses superficial redactions, revealing complete PII. Prerequisites include the downloaded file; outcomes enable full identity data exfiltration for theft or reconnaissance.

## Requirements

1. PowerPoint editor or ZIP tools (e.g., unzip, zip)
2. Downloaded PPTX with redacted content
3. Image editing knowledge for screenshot alterations

## Defense

Defensive measures and detection strategies:

- Use irreversible redaction (e.g., crop or pixelate images, not cover with shapes)
- Encrypt sensitive documents and restrict public hosting
- Implement file scanning for editable formats before upload

## Objectives

1. Bypass redaction layers to uncover SSNs
2. Confirm vulnerability in document security
3. Compile complete PII dataset

## Instructions

### Step 1: Unzip the PPTX Archive

**Context**: Extract components to access editable slides and images.

```bash
unzip HR_TECH_WOBC_Perform_eMILPO_Functions_eMILPO_Brief.pptx -d temp_pptx
```

> Expected output: Directory with ppt/slides/, ppt/media/ folders containing XML and images.

### Step 2: Edit Redaction in Slides or Images

**Context**: Remove blackout shapes from XML or edit underlying images.

For XML edits:

```bash
# Example: Edit slide XML to remove shape elements
sed -i '/<a:schemeClr val="blk"/,/<\/a:solidFill>/d' temp_pptx/ppt/slides/slide13.xml
# For images, use an editor like GIMP on ppt/media/imageX.png to uncover text
```

> Re-zip after edits: cd temp_pptx; zip -r ../revealed.pptx * . Expected: Full SSNs visible upon reopening.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- redaction-bypass
- pii-recovery
