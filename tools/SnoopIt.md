---
url: ''
tags:
  - runtime-analysis
  - ios
  - debugger
  - manipulation
type: tool
verified: false
platforms:
  - iOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.208Z'
id: 6565f4d7-043c-4e13-8ac0-0bc44ad3d04c
validated: true
submitted: true
---
# SnoopIt

**Status**: Unverified

## Overview

SnoopIt is a specialized tool for runtime analysis, inspection, and manipulation of iOS applications on jailbroken devices. It is commonly used in security testing to attach to app processes, explore Objective-C classes, and invoke methods dynamically, aiding in vulnerability discovery like authentication bypasses.

## Description

SnoopIt operates by hooking into running iOS app processes via a web-based interface, allowing users to browse runtime structures such as classes, instances, and methods. Features include real-time method invocation, object inspection, and logging of app behavior. In offensive security, it's ideal for testing anti-tampering measures and exploiting design flaws in mobile apps, particularly those lacking debugger protections. It requires root access and is typically installed via jailbreak repositories.

## Features

- Feature 1: Process attachment to live iOS apps for non-intrusive monitoring
- Feature 2: Web-based control panel for browsing Objective-C runtime elements
- Feature 3: Direct method calling and parameter injection to alter app flow
- Feature 4: Logging and screenshot capabilities for evidence collection

## Installation

### Requirements

- Jailbroken iOS device (iOS 8+ typically supported)
- Cydia or Sileo package manager
- Stable local network for web interface access

### Install Commands

No bash commands; use Cydia:

1. Open Cydia on the device.
2. Add repository if needed (e.g., for SnoopIt source).
3. Search for 'SnoopIt' and install.

## Basic Usage

Launch SnoopIt on the device, then access via browser at the provided localhost URL.

### Common Options

| Option | Description |
|--------|-------------|
| Attach Process | Select target app PID |
| Browse Classes | Navigate to Objective-C section |
| Invoke Method | Call selected method with optional args |

## Examples

### Example 1: Basic Usage

1. Launch target app (e.g., Coinbase).
2. In SnoopIt, attach to its process.
3. Browse to classes and inspect.

### Example 2: Advanced Usage

1. With app at PIN screen, attach SnoopIt.
2. Navigate to CBPINViewController.
3. Invoke userAuthenticated() to bypass.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Modify Authentication Process]] Modify Authentication Process
- [[Execution through API]] Native API

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for ptrace() system calls or debugger ports on device
- Detection method 2: Check for web server processes on non-standard ports (e.g., SnoopIt listener)
- Detection method 3: App crash logs showing anomalous method calls

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- HackerOne Report #80512
- iOS Security Testing Resources
