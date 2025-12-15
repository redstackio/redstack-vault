---
tags:
  - pii-leak
  - information-disclosure
  - health-records
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
updated_at: '2025-12-14T17:24:56.466Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
id: bc749c5d-fde2-4925-a80b-c3c06808e811
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Examine-Slides-for-PII-Leakage

## Summary

This procedure focuses on inspecting specific slides within the downloaded PowerPoint file to identify leaked PII from screenshots of soldiers' medical records, including names, CIV#, PAD DSN#, and health details.

## Description

Once the PPTX is obtained, attackers open it in a compatible viewer to scrutinize slides like slide 13, which contain unredacted screenshots from the eMILPO system. The target environment is the local file system post-download. This step uncovers visible sensitive data, enabling reconnaissance for identity exploitation. Outcomes include cataloging PII for potential theft or social engineering.

## Requirements

1. Downloaded PPTX file from the public URL
2. PowerPoint software or compatible viewer (e.g., LibreOffice)
3. Basic file navigation skills

## Defense

Defensive measures and detection strategies:

- Redact all PII in documents before public sharing using secure methods (e.g., pixel-level removal, not overlays)
- Audit training materials for sensitive embeds and use DLP tools to scan uploads
- Monitor access logs for unusual downloads of media files

## Objectives

1. Locate slides with health record screenshots
2. Extract visible PII elements
3. Assess redaction quality for further steps

## Instructions

### Step 1: Open and Navigate to Suspect Slides

**Context**: Load the file and jump to slides known or suspected to contain screenshots.

Use PowerPoint GUI or convert for inspection:

```bash
libreoffice HR_TECH_WOBC_Perform_eMILPO_Functions_eMILPO_Brief.pptx
# Navigate to slide 13 manually
```

> Expected output: Slides display with embedded images showing medical interfaces and text overlays.

### Step 2: Document Visible PII

**Context**: Note down names, numbers, and health info from screenshots.

Screenshot or copy text:

```bash
# For text extraction, unzip and grep XML:
unzip -p HR_TECH_WOBC_Perform_eMILPO_Functions_eMILPO_Brief.pptx ppt/slides/slide13.xml | grep -i "name\|civ\|dsn"
```

> Output: Extracts strings like soldier names and IDs if not fully image-based.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- pii-leak
- slide-examination
