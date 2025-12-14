---
url: null
tags:
  - emulator
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.147Z'
id: 32e9c444-efa6-4e50-a90d-50dbc1a07261
validated: true
submitted: true
---
# Genymotion

**Status**: Unverified

## Overview

Genymotion is a fast Android emulator for app testing and development.

## Description

Provides virtual devices for running APKs in a controlled environment, compatible with ADB.

## Features

- Feature 1: Multiple device profiles
- Feature 2: GPS, battery simulation
- Feature 3: ADB integration

## Installation

### Requirements

- VirtualBox

### Install Commands

Download from genymotion.com; install and create VM.

## Basic Usage

Launch VM and install APK via drag-drop.

### Common Options

GUI-based.

## Examples

### Example 1: Basic Usage

Start emulator, adb install apk.

### Example 2: Advanced Usage

Use with MobSF for dynamic analysis.

## MITRE ATT&CK Mapping

### Techniques

- [[Software Discovery]] Software Discovery (mobile env)

### Tactics

- [[Discovery]] Discovery

## Detection

N/A.

## Related Procedures

- [[procedures/Android-APK-Reverse-Engineering]]

## Related Tools

- [[tools/Android-Studio-Emulator]]

## References

- Official site
