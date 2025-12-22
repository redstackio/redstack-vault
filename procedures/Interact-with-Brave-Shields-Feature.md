---
tags:
  - url-spoofing
  - brave-browser
  - android
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile Browser
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:44.970Z'
sub_techniques: []
id: b242ff76-ca00-4260-95db-7eab9700faff
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Interact-with-Brave-Shields-Feature

## Summary

This procedure triggers the Brave Shields popup on Android by interacting with the Shields icon, simulating user actions that expose the vulnerable URL display.

## Description

Brave Shields is a core security feature for blocking ads, trackers, and other threats. On Android, tapping the Shields icon opens a popup where the site's URL is shown. Due to the eliding flaw, long subdomains here are not truncated properly, potentially misleading users about the domain during critical decisions like enabling protections.

## Requirements

1. Brave Browser open with the test site loaded from previous procedure.
2. Shields feature enabled in browser settings.
3. Android device screen unlocked for interaction.

## Defense

Defensive measures and detection strategies:

- Monitor browser logs for unusual UI interactions.
- Implement user training on double-checking domains in popups.
- Patch browser to align with Chromium URL display standards.

## Objectives

1. Open the Shields popup to access URL rendering.
2. Toggle Shields settings to observe dynamic UI updates.
3. Highlight the context where confusion could occur.

## Instructions

### Step 1: Locate Shields Icon

**Context**: Identify the entry point for the security feature.

With the test site loaded, look for the lion-head Shields icon in the URL bar (omnibox) at the top of the screen.

> The icon appears if Shields is active or available for the site.

### Step 2: Tap to Open Popup

**Context**: Activate the UI to display the vulnerable URL element.

Tap the Shields icon to open the popup panel.

> Popup slides in, showing Shields options and the site's URL.

### Step 3: Toggle Shields

**Context**: Simulate user decision-making to trigger URL re-display.

In the popup, switch the Shields toggle from on to off or vice versa for the site.

> The UI updates, but the long subdomain remains untruncated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- url-spoofing
- brave-browser
- android
