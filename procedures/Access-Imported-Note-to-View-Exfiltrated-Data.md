---
tags:
  - data-exfiltration
  - gitlab
type: procedure
tools:
  - '[[tools/CarrierWave]]'
  - '[[tools/GitLab]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Network Service Scanning]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 432d062e-11b7-437b-9717-56f6fea356d2
created_at: '2025-12-11T03:47:39.479Z'
updated_at: '2025-12-11T03:47:39.479Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1046]]'
---
# Access Imported Note to View Exfiltrated Data

## Summary

This procedure accesses the imported project's note to view the SSRF-fetched attachment containing internal data.

## Description

After import, the note displays the downloaded file from internal services, revealing metrics, metadata, or enabling further attacks like RCE via Redis.

## Requirements

1. Successfully imported project.
2. GitLab access to view issues and notes.
3. SSRF payload that fetched viewable data.

## Defense

Defensive measures and detection strategies:

- Restrict attachments from untrusted imports.
- Audit note attachments for suspicious origins.

## Objectives

1. View exfiltrated internal data.
2. Analyze for further exploitation.
3. Achieve impact like metadata exposure or RCE.

## Instructions

### Step 1: View Note on Issue

**Context**: Access the issue and note in the imported project.

Navigate to the project's issue in GitLab UI and view the note's attachment.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Network Service Scanning]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/GitLab]]

## Tags

- #data-exfiltration
- [[tools/GitLab]]
