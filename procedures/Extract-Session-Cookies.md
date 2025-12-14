---
tags:
  - cookie-theft
  - session-extraction
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/EditThisCookie]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:33:12.460Z'
sub_techniques: []
id: 48ad2bfe-f609-4b05-bf17-79c0b4136ce8
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Extract-Session-Cookies

## Summary

This procedure captures session cookies from an active browser session on https://micropurchase.18f.gov/, simulating theft via interception or extensions, which can be reused for account takeover due to lack of expiration.

## Description

After authentication, session cookies (e.g., those handling GitHub OAuth state) are stored client-side without proper invalidation. Tools like Burp Suite intercept HTTP traffic to extract them, or browser extensions directly access cookie storage. In a real attack, these could be stolen via XSS, MITM, or malware. The target environment is a web browser interacting with the site's HTTPS endpoint.

## Requirements

1. Active session established via prior authentication
2. Installed browser extensions or proxy tools for cookie access
3. Permissions to read browser storage (no elevated privileges needed)

## Defense

Defensive measures and detection strategies:

- Enforce Secure and HttpOnly cookie flags to block JavaScript access
- Implement cookie encryption and server-side validation with timestamps
- Log and alert on cookie access patterns or bulk extractions

## Objectives

1. Obtain raw session cookie data for hijacking
2. Simulate real-world theft vectors like network sniffing
3. Ensure cookies are complete for full session replay

## Instructions

### Step 1: Intercept Traffic with Proxy

**Context**: Route browser traffic through a proxy to capture cookies during session activity.

Configure [[tools/Burp-Suite]] as a proxy and browse the site.

> Expected: Proxy history shows requests with Set-Cookie headers; export cookies from the tool.

### Step 2: Use Browser Extension for Direct Extraction

**Context**: Directly view and copy cookies from the browser's storage.

Install and open [[tools/EditThisCookie]], select the domain, and export cookies.

> Expected: JSON or text export of cookies like session_id=abc123; auth_token=xyz789.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/EditThisCookie]]

## Tags

- [[cookie-theft]]
- [[session-extraction]]
- [[web]]
