---
tags:
  - stored-xss
  - xss
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-xss-payload]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 472b487c-fdd6-4ee8-ad2b-9e042f0d20d7
created_at: '2025-12-14T17:30:58.270Z'
updated_at: '2025-12-14T17:30:58.270Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored-XSS-Injection-via-Bypassed-Access

## Summary

Using bypassed authentication, this procedure injects a persistent XSS payload into TikTok Ads inputs, storing it site-wide to execute malicious JavaScript on visiting users' browsers.

## Description

With unauthorized access from JWT bypass, attackers target unsanitized input fields (e.g., ad descriptions) via POST requests. The payload persists in the backend and renders without escaping, affecting all users viewing the content. This can lead to session theft, keylogging, or phishing. The attack assumes web access to the Ads platform.

## Requirements

1. Valid malicious JWT from prior bypass
2. Proxy for request tampering (Burp Suite)
3. Target endpoint for content submission (e.g., /api/submit-ad)

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs with output encoding
- Implement Content Security Policy (CSP) to block inline scripts
- Scan for XSS patterns in logs and use WAF rules for payload detection

## Objectives

1. Store malicious script persistently
2. Achieve site-wide execution on user visits
3. Compromise sessions or exfiltrate data

## Instructions

### Step 1: Identify Injection Point

**Context**: Locate vulnerable forms or APIs accepting HTML/JS.

Use Burp to spider the Ads dashboard and find POST to /api/submit-ad.

### Step 2: Inject Payload

**Context**: Submit XSS script in a field like 'description'.

**Command** ([[commands/inject-xss-payload]]):
```bash
curl -X POST -H "Authorization: Bearer $(cat malicious.jwt)" -d 'description=<script>alert("XSS via JWT Bypass")</script>' https://ads.tiktok.com/api/submit-ad
```

> Response should confirm storage (e.g., 201 Created). Expected output: Payload echoed back unsanitized.

### Step 3: Confirm Storage

**Context**: Retrieve and verify the injected content.

GET the ad preview endpoint; check for raw script in HTML.

> Success if payload appears in source without encoding.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/inject-xss-payload]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[stored-xss]]
- [[xss]]
