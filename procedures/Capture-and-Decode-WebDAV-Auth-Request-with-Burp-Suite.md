---
tags:
  - burp-suite
  - webdav
  - auth-capture
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
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:31:43.025Z'
sub_techniques: []
id: dd6d216c-5055-4e62-b090-86a84f250bdc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Capture-and-Decode-WebDAV-Auth-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept an authentication attempt to a Nextcloud WebDAV endpoint triggered by a private share link, allowing capture and decoding of the Basic Auth header to confirm the username and prepare for brute forcing.

## Description

When accessing a private WebDAV share link, Nextcloud prompts for Basic Authentication. By proxying the browser traffic through Burp Suite, the HTTP request can be captured, revealing the Base64-encoded Authorization header in the format 'username:password'. Decoding this provides the exact username from the URL and a failed password attempt, exploiting the lack of rate limiting for unlimited tries.

## Requirements

1. Burp Suite installed and running with proxy listener (default port 8080)
2. Browser configured to use Burp proxy (e.g., via FoxyProxy extension)
3. Private share link from Nextcloud Tasks

## Defense

Defensive measures and detection strategies:

- Enable rate limiting on all authentication endpoints, including WebDAV
- Log and monitor Basic Auth attempts for high-volume requests from single IPs
- Use CAPTCHA or multi-factor authentication for share link access

## Objectives

1. Intercept the WebDAV authentication request
2. Decode the Basic Auth header to extract username
3. Validate the endpoint for brute force vulnerability

## Instructions

### Step 1: Configure Proxy and Access Link

**Context**: Set up Burp to intercept traffic and trigger the auth prompt.

No command required; configure in Burp Suite:

- Start Burp Suite and ensure Proxy tab is listening on 127.0.0.1:8080
- Configure browser proxy to 127.0.0.1:8080
- Paste the private share link into a new browser tab and submit with username and random password

> Expected output: Request intercepted in Burp Proxy > HTTP history, showing POST/GET to /remote.php/dav/... with HTTP 401.

### Step 2: Decode Authorization Header

**Context**: Examine and decode the Base64 header in the captured request.

No command required; use Burp's built-in decoder:

- In the intercepted request, locate `Authorization: Basic <base64-string>`
- Right-click the header > Send to Decoder > Base64 Decode
- View the output: `username:randompassword`

> Expected output: Decoded string confirming username (e.g., ha.ckitbharat3@gmail.com:wrongpass).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[tools/Burp-Suite]]
- [[webdav]]
