---
id: proc-examine-irccloud-storage
tags:
  - ios
  - data-protection
  - file-access
type: procedure
tools:
  - '[[tools/iOS-Data-Protection-Tool]]'
  - '[[tools/iExplorer]]'
tactics:
  - '[[Credential Access]]'
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:24:39.896Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Examine-IRCCloud-App-Storage

## Summary

This procedure inspects the IRCCloud iOS app's file storage to identify unsecured files like the session plist, confirming accessibility on a locked device.

## Description

Attackers with physical access use tools to probe the app's sandboxed storage in the Preferences folder. The com.irccloud.IRCCloud.plist lacks protection, allowing reads without unlocking or jailbreaking. This step verifies the vulnerability before extraction.

## Requirements

1. Locked iOS device with IRCCloud app
2. Computer with USB connection
3. Tools: iOS Data Protection tool and iExplorer

## Defense

Defensive measures and detection strategies:

- Enforce data protection classes in apps
- Log USB connections and file access attempts
- Use MDM to restrict physical access

## Objectives

1. Locate unsecured plist file
2. Confirm lock-state accessibility
3. Validate vulnerability for token theft

## Instructions

### Step 1: Connect and Probe Protection

**Context**: Use the data protection tool to check file accessibility.

Connect the locked device via USB and run [[tools/iOS-Data-Protection-Tool]]:

Follow tool's interface to select the app and query protection status.

> Output: File reported as accessible (no NSFileProtectionComplete).

### Step 2: Navigate to Preferences Folder

**Context**: Browse app storage to find the plist.

Launch [[tools/iExplorer]], connect device, and navigate to /var/mobile/Containers/Data/Application/[AppID]/Library/Preferences/com.irccloud.IRCCloud.plist.

> Expected: File visible and readable in locked state.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Credentials In Files]] Credentials In Files

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/iOS-Data-Protection-Tool]]
- [[tools/iExplorer]]

## Tags

- ios
- data-protection
- file-access
