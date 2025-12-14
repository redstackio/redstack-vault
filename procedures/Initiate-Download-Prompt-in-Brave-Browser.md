---
tags:
  - brave-browser
  - webtorrent
  - download-trigger
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
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:46:32.001Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: fec58642-8213-4909-b436-fd09d76d3ede
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Initiate Download Prompt in Brave Browser

## Summary

This procedure involves accessing a malicious page in Brave browser to trigger a download prompt via WebTorrent integration, exploiting the lack of content validation to save a malicious file as a torrent.

## Description

Brave's built-in WebTorrent feature relies on server-sent Content-Disposition and Content-Type headers to classify downloads. By visiting a page hosted on the malicious PHP server, the browser sends a Referer header that the server uses to respond with torrent-mimicking headers. Clicking a link on the page initiates the download, prompting the user to 'Save .torrent file', which downloads the batch payload without inspection. This targets Windows users with default Brave settings.

## Requirements

1. Brave browser on Windows with WebTorrent enabled
2. Access to the malicious server URL
3. User interaction to click the download link

## Defense

Defensive measures and detection strategies:

- Update Brave to latest version and disable experimental features like WebTorrent
- Use antivirus software to scan downloads
- Browser policies to block automatic downloads or validate file types
- Network monitoring for suspicious Referer patterns

## Objectives

1. Trigger server-side header manipulation via Referer
2. Initiate WebTorrent download prompt
3. Save file with deceptive extension

## Instructions

### Step 1: Navigate to Malicious Page

**Context**: Load the page to send the Referer header.

**Instructions**: Open Brave on Windows and visit https://your-server.com/test-driver.php or a wrapper page with the link.

> The server logs the Referer containing 'brave' and prepares response.

### Step 2: Click Download Link

**Context**: Activate the WebTorrent integration.

**Instructions**: On the page, click <a href="download-endpoint.php">Click me</a>, where download-endpoint.php is the PHP script.

> Browser detects torrent headers and shows download dialog.

### Step 3: Select Save Option

**Context**: Choose the torrent save to bypass validation.

**Instructions**: In the prompt, select 'Save .torrent file' and choose a save location.

> File saves as PoC.torrent with batch content inside.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/WebTorrent]]

## Tags

- brave-browser
- webtorrent
- download-trigger
