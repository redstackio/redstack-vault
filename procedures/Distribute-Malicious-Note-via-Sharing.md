---
id: proc-distribute-note
tags:
  - phishing
  - sharing
  - simplenote
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Desktop
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:23:36.296Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Distribute-Malicious-Note-via-Sharing

## Summary

This procedure uses Simplenote's tag-based sharing system to distribute the malicious note to targeted users, who achieve RCE upon previewing.

## Description

Simplenote allows sharing notes via tags linked to email addresses, enabling phishing-like distribution without direct file attachments. Targets must have Simplenote accounts.

## Requirements

1. Malicious note created
2. Target email addresses
3. Attacker's Simplenote account

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious shared notes
- Implement note scanning for malicious HTML
- Limit sharing to trusted contacts

## Objectives

1. Share note with targets
2. Prompt preview for execution
3. Achieve lateral RCE

## Instructions

### Step 1: Add Tags for Sharing

**Context**: In the note, add tags like #target1@ victim@example.com.

Save and use Simplenote's share feature.

> Expected: Notification sent to targets; they can access and preview.

### Step 2: Monitor Distribution

**Context**: Wait for targets to open and preview.

> Success: RCE on targets' machines via the chain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment (adapted to note sharing)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- phishing
- distribution
