---
id: p-bypass-brave-trailing-dot
tags:
  - brave
  - ios
  - phishing-bypass
  - malware-bypass
  - trailing-dot
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
updated_at: '2025-12-14T17:24:42.131Z'
skill_level: novice
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Bypass-Brave-Blocking-with-Trailing-Dot

## Summary

This procedure exploits a flaw in Brave iOS's safe browsing by appending a trailing dot to a blocked domain's hostname, bypassing the phishing/malware blocklist matching due to improper normalization.

## Description

The Brave iOS safe browsing feature compares hostnames against the simple_malware.txt blocklist without stripping or normalizing trailing dots, allowing variants like http://example.com. to evade detection while http://example.com/ is blocked. This bypass enables attackers or users to access prohibited sites, exposing them to phishing or malware risks. The technique was identified through testing URL modifications and is effective on affected Brave versions.

## Requirements

1. Brave iOS with safe browsing enabled (see [[procedures/Enable-Brave-iOS-Safe-Browsing]])
2. Knowledge of a blocked domain from simple_malware.txt (e.g., 3e1.cn)
3. iOS device with internet access for navigation

## Defense

Defensive measures and detection strategies:

- Update Brave to patch the normalization issue
- Implement URL canonicalization in custom blocklists or extensions
- Educate users on URL manipulation risks and encourage reporting anomalies
- Use supplementary security tools like content filters or VPNs with web protection

## Objectives

1. Evade Brave's domain-based blocking to load prohibited content
2. Demonstrate the impact of unnormalized hostname handling
3. Expose users to potential phishing/malware without Shields interference

## Instructions

### Step 1: Identify Blocked Domain

**Context**: Select a known malicious domain from the blocklist to prepare the bypass.

Reference the simple_malware.txt list or test with http://3e1.cn/, confirming it triggers a block warning in Brave.

> This step verifies the baseline protection before modification.

### Step 2: Modify URL with Trailing Dot

**Context**: Append a trailing dot to the hostname to exploit the matching flaw.

In the Brave address bar, enter http://3e1.cn./ and press go to navigate.

> The browser processes the hostname without normalizing the dot, failing to match the blocklist entry, resulting in direct site access.

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
- [[phishing-bypass]]
- [[trailing-dot]]
