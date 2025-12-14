---
id: quarantine-threat-file
tags:
  - quarantine
  - av-ui
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:29:44.746Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Quarantine-Threat-File

## Summary

This procedure involves interacting with the Acronis AV user interface to quarantine the modified threat file, moving it to a secure location for later exploitation during restore.

## Description

After detection and modification, use the AV overlay to select quarantine. This stores the attacker-controlled file in the AV's quarantine directory, preserving the payload for restoration. The vulnerability lies in the restore process not validating junctions, allowing redirection.

## Requirements

1. AV detection prompt visible
2. User access to AV interface
3. Modified file still in original location

## Defense

Defensive measures and detection strategies:

- Restrict quarantine/restore to admin only
- Audit all quarantine actions and restores
- Validate restore paths against whitelists

## Objectives

1. Secure the payload in quarantine
2. Prepare for junction-based redirection
3. Maintain chain integrity

## Instructions

### Step 1: Select Quarantine Option

**Context**: Confirm the action in the AV UI to isolate the file.

**Command** (None - UI Interaction):
No command; in the Acronis threat detection window, click 'Quarantine'.

> This moves 'eicar.bat' to the quarantine folder (typically under ProgramData\Acronis). Expected output: UI confirmation of quarantine.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Disable or Modify Tools]] Disable or Modify Tools

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- quarantine
- av-ui
