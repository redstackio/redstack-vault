---
id: proc-analyze-imageviewer-intent-001
tags:
  - xss
  - webview
  - code-review
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
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.327Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Analyze ImageViewerActivity Intent Handling

## Summary

This procedure decompiles and reviews the Java code of ImageViewerActivity and related classes to trace how intent data flows to WebView, identifying XSS risks from unsanitized HTML insertion.

## Description

For the IRCCloud app, analysis reveals that onCreate processes intent data by fetching image info via ImageList, assigning URLs without validation, and concatenating them into HTML for WebView loadImage. This allows breakout from img src attributes. Requires decompiled code; outcomes pinpoint injection points for PoC development.

## Requirements

1. Decompiled APK source (from JADX)
2. IDE or text editor for Java code review
3. Understanding of Android intents and WebView

## Defense

Defensive measures and detection strategies:

- Sanitize/escape user input before HTML insertion (e.g., use Html.escape)
- Validate URLs against whitelists in fetchImageInfo
- Enable WebView safe browsing and JS restrictions

## Objectives

1. Trace data flow from intent to WebView
2. Identify lack of sanitization leading to XSS
3. Document vulnerable methods for exploitation

## Instructions

### Step 1: Review onCreate Method

**Context**: Check initial intent data handling.

In ImageViewerActivity.java, examine:

```java
if (getIntent() != null && getIntent().getDataString() != null) {
    String url = getIntent().getDataString().replace("irccloud-image://", "http");
    ImageList.getInstance().fetchImageInfo(url, new OnImageInfoListener() { ... });
}
```

> Data string is minimally modified and passed without checks.

### Step 2: Examine fetchImageInfo in ImageList

**Context**: Trace URL assignment.

In ImageList.java:

```java
public void fetchImageInfo(String urlStr, OnImageInfoListener listener) {
    ImageURLInfo info = new ImageURLInfo();
    info.thumbnail = urlStr;
    info.original_url = urlStr;
    listener.onImageInfo(info);
}
```

> No validation; direct assignment.

### Step 3: Analyze loadImage for HTML Construction

**Context**: Identify injection point.

In loadImage:

```java
String html = "<img src='" + new URL(urlStr).toString() + "' onload='...'>";
webView.loadData(html, "text/html", "UTF-8");
```

> String concatenation allows quote breakout for JS injection.

**Expected Output**: Vulnerable code paths documented.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- android-code-review
- webview-xss
