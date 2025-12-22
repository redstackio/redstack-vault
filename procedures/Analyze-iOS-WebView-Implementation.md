---
id: proc-grab-analyze-ios
tags:
  - ios
  - webview
  - analysis
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/grep-getGrabUser]]'
verified: false
platforms:
  - iOS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:22.865Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze-iOS-WebView-Implementation

## Summary

This procedure inspects the Grab help page source to confirm iOS-specific WebView exposure via a global window.grabUser object, enabling similar data theft.

## Description

By searching the https://help.grab.com/ JavaScript, the procedure reveals iOS logic using window.grabUser for user data injection into Stores.GrabUser, mirroring Android's interface but via a global variable, allowing JS access without authentication.

## Requirements

1. Web browser with dev tools
2. Access to Grab help site
3. Basic JS source inspection skills

## Defense

Defensive measures and detection strategies:

- Avoid global variables for sensitive data in WKWebView
- Use message handlers with validation instead of globals
- Obfuscate or scope user objects to prevent exposure

## Objectives

1. Identify iOS exposure mechanism
2. Confirm cross-platform vulnerability
3. Adapt payload for iOS

## Instructions

### Step 1: Inspect Help Page Source

**Context**: Load and view page source.

Visit https://help.grab.com/ and open dev tools.

### Step 2: Search for Exposure Indicators

**Context**: Use grep or browser search for key functions.

Execute [[commands/grep-getGrabUser]] on downloaded source or in console:

```bash
grep getGrabUser page_source.html
```

> Reveals: public static initGrabUser() { if(Utils.Condition.isIOSApp()){ Stores.GrabUser.setGrabUser(window.grabUser); } ... }. Expected output: JS snippet confirming window.grabUser.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/grep-getGrabUser]]

## Tools Used


## Tags

- ios
- analysis
