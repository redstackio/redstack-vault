---
tags:
  - javascript
  - webview
  - exposure
type: procedure
tools:
  - '[[tools/grep]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/grep-search-string]]'
platforms:
  - Android
  - iOS
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f8d8f6fc-89ba-4486-97a0-b3dcf1e85f3d
created_at: '2025-12-11T06:10:22.728Z'
updated_at: '2025-12-11T06:10:22.728Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Identify Exposed JavaScript Interfaces in WebView

## Summary

This procedure discovers JavaScript interfaces added to WebViews that expose native methods, allowing access to sensitive data without origin checks.

## Description

In the Grab app, the WebView adds an 'Android' interface with getGrabUser method, returning serialized user data. This is identified through code analysis, targeting WebView implementations in mobile apps.

## Requirements

1. Decompiled app source
2. Knowledge of WebView APIs
3. Testing environment to invoke interfaces

## Defense

Defensive measures and detection strategies:

- Add origin whitelisting to JavaScript interfaces
- Use @JavascriptInterface annotations sparingly

## Objectives

1. Locate added JavaScript interfaces
2. Analyze exposed methods for sensitive data
3. Confirm lack of restrictions

## Instructions

### Step 1: Search for WebView Additions

**Context**: Inspect code for addJavascriptInterface calls.

Look for interfaces named 'Android' with methods like getGrabUser.

> Expect to find serialization via GsonUtils.

### Step 2: Test Interface Access

**Context**: Load a test page in WebView to call the method.

Use JavaScript like window.Android.getGrabUser() to retrieve data.

> Validation: Sensitive user info is returned.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[JavaScript]]
- [[webview]]
