---
tags:
  - web
  - iframe
  - cross-origin
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - iOS
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 996fef5e-b407-45b5-9d2e-474eaa97e69b
created_at: '2025-12-14T03:47:12.892Z'
updated_at: '2025-12-14T03:47:12.892Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Load-Victim-Page-with-Cross-Origin-Iframe

## Summary

This procedure sets up the initial attack context by loading a victim web page in Brave iOS that embeds a malicious cross-origin iframe, allowing subsequent subframe actions without immediate detection.

## Description

In the context of exploiting Brave's iOS FIDO U2F weaknesses, the attacker hosts a malicious iframe on a cross-origin domain (e.g., evil.csrf.jp) and embeds it in a victim-controlled page (e.g., alice.csrf.jp). This positions the subframe to invoke privileged APIs like u2f.register() via postMessage, bypassing standard same-origin policy checks. The procedure requires the victim to visit the page, simulating a drive-by compromise scenario. Expected outcomes include successful iframe loading and readiness for U2F triggering, leading to universal XSS.

## Requirements

1. Brave browser on iOS device
2. Access to host malicious iframe content on a cross-origin domain
3. Victim page URL that can embed arbitrary iframes (e.g., via user-generated content or phishing link)

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict iframe sources
- Monitor for unexpected cross-origin postMessage invocations in browser logs
- Educate users on verifying embedded content origins

## Objectives

1. Establish cross-origin subframe context for privilege escalation
2. Position for FIDO U2F exploitation without alerting the user
3. Enable subsequent injection of malicious payloads

## Instructions

### Step 1: Host Malicious Iframe Content

**Context**: Prepare the attacker's domain with JavaScript to invoke U2F APIs.

Create an HTML page on evil.csrf.jp containing script to call U2F.postMessage for u2f.register().

> No command; this is done via web development tools like a simple text editor or server setup.

### Step 2: Embed Iframe in Victim Page

**Context**: Modify or lure victim to a page that loads the malicious iframe.

Use an iframe tag: <iframe src="https://evil.csrf.jp/u2f-trigger.html"></iframe> in https://alice.csrf.jp/brave/uxss_victim.php.

> Load the page in Brave iOS; confirm iframe renders without CSP blocks.

### Step 3: Verify Setup

**Context**: Ensure the cross-origin context is active.

Inspect the page in browser dev tools (if available) or observe no errors on load.

> Expected: Page and iframe load; subframe JavaScript executes in isolation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[iframe]]
- [[cross-origin]]
