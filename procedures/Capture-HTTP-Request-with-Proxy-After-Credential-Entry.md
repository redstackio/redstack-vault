---
tags:
  - proxy
  - http-capture
  - basic-auth
type: procedure
tools:
  - '[[tools/HTTP-Proxy-Tool]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:31:10.657Z'
sub_techniques: []
id: 2dadc186-6daa-4148-8094-a2906c660736
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Capture-HTTP-Request-with-Proxy-After-Credential-Entry

## Summary

This procedure involves entering credentials into the Basic Auth prompt while using a proxy to intercept the HTTP request, allowing inspection of how credentials are transmitted in Nextcloud WebDAV access.

## Description

After triggering the auth prompt, submitting credentials via the browser sends them in the Authorization header. Intercepting this with a proxy tool reveals the insecure transmission. This is key to understanding the vulnerability where Base64 encoding provides no real protection, especially over HTTP. Targets Nextcloud WebDAV; requires proxy setup and valid test credentials.

## Requirements

1. [[tools/HTTP-Proxy-Tool]] configured and running (e.g., listening on 127.0.0.1:8080)
2. Browser proxy settings updated to route through the tool
3. Valid username/password for the Nextcloud instance

## Defense

Defensive measures and detection strategies:

- Disable Basic Auth or restrict WebDAV to HTTPS-only
- Use WAF to block or log proxy-intercepted traffic patterns
- Enable HSTS to prevent HTTP downgrades

## Objectives

1. Intercept the credential submission request
2. Capture full HTTP headers including Authorization
3. Validate transmission method for exposure analysis

## Instructions

### Step 1: Configure Proxy and Enter Credentials

**Context**: Set up interception and submit credentials to generate the request.

No command; manual setup:

1. Start [[tools/HTTP-Proxy-Tool]] and configure browser to use it as proxy.
2. In the auth prompt, enter username (e.g., testuser) and password (e.g., testpass), then submit.

> The browser sends the request with credentials; proxy captures it. Expected: Proxied request shows method GET, path /remote.php/webdav/Photos/Squirrel.jpg, and headers.

### Step 2: Verify Capture

**Context**: Confirm the request is intercepted without errors.

Inspect in proxy interface.

> Look for status 200 OK if credentials valid, or 401 if invalid. Key: Presence of Authorization header.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/HTTP-Proxy-Tool]]

## Tags

- [[proxy]]
- [[http-capture]]
- [[basic-auth]]
