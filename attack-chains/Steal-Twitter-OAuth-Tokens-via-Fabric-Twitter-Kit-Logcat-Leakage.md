---
id: ac-uuid-001
tags:
  - oauth-leak
  - android
  - twitter-kit
  - information-disclosure
  - credential-access
type: attack_chain
tools:
  - '[[tools/logcat]]'
  - '[[tools/Fabric-Twitter-Kit]]'
tactics:
  - '[[Credential Access]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Vulnerable-Android-App-with-Twitter-Kit]]'
  - '[[procedures/Extract-Leaked-OAuth-Token-from-Logcat]]'
step_count: 4
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:24:35.257Z'
description: >-
  Multi-stage attack exploiting Fabric's Twitter Kit on Android to leak
  temporary OAuth tokens via device logcat, allowing unauthorized access to
  Twitter accounts.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Steal Twitter OAuth Tokens via Fabric Twitter Kit Logcat Leakage

Multi-stage attack chain demonstrating exploitation of Fabric's Twitter Kit vulnerability on Android devices to leak OAuth tokens through logcat, enabling credential theft by any co-installed malicious app.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[App Integration] --> B[Installation and Login] --> C[Log Capture]
    C --> D[Token Extraction]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Fabric-Twitter-Kit]]
- [[tools/logcat]]

### Target Environment

- Android device (API level supporting Fabric SDK)
- Twitter developer account for app registration
- ADB (Android Debug Bridge) for logcat access

### Initial Access Requirements

- Physical or ADB access to the target Android device
- Development environment for building Android apps (Android Studio)
- No prior network access needed; local device exploitation

## Detailed Attack Procedures

### Step 1: Integrate Twitter Kit into Android App

procedure: [[procedures/Set-Up-Vulnerable-Android-App-with-Twitter-Kit]]

**Objective**: Create a test Android application incorporating Fabric's Twitter Kit to trigger OAuth token logging during authentication.

**Instructions**: Follow the procedure to add Twitter login integration, build, and prepare the app for installation. This sets up the vulnerable authentication flow.

**Expected Output**: Compiled APK with Twitter login feature.

**Success Indicators**:
- App builds without errors
- Twitter Kit dependencies resolve correctly

### Step 2: Install the Application on Android Device

procedure: [[procedures/Set-Up-Vulnerable-Android-App-with-Twitter-Kit]]

**Objective**: Deploy the vulnerable app to the target device to enable execution of the Twitter login process.

**Instructions**: Use ADB to push and install the APK on the device. Ensure the device is in developer mode with USB debugging enabled.

**Expected Output**: App installed and visible in the device's app drawer.

**Success Indicators**:
- Installation completes without errors
- App launches successfully

### Step 3: Perform Twitter Login in the Application

procedure: [[procedures/Set-Up-Vulnerable-Android-App-with-Twitter-Kit]]

**Objective**: Trigger the authentication process to generate and log the temporary OAuth token in logcat.

**Instructions**: Launch the app, select Twitter login, and enter valid Twitter credentials. This initiates the OAuth flow, causing the token to be logged unsanitized.

**Expected Output**: Successful login redirect or callback, with logs generated in the background.

**Success Indicators**:
- User authenticates with Twitter
- No visible errors in app UI

### Step 4: Search Logcat for Leaked OAuth Token

procedure: [[procedures/Extract-Leaked-OAuth-Token-from-Logcat]]

**Objective**: Capture and filter device logs to retrieve the exposed temporary OAuth token for potential account compromise.

**Instructions**: Use [[commands/logcat-grep-twitter]] to monitor and filter logcat output immediately after login:

```bash
adb logcat | grep twitter
```

Search for entries containing the OAuth token in the authorize URL logged by Twitter Kit.

**Expected Output**: Log lines revealing the temporary OAuth token, e.g., lines with 'twitter' and URL parameters including the token.

**Success Indicators**:
- Token visible in filtered logs
- Token can be copied for testing unauthorized access

## Attack Chain Summary

### Key Achievements

1. Successful integration of vulnerable Twitter Kit into an Android app
2. Triggered OAuth leakage during login authentication
3. Extracted temporary token from accessible logcat, demonstrating inter-app credential theft potential

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### MITRE ATT&CK Tactics

- [[Credential Access]] Credential Access

---
*Last updated: 2023-10-01T00:00:00Z*
