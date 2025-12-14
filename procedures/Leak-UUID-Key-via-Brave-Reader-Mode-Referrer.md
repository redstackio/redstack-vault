---
id: proc-brave-referrer-leak
tags:
  - referrer-leak
  - information-disclosure
  - brave-ios
type: procedure
tools:
  - '[[tools/reader_uuid_leakage-php]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Archive via Utility]]'
updated_at: '2025-12-14T03:16:14.696Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Archive via Utility]]'
---
# Leak UUID Key via Brave Reader Mode Referrer

## Summary

This procedure exploits a referrer policy misconfiguration in Brave iOS's ReaderViewLoading.html to leak a sensitive UUID key from the internal reader mode URL, enabling attackers to gather data for subsequent privilege escalation attacks.

## Description

The attack targets Brave iOS versions 1.32.3 and higher on iOS 14.x and below. By activating reader mode and navigating via a long-press in a new private tab, the ReaderViewLoading.html template loads without a meta referrer tag (unlike Reader.html), causing the REFERER header to include the full reader mode URL with the uuidKey during session restoration. This key is captured by an attacker-controlled server, providing a foothold for further exploits like XSS. Prerequisites include the victim using Brave iOS and visiting an attacker-controlled page.

## Requirements

1. Victim device running Brave iOS 1.32.3+ on iOS 14.x or below.
2. Attacker controls an HTTPS server hosting the malicious page and logging script.
3. Network access for the victim to load the attacker's page.

## Defense

Defensive measures and detection strategies:

- Add `<meta name="referrer" content="never">` to all reader mode templates in Brave iOS.
- Implement URL validation in navigation handlers to strip or block sensitive internal parameters.
- Monitor server logs for unexpected REFERER headers containing internal URLs or UUID patterns.

## Objectives

1. Leak the uuidKey from the internal reader mode URL.
2. Capture it on an attacker-controlled server.
3. Enable chaining with XSS for privilege escalation.

## Instructions

### Step 1: Host Malicious Page

**Context**: Set up the server to host the page and capture leaks using the provided PHP script.

Deploy [[tools/reader_uuid_leakage-php]] on your HTTPS server at a URL like `https://yourserver.com/brave/reader_uuid_leakage.php`. Ensure it logs REFERER headers.

### Step 2: Lure Victim to Page and Activate Reader Mode

**Context**: Load the page and switch to reader mode to generate the internal URL with uuidKey.

Instruct the victim to visit `https://yourserver.com/brave/reader_uuid_leakage.php` in Brave iOS and activate reader mode via the reader icon.

### Step 3: Trigger Navigation and Leak

**Context**: Perform actions to send the leaky REFERER header.

Have the victim long-press a hyperlink on the page, open in a new private tab, wait a few seconds, and tap 'Load original page'. The server captures the uuidKey from the REFERER.

**Expected Output**: Server logs show REFERER like `internal://reader?url=...&uuidKey=leakedvalue`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Archive via Utility]] Archive Collected Data: Archive via Utility

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/reader_uuid_leakage-php]]

## Tags

- referrer-leak
- brave-ios
- ios
