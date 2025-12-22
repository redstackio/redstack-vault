---
url: 'https://github.com/pxb1988/dex2jar'
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
updated_at: '2025-12-14T17:33:05.872Z'
id: 70757246-47d8-4690-9181-704df3148775
validated: true
submitted: true
---
# dex2jar

**Status**: Unverified

## Overview

Converts Android DEX bytecode to Java JAR for decompilation.

## Description

Intermediate step in APK analysis to view Java source.

## Features

- Feature 1: DEX to JAR conversion
- Feature 2: ODEX support

## Installation

### Requirements

- Java

### Install Commands

```bash
git clone https://github.com/pxb1988/dex2jar.git
cd dex2jar
chmod +x *.sh
```

## Basic Usage

```bash
sh d2j-dex2jar.sh app.apk
```

### Common Options

| Option | Description |
|--------|-------------|
| -f | Force overwrite |

## Examples

### Example 1: Basic Usage

```bash
d2j-dex2jar BountyPay.apk
```

## MITRE ATT&CK Mapping

### Techniques

- [[Unsecured Credentials]]

### Tactics

- [[Collection]]

## Detection

- JAR files generated

## Related Procedures

- APK RE

## Related Tools

- [[tools/jd-gui]]

## References

- GitHub
