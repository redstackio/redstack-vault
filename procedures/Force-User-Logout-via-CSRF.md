---
tags:
  - csrf
  - exploit
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-simulate-csrf]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:23.655Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: db636b3f-da11-437c-9098-f2b39edb6395
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Force-User-Logout-via-CSRF

## Summary

This procedure exploits a CSRF vulnerability in the logout endpoint to force a logged-in user's session to terminate by tricking them into loading a malicious URL, demonstrated on the Weblate demo site.

## Description

The attack leverages the unprotected GET-based logout at /accounts/logout/ in Django apps, where no CSRF token is validated. An attacker crafts a link or embeds the URL in a resource (e.g., img src) on a malicious page. When a victim visits it while authenticated, their browser sends the request with session cookies, triggering logout. This disrupts workflow but has low impact. Prerequisites: Victim logged in; attacker can deliver the link via phishing. Expected outcome: Immediate session invalidation.

## Requirements

1. Valid session cookie from a logged-in user (for testing)
2. Attacker-controlled site or email for link delivery
3. Target endpoint confirmed vulnerable (from prior recon)

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens and same-site cookies for session management
- Log and alert on cross-origin requests to sensitive endpoints
- Educate users on phishing and suspicious links

## Objectives

1. Terminate victim sessions to deny access temporarily
2. Demonstrate CSRF impact on authentication flows
3. Highlight need for secure logout implementations

## Instructions

### Step 1: Craft Malicious Link

**Context**: Create a URL pointing to the vulnerable endpoint for delivery to the victim.

**Command** ([[commands/curl-simulate-csrf]]):
```bash
curl -X GET https://demo.weblate.org/accounts/logout/ -b "sessionid=abc123" -v
```

> Simulate the victim's browser by including a session cookie; the command executes the logout, showing redirect in output. In real attack, embed as <a href="https://demo.weblate.org/accounts/logout/">Click here</a> on attacker site.

### Step 2: Deliver and Trigger

**Context**: Trick the victim into visiting the link, causing the cross-site request.

**Command** ([[commands/curl-simulate-csrf]]):
```bash
curl -X GET https://demo.weblate.org/accounts/logout/ --cookie "sessionid=abc123" --referer https://evil.com -v
```

> Use referer to mimic cross-site origin; success confirms logout without origin checks. Victim experiences redirect to login upon click.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/curl-simulate-csrf]]

## Tools Used


## Tags

- [[csrf]]
- [[exploit]]
- [[web]]
