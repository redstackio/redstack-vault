---
tags:
  - web-analysis
  - parameter-discovery
  - json
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
  - '[[tools/Mozilla-Firefox]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-13T23:52:25.422Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b36998f9-a206-4602-99ce-e69c4e185ce3
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Analyze Page and Identify Vulnerable Parameter

## Summary

This procedure details inspecting a web page's URL parameters and structure to identify points for injection, specifically decoding Base64-encoded JSON to find unsanitized fields like 'promo_code'.

## Description

Load the target page in a browser and examine the query string. Decode the 'q' parameter to reveal JSON data used for rendering personalized content. The 'promo_code' field, meant for referral links, lacks validation, allowing javascript: schemes to be processed in a dangerous context, such as hyperlinks or clipboard operations.

## Requirements

1. Modern web browser for inspection
2. Ability to decode Base64 (built-in browser dev tools or online tools)
3. Basic JSON parsing knowledge

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all decoded inputs, rejecting javascript: URLs
- Use Content Security Policy (CSP) to block inline scripts
- Log and monitor unusual parameter values

## Objectives

1. Map the data flow from URL to page rendering
2. Pinpoint injectable fields
3. Assess lack of sanitization

## Instructions

### Step 1: Load and Inspect Page

**Context**: Visit the URL and use dev tools to examine parameters.

Open https://growth.grab.com/valentine/active/my.html?q=<sample_base64> in [[tools/Google-Chrome]] or [[tools/Mozilla-Firefox]].

> Use Network tab to capture requests and decode 'q' parameter.

### Step 2: Decode and Analyze JSON

**Context**: Extract and parse the Base64 content.

Copy the 'q' value, decode it (e.g., via browser console: atob('encoded_string')), and review keys like 'promo_code'.

> Expected: JSON with 'promo_code' as a string field for URLs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Steal Application Access Token]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]
- [[tools/Mozilla-Firefox]]

## Tags

- [[web-analysis]]
- [[parameter-discovery]]
