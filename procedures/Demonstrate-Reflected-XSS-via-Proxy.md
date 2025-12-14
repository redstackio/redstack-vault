---
tags:
  - xss
  - reflected
  - proxy-chain
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:53:38.170Z'
sub_techniques: []
id: 9325f2cf-0597-4e39-a86f-8f92e218ab8f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Demonstrate Reflected XSS via Proxy

## Summary

This procedure chains the SSRF proxy to inject and reflect malicious HTML/JavaScript, enabling cross-site scripting attacks in the victim's browser.

## Description

The CORS proxy returns unsanitized HTML, allowing attackers to proxy malicious payloads that execute on reflection. This bypasses CORS and enables client-side attacks like session theft. In the Flyte context, it amplifies SSRF impact; prerequisites: Working SSRF; outcomes: Script execution in browser.

## Requirements

1. Functional SSRF via proxy confirmed
2. Malicious HTML payload (e.g., <script>alert(1)</script>)
3. Victim browser to trigger reflection

## Defense

Defensive measures and detection strategies:

- Sanitize all proxied content with HTML escaping
- Enforce Content-Security-Policy headers
- Detect JS injection patterns in proxy logs

## Objectives

1. Inject arbitrary HTML through the proxy
2. Achieve reflection and execution in browser
3. Demonstrate potential for data theft

## Instructions

### Step 1: Prepare Malicious Payload

**Context**: Create an HTML document with XSS payload.

Embed JS in a simple HTML: <html><body><script>alert('XSS')</script></body></html>

> Host or inline the payload for proxying.

### Step 2: Proxy and Trigger XSS

**Context**: Use the proxy to fetch and reflect the payload.

Request the proxy with the malicious HTML URL; view in browser to trigger.

> Alert pops if XSS succeeds, confirming reflection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected]]
- [[proxy-chain]]
