---
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/inject-xss-payload-via-curl]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 85444c6d-7ba3-4dec-9df5-95dcc6d53683
created_at: '2025-12-13T23:56:20.008Z'
updated_at: '2025-12-13T23:56:20.008Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Stored XSS Payload in Friend Request Message

## Summary

This procedure involves injecting a malicious XSS payload into the optional Message field of a friend request on socialclub.rockstargames.com, exploiting insufficient input sanitization to store and later execute arbitrary JavaScript.

## Description

The attack targets the Add Friend functionality, where the Message field allows HTML tags like SVG objects with escaped characters to be stored. This persists until the victim accepts the request, executing the payload in their browser context, potentially leading to session hijacking or data theft. The root cause is lack of proper escaping and sanitization.

## Requirements

1. Valid attacker account on Social Club
2. Victim's user ID or profile access
3. Web proxy tool like Burp Suite for request manipulation

## Defense

Defensive measures and detection strategies:

- Implement anti-XSS libraries and input sanitization on all user inputs
- Monitor for suspicious HTML tags in stored messages via WAF or logs

## Objectives

1. Store malicious payload in friend request
2. Prepare for execution upon acceptance
3. Achieve arbitrary JS injection

## Instructions

### Step 1: Prepare and Send Friend Request

**Context**: Intercept or craft the friend request to inject the XSS payload.

**Command** ([[commands/inject-xss-payload-via-curl]]):
```bash
curl -X POST 'https://socialclub.rockstargames.com/friends/add' -d 'friendId=victim_id&message=<svg><object data="javascript:alert(\'XSS\')">' -H 'Cookie: your_session_cookie'
```

> This command sends the friend request with the SVG-based XSS payload, bypassing basic filters through character escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/inject-xss-payload-via-curl]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[stored-xss]]
