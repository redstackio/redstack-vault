---
id: tool-android-upload-service
url: 'https://github.com/gotev/android-upload-service'
tags:
  - upload-library
  - android
type: tool
verified: false
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.663Z'
validated: true
submitted: true
---
# android-upload-service

**Status**: Unverified

## Overview

android-upload-service is a third-party Android library for handling HTTP multipart file uploads, commonly integrated into apps like Quora for background upload tasks. In vulnerable configurations, its exported UploadService allows cross-app exploitation for arbitrary file theft.

## Description

The library provides classes like UploadService, UploadTaskParameters, and MultipartUploadTask for efficient file uploads. When declared exported without restrictions (pre-version 3.4), it enables intents from any app to trigger uploads from private directories, exposing sensitive data.

## Features

- Feature 1: Multipart HTTP uploads with progress tracking
- Feature 2: Configurable parameters for files, URLs, and tasks
- Feature 3: Background service execution via Android intents

## Installation

### Requirements

- Android SDK
- Gradle build system

### Install Commands

```bash
# Add to build.gradle (Module: app)
dependencies {
    implementation 'net.gotev:upload-service:3.3.+'  # Vulnerable version
}
```

## Basic Usage

```bash
gradle build  # No CLI; integrated in Android projects
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Library integrated via Gradle; configure in code |

## Examples

### Example 1: Basic Usage

In app code:

```java
UploadTaskParameters params = new UploadTaskParameters();
params.addFile(new UploadFile("/path/to/file"));
// etc.
```

### Example 2: Advanced Usage

Declare in manifest:

```xml
<service android:enabled="true" android:exported="true" android:name="net.gotev.uploadservice.UploadService"/>
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1417]] - Hijack Execution Flow

### Tactics

- [[Execution]] - Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Scan manifests for exported UploadService
- Detection method 2: Monitor intents targeting net.gotev.uploadservice

## Related Procedures


## Related Tools

- [[APKTool]]
- [[Jadx]]

## References

- Official documentation: https://github.com/gotev/android-upload-service
- Related resources: Android Security Bulletins on exported components
