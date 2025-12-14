---
url: 'http://developer.android.com/tools/help/proguard.html'
tags:
  - obfuscation
  - code-protection
type: tool
verified: false
platforms:
  - Android
  - Java
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:40.175Z'
id: 1fcd5b7c-f467-4b88-8615-c9686d08dd02
validated: true
submitted: true
---
# ProGuard

**Status**: Unverified

## Overview

ProGuard is a free Java class file shrinker, optimizer, obfuscator, and preverifier, recommended for Android apps to hide hardcoded secrets by renaming classes, fields, and methods, and removing unused code, making reverse engineering and credential extraction more difficult.

## Description

In the context of the Coinbase vulnerabilities, ProGuard could have obscured the plaintext consumer ID/secret in LoginManager.java, preventing easy discovery from public source or decompiled APKs. It processes Java bytecode during build (integrated with Android SDK), applying rules to obfuscate strings and control flow. Primarily defensive, it's used in offensive security to understand app protections or test evasion.

## Features

- Feature 1: Obfuscation - Renames identifiers to short, meaningless names (e.g., a.b.c)
- Feature 2: String Encryption - Optionally encrypts sensitive strings (via plugins)
- Feature 3: Optimization - Removes dead code and inlines methods for smaller APKs

## Installation

### Requirements

- Android SDK Build Tools
- Java JDK

### Install Commands

```bash
# Integrated in Android Studio; or standalone
download proguard.jar from sourceforge.net/projects/proguard

# In Android project: Add to build.gradle
android {
    buildTypes {
        release {
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
}
```

## Basic Usage

```bash
java -jar proguard.jar @proguard.conf
# Config file specifies input/output jars and rules
```

### Common Options

| Option | Description |
|--------|-------------|
| -keep class com.example.LoginManager | Preserve specific classes from obfuscation |
| -obfuscationdictionary dict.txt | Use custom dictionary for renaming |
| -dontobfuscate | Disable obfuscation for testing |

## Examples

### Example 1: Basic Usage

```bash
# Build release APK with ProGuard in Android Studio
./gradlew assembleRelease
# Obfuscated APK in build/outputs/apk/release/
```

### Example 2: Advanced Usage

```bash
# Custom rule in proguard-rules.pro to hide strings
-keepclassmembers class * {
    *** consumerId;
    *** consumerSecret;
}
-repackageclasses ''
# Rebuild to apply
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information (defensive use)

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- APK analysis showing obfuscated class names (e.g., via jadx decompiler)
- Build logs referencing proguard
- Smaller-than-expected APK sizes due to shrinking

## Related Procedures


## Related Tools

- [[R8]] (Android's successor to ProGuard)
- [[DexGuard]]

## References

- Official documentation: https://www.guardsquare.com/proguard
- Related resources: Android Developer Guide on Shrinking
