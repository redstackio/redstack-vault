---
tags:
  - ios
  - runtime-analysis
  - setup
  - debugger
type: procedure
tools:
  - '[[tools/SnoopIt]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Execution through API]]'
updated_at: '2025-12-14T17:28:20.213Z'
sub_techniques: []
id: ba75f16f-5f60-4265-8beb-4d0346ea4458
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Execution through API]]'
---
# Install-and-Configure-SnoopIt-for-iOS-Analysis

## Summary

This procedure installs and configures SnoopIt, a runtime analysis tool for iOS apps, to attach to and monitor a target application like Coinbase on a jailbroken device. It sets the foundation for inspecting and manipulating app behavior at runtime.

## Description

SnoopIt allows developers and security researchers to attach to running iOS app processes, browse classes, and invoke methods dynamically. In this scenario, it's used on a jailbroken iOS device to target the Coinbase app, exploiting the absence of anti-debugging measures. Prerequisites include a jailbroken device, as root access is needed for process attachment. Expected outcome: Tool ready for app-specific manipulation, enabling subsequent auth bypass.

## Requirements

1. Jailbroken iOS device with root access
2. Internet access for tool installation (if not sideloaded)
3. Target app (Coinbase) installed on the device
4. Web browser for accessing SnoopIt's control interface

## Defense

Defensive measures and detection strategies:

- Implement anti-debugging checks (e.g., ptrace denial) to prevent attachment
- Use app hardening tools like iXGuard to obfuscate classes and methods
- Monitor for jailbreak indicators and block functionality on rooted devices
- Log anomalous method invocations or debugger presence

## Objectives

1. Install SnoopIt successfully on the iOS device
2. Attach to the target app process without crashing it
3. Prepare interface for class exploration and method calls

## Instructions

### Step 1: Install SnoopIt

**Context**: Download and install the tool on the jailbroken device to enable runtime capabilities.

SnoopIt can be installed via Cydia or sideloading. Search for and install the SnoopIt package.

> No specific command; use device package manager. Expected output: Tool icon or confirmation in app list.

### Step 2: Configure Target App

**Context**: Select the Coinbase app for monitoring to attach the debugger.

In SnoopIt settings, choose the running or target process for the Coinbase app.

> Interface-based selection. Expected output: Process attached; status shows 'Connected'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Execution through API]] Native API

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/SnoopIt]]

## Tags

- ios
- runtime-analysis
- setup
