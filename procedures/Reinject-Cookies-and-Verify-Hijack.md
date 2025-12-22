---
tags:
  - session-hijacking
  - cookie-injection
  - account-takeover
type: procedure
tools:
  - '[[tools/EditThisCookie]]'
  - '[[tools/Cookies-Manager-Plus]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:12.455Z'
sub_techniques: []
id: c17d4368-235c-4730-b589-e50afcd99175
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Valid Accounts]]'
---
# Reinject-Cookies-and-Verify-Hijack

## Summary

This procedure reinjects stolen session cookies into the browser to hijack the victim's account on https://micropurchase.18f.gov/, exploiting the lack of expiration for full unauthorized access.

## Description

With cookies extracted earlier, they are imported back post-logout, reviving the session server-side. Tools like EditThisCookie allow direct injection. Verification shows the account dashboard accessible, confirming takeover. This targets web sessions with GitHub OAuth, where cookies persist indefinitely.

## Requirements

1. Extracted cookie data from prior extraction step
2. Clean browser session after logout
3. Extensions for cookie import

## Defense

Defensive measures and detection strategies:

- Bind sessions to IP/user-agent and invalidate on mismatch
- Implement CSRF tokens and session fingerprinting
- Alert on session revivals from cleared states or unusual agents

## Objectives

1. Restore session using stolen cookies
2. Gain unauthorized account control
3. Validate impact through access to protected features

## Instructions

### Step 1: Inject Hijacked Cookies

**Context**: Load the stolen cookies into the browser storage.

Use [[tools/EditThisCookie]] or [[tools/Cookies-Manager-Plus]] to import and set the cookies for the domain.

> Expected: Cookies appear in browser dev tools as active.

### Step 2: Refresh and Verify Access

**Context**: Test if the session is hijacked by accessing the site.

Navigate to https://micropurchase.18f.gov/ and refresh.

> Expected: Logged-in state with victim's account options; no login prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/EditThisCookie]]
- [[tools/Cookies-Manager-Plus]]

## Tags

- [[session-hijacking]]
- [[cookie-injection]]
- [[account-takeover]]
