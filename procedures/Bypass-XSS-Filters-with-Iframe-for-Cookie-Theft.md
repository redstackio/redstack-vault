---
tags:
  - xss-bypass
  - iframe
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T00:11:09.423Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8156a92d-0e35-4eb8-be07-0fe59e6ad317
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Bypass-XSS-Filters-with-Iframe-for-Cookie-Theft

## Summary

This procedure demonstrates bypassing basic XSS filters by injecting a same-origin iframe via reflected UTM parameters, allowing access to the document's cookie storage for theft of session data, potentially enabling account takeover.

## Description

When simple script tags are filtered, attackers can use alternative vectors like iframes sourcing from the same domain to inherit context and execute events (e.g., onmouseover). This leverages the browser's same-origin policy in reverse, granting access to document.cookie and document.domain. Tested on Instacart's main domain, it requires crafting encoded payloads that evade sanitization. Outcomes include alerting sensitive data, with prerequisites being a confirmed XSS vector and browser support for iframes.

## Requirements

1. A vulnerable reflected XSS endpoint with UTM parameters
2. Web browser capable of rendering iframes (e.g., modern browsers)
3. URL encoding tool or manual knowledge for payload obfuscation

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected parameters with HTML entity encoding and context-aware escaping
- Enforce strict CSP headers to block inline iframes and unsafe events
- Implement client-side monitoring for unauthorized iframe loads and cookie access attempts

## Objectives

1. Evade filters to load a same-domain iframe
2. Access and exfiltrate document.cookie via event handlers
3. Highlight risks of session hijacking from stolen cookies

## Instructions

### Step 1: Craft Bypass Payload

**Context**: Design a payload that closes HTML attributes and injects an iframe with an event handler to access cookies, using URL encoding to avoid detection.

Manually construct the URL:

```url
https://www.instacart.com/green-zebra-grocery?utm_source=%3E'%3d'%3E%22%3E%3Ciframe src=%22https://www.instacart.com%22 onmouseover=alert(document.cookie)%3E%3C/iframe%3E/927&utm_campaign=%22%27%3E<script>alert(/XSS/)</script>
```

> The payload ">'=\'>\" ><iframe src=\"https://www.instacart.com\" onmouseover=alert(document.cookie)></iframe>/927 breaks out and loads the iframe. The /927 is a dummy path to balance tags.

### Step 2: Execute and Verify Cookie Access

**Context**: Load the URL and interact with the iframe to trigger cookie revelation.

Visit the URL in the browser and hover over the iframe element.

> Expected behavior: The iframe loads content from www.instacart.com, and onmouseover alerts the full document.cookie string, exposing session tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-bypass]]
- [[iframe]]
- [[cookie-theft]]
