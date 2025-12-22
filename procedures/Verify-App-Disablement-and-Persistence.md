---
id: proc-slack-verify-disablement-001
tags:
  - slack
  - macos
  - persistence
  - disablement
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-13T23:52:33.512Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Verify-App-Disablement-and-Persistence

## Summary

This procedure confirms the CSS injection's success by checking app non-functionality and persistence after restarts or reinstalls on macOS.

## Description

Post-injection, the app's HTML is hidden, making it unusable. The malicious CSS stores in app config, surviving reinstalls due to macOS persistence mechanisms. This step validates impact and explores exfiltration potential without PoC. Targets local Slack instance; no network involved.

## Requirements

1. Malicious CSS injected successfully
2. Ability to restart or reinstall Slack
3. macOS terminal for reinstall verification if needed

## Defense

Defensive measures and detection strategies:

- Clear app cache and configs on reinstall (e.g., delete ~/Library/Application Support/Slack)
- Detect anomalous CSS in app storage files
- Endpoint monitoring for app crashes or UI failures

## Objectives

1. Confirm rendering disablement
2. Test persistence across app lifecycle
3. Assess exfiltration feasibility via CSS keylogging

## Instructions

### Step 1: Restart App

**Context**: Check if effect holds after immediate restart.

Quit and relaunch Slack.

> Interface remains hidden if persistent.

### Step 2: Reinstall and Verify

**Context**: Simulate recovery attempt to confirm exploit durability.

Uninstall Slack via App Store or drag to Trash, then reinstall; launch and observe.

> Malicious CSS reapplies, keeping app disabled.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Disable or Modify Tools]] Disable or Modify Tools
- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel Using File Transfer Protocol

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[slack]]
- [[macos]]
- [[Persistence]]
