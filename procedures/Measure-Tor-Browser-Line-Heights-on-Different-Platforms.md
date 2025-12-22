---
id: proc-measure-tor-lineheights
tags:
  - tor-browser
  - fingerprinting
  - css
  - os-detection
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web Browser
  - Linux
  - Windows
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T03:46:31.482Z'
skill_level: novice
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Measure Tor Browser Line-Heights on Different Platforms

## Summary

This procedure tests Tor Browser's rendering of CSS line-height on Linux, Windows, and macOS to confirm inheritance of platform-specific defaults, revealing fingerprintable differences.

## Description

Tor Browser, based on Firefox, aims to reduce fingerprinting but fails to override the default 'normal' line-height, which varies by OS: 19px on Linux, 19.2px on Windows, 19.5167px on macOS. This step involves direct measurement using developer tools or JavaScript on a controlled test environment. The attack scenario targets Tor users visiting a malicious site, with prerequisites including Tor Browser installations on test machines. Outcomes validate the vulnerability for subsequent exploitation.

## Requirements

1. Tor Browser installed on Linux, Windows, and macOS test environments.
2. Access to browser console for style inspection.
3. Sample HTML page as in baseline observation.

## Defense

Defensive measures and detection strategies:

- Tor Browser updates that enforce uniform line-height (e.g., via CSS resets).
- User awareness of fingerprinting risks and use of virtual machines for isolation.
- Web application firewalls detecting unusual JS style queries.

## Objectives

1. Measure and record Tor-specific line-height values per OS.
2. Verify lack of uniformity in Tor's rendering engine.
3. Enable accurate OS inference in detection scripts.

## Instructions

### Step 1: Setup Tor Browser on Each Platform

**Context**: Ensure clean Tor Browser instances for accurate measurements.

Download and launch Tor Browser on Linux (19px expected), Windows (19.2px), macOS (19.5167px).

> No command; manual installation via official Tor Project site.

### Step 2: Run Measurement Script

**Context**: Use JavaScript to query line-height in Tor Browser console.

Load the test HTML in Tor Browser and execute in console:

```javascript
let p = document.querySelector('p');
let style = window.getComputedStyle(p);
console.log('Tor Line-Height: ' + style.lineHeight);
```

> Expected output: Platform-specific value, e.g., "Tor Line-Height: 19.2px" on Windows.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[tor-browser]]
- [[fingerprinting]]
- [[css]]
