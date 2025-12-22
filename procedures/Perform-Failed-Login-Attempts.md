---
id: proc-lichess-failed-logins
tags:
  - dos
  - authentication
  - web
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-failed-login]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:31:52.594Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Perform-Failed-Login-Attempts

## Summary

This procedure submits multiple incorrect login attempts to Lichess using a target username, exploiting username-only throttling to trigger account lockout and deny service to legitimate users.

## Description

The Lichess login endpoint rate-limits based solely on username, ignoring IP, session, or fingerprint. By sending 5-10 failed logins with wrong passwords from varying IPs, an attacker locks the account for new sessions. Existing sessions persist due to long cookies, but this disrupts logins, increases support tickets, and erodes trust. Prerequisites include a valid username; no tools beyond HTTP clients are needed.

## Requirements

1. Valid target username from reconnaissance
2. Ability to send HTTP POST requests (browser or curl)
3. Optional: IP rotation via proxies/VPN to simulate distributed attempts

## Defense

Defensive measures and detection strategies:

- Tie rate limits to IP, session, or device fingerprint in addition to username
- Implement exponential backoff or CAPTCHA after few failures
- Log and alert on rapid failed attempts per username

## Objectives

1. Exhaust authentication attempts quota
2. Activate lockout mechanism
3. Disrupt legitimate user access

## Instructions

### Step 1: Prepare Login Payload

**Context**: Craft incorrect login data for the target.

Use the username and generate random passwords, e.g., "wrongpass123".

### Step 2: Submit Failed Attempts

**Context**: Send multiple POST requests to the login endpoint.

Execute [[commands/curl-failed-login]] to simulate attempts:

```bash
curl -X POST https://lichess.org/login \
  -d "username=targetuser" \
  -d "password=wrongpass123" \
  -d "next=https://lichess.org"
```

> Repeat 5-10 times, changing passwords each time. Expected output: HTTP 200 with error like "Invalid username or password", no IP block.

### Step 3: Rotate Origin if Needed

**Context**: Use different IPs to confirm vulnerability.

Switch VPN or proxy and repeat Step 2. Lockout still triggers per username only.

> Output: Consistent failures without origin-based limits.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/curl-failed-login]]

## Tools Used


## Tags

- [[dos]]
- [[authentication]]
