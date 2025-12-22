---
id: 123e4567-e89b-12d3-a456-426614174003
name: Verify-and-Capture-Disclosure-Evidence
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.516Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Gather Victim Host Information]]'
sub_techniques: []
tags:
  - evidence-capture
  - verification
  - persistence-check
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---

# Verify-and-Capture-Disclosure-Evidence

## Summary

This procedure involves verifying the ongoing availability of the disclosed information, capturing proof, and checking for related exposures like re-uploads, ensuring comprehensive documentation of the vulnerability.

## Description

After initial discovery, confirm if the video remains accessible. Download it for evidence, note deletions, and search for re-uploads (e.g., YouTube @bugbountypocs). Cross-reference with similar reports (#1826141) to identify patterns in platform misconfigurations, preserving integrity for responsible disclosure.

## Requirements

1. Browser download capabilities
2. Access to external sites like YouTube
3. Screenshot or screen recording software

## Defense

Defensive measures and detection strategies:

- Rapid response teams for content takedown upon violation reports
- Watermarking or metadata tracking for media files
- Logging access to attachments for anomaly detection

## Objectives

1. Preserve irrefutable evidence of the leak
2. Confirm persistence or changes in availability
3. Identify related disclosure incidents

## Instructions

### Step 1: Download Video

**Context**: Secure a local copy before potential removal.

Right-click the video and select 'Save video as' or use browser dev tools to download.

> File saved as local evidence, e.g., video.mp4.

### Step 2: Check for Re-uploads and Cross-References

**Context**: Verify external persistence and patterns.

Navigate to https://www.youtube.com/@bugbountypocs and search for the video; visit https://hackerone.com/reports/1826141 for similarities.

> Note any re-uploaded versions or analogous disclosures.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[evidence-capture]]
- [[verification]]
- [[persistence-check]]
