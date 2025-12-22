---
id: proc-uuid-3
tags:
  - gitlab
  - import
  - bypass
type: procedure
tools:
  - '[[tools/GitLab]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:56:03.862Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Import-Modified-GitLab-Project

## Summary

This procedure imports the tampered project export into GitLab, processing the Note objects with the injected XSS payload intact due to the bypassed cache regeneration.

## Description

During import, GitLab's logic checks cached_markdown_version against an invalidations array, which can become empty due to changed_attributes handling. This flaw allows the malicious note_html to load directly without markdown-to-HTML conversion, storing the XSS persistently.

## Requirements

1. Modified project export archive
2. GitLab account with import permissions
3. Target GitLab instance

## Defense

Defensive measures and detection strategies:

- Force full data validation and cache reset on all imports
- Log and review import payloads for anomalies
- Restrict import features to trusted sources

## Objectives

1. Successfully import project without triggering regeneration
2. Preserve injected note_html in database
3. Set up for XSS execution in discussions

## Instructions

### Step 1: Start New Project Import

**Context**: Initiate the import process in GitLab UI.

Log in, go to 'New project', select 'Import project', and choose 'GitLab export' option.

### Step 2: Upload and Complete Import

**Context**: Submit the modified archive for processing.

Upload the .tar.gz file and follow prompts to complete import. Monitor for errors.

**Expected Output**: New project created with imported discussions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GitLab]]

## Tags

- [[tools/GitLab]]
- [[import]]
- [[bypass]]
