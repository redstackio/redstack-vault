---
id: proc-craft-webview-intent
tags:
  - android
  - intent-crafting
  - xss
  - phishing
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/create-webview-intent]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Abuse Elevation Control Mechanism]]'
updated_at: '2025-12-14T17:24:44.617Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Abuse Elevation Control Mechanism]]'
---
# Craft-Embedded-Intent-for-WebViewActivity

## Summary

This procedure crafts an inner intent targeting the protected WebViewActivity in Slack to load arbitrary URLs, enabling XSS or phishing attacks by embedding malicious content.

## Description

The target environment is an Android device with Slack installed. The procedure creates an Intent with setClassName for WebViewActivity and adds extras like 'extra_url' for attacker-controlled content (e.g., javascript: for XSS). This inner intent is prepared for embedding into HomeActivity. Prerequisites: Malicious app context with Intent API access. Expected outcomes: Intent that loads fake content in WebView without exposing the real URL.

## Requirements

1. Android app development environment
2. Knowledge of Slack's component names (com.Slack.ui.WebViewActivity)
3. Target device with Slack app

## Defense

Defensive measures and detection strategies:

- Mark sensitive activities as non-exported and add intent filters
- Validate URL extras in WebViewActivity (e.g., whitelist domains)
- Use runtime permission checks for intent extras

## Objectives

1. Target protected WebViewActivity with malicious extras
2. Enable loading of arbitrary URLs for exploitation
3. Spoof titles to enhance phishing

## Instructions

### Step 1: Create Inner Intent

**Context**: Initialize and configure the intent for WebViewActivity.

**Command** ([[commands/create-webview-intent]]):
```java
Intent next = new Intent(); next.setClassName("com.Slack","com.Slack.ui.WebViewActivity"); next.putExtra("extra_url","http://example.com/"); next.putExtra("extra_title","test");
```

> This sets the class to the protected WebViewActivity, adds 'extra_url' for arbitrary content (replace with javascript:alert(1) for XSS), and 'extra_title' for fake display. Expected output: Intent object with extras ready for embedding.

### Step 2: Verify Intent Configuration

**Context**: Ensure extras are set correctly for exploitation.

No command; inspect the Intent object in code.

> Confirm setClassName targets com.Slack.ui.WebViewActivity and extras are populated. Expected output: Valid inner intent for WebView manipulation.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Abuse Elevation Control Mechanism]] Abuse Elevation Control Mechanism

### Sub-Techniques


## Commands Used

- [[commands/create-webview-intent]]

## Tools Used


## Tags

- [[android]]
- [[intent-crafting]]
- [[xss]]
- [[Phishing]]
