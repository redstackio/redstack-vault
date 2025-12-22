---
id: proc-twitter-trigger-001
tags:
  - twitter
  - ios
  - webview
  - url-scheme
  - facetime
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
  - Web (WebView)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:44.709Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trigger-URL-Scheme-via-Twitter-iOS-WebView

## Summary

This procedure delivers the malicious HTML payload via the Twitter iOS app, exploiting the app's web view to automatically invoke the FaceTime URL scheme and initiate an unauthorized call, leaking the victim's caller ID.

## Description

The Twitter iOS app's web view lacks restrictions on iframe-embedded URL schemes, allowing silent native app launches. By sharing a link to the hosted HTML in a tweet or DM, an attacker can target victims browsing Twitter on iOS. Upon loading, the web view triggers FaceTime, exposing the user's email/phone without consent. This is effective on iOS 8+ and relies on social engineering for link clicks.

## Requirements

1. Hosted malicious HTML from the embedding procedure
2. Twitter account to share the link
3. Victim using Twitter iOS app with FaceTime enabled
4. Attacker's FaceTime account to receive the call

## Defense

Defensive measures and detection strategies:

- App developers should block or prompt for custom URL schemes in web views
- Implement web view sandboxing to prevent native app invocation
- User training on phishing links in social apps
- Log and alert on unexpected FaceTime initiations

## Objectives

1. Induce victim to load payload in vulnerable web view
2. Achieve silent call initiation
3. Collect leaked caller ID for further targeting

## Instructions

### Step 1: Share the Malicious Link in Twitter

**Context**: Post or DM the hosted HTML URL to entice the victim to click it within the Twitter app.

Example tweet: "Check out this interesting page: http://binaryfactory.ca/urlschemes/facetime.html"

> The link appears innocuous but loads the iframe in the app's web view.

### Step 2: Monitor for Execution

**Context**: Wait for the victim to open the link on iOS, triggering the call.

On the attacker's FaceTime device, expect an incoming audio call from the victim's account.

> Success: Call rings with victim's email/phone displayed as caller ID, confirming leakage.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[twitter]]
- [[ios]]
- [[webview]]
- [[url-scheme]]
- [[facetime]]
