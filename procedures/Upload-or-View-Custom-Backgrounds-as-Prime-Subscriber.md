---
tags:
  - file-upload
  - unauth-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.083Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 495fe682-54a3-4eea-ba20-1708a12f25de
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Upload-or-View-Custom-Backgrounds-as-Prime-Subscriber

## Summary

This procedure demonstrates unauthorized interaction with custom background features on 3d.cs.money, including upload via Ctrl+V or viewing existing ones, using the bypassed session.

## Description

As the final exploitation step, this targets Prime-exclusive features vulnerable due to auth laxity. Web-based, it requires Prime status and partial session. Impact is limited to non-sensitive media access.

## Requirements

1. Prime subscriber status on CS.Money
2. Partial session on 3d.cs.money
3. Image file for upload testing

## Defense

Defensive measures and detection strategies:

- Enforce full auth for all user-generated content features
- Rate-limit uploads and log unauthorized access attempts

## Objectives

1. Upload custom background without 2FA
2. View protected content
3. Prove unauthorized feature access

## Instructions

### Step 1: Access Background Interface

**Context**: Load the feature area on the subdomain.

Once on https://3d.cs.money, locate the custom background section.

> Interface should be accessible without barriers.

### Step 2: View Existing Backgrounds

**Context**: Test read access to user-specific content.

Browse or select options to display previously uploaded backgrounds.

> Content loads if session is recognized as valid.

### Step 3: Attempt Upload

**Context**: Exploit upload functionality with keyboard shortcut.

Copy an image (Ctrl+C), then paste (Ctrl+V) in the upload area.

> Upload succeeds without additional verification; confirmation appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[unauth-access]]
