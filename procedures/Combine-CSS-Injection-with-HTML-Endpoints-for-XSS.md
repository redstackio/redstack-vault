---
id: proc-combine-css-injection-xss
tags:
  - xss
  - css-injection
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
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:34.297Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Combine CSS Injection with HTML Endpoints for XSS

## Summary

This procedure chains CSS injection with POST endpoints returning HTML (e.g., /choose_broadcaster_chat_color) to inject executable scripts, escalating to DOM-based XSS.

## Description

Endpoints like POST /choose_broadcaster_chat_color return text/html without escaping, allowing CSS payloads to close HTML tags and insert <script> tags. Combined with bgcolor injection, this executes JS in the victim's context. Prerequisites: Control over POST parameters and confirmed CSS vuln.

## Requirements

1. Ability to send POST requests (browser or proxy).
2. Knowledge of HTML-returning endpoints.
3. Encoded payloads for CSS-to-HTML breakout.

## Defense

Defensive measures and detection strategies:

- Escape all user input in HTML responses.
- Use Content-Type: text/plain for non-HTML or strict parsing.
- WAF rules to block script injections in POST bodies.

## Objectives

1. Inject CSS into HTML context.
2. Break out to insert JS.
3. Achieve arbitrary execution.

## Instructions

### Step 1: Identify Target Endpoint

**Context**: Select an endpoint returning HTML.

Target: POST /choose_broadcaster_chat_color (Content-Type: text/html; charset=utf-8).

### Step 2: Craft Chained Payload

**Context**: Use CSS injection to manipulate the HTML response.

In POST body or params, inject via bgcolor or similar: payload closing CSS and HTML, e.g., %7D%3Cscript%3Ealert(1)%3C/script%3E

Send via browser POST or curl equivalent (adapt as needed):

```http
POST /choose_broadcaster_chat_color HTTP/1.1
Host: chaturbate.com
Content-Type: application/x-www-form-urlencoded

bgcolor=%7D%3Cscript%3Ealert('XSS')%3C/script%3E&other_param=value
```

> This attempts to inject <script> into the HTML response.

**Expected Output**: Alert or JS execution on render.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[css-injection]]
