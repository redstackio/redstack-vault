---
tags:
  - library-hijacking
  - rce-trigger
  - app-restart
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Dynamic Linker Hijacking]]'
updated_at: '2025-12-14T17:24:42.966Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0cc5adea-2fc5-43e7-bf99-7bc13a327c1a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Dynamic Linker Hijacking]]'
---
# Restart-App-to-Execute-Malicious-Library

## Summary

This procedure forces an app restart to load the overwritten malicious native library, executing the embedded code for remote access.

## Description

After download, the tampered `libjnigraphics.so` resides in the app's lib directory. Restarting Evernote causes the Android runtime to load this library instead of the legitimate one, triggering the reverse shell payload. The vulnerability stems from the app's React Native implementation compiled to Hermes bytecode, which handles the unsanitized write.

## Requirements

1. Overwritten library in `/data/data/com.evernote/lib-1/`
2. Victim's device with the app
3. Payload configured for post-load execution

## Defense

Defensive measures and detection strategies:

- Verify library integrity on app load (checksums)
- Restrict write access to lib directories via app permissions
- Use mobile security frameworks to detect library tampering

## Objectives

1. Trigger payload execution via normal app behavior
2. Establish reverse connection without further interaction
3. Achieve persistence through library hijack

## Instructions

### Step 1: Instruct App Closure

**Context**: Ensure the malicious library is positioned for loading.

Have the victim force-close the Evernote app via device settings or recent apps.

### Step 2: Reopen App

**Context**: Initiate library load on startup.

Victim reopens Evernote; the app loads the hijacked `libjnigraphics.so`.

> Payload executes silently; connection attempts to listener if set up.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Dynamic Linker Hijacking]] Dynamic-link Library Injection

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- native-library
- execution
- android
