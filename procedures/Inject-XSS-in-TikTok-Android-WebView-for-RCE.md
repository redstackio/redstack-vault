---
id: proc-tiktok-webview-xss-2020
name: Inject XSS in TikTok Android WebView for RCE
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.374Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
tags:
  - xss
  - webview
  - rce
  - android
  - tiktok
  - execution
platforms:
  - Android
tools: []
commands: []
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Inject XSS in TikTok Android WebView for RCE

## Summary

This procedure demonstrates injecting cross-site scripting (XSS) payloads into the WebView components of the TikTok Android app, exploiting improper content handling to execute JavaScript and chain to remote code execution (RCE), as detailed in the 2020 HackerOne report with CVSS 9.6 severity.

## Description

The TikTok app's WebView fails to sanitize or restrict user-supplied content, allowing attackers to inject malicious JavaScript when content is loaded via the vulnerable interface (accessible post-component export exploitation). This leads to JavaScript execution within the app's context, potentially manipulating native Android APIs or spawning processes for RCE. The attack targets Android devices; outcomes include arbitrary code execution, data exfiltration, or device compromise. Prerequisites: Access to the WebView via prior component exploitation and a debuggable device.

## Requirements

1. Android device with vulnerable TikTok app and ADB access
2. Knowledge of the target WebView loading mechanism from decompiled code
3. Payload crafting tools for JavaScript (e.g., basic editor)

## Defense

Defensive measures and detection strategies:

- Enable WebView safe browsing and disable JavaScript if unnecessary
- Implement content security policies (CSP) and input validation in WebView loads
- Monitor app logs for anomalous JavaScript execution and use runtime protection like Google Play Protect

## Objectives

1. Inject and execute malicious JavaScript in WebView
2. Escalate from script execution to native RCE
3. Compromise the device for persistence or data theft

## Instructions

### Step 1: Identify WebView Loading Point

**Context**: From decompiled APK, locate the WebView instance and its loadUrl or loadData methods vulnerable to unsanitized input.

Use JADX to search for WebView usages in TikTok's code, noting parameters that accept external content without escaping.

> Focus on areas handling user-generated content or URLs from exported components.

### Step 2: Craft and Inject XSS Payload

**Context**: Prepare a payload that executes JavaScript to test or chain to RCE, injecting via the accessible interface.

Via ADB or the exploited component, supply input like: javascript:alert('XSS') or more advanced <script>alert('XSS')</script> in loaded HTML. For RCE chaining, use payloads targeting Android's addJavascriptInterface if exposed.

> Example payload for testing: Load a URL with reflected input, e.g., via intent extra: http://example.com/?q=<script>alert(1)</script>

### Step 3: Execute and Verify RCE

**Context**: Trigger the WebView load and observe JavaScript execution, chaining to native calls if possible (e.g., via interface to Runtime.exec).

Monitor with `adb logcat | grep WebView` for execution traces. For RCE, craft payload to invoke system commands, confirming with file writes or process lists.

> Expected: Alert pops or console logs; RCE shown by `ls` output in app sandbox or escalated privileges.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript (via XSS in WebView)

### Sub-Techniques

- N/A

## Commands Used

- N/A

## Tools Used

- N/A

## Tags

- xss
- webview
- rce
- android
- tiktok
