---
id: proc-uuid-123
tags:
  - information-disclosure
  - privacy-leak
  - browser
  - tor
  - referer
type: procedure
tools:
  - '[[tools/Brave-Browser]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Browser
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:25:13.409Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Demonstrate Brave Tor Referer Leak

## Summary

This procedure demonstrates an information disclosure vulnerability in Brave browser's Tor private window feature, where the Referer header is sent during cross-origin navigations instead of being blanked, leaking the originating domain and potentially compromising user anonymity in the Tor network.

## Description

The vulnerability occurs because Brave fails to enforce a strict no-referrer policy in Tor mode. When navigating from a controlled page (e.g., an attacker-hosted site) to an external site, the Referer header includes the source domain. This is particularly dangerous for Tor users visiting .onion sites, as it can reveal sensitive browsing patterns to third parties. The procedure involves launching Tor mode, visiting a test page, clicking a link, and verifying the leak on the destination site. Tested on Brave 1.29.79 based on Chromium 93.0.4577.63 on Windows 10.

## Requirements

1. Brave browser installed with Tor support (version 1.29.79 or vulnerable equivalent)
2. Windows 10 or compatible OS for testing
3. Internet access to load test pages via Tor
4. No special privileges or credentials required

## Defense

Defensive measures and detection strategies:

- Update to a patched version of Brave where Referer is properly stripped in Tor mode
- Use browser extensions like uBlock Origin or Referer Control to enforce no-referrer policies
- Monitor network traffic for unexpected Referer headers in Tor sessions using tools like Wireshark
- Educate users on verifying browser privacy settings and avoiding untrusted links in private modes

## Objectives

1. Reproduce the Referer leak to confirm vulnerability presence
2. Highlight privacy risks for Tor users accessing .onion sites
3. Demonstrate potential for deanonymization through browsing history exposure

## Instructions

### Step 1: Launch Brave in Tor Private Window

**Context**: Start the browser in anonymity mode to simulate a privacy-focused session.

No specific command; manually open Brave and select 'New Private Window with Tor' from the menu. Confirm Tor connection via the browser's status indicator.

> Expected: Tor onion icon appears, and all traffic routes through Tor network.

### Step 2: Navigate to Test Page

**Context**: Load a page that will serve as the referer source.

Manually enter the URL https://kirtikumarar.com/referrer/top-page.html in the address bar.

> Expected: Page loads, showing a link to an external site like whatismybrowser.com.

### Step 3: Click Link to Trigger Navigation

**Context**: Perform the action that sends the Referer header.

Click the link on the page to https://www.whatismybrowser.com/.

> Expected: Browser navigates to the external site without blocking the request.

### Step 4: Verify Referer Leak

**Context**: Inspect the destination to confirm disclosure.

On whatismybrowser.com, check the displayed request headers or use browser developer tools (F12 > Network tab) to view the incoming request's Referer field.

> Expected: Referer shows 'https://kirtikumarar.com/referrer/top-page.html' or similar, not empty.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Brave-Browser]]

## Tags

- information-disclosure
- privacy-leak
- browser
- tor
- referer
