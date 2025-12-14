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
updated_at: '2025-12-14T17:24:44.974Z'
sub_techniques: []
id: 4679c50b-333f-461f-bae3-fda2254bfe23
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Navigate-to-Long-Subdomain-Test-Site-in-Brave-Android

## Summary

This procedure loads a test website in Brave Browser on Android using a URL with an extended subdomain to prepare for demonstrating the URL eliding vulnerability in the Shields UI.

## Description

The procedure involves opening Brave on an Android device and navigating to a specific test URL from badssl.com, which includes a long subdomain designed to test URL display behaviors. This sets the stage for observing how Brave handles long URLs in its security interfaces, differing from desktop implementations that follow Chromium guidelines by truncating from the front to prevent confusion and spoofing.

## Requirements

1. Android device with Brave Browser version 1.62.165 (Chromium M121 base) installed.
2. Internet connectivity to access external test sites.
3. No special permissions or root access needed.

## Defense

Defensive measures and detection strategies:

- Keep Brave Browser updated to patch UI rendering issues.
- Educate users on verifying full URLs before interacting with browser features.
- Use browser extensions or settings that enforce strict URL validation.

## Objectives

1. Load the test site without errors to simulate a potential malicious page.
2. Confirm the full long subdomain is visible in the omnibox.
3. Establish baseline for comparing UI behaviors in subsequent steps.

## Instructions

### Step 1: Launch Brave Browser

**Context**: Start the browser to access the navigation interface.

Open the Brave app on your Android device from the home screen or app drawer.

> The browser launches to the default new tab or last visited page.

### Step 2: Enter Test URL

**Context**: Navigate to the specific test site to trigger the long subdomain display.

In the omnibox (address bar), type or paste: https://long-extended-subdomain-name-containing-many-letters-and-dashes.badssl.com/ and press enter or tap go.

> The page loads, and the omnibox shows the full URL including the extended subdomain.

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
