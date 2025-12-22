---
tags:
  - android
  - decompile
  - reconnaissance
  - domain-takeover
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Android
techniques:
  - '[[Hardware]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c7da5717-16e0-4e46-8c11-9ed5608ef038
created_at: '2025-12-14T04:38:39.405Z'
updated_at: '2025-12-14T04:38:39.405Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Decompile-and-Analyze-Android-App-for-Dangling-Domains

## Summary

This procedure involves decompiling an Android APK to inspect its source code for hardcoded domain references that may be unregistered, enabling domain takeover attacks.

## Description

In scenarios like the Basecamp3 app, attackers review decompiled code to find intents or URLs referencing domains similar to the company's official ones (e.g., '3737signals.com' vs. '37signals.com'). If unregistered, this allows takeover for malicious use. Prerequisites include obtaining the APK and a decompiler; outcomes include identifying exploitable dangling references.

## Requirements

1. Access to the target Android APK file
2. Decompilation tool like JADX or APKTool installed
3. Basic knowledge of Android intent handling and Java/Smali code

## Defense

Defensive measures and detection strategies:

- Perform static code analysis on apps to remove or secure hardcoded domains
- Register all potentially referenced domains proactively
- Monitor for app updates that fix such references

## Objectives

1. Locate hardcoded domains in app code
2. Assess if they are owned by the company
3. Flag potential takeover risks

## Instructions

### Step 1: Obtain and Decompile APK

**Context**: Acquire the app and extract readable source code.

Download the Basecamp3 APK from a trusted source like the Google Play Store (using tools like APK Downloader if needed). Open it in JADX GUI or run via command line to decompile.

### Step 2: Search for Domain References

**Context**: Scan decompiled files for suspicious URLs or intents.

Navigate to the decompiled Java/Kotlin sources, particularly in activity or intent-related classes. Use search functionality (Ctrl+F in JADX) for strings like '3737signals.com' or patterns matching company domains.

**Expected Output**: Code line showing intent.putExtra("url", "http://3737signals.com"); or similar.

### Step 3: Document Findings

**Context**: Note the context of the reference for impact assessment.

Record the file path, class, and usage (e.g., passed to WebView intent). Infer if it's a fallback or error URL.

**Expected Output**: Screenshot or excerpt of the vulnerable code.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[android]]
- [[decompile]]
- [[Reconnaissance]]
- [[domain-takeover]]
