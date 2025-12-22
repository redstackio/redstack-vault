---
tags:
  - android
  - open-redirect
type: procedure
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/adb-start-twitterlite-with-http-redirect]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:34.644Z'
sub_techniques: []
id: 04581d59-a439-4861-b6bb-a250b8e053f3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trigger Open Redirect via http:// URI in TwitterLiteActivity

## Summary

This procedure forces the Twitter Lite WebView to load an arbitrary external HTTP site by sending an intent with an http:// URI to the exported TwitterLiteActivity, bypassing any URL checks and enabling redirects to phishing or malicious domains.

## Description

The activity accepts incoming intents without validating the scheme or host of the data URI, allowing direct loading of external http:// URLs in the WebView. This can lead to user interaction with malicious content, credential phishing, or cross-origin attacks if combined with other vulns.

## Requirements

1. ADB access to the Android device with Twitter Lite
2. A target malicious URL (e.g., http://evilzone.org)

## Defense

Defensive measures and detection strategies:

- Add intent filters to restrict data schemes to trusted ones (e.g., twitter.com domains)
- Use WebViewClient to override URL loading and validate hosts
- Enable safe browsing in WebView settings

## Objectives

1. Redirect app traffic to attacker-controlled sites
2. Facilitate phishing or UXSS attacks
3. Demonstrate lack of external URL controls

## Instructions

### Step 1: Select Malicious URL

**Context**: Choose an external site to load for testing.

Use http://evilzone.org as the redirect target.

### Step 2: Send Redirect Intent

**Context**: Launch the activity with the http:// URI.

**Command** ([[commands/adb-start-twitterlite-with-http-redirect]]):
```bash
adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "http://evilzone.org"
```

> The WebView loads the specified URL without restrictions.

**Expected Output**: External site content appears in the app.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/adb-start-twitterlite-with-http-redirect]]

## Tools Used

- [[tools/ADB-Android-Debug-Bridge]]

## Tags

- android
- open-redirect
- webview
