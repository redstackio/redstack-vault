---
id: proc-uuid-001
tags:
  - android
  - twitter-kit
  - app-integration
type: procedure
tools:
  - '[[tools/Fabric-Twitter-Kit]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:24:35.253Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Set-Up-Vulnerable-Android-App-with-Twitter-Kit

## Summary

This procedure outlines integrating Fabric's Twitter Kit into an Android application to enable Twitter login, which inadvertently logs temporary OAuth tokens in the device's logcat during authentication. It is used to demonstrate the vulnerability in a controlled test environment for security research.

## Description

The procedure involves registering a Twitter app, adding the Fabric Twitter Kit SDK to an Android project, implementing the login button and callback handlers, building the APK, installing it on a device, and performing the login to trigger the leak. The target environment is any Android device with the app installed. Prerequisites include Android Studio, a Twitter developer account, and ADB access. Expected outcomes include a functional app that leaks tokens upon login, allowing subsequent extraction.

## Requirements

1. Android Studio installed with SDK tools
2. Twitter developer account to obtain API keys and secrets
3. ADB enabled on the target Android device for installation and debugging
4. Fabric account for Twitter Kit integration

## Defense

Defensive measures and detection strategies:

- Avoid using Fabric Twitter Kit; migrate to Twitter's official SDK which sanitizes logs
- Monitor app logs in production and implement log filtering to exclude sensitive data
- Use app shielding tools to restrict logcat access from other apps
- Educate developers on secure logging practices during OAuth flows

## Objectives

1. Create and deploy an Android app with vulnerable Twitter login integration
2. Trigger OAuth authentication to log temporary tokens
3. Prepare for token extraction by malicious actors on the same device

## Instructions

### Step 1: Register Twitter App and Obtain Credentials

**Context**: Set up the necessary Twitter app credentials for integration.

No command required; use the Twitter Developer Portal to create an app, enable OAuth, and note the consumer key and secret.

> Add these to your app's build.gradle or strings.xml securely.

### Step 2: Integrate Fabric Twitter Kit SDK

**Context**: Add the SDK dependency and initialize Twitter login in the app code.

In your app-level build.gradle, add:

```gradle
dependencies {
    implementation 'io.fabric.sdk.android:fabric:1.4.8'
    implementation 'com.twitter.sdk.android:twitter:3.3.0'
    implementation 'com.twitter.sdk.android:tweet-composer:3.0.1'
}
```

Then, in your MainActivity.java or Kotlin equivalent, implement Twitter login:

```java
TwitterAuthConfig authConfig = new TwitterAuthConfig(TWITTER_KEY, TWITTER_SECRET);
Fabric.with(this, new Twitter(authConfig));

// Add login button listener
loginButton.setCallback(new Callback<TwitterSession>() {
    @Override
    public void success(Result<TwitterSession> result) {
        // Handle success
    }
    // ... other overrides
});
```

> This adds the login with Twitter feature to the application code, enabling the vulnerable authentication process.

### Step 3: Build, Install, and Perform Login

**Context**: Compile the app, deploy to device, and execute login to generate logs.

Build the APK in Android Studio, then install via ADB:

```bash
adb install app-debug.apk
```

Launch the app, click login with Twitter, and enter username/password.

> Successful login triggers the OAuth flow, logging the temporary token in logcat without sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Fabric-Twitter-Kit]]

## Tags

- android
- twitter-kit
- oauth
