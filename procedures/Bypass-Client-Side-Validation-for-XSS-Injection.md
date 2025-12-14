---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - persistent-xss
  - validation-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:33.613Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Client-Side-Validation-for-XSS-Injection

## Summary

This procedure exploits a lack of server-side sanitization in the SoundCloud link field of Reverb.com product listings by bypassing client-side URL validation through HTTP request tampering, enabling persistent XSS payload injection that executes JavaScript on any viewer of the listing.

## Description

In the Reverb.com sandbox environment, the SoundCloud link field enforces client-side validation to ensure only valid URLs are entered, but the server does not encode or sanitize inputs upon storage. By entering a valid URL initially and then using a tool like Burp Suite to intercept and modify the submission request, an attacker can inject a payload such as `https://soundcloud.com/rich-the-kid/sets/the-world-is-yours-15?fuzzing" onload=alert(document.domain) x="`. When the listing is viewed, the payload renders unsafely, executing JavaScript. This can lead to outcomes like alerting the domain, defacing the store page, denying access to shop owners, or performing actions as the authenticated victim. Prerequisites include authenticated access to a listing edit page and the ability to proxy traffic.

## Requirements

1. Authenticated session on Reverb.com sandbox with a product listing ID
2. Proxy tool like [[tools/Burp-Suite]] configured to intercept browser traffic
3. Direct network access to the edit endpoint (`https://sandbox.reverb.com/listings/[ID]/edit`)

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and sanitization for all URL fields, using libraries like DOMPurify for HTML/JS escaping
- Enable Content Security Policy (CSP) to restrict inline script execution on listing pages
- Monitor for anomalous request patterns, such as tampered parameters in POST requests to listing endpoints, using WAF rules

## Objectives

1. Bypass client-side restrictions to store malicious JavaScript in the database
2. Achieve persistent execution of arbitrary code on victim browsers viewing the listing
3. Demonstrate potential for escalation to account takeover or data exfiltration

## Instructions

### Step 1: Access and Test Direct Injection

**Context**: Identify client-side validation by attempting payload entry directly.

Navigate to `https://sandbox.reverb.com/listings/[YOUR_LISTING_ID]/edit` and enter the payload `https://soundcloud.com/rich-the-kid/sets/the-world-is-yours-15?fuzzing" onload=alert(document.domain) x="` in the SoundCloud link field.

> This triggers a validation error, confirming client-side checks but no server protection.

### Step 2: Input Valid URL

**Context**: Satisfy validation to enable form submission for interception.

Replace with `https://soundcloud.com/rich-the-kid/sets/the-world-is-yours-15` and prepare to submit.

> Form validates successfully, allowing request capture.

### Step 3: Tamper with Request

**Context**: Modify the intercepted POST to inject the payload.

Intercept the save request in [[tools/Burp-Suite]] and change `_product[soundcloud_link_attributes][link]` to the malicious payload. Forward the request.

> Server stores the unsanitized input, completing the injection.

### Step 4: Trigger Execution

**Context**: Render the listing to execute the XSS.

Visit `https://sandbox.reverb.com/item/[LISTING_ID]` to see the alert.

> JavaScript executes, proving persistence and impact.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[persistent-xss]]
- [[validation-bypass]]
