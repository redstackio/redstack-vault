---
tags:
  - path-traversal
  - deeplink
  - payload-crafting
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:27.192Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 0249333b-d495-40a6-8f62-6ef1236f7a0b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Malicious Path Traversal Deeplink

## Summary

This procedure crafts a deeplink URL exploiting path traversal in the Basecamp app's 'filename' parameter to force file saves to arbitrary locations like shared device storage.

## Description

Building on manifest analysis, this involves constructing a URL where the 'filename' query parameter includes directory traversal sequences (e.g., '../') to escape the app's intended sandbox and write to /sdcard/Download/. The attack targets deeplinks like https://3.basecamp.com/{project_id}/reports/progress, appending the malicious parameter. This enables local data exfiltration without network involvement, relying on the victim's device storage permissions.

## Requirements

1. Knowledge of target project ID or endpoint from Basecamp (e.g., 5195267)
2. Understanding of Android file paths (e.g., /sdcard/ for external storage)
3. Text editor or URL builder for crafting the payload

## Defense

Defensive measures and detection strategies:

- Sanitize 'filename' with whitelist paths and block '../' sequences
- Use scoped storage in Android 10+ to restrict app writes
- Log and alert on anomalous file write paths in app telemetry

## Objectives

1. Create a traversable filename payload
2. Integrate into valid Basecamp deeplink structure
3. Ensure payload evades basic URL parsing

## Instructions

### Step 1: Build Traversal Payload

**Context**: Design the path traversal string to reach shared storage.

Construct payload: ../../../../../../../../../../sdcard/Download/disclosure.txt (adjust depth based on app's base path).

> Expected: Payload resolves to target directory when processed.

### Step 2: Assemble Full Deeplink

**Context**: Append payload to Basecamp URL template.

Form URL: https://3.basecamp.com/5195267/reports/progress?filename=/../../../../../../../../../../sdcard/Download/disclosure.txt.

> Expected: URL is clickable and triggers app intent on device.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[path-traversal]]
- [[deeplink]]
- [[payload-crafting]]
