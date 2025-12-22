---
tags:
  - ssrf
  - project-import
type: procedure
tools:
  - '[[tools/CarrierWave]]'
  - '[[tools/GitLab]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[Network Service Scanning]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 7f44abb7-336d-4834-9100-7f64bf7ef1eb
created_at: '2025-12-11T03:47:39.483Z'
updated_at: '2025-12-11T03:47:39.483Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1046]]'
---
# Import Modified Project to Trigger SSRF

## Summary

This procedure recompresses the modified export and imports it into GitLab, triggering SSRF via CarrierWave.

## Description

During import, the unsanitized remote_attachment_url is processed, fetching internal resources and attaching them to the note, enabling access to sensitive data.

## Requirements

1. Modified project tar.gz.
2. GitLab access for import.
3. Vulnerable GitLab version (e.g., 12.8.7-ee).

## Defense

Defensive measures and detection strategies:

- Patch AttributeCleaner to remove remote_attachment_url.
- Monitor network requests from GitLab to internal services.

## Objectives

1. Execute SSRF request during import.
2. Attach fetched data to note.
3. Enable viewing of internal content.

## Instructions

### Step 1: Recompress Export

**Context**: Repackage the modified files into tar.gz.

Use tar to create a new archive.

### Step 2: Import Project

**Context**: Upload and import the modified tar.gz.

Use GitLab UI to import as a new project.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Network Service Scanning]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/GitLab]]
- [[tools/CarrierWave]]

## Tags

- #ssrf
- #project-import
