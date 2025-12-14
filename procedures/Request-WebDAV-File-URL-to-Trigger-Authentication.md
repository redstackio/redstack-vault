---
tags:
  - webdav
  - basic-auth
  - nextcloud
type: procedure
tools:
  - '[[tools/HTTP-Proxy-Tool]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:31:10.667Z'
sub_techniques: []
id: fda26c8e-358e-4f98-91a4-9ab2229966a4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Request-WebDAV-File-URL-to-Trigger-Authentication

## Summary

This procedure triggers a Basic Authentication prompt by requesting a direct file URL through Nextcloud's WebDAV endpoint, revealing the use of insecure authentication without HTTPS.

## Description

In Nextcloud, WebDAV endpoints like /remote.php/webdav/ allow direct file access. Requesting such a URL without prior authentication initiates a Basic Auth challenge. This exposes the authentication mechanism, which sends credentials in Base64 over potentially unencrypted HTTP, as per the vulnerability in report #151847. The target environment is a web-based Nextcloud instance with WebDAV enabled. Prerequisites include network access to the server and a web browser.

## Requirements

1. Network connectivity to the Nextcloud server (e.g., http://nc.hostiso.cloud)
2. Knowledge of a file path in the WebDAV structure (e.g., /Photos/Squirrel.jpg)
3. Web browser for making the request

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS for all endpoints to encrypt transmissions
- Implement token-based auth (e.g., app passwords) instead of Basic Auth for WebDAV
- Monitor for unusual direct file access attempts via WebDAV logs

## Objectives

1. Initiate Basic Auth challenge to observe the mechanism
2. Confirm lack of additional protections like HTTPS
3. Highlight risk for subsequent brute-force attempts

## Instructions

### Step 1: Navigate to WebDAV File URL

**Context**: Use a browser to request a protected file, triggering the auth prompt.

No specific command; perform manually:

Open browser and enter: http://nc.hostiso.cloud/remote.php/webdav/Photos/Squirrel.jpg

> This sends an HTTP GET request to the WebDAV endpoint, resulting in a 401 Unauthorized response with a Basic Auth WWW-Authenticate header. The browser prompts for credentials.

### Step 2: Observe the Prompt

**Context**: Verify the authentication dialog appears, confirming Basic Auth usage.

No command needed; inspect the browser dialog.

> Expected: Popup asking for username and password. Do not enter credentials yet if planning to capture.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/HTTP-Proxy-Tool]]

## Tags

- [[webdav]]
- [[basic-auth]]
- [[nextcloud]]
