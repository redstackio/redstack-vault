---
url: 'https://github.com/SurveyMonkey/surveymonkey-android-sdk/'
tags:
  - sdk
  - webview
  - xss
type: tool
verified: false
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.910Z'
id: eca55a9f-e9c0-4166-9379-81bfa53ee23c
validated: true
submitted: true
---
# SurveyMonkey-Android-SDK

**Status**: Unverified

## Overview

The SurveyMonkey Android SDK is used for integrating user surveys and feedback collection into Android apps, but its improper implementation can lead to vulnerabilities like exported activities and unsanitized WebView loads enabling XSS.

## Description

This SDK provides components like SMFeedbackActivity for displaying surveys via WebView, loading HTML from Intent Extras with JavaScript enabled. In the Exness app, it's misconfigured with exported activity and direct extra passing to loadDataWithBaseURL, allowing external injection.

## Features

- Feature 1: Survey embedding via fragments/activities
- Feature 2: WebView-based feedback collection with custom HTML/URL
- Feature 3: Analytics integration for user responses

## Installation

### Requirements

- Android Studio
- Gradle build system

### Install Commands

```bash
# Add to build.gradle
implementation 'com.surveymonkey:surveymonkey-android-sdk:3.0.0'
```

## Basic Usage

```java
// Initialize SDK
SurveyMonkey.init(this, "api_key");
```

### Common Options

| Option | Description |
|--------|-------------|
| init | Initialize with API key |
| startFeedbackActivity | Launch survey activity with extras |

## Examples

### Example 1: Basic Usage

```java
Intent intent = new Intent(this, SMFeedbackActivity.class);
intent.putExtra("smSPageURL", "https://surveymonkey.com");
startActivity(intent);
```

### Example 2: Advanced Usage

```java
// With custom HTML
intent.putExtra("smSPageHTML", "<html><body>Survey</body></html>");
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1626.002]] Component with Known Vulnerability
- [[T1416]] Cross-site Scripting (XSS)

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Scan for exported SMFeedbackActivity in manifests
- Monitor WebView loads from untrusted intents
- Audit SDK versions for known issues

## Related Procedures


## Related Tools

- [[Android Studio]]
- [[WebView]]

## References

- Official documentation: https://github.com/SurveyMonkey/surveymonkey-android-sdk/
- Related resources: Android Security Best Practices
