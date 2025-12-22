---
id: ac-uuid-001
tags:
  - android
  - mobile
  - webview
  - javascript-execution
  - url-bypass
  - rce
type: attack_chain
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Analyze-Shopify-App-Package-for-NavigationActivity]]'
  - '[[procedures/Craft-Malicious-JavaScript-URL-Payload]]'
  - '[[procedures/Launch-NavigationActivity-via-ADB-with-Malicious-URL]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:45.155Z'
description: >-
  A multi-stage attack exploiting lack of URL scheme validation in the Shopify
  Android app's NavigationActivity to execute arbitrary JavaScript in the
  WebView, potentially accessing device files via EASDK and SmartWebview
  interfaces.
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# URL Scheme Validation Bypass in Shopify Mobile App Leading to Arbitrary JavaScript Execution

Multi-stage attack chain demonstrating exploitation of unvalidated URL schemes in the Shopify Android app to achieve arbitrary JavaScript execution within the app's WebView context.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Analyze App Package] --> B[Craft Malicious Payload]
    B --> C[Launch Activity via ADB]
    C --> D[JavaScript Execution in WebView]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ADB-Android-Debug-Bridge]]

### Target Environment

- Target OS/Platform: Android device with Shopify mobile app installed (com.shopify.mobile)
- Required services/ports: USB debugging enabled on device; no network ports required
- Network access requirements: Local USB connection to device

### Initial Access Requirements

- Physical or emulated access to Android device
- ADB debugging enabled (developer options)
- Shopify app installed; no credentials needed for this exploit
- Prior access needed: None beyond device setup

## Detailed Attack Procedures

### Step 1: Analyze App Package
procedure: [[procedures/Analyze-Shopify-App-Package-for-NavigationActivity]]

**Objective**: Identify the vulnerable NavigationActivity component in the Shopify app that accepts unvalidated URL parameters.

**Instructions**: Decompile or examine the app's Android manifest using tools like APKTool or ADB to locate com.shopify.mobile.navigation.NavigationActivity, which processes a 'url' extra without scheme validation.

**Expected Output**: Confirmation of the component and its parameters in the manifest.

**Success Indicators**:
- NavigationActivity identified with 'url' extra
- No scheme validation logic observed

### Step 2: Craft Malicious Payload
procedure: [[procedures/Craft-Malicious-JavaScript-URL-Payload]]

**Objective**: Create a JavaScript URL payload using the 'javascript:' scheme to inject and execute arbitrary code in the WebView.

**Instructions**: Construct a payload like 'javascript://shopify.com/admin/articles/%0aalert(1);//' to bypass restrictions and trigger JS execution upon loading in the NavigationActivity.

**Expected Output**: Validated payload string ready for use in intents.

**Success Indicators**:
- Payload syntax verified
- Scheme confirmed as 'javascript:' for WebView injection

### Step 3: Launch Activity via ADB
procedure: [[procedures/Launch-NavigationActivity-via-ADB-with-Malicious-URL]]

**Objective**: Use ADB to start the NavigationActivity with the malicious URL, leading to JS execution and potential takeover of EASDK and SmartWebview interfaces.

**Instructions**: Execute the ADB command to launch the activity with required extras including the malicious URL.

Use [[commands/am-start-shopify-navigationactivity-malicious-url]]:

```bash
am start -n com.shopify.mobile/com.shopify.mobile.navigation.NavigationActivity --es notification_type 2 --es notification_category 1 --es url 'javascript://shopify.com/admin/articles/%0aalert(1);//'
```

**Expected Output**: The app launches and an alert box displays '1' in the WebView, confirming JS execution.

**Success Indicators**:
- Alert triggered in app
- WebView loads arbitrary JS without errors
- Access to EASDK/SmartWebview interfaces possible with further payloads

## Attack Chain Summary

### Key Achievements

1. Bypassed URL scheme validation in Shopify's NavigationActivity
2. Achieved arbitrary JavaScript execution in the app's WebView
3. Demonstrated potential for device file access via exposed JS interfaces like EASDK, requiring user interaction and a malicious companion app

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
