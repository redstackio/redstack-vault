---
tags:
  - waf-bypass
  - xss
  - fuzzing
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-bypass-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.120Z'
sub_techniques: []
id: 8b0cb512-88eb-4e82-b68f-18fb12bce839
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass WAF for Reflected XSS

## Summary

This procedure fuzzes XSS payloads to evade the WAF, enabling JavaScript execution via the reflected 'url' parameter in the MongoDB error message.

## Description

After standard payloads are blocked, use variations like HTML object tags with javascript: URIs. The payload <object data=javascript:confirm(document.domain)> bypasses by mimicking non-script content, allowing execution when reflected and rendered in the browser.

## Requirements

1. WAF blocking confirmed
2. Fuzzing capability or manual payload testing
3. Browser for final execution verification

## Defense

Defensive measures and detection strategies:

- Update WAF signatures for obfuscated XSS (e.g., object tags)
- Content Security Policy (CSP) to restrict javascript: URIs
- Rate-limit API error endpoints

## Objectives

1. Evade WAF with crafted payload
2. Achieve JavaScript execution in browser context
3. Demonstrate impact (e.g., domain confirmation)

## Instructions

### Step 1: Craft and Send Bypass Payload

**Context**: Insert the evasive payload into the 'url' parameter.

**Command** ([[commands/curl-bypass-xss]]):
```bash
curl -X GET "https://api.semrush.com/reports/v1/projects/YOUR_PROJECT_ID/siteaudit/page/list?url=<object data=javascript:confirm(document.domain)>" -H "Authorization: Bearer YOUR_API_TOKEN"
```

> The response reflects the payload; when viewed in a browser (e.g., via proxy), it executes the confirm dialog.

### Step 2: Verify Execution

**Context**: Load the reflected response in a browser to trigger JS.

No command; use browser or HTML viewer.

> Success if confirm() pops up showing the domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/curl-bypass-xss]]

## Tools Used


## Tags

- [[waf-bypass]]
- [[xss]]
- [[fuzzing]]
