---
id: 168438eb-0fa9-4466-8524-2b629ed0e051
name: Open-Malicious-ZIP-in-LINE-Android
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:21.753Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploitation for Client Execution]]'
tags:
  - extraction
  - zip-open
  - android
platforms:
  - Android
tools: []
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---

# Open-Malicious-ZIP-in-LINE-Android

## Summary

This procedure triggers the vulnerable ZIP extraction in the LINE Android app by opening the replaced malicious file, initiating the path traversal exploit.

## Description

User interaction in the LINE app UI opens the ZIP note, calling the Keep service's extraction routine. The unsafe unzipping fails to sanitize entry names, allowing '../' sequences to traverse to private directories like /data/data/jp.naver.line.android/files/. This leads to overwrite before a SecurityException crashes the app. Targets vulnerable LINE Android versions prior to patch.

## Requirements

1. Malicious ZIP in LINE Keep
2. LINE Android app installed and open
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Patch ZIP extraction to validate paths
- Crash reporting to detect traversal attempts
- Restrict extraction to app-private directories only

## Objectives

1. Invoke the extraction routine on malicious ZIP
2. Exploit path traversal for file overwrite
3. Trigger crash as indicator of success

## Instructions

### Step 1: Navigate to Keep

**Context**: Locate the malicious ZIP note.

No command; in LINE Android, go to Keep section.

> Ensure the replaced ZIP is listed.

### Step 2: Tap to Open

**Context**: Start extraction process.

No command; tap the ZIP note to view contents.

> App processes the file immediately.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[extraction]]
- [[zip-open]]
- [[android]]
