---
tags:
  - webview-exploitation
  - timing-attack
  - address-bar
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - iOS
  - WebView
techniques:
  - '[[Phishing]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: a26891ab-5609-4984-b21f-d636f5e801f9
created_at: '2025-12-14T17:24:44.878Z'
updated_at: '2025-12-14T17:24:44.878Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Trigger-Address-Bar-Update-in-WebView

## Summary

This procedure exploits the timing mismatch in the LINE iOS WebView's address bar updates during navigation to a Unicode-spoofed URL, causing a deceptive display despite cancellation.

## Description

Reported in HackerOne #1082991, the LINE app's internal browser updates the address bar asynchronously with normalized URL data before fully validating navigation. For invalid hostnames or redirects with malicious Unicode, this results in showing a legitimate domain while the actual load is from phishing sources. Target: LINE iOS client WebView. Prerequisites: Crafted URL from prior step. Outcomes: User sees spoofed bar, increasing phishing success.

## Requirements

1. Vulnerable LINE iOS app installed
2. Crafted Unicode URL ready
3. User interaction within the app (e.g., clicking link)

## Defense

Defensive measures and detection strategies:

- Synchronize address bar updates with full navigation validation
- Block or warn on Unicode domains exceeding safe character sets
- Monitor WebView logs for timing anomalies in app debugging

## Objectives

1. Initiate navigation to trigger update
2. Exploit async processing for deception
3. Maintain user trust via visual spoof

## Instructions

### Step 1: Open URL in LINE App

**Context**: Use the app's internal browser to process the URL.

No command; navigate via chat link or direct input.

> The WebView starts HTTP redirect handling.

### Step 2: Observe Normalization During Processing

**Context**: App normalizes Unicode but cancels due to invalidity, updating bar prematurely.

Monitor visually; no tool needed.

> Address bar shows deceptive domain (e.g., "line.me" variant).

### Step 3: Confirm Cancellation with Partial Load

**Context**: Ensure navigation halts but UI persists spoof.

Test on device; expected mismatch between bar and content attempt.

> Success if bar remains spoofed without error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[webview-spoofing]]
- [[timing-exploit]]
