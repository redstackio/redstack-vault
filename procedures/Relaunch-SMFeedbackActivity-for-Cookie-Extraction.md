---
id: proc-uuid-005
tags:
  - cookie-theft
  - xss
  - data-exfiltration
type: procedure
tools:
  - '[[tools/Custom-Attacker-App]]'
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Android
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:33:06.348Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Credentials In Files]]'
---
# Relaunch-SMFeedbackActivity-for-Cookie-Extraction

## Summary

This procedure relaunches the vulnerable activity with a payload that extracts and displays cookies from the app's shared WebView storage.

## Description

After a 20-second delay, the intent is resent with smSPageHTML='<h1>Exploited</h1><script>document.write(document.cookie)</script>' and the same baseURL. The JS accesses document.cookie, which includes cookies from all domains loaded in the app's WebViews (e.g., my.exness.asia JWTs), due to shared storage and no origin isolation.

## Requirements

1. Prior successful initial payload
2. User logged into Exness app for valid cookies
3. WebView cookie manager enabled

## Defense

Defensive measures and detection strategies:

- Isolate WebView cookie storage per domain or app
- Sanitize HTML inputs and disable JS for user-supplied data
- Implement CSP or JS hooks to block cookie access

## Objectives

1. Steal session credentials via XSS
2. Display cookies for capture
3. Enable downstream account compromise

## Instructions

### Step 1: Wait and Relaunch

**Context**: Allow time for session establishment.

App delays 20 seconds, then launches intent again.

**Expected Output**: Activity relaunches with new payload.

### Step 2: Extract Cookies

**Context**: JS reads and writes cookies to DOM.

Observe WebView output showing cookie strings.

**Expected Output**: Cookies like 'jwt=eyJ...' displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript (for cookie access)
- [[Credentials In Files]] Credentials In Files (shared cookie storage)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-Attacker-App]]

## Tags

- cookie-theft
- xss
- data-exfiltration
