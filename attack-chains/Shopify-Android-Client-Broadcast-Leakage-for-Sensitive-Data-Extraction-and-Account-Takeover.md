---
id: ac-shopify-android-broadcast-leak-001
tags:
  - android
  - broadcast-leakage
  - token-theft
  - account-takeover
  - api-interception
type: attack_chain
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
  - '[[tools/Custom-POC-APK-shopifyhack]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Android
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Install-Malicious-POC-APK-for-Broadcast-Interception]]'
  - '[[procedures/Trigger-Shopify-API-Requests-via-User-Login]]'
  - '[[procedures/Intercept-and-Extract-Sensitive-Data-from-Broadcast]]'
  - '[[procedures/View-Leaked-Data-in-Android-Logs]]'
step_count: 4
techniques:
  - '[[T1475]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:32:11.012Z'
description: >-
  Multi-stage attack exploiting unprotected implicit broadcasts in the Shopify
  Android app to intercept API responses containing access tokens, cookies, and
  other sensitive data, enabling silent account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[T1475]]'
  - '[[Steal Web Session Cookie]]'
---
# Shopify Android Client Broadcast Leakage for Sensitive Data Extraction and Account Takeover

Multi-stage attack chain demonstrating exploitation of unprotected implicit broadcasts in the Shopify Android client to leak API request responses, including access tokens, cookies, headers, and body content, allowing a malicious app to achieve full account takeover without user awareness.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Install Malicious App] --> B[Trigger API Requests]
    B --> C[Intercept Broadcast]
    C --> D[Extract and View Data]
    D --> E[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ADB-Android-Debug-Bridge]]
- [[tools/Custom-POC-APK-shopifyhack]]

### Target Environment

- Android device or emulator (API level compatible with Shopify app, e.g., Android 8+)
- Shopify Android client installed
- USB debugging enabled on device for ADB access
- No special network access beyond local device; attack occurs on-device

### Initial Access Requirements

- Physical or ADB access to the target Android device
- Ability to install APKs (developer mode or sideloading enabled)
- No prior credentials needed; exploits app's implicit broadcasts post-install

## Detailed Attack Procedures

### Step 1: Install Malicious POC APK
procedure: [[procedures/Install-Malicious-POC-APK-for-Broadcast-Interception]]

**Objective**: Deploy a proof-of-concept malicious app to register a broadcast receiver for intercepting Shopify's unprotected broadcasts without requiring permissions.

**Instructions**: Download and install the custom POC APK alongside the Shopify app. The POC registers a receiver in the background for the 'com.shopify.service.requestComplete' action.

**Expected Output**: Both apps installed successfully; no visible indicators to the user.

**Success Indicators**:
- POC APK installed without errors
- Broadcast receiver active in background

### Step 2: Trigger Shopify API Requests
procedure: [[procedures/Trigger-Shopify-API-Requests-via-User-Login]]

**Objective**: Initiate user login in the Shopify app to trigger API requests that send unprotected implicit broadcasts containing response data.

**Instructions**: Launch the Shopify app and perform a standard login with valid credentials. This triggers NetworkService to broadcast Intent extras like 'request_id', 'response_code', 'response_headers', and 'response_body'.

**Expected Output**: Successful login; broadcasts sent invisibly.

**Success Indicators**:
- User logged in to Shopify app
- API requests completed, triggering broadcasts

### Step 3: Intercept Sensitive Data
procedure: [[procedures/Intercept-and-Extract-Sensitive-Data-from-Broadcast]]

**Objective**: Capture the broadcasted Intent extras to extract sensitive information such as admin cookies from headers and access tokens from the response body.

**Instructions**: The POC's HackBroadcastReceiver automatically processes the Intent, logging extras including cookies and tokens for potential storage or remote exfiltration.

**Expected Output**: Sensitive data logged internally by the POC app.

**Success Indicators**:
- Broadcast received and processed
- Sensitive data (e.g., access_token, admin_cookie) extracted

### Step 4: View Leaked Data
procedure: [[procedures/View-Leaked-Data-in-Android-Logs]]

**Objective**: Retrieve and inspect the intercepted sensitive data from device logs to verify the leakage and prepare for account takeover.

**Instructions**: Use ADB to filter logs for the POC's tag and display the dumped data.

**Expected Output**: Console output showing headers (e.g., admin_cookie) and body (e.g., access_token).

**Success Indicators**:
- Logs display sensitive data
- Confirmation of full API response leakage

## Attack Chain Summary

### Key Achievements

1. Silent installation of a malicious app to monitor broadcasts
2. Interception of API responses without user interaction or permissions
3. Extraction of credentials enabling account takeover
4. Verification of data leakage via logs

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1475]] Install Malicious Application
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---
*Last updated: 2023-10-01T12:00:00Z*
