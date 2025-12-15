---
id: tool-uuid-002
url: 'https://docs.fabric.io/android/twitter'
tags:
  - android
  - sdk
  - twitter
  - oauth
type: tool
verified: false
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.218Z'
validated: true
submitted: true
---
# Fabric-Twitter-Kit

**Status**: Unverified

## Overview

Fabric Twitter Kit is an SDK provided by Fabric (now part of Google) for integrating Twitter features like login, sharing, and analytics into Android applications. It simplifies OAuth-based authentication but is vulnerable to logging sensitive tokens in logcat, making it a target for security research on credential leakage.

## Description

The kit handles Twitter API interactions, including user authentication via OAuth 1.0a. In offensive security, it is used to demonstrate flaws where temporary tokens are logged unsanitized during the authorize step, accessible via logcat by other apps on the device. It requires Fabric integration and Twitter app credentials.

## Features

- Feature 1: Easy Twitter login with session management
- Feature 2: Tweet composition and sharing UI components
- Feature 3: Analytics for user engagement

## Installation

### Requirements

- Android Studio project
- Fabric account
- Twitter developer app credentials

### Install Commands

```bash
# Add to build.gradle
implementation 'io.fabric.sdk.android:twitter:3.1.0'
```

Initialize in Application class:

```java
Fabric.with(this, new TwitterCore(new TwitterAuthConfig(key, secret)));
```

## Basic Usage

```bash
# No direct CLI; integrated via Gradle
./gradlew build
```

### Common Options

| Option | Description |
|--------|-------------|
| TwitterAuthConfig | Configures API keys |
| loginButton.setCallback | Handles auth callbacks |

## Examples

### Example 1: Basic Usage

Implement login in Activity:

```java
Twitter.login(this, new com.twitter.sdk.android.core.Callback<TwitterSession>() { ... });
```

Triggers OAuth flow and logs tokens.

### Example 2: Advanced Usage

Add tweet composer:

```java
TweetComposer.Builder.from(this).text("Hello").createIntent();
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of Fabric dependencies in app APK
- Logcat entries with Twitter tags post-login
- App crashes or anomalies during auth

## Related Procedures

- [[procedures/Set-Up-Vulnerable-Android-App-with-Twitter-Kit]]

## Related Tools

- [[Twitter SDK]]

## References

- Official documentation: https://docs.fabric.io/android/twitter
