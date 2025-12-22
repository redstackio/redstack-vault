---
id: proc-uuid-1
tags:
  - url-scheme
  - discovery
  - ios
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:42.643Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover-TikTok-URL-Scheme-for-Follows

## Summary

This procedure involves analyzing the TikTok iOS app to identify vulnerable URL schemes that handle sensitive actions like following accounts without proper CSRF protections.

## Description

URL schemes in iOS apps allow deep linking from web content to app functions. In TikTok's case, a misconfiguration in the 'tiktok://' scheme permits direct execution of follows via parameters like 'username' without token validation or user confirmation. This enables CSRF attacks when triggered from a malicious webpage. The procedure targets iOS environments with the app installed, requiring reverse engineering or empirical testing to map endpoints.

## Requirements

1. iOS device with TikTok app installed and authenticated user session
2. Development tools like Xcode or a decompiler (e.g., Hopper) for app analysis
3. Local web server for testing URL triggers

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens or user confirmation dialogs for URL scheme actions
- Monitor app logs for unexpected URL scheme invocations
- Use App Transport Security to restrict scheme handling from untrusted sources

## Objectives

1. Identify exploitable URL schemes for unauthorized actions
2. Confirm lack of protections like confirmation prompts
3. Map parameters for follow functionality

## Instructions

### Step 1: Analyze App Binary

**Context**: Decompile or inspect the TikTok app to locate URL scheme registrations.

Use a tool like class-dump or strings command on the IPA file:

```bash
strings TikTok.app/TikTok | grep -i 'tiktok://'
```

> This extracts potential scheme patterns, revealing paths like 'tiktok://user'.

### Step 2: Test Scheme Manually

**Context**: Verify the scheme triggers sensitive actions without consent.

Create a test HTML file and open it in Safari on iOS:

```html
<a href="tiktok://user?username=testuser">Test Follow</a>
```

> Expected: App opens and follows 'testuser' silently if vulnerable.

### Step 3: Document Vulnerable Endpoints

**Context**: Record the exact URL format for exploitation.

Note the working scheme, e.g., 'tiktok://user?username=arbitrary' leads to auto-follow.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[url-scheme]]
- [[Discovery]]
- [[ios]]
