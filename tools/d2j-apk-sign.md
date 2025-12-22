---
id: 758caa7e-b52c-4e62-a5d6-553f849ff826
type: tool
verified: true
created_at: '2019-08-28T21:17:43.264523+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - android
  - reverse-engineering
  - apk-signing
  - dex2jar
url: 'https://github.com/pxb1988/dex2jar'
commands:
  - '[[commands/d2j-apk-sign-apk]]'
validated: true
---

# d2j-apk-sign

**Status**: Unverified

## Overview

d2j-apk-sign is a utility script from the dex2jar toolkit designed for signing Android APK files. It is commonly used in mobile reverse engineering workflows to sign modified or unsigned APKs after decompilation, editing, or repackaging. This tool integrates with jarsigner (from the JDK) to apply digital signatures, ensuring the APK can be installed on Android devices without signature verification errors.

## Description

dex2jar is a comprehensive toolkit for working with Android Dalvik Executable (.dex) and APK files. The d2j-apk-sign component specifically handles APK signing, which is essential after tasks like dex-to-jar conversion, bytecode modification, or resource editing. It supports signing with a default debug keystore or custom certificates, making it suitable for penetration testing, malware analysis, and app security assessments. The tool is Java-based and script-driven, providing a simple interface for automating signing in build pipelines or manual reverse engineering sessions.

## Features

- Feature 1: Signs APKs using jarsigner with configurable keystores
- Feature 2: Handles unsigned APKs from decompilation tools like apktool or dex2jar
- Feature 3: Supports batch signing and integration with other dex2jar utilities (e.g., d2j-dex2jar for conversion)

## Installation

### Requirements

- Java Development Kit (JDK) 8 or higher
- dex2jar toolkit (includes d2j-apk-sign script)

### Install Commands

```bash
# On Kali/Ubuntu (install via apt if available, or manual download)
sudo apt update
sudo apt install default-jdk
d2j-dex2jar  # This may pull dex2jar; if not, proceed to manual

# Manual installation from GitHub
wget https://github.com/pxb1988/dex2jar/releases/download/v2.1/dex2jar-2.1.zip
unzip dex2jar-2.1.zip
cd dex2jar-2.1
chmod +x *.sh
```

For Windows/macOS, download the ZIP, extract, and ensure Java is in PATH. The scripts (e.g., d2j_apk_sign.sh) are executable on Unix-like systems; use batch equivalents on Windows.

## Basic Usage

```bash
sh d2j_apk_sign.sh --help
```

This displays available options, including keystore paths and alias specifications.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-k, --keystore` | Path to custom keystore file |
| `-a, --alias` | Keystore alias for signing |

## Examples

### Example 1: Basic Usage

Sign an unsigned APK with default debug keystore:

```bash
sh d2j_apk_sign.sh unsigned.apk signed.apk
```

### Example 2: Advanced Usage

Sign with a custom keystore:

```bash
sh d2j_apk_sign.sh -k mykeystore.jks -a myalias unsigned.apk signed.apk
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Bypass User Account Control]] Bypass User Account Control (for Android app modification in testing)
- [[Obfuscated Files or Information]] Obfuscated Files or Information (APK repackaging)

### Tactics

- [[Execution]] Execution
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Presence of dex2jar scripts or jarsigner logs in build directories
- Detection method 2: Modified APKs with mismatched signatures (e.g., via apksigner verify)
- Detection method 3: Java processes invoking jarsigner during app analysis

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/apktool]]
- [[tools/jadx]]

## References

- Official GitHub: https://github.com/pxb1988/dex2jar
- JDK Documentation: https://docs.oracle.com/javase/8/docs/technotes/tools/windows/jarsigner.html
