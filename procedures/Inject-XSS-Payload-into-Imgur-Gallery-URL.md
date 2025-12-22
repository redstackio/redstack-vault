---
tags:
  - xss
  - reflected-xss
  - url-injection
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.552Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: a49312b7-d100-4ce1-84ee-0d0ec562ee86
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Imgur-Gallery-URL

## Summary

This procedure constructs a malicious URL by injecting a reflected XSS payload into the gallery ID parameter of Imgur's mobile site (m.imgur.com), exploiting insufficient sanitization to enable JavaScript execution when accessed by a victim.

## Description

The attack targets the /gallery/ endpoint on m.imgur.com, where the gallery ID parameter is reflected without proper escaping, allowing HTML/JS injection. The payload closes an existing HTML attribute (e.g., via ") and injects an <img> tag with an onerror handler that executes JS on load. This is effective only on mobile devices due to rendering differences. Prerequisites include understanding URL encoding and basic web app testing; no special access is needed beyond crafting the URL for social engineering delivery.

## Requirements

1. Knowledge of URL encoding (e.g., %22 for ")
2. Base URL: http://m.imgur.com/gallery/
3. A valid gallery ID prefix (e.g., 'iT5l7') to mask the payload
4. Mobile device for testing (desktop may not trigger)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding) for URL parameters
- Use Content Security Policy (CSP) to restrict inline JS and img src
- Monitor for anomalous URLs in access logs and block suspicious patterns
- Employ Web Application Firewall (WAF) rules to detect common XSS payloads

## Objectives

1. Craft a functional malicious URL that evades basic filters
2. Prepare for delivery to victims via links or phishing
3. Demonstrate potential for JS-based attacks like cookie theft

## Instructions

### Step 1: Select and Encode Payload

**Context**: Choose a simple XSS payload that breaks out of the context and executes JS, then URL-encode it to ensure safe transmission.

Payload: ">%3Cimg src=x onerror=alert(1)%3E (decoded: "><img src=x onerror=alert(1)>")

Encoded: %22%3E%3Cimg%20src=x%20onerror=alert(1)%3E

### Step 2: Append to Base URL

**Context**: Combine the base gallery URL with a legitimate-looking ID followed by the encoded payload to form the attack URL.

Construct:

```url
http://m.imgur.com/gallery/iT5l7%22%3E%3Cimg%20src=x%20onerror=alert(1)%3E
```

> This URL appears as a normal gallery link but injects the payload into the reflected parameter.

**Expected Output**: A shareable URL ready for testing or distribution.

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
- [[reflected-xss]]
- [[web]]
- [[JavaScript]]
