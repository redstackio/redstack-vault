---
id: proc-uuid-2
tags:
  - brave
  - webtorrent
  - download-bypass
type: procedure
tools:
  - '[[tools/WebTorrent]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:23:28.246Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trigger-Download-via-Brave-WebTorrent

## Summary

This procedure simulates victim interaction with a malicious webpage in Brave browser, using WebTorrent to request and download a spoofed .torrent file that contains executable content, bypassing type validation.

## Description

Attackers host a demo page with a link that prompts WebTorrent download. When the user selects 'Save .torrent file', Brave sends a request with Referer header, receiving spoofed headers but malicious payload. The file saves as .torrent but executes as .bat upon opening, enabling RCE. Targets Windows users with Brave.

## Requirements

1. Brave browser on Windows with WebTorrent enabled
2. Access to the malicious server URL
3. Victim interaction (clicking link and selecting save option)

## Defense

Defensive measures and detection strategies:

- Use browser extensions to scan downloads for malware
- Disable automatic torrent handling in Brave settings
- Verify file contents before opening, especially mismatched extensions
- Network proxies to inspect download requests

## Objectives

1. Initiate download via browser-integrated torrent client
2. Exploit header validation to receive disguised malware
3. Save file in a way that evades user suspicion

## Instructions

### Step 1: Visit Malicious Page

**Context**: Direct victim to the attack page to start the process.

**Instructions**: Open https://php-demo-app-shibli.cfapps.io/test-driver.php in Brave on Windows.

> Expected: Page loads with 'click me' link.

### Step 2: Initiate and Save Download

**Context**: Trigger WebTorrent dialog and select save option.

**Instructions**: Click the 'click me' link, then in the download prompt, choose 'Save .torrent file'.

> This sends request with Referer; server responds with .torrent headers but .bat content. File saves as PoC.torrent.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/WebTorrent]]

## Tags

- brave
- download
- spoofing
