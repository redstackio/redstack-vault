---
id: proc-uuid-4
tags:
  - rce
  - library-injection
  - android
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:24:45.200Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
---
# Relaunch-Mattermost-to-Execute-Malicious-Library

## Summary

This procedure relaunches the Mattermost app after library overwrite, triggering the Android runtime to load the malicious libyoga.so during startup, resulting in arbitrary code execution. In a POC, it causes a crash, but with a tailored payload, it enables full compromise.

## Description

On app launch, React Native or native code in Mattermost loads libraries from /lib-main/, including the overwritten libyoga.so. The malicious .so executes its payload (e.g., shellcode) when loaded via System.loadLibrary(). This provides persistence as the library reloads on every app start. Prerequisites: Overwritten file in place. Expected outcome: Code execution within Mattermost's process.

## Requirements

1. Malicious library overwritten
2. Device with Mattermost
3. Ability to relaunch app

## Defense

Defensive measures and detection strategies:

- Verify library integrity with checksums on load
- Use app shielding or integrity checks
- Monitor for crashes or anomalous native loads

## Objectives

1. Trigger malicious library load
2. Achieve RCE in app context
3. Establish persistence

## Instructions

### Step 1: Force Close App

**Context**: Ensure clean relaunch.

Via ADB:

```bash
am force-stop com.mattermost.rn
```

> Stops the app process.

### Step 2: Relaunch Main Activity

**Context**: Start the app to load libraries.

Use ADB:

```bash
am start -n com.mattermost.rn/.MainActivity
```

> Triggers onCreate() and library loading.

### Step 3: Monitor Execution

**Context**: Observe payload activation.

Run:

```bash
adb logcat | grep -E "yoga|crash|native"
```

> Expected: Crash or custom log from malicious code.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Persistence]] Persistence

### Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- library-injection
- android
