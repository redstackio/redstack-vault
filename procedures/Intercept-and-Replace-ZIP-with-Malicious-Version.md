---
id: 3447cb33-39da-4fd8-8ae8-70bebd407356
name: Intercept-and-Replace-ZIP-with-Malicious-Version
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:21.761Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploitation for Client Execution]]'
tags:
  - interception
  - zip-replacement
  - path-traversal
platforms:
  - Android
tools:
  - '[[tools/PoC-Android-Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---

# Intercept-and-Replace-ZIP-with-Malicious-Version

## Summary

This procedure uses the PoC app to detect an incoming ZIP sync from LINE Keep and replace it with a malicious ZIP containing path traversal sequences for exploitation.

## Description

During LINE Android's sync process, the PoC app hooks into file downloads, identifies the memo ZIP, and overwrites it with a crafted archive. The malicious ZIP includes entries with traversal paths like '../../../../../../../data/data/jp.naver.line.android/files/something' to target private app directories. This sets up the extraction vulnerability without user notice. The target environment is Android with LINE app v10.x or vulnerable versions.

## Requirements

1. PoC app installed and running with STORAGE permission
2. LINE account synced with a pending memo ZIP
3. Malicious ZIP pre-crafted with traversal payloads

## Defense

Defensive measures and detection strategies:

- Validate ZIP integrity on download with checksums
- Sandbox file syncs to prevent interception
- Log and alert on unexpected file modifications in app storage

## Objectives

1. Detect and isolate the legitimate ZIP during sync
2. Substitute with malicious version seamlessly
3. Ensure traversal paths target sensitive private files

## Instructions

### Step 1: Trigger Sync in LINE Android

**Context**: Initiate download to activate interception.

No command; open LINE Android, go to Keep, pull to refresh.

> PoC app monitors in background.

### Step 2: Automatic Replacement

**Context**: PoC app performs the swap.

No manual command; the app automatically replaces the ZIP with the malicious one upon detection.

> Verify via app logs if replacement succeeded.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PoC-Android-Application]]

## Tags

- [[interception]]
- [[zip-replacement]]
- [[path-traversal]]
