---
tags:
  - cache-serving
  - xss-delivery
  - expiration-wait
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-check-expires]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: bd95a4e0-cee1-4917-ad81-57f17db4fc87
created_at: '2025-12-14T03:15:26.531Z'
updated_at: '2025-12-14T03:15:26.531Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Wait-for-Cache-Expiration-and-Serve-to-Victims

## Summary

This procedure involves monitoring cache expiration headers, waiting for the poisoned cache to become active, and verifying that subsequent requests serve pages with the fake domain, executing stored XSS payloads in victims' browsers.

## Description

After poisoning the cache via spidering, the full page cache in Concrete CMS serves the manipulated pages after the initial generation phase expires. Attackers check 'Expires' headers to time the wait, then normal visitors receive content with fake-site.com as BASE_URL, altering relative links to point to XSS payloads (e.g., javascript:alert('XSS')). Prerequisites: Poisoned cache generated. Expected outcome: XSS execution on victim browsers without further attacker action.

## Requirements

1. Poisoned cache files already generated on the server
2. Ability to send HTTP requests to check headers (e.g., curl)
3. Control over a fake domain with XSS payload hosted (e.g., <img src="x" onerror="alert('XSS')">)

## Defense

Defensive measures and detection strategies:

- Shorten cache TTL to limit poisoning window
- Validate cached content for hostname consistency before serving
- Deploy XSS filters or CSP to block injected scripts

## Objectives

1. Determine and wait for cache serving phase
2. Confirm poisoned content delivery
3. Achieve XSS execution via link manipulation

## Instructions

### Step 1: Inspect Cache Expiration Headers

**Context**: Fetch a page to read the 'Expires' header and calculate wait time.

**Command** ([[commands/curl-check-expires]]):
```bash
curl -I https://target-ip-or-fake-site.com/page
```

> The -I flag gets headers only. Look for 'Expires: [timestamp]' or 'Cache-Control: max-age'. Expected output: Headers showing expiration (e.g., Expires: Wed, 01 Oct 2023 12:00:00 GMT).

### Step 2: Re-Request After Expiration

**Context**: After waiting, access the page normally to serve the cache and test XSS.

**Command** ([[commands/curl-check-expires]] for full response):
```bash
curl https://target-domain/page
```

> Inspect response for fake-site.com in HTML (e.g., <base href="https://fake-site.com/">). Load in browser to trigger XSS. Expected output: HTML with embedded fake domain; alert or script execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-expires]]

## Tools Used


## Tags

- [[xss-delivery]]
- [[cache-serving]]
