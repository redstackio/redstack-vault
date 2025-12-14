---
tags:
  - android
  - decompilation
  - webview
type: procedure
tools:
  - '[[tools/Jadx-Decompiler]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/jadx-decompile]]'
verified: false
platforms:
  - Android
submitted: true
techniques:
  - '[[Hardware]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: dd60ebec-fec4-4f14-a406-40e78c445e86
created_at: '2025-12-14T17:25:18.219Z'
updated_at: '2025-12-14T17:25:18.219Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Review-DeepLinkRouter-for-Vulnerabilities

## Summary

This procedure decompiles the Zomato Order app to inspect the DeepLinkRouter activity code, identifying lack of host validation when loading URLs into the WebView for the zloyaltywebview scheme.

## Description

Decompiling reveals implementation details in methods like onCreate and a(Uri), where the URL parameter is passed directly to WebViewActivity without checking trusted domains, especially for navigation_bar_type=transparent. This enables arbitrary URL loading. Requires Jadx tool and the APK. Outcome: Code evidence of the vulnerability.

## Requirements

1. Decompiled APK from prior analysis
2. Jadx decompiler installed
3. Basic Java/Android knowledge

## Defense

Defensive measures and detection strategies:

- Implement URL whitelisting in intent handlers
- Use custom URI parsers to validate schemes/hosts
- Static analysis tools like MobSF for code review

## Objectives

1. Confirm absence of URL validation
2. Identify exact code paths for exploitation
3. Document vulnerable parameters

## Instructions

### Step 1: Decompile the APK

**Context**: Generate readable Java source from the APK.

**Command** ([[commands/jadx-decompile]]):
```bash
jadx zomato.apk -d zomato_decompiled
```

> Decompiles to a directory. Expected output: Source files in zomato_decompiled.

### Step 2: Inspect DeepLinkRouter Code

**Context**: Manually review for validation flaws.

Open zomato_decompiled/sources/com/application/zomato/activities/DeepLinkRouter.java in an editor. Search for 'zloyaltywebview' and 'WebView'. Note direct loadUrl calls without host checks.

> No command; manual inspection. Expected output: Code snippets showing vulnerability, e.g., WebViewActivity.newIntent(context, url).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/jadx-decompile]]

## Tools Used

- [[tools/Jadx-Decompiler]]

## Tags

- [[android]]
- [[decompilation]]
