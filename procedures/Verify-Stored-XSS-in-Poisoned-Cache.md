---
tags:
  - xss
  - stored-xss
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-access-poisoned-page]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c8487bcf-9f64-4712-b666-f0a23c5cc437
created_at: '2025-12-13T09:00:33.954Z'
updated_at: '2025-12-13T09:00:33.954Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify Stored XSS in Poisoned Cache

## Summary

This procedure verifies the successful execution of stored XSS from a poisoned web cache by accessing the affected page and checking for payload delivery.

## Description

After poisoning the cache, this step simulates user access to confirm that the injected XSS payload is served and would execute in a browser context. It targets the okmedia.insideok.ru endpoint and assesses the persistence of the attack, potentially leading to arbitrary script execution for data theft or hijacking.

## Requirements

1. Previously poisoned cache
2. Access to the target URL
3. Browser or tool to inspect responses

## Defense

Defensive measures and detection strategies:

- Enable Content Security Policy (CSP) to block unauthorized scripts
- Monitor for XSS patterns in cached responses and user reports of alerts

## Objectives

1. Confirm payload delivery from cache
2. Validate persistent XSS execution
3. Evaluate overall attack impact

## Instructions

### Step 1: Access the Poisoned Page

**Context**: Send a request to the poisoned endpoint to retrieve the cached response.

**Command** ([[commands/curl-access-poisoned-page]]):
```bash
curl https://okmedia.insideok.ru/
```

> This fetches the page; inspect for the injected script tag.

### Step 2: Check for XSS Payload Execution

**Context**: Grep the response for the XSS payload to confirm it's present.

**Command** ([[commands/curl-access-poisoned-page]]):
```bash
curl https://okmedia.insideok.ru/ | grep "<script>alert('XSS')</script>"
```

> If the payload is found, it indicates successful stored XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/curl-access-poisoned-page]]

## Tools Used

- [[tools/curl]]

## Tags

- xss
- stored-xss
