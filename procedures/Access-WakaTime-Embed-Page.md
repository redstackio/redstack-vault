---
tags:
  - clickjacking
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-check-headers]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:12.346Z'
sub_techniques: []
id: 9bb9140a-db91-4ee9-8f5e-a5a0d2b8f56b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-WakaTime-Embed-Page

## Summary

This procedure involves navigating to the WakaTime authenticated embed page to establish access for subsequent vulnerability assessment in a clickjacking attack scenario.

## Description

In the context of exploiting clickjacking on WakaTime, this initial step ensures the target page is reachable under an authenticated session. The page at https://wakatime.com/share/embed displays user-specific shared code information, making it a prime target for UI redressing where attackers overlay invisible elements to capture clicks. Prerequisites include a valid WakaTime login; without authentication, the page may not render sensitive content. Expected outcomes include successful page load, confirming the environment for header inspection and iframe testing.

## Requirements

1. Authenticated WakaTime account with access to share/embed features
2. Web browser with developer tools enabled
3. Network connectivity to wakatime.com

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN on all pages
- Monitor for unusual iframe embedding attempts via web application firewall (WAF)
- Educate users on phishing risks involving overlaid UI elements

## Objectives

1. Gain access to the vulnerable authenticated page
2. Verify session authentication for impact assessment
3. Prepare for vulnerability demonstration

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Log in to WakaTime and access the target URL to simulate an authenticated user session.

**Command** (No command; browser action):

Open your web browser, navigate to https://wakatime.com, log in with credentials, then go to https://wakatime.com/share/embed.

> This loads the page with user dashboard elements. Successful execution shows personalized content without redirects or errors.

### Step 2: Confirm Page Load

**Context**: Verify the page is fully rendered and interactive.

**Command** ([[commands/curl-check-headers]]):
```bash
curl -I https://wakatime.com/share/embed
```

> Use this to get headers early; expect 200 OK status. If authenticated, cookies may influence response, but focus on frame headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-headers]]

## Tools Used


## Tags

- [[clickjacking]]
- [[web]]
