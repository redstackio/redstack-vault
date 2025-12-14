---
tags:
  - xss
  - html-injection
type: procedure
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.695Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: cd5a2436-7fa4-4f9e-838c-e4ea91e72c45
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Trigger-XSS-with-onfinish-in-Marquee

## Summary

This procedure exploits an HTML injection vulnerability in the rhsearch URL parameter to execute JavaScript via an onfinish event in a <marquee> tag, confirming reflected XSS on page load.

## Description

The target help page renders the rhsearch fragment without sanitization, allowing injected HTML tags with event handlers to execute JS in the victim's browser. This can lead to session theft or other client-side attacks when a user is tricked into visiting the URL. The attack requires no authentication and works on standard web browsers.

## Requirements

1. Web browser with JavaScript enabled
2. Direct access to the vulnerable URL: https://[redacted]/help-leave/help/index.htm?ux=search
3. Ability to encode payloads for URL transmission

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side input sanitization for URL fragments using libraries like DOMPurify
- Use Content Security Policy (CSP) to restrict inline scripts and event handlers
- Monitor for anomalous JavaScript alerts or network requests from help pages

## Objectives

1. Verify arbitrary JS execution in the browser context
2. Demonstrate potential for data exfiltration via alerts
3. Highlight lack of HTML escaping in URL handling

## Instructions

### Step 1: Encode and Construct Payload

**Context**: Create a basic HTML payload using <marquee> with an onfinish event to trigger JS immediately after rendering.

Encode the payload: `<marquee loop=1 onfinish=alert(document.domain)>test</marquee>` becomes `%3Cmarquee%20loop=1%20onfinish=alert(document.domain)%3Etest%3C%2Fmarquee%3E`.

Append to the base URL:

```url
https://[redacted]/help-leave/help/index.htm#rhsearch=%3Cmarquee%20loop=1%20onfinish=alert(document.domain)%3Etest%3C%2Fmarquee%3E&ux=search
```

> The marquee tag animates once and fires the onfinish event, executing alert(document.domain) to display the current domain, proving JS execution.

### Step 2: Visit and Validate

**Context**: Load the crafted URL in a browser to observe execution.

Navigate to the URL and wait for the page to render.

> Expected: Alert box pops up showing the domain (e.g., subdomain.dod.mil). Check browser developer tools for injected DOM elements.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[html-injection]]
