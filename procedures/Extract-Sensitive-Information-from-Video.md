---
id: 123e4567-e89b-12d3-a456-426614174002
name: Extract-Sensitive-Information-from-Video
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.217Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Information Repositories]]'
sub_techniques: []
tags:
  - information-disclosure
  - data-extraction
  - video-analysis
commands: []
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---

# Extract-Sensitive-Information-from-Video

## Summary

This procedure details the analysis of a video attachment in a public report to extract accidentally disclosed sensitive details, such as private bug report IDs, titles, severities, company names, and subdomains, enabling potential exploitation.

## Description

The video contains unredacted screenshots or recordings from private HackerOne programs, showing details like report #1841996 ("Deleted Admin still can invite admins and delete owner of the portal at ██████", High severity, ██████████) and #1838699 ("sql error disclose internal system path", Low severity, ██████). This extraction highlights a Code of Conduct violation and high-impact privacy breach, with outcomes including public knowledge of unfixed flaws.

## Requirements

1. Access to the playing video
2. Note-taking tools (e.g., text editor or screenshot utility)
3. Basic understanding of bug bounty report formats

## Defense

Defensive measures and detection strategies:

- Enforce multi-stage review for all attachments in disclosures
- Apply automated redaction to media files
- Audit video content for private data leaks post-upload

## Objectives

1. Identify and document exposed private report details
2. Assess the severity and potential exploitation risks
3. Compile evidence of the disclosure

## Instructions

### Step 1: Play and Pause Video

**Context**: Review the video frame-by-frame to spot sensitive elements.

Play the video and pause at timestamps showing redacted text or overlays.

> Visible details include bug types, subdomains, and report references.

### Step 2: Document Extracted Data

**Context**: Record all disclosed information systematically.

Note down elements like company names (█████), severities (High/Low), and titles.

> Create a list or table of findings for reporting.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[data-extraction]]
- [[video-analysis]]
