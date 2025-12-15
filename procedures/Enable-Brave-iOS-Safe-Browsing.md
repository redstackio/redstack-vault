---
id: p-enable-brave-safe-browsing
tags:
  - brave
  - ios
  - safe-browsing
  - setup
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:24:42.134Z'
skill_level: novice
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Enable-Brave-iOS-Safe-Browsing

## Summary

This procedure configures Brave Browser on iOS to activate its phishing and malware site blocking feature, preparing the environment for testing bypass vulnerabilities in the safe browsing protection.

## Description

Brave iOS includes a safe browsing feature that checks URLs against a blocklist (simple_malware.txt) to prevent access to known phishing and malware sites. Enabling this feature is a prerequisite for demonstrating bypasses, as it ensures the protection logic is active. The process involves navigating the app's settings to toggle the option, which triggers domain matching during navigation. This setup is essential for verifying that standard blocked domains are intercepted before attempting variants.

## Requirements

1. iOS device with Brave Browser installed (version affected by the vulnerability)
2. Access to the device's Settings app within Brave
3. No network or credential requirements; local configuration only

## Defense

Defensive measures and detection strategies:

- Ensure Brave is updated to versions that normalize trailing dots in hostname matching
- Monitor for unusual navigation patterns or user reports of bypassed blocks
- Use device-level parental controls or MDM policies to enforce safe browsing

## Objectives

1. Activate Brave Shields' phishing/malware blocking to rely on the vulnerable domain matching
2. Confirm protection is working on standard blocked URLs
3. Set up for subsequent bypass exploitation

## Instructions

### Step 1: Open Brave Settings

**Context**: Access the configuration menu to locate safe browsing options.

Launch the Brave app on your iOS device and tap the menu icon (three lines) in the bottom-right corner, then select "Settings."

> This navigates to the main settings screen without any commands.

### Step 2: Enable Phishing and Malware Blocking

**Context**: Toggle the specific protection feature to activate blocklist checking.

Navigate to "Brave Shields & Privacy" > "Safe Browsing," and toggle on "Block phishing and malware sites."

> Upon enabling, the feature loads the simple_malware.txt list for domain comparisons during browsing. Test by visiting http://3e1.cn/, which should trigger a block.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Disable or Modify Tools]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[brave]]
- [[ios]]
- [[safe-browsing]]
