---
url: 'https://ibotpeaches.github.io/Apktool/'
tags:
  - reverse-engineering
  - android
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:05.888Z'
id: d93040e5-e7be-4914-8d8e-22206c96de8f
validated: true
submitted: true
---
# Apktool

**Status**: Unverified

## Overview

Tool for reverse engineering Android APK files, unpacking resources and manifest.

## Description

Used to examine the manifest for deep link intents in BountyPay.apk.

## Features

- Feature 1: Smali disassembly
- Feature 2: Resource decoding
- Feature 3: Repackaging

## Installation

### Requirements

- Java

### Install Commands

```bash
wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.7.0.jar
```

## Basic Usage

```bash
java -jar apktool.jar d app.apk
```

### Common Options

| Option | Description |
|--------|-------------|
| d | Decode |

## Examples

### Example 1: Basic Usage

```bash
apktool d BountyPay.apk
```

## MITRE ATT&CK Mapping

### Techniques

- [[Unsecured Credentials]]

### Tactics

- [[Collection]]

## Detection

- Decompiled files on disk

## Related Procedures

- APK reverse engineering

## Related Tools

- [[tools/jadx]]

## References

- Official site
