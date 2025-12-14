---
tags:
  - nextcloud
  - recon
  - share-link
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:31:43.027Z'
sub_techniques: []
id: aa915cf8-0a9c-4cfe-9a24-1d78c94267b8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Obtain-Private-Share-Link-from-Nextcloud-Tasks

## Summary

This procedure involves logging into a Nextcloud instance, navigating to the Tasks app, and generating a private share link for a task or calendar, which exposes the target username in the URL path, enabling subsequent authentication attacks.

## Description

In Nextcloud, the Tasks feature allows users to share calendar items via private links that point to WebDAV endpoints. These links include the username in the path (e.g., /remote.php/dav/calendars/<username>/), providing attackers with the credential for brute forcing. This step requires initial legitimate access or social engineering to obtain the link, and sets up the vulnerability exploitation by revealing the username without additional reconnaissance.

## Requirements

1. Valid login credentials to the target Nextcloud account (or phishing to obtain a share link)
2. Browser access to the Nextcloud web interface
3. Tasks app enabled in the Nextcloud instance

## Defense

Defensive measures and detection strategies:

- Disable public or private sharing in Tasks app for sensitive calendars
- Monitor for unusual share link generations via Nextcloud audit logs
- Implement username obfuscation or short tokens in share URLs (if configurable)

## Objectives

1. Extract the target username from the share link URL
2. Obtain a WebDAV endpoint for authentication testing
3. Prepare for credential brute forcing

## Instructions

### Step 1: Access Nextcloud Tasks

**Context**: Log in and navigate to the Tasks section to create or select a shareable item.

No command required; use the web interface:

- Log in to Nextcloud at `https://<target-host>/`
- Click on the Tasks app icon in the top menu
- Select or create a task/calendar entry

> Expected output: Tasks interface loads, showing calendar items.

### Step 2: Generate Private Share Link

**Context**: Create a private share link that exposes the WebDAV path with username.

No command required; use the sharing UI:

- Right-click on a task or calendar and select "Share"
- Choose "Private link" and generate the link
- Copy the URL, which will be in the format `https://<host>/remote.php/dav/calendars/<username>/<calendar-id>/`

> Expected output: URL with embedded username (e.g., ha.ckitbharat3@gmail.com).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[nextcloud]]
- [[recon]]
