---
tags:
  - unicode-phishing
  - url-crafting
  - spoofing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - iOS
  - WebView
techniques:
  - '[[Phishing]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 265d0485-1f71-4896-bdbe-d95358211270
created_at: '2025-12-14T17:24:44.881Z'
updated_at: '2025-12-14T17:24:44.881Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Craft-Malicious-Unicode-URL-for-Spoofing

## Summary

This procedure involves creating a URL with malicious Unicode characters in the domain name to exploit improper normalization in the LINE iOS app's WebView, setting the stage for address bar spoofing during navigation or redirects.

## Description

In the context of the LINE iOS client vulnerability (HackerOne #1082991), attackers craft URLs using Unicode characters that resemble legitimate domains but cause the app to normalize them deceptively. When processed via HTTP redirects or invalid hostname navigation, this leads to the address bar displaying a trusted domain while preparing to load phishing content. Prerequisites include knowledge of Unicode homoglyphs and access to an attacker-controlled server for hosting the phishing page. Expected outcome: A URL that initiates the spoofing chain without immediate detection.

## Requirements

1. iOS device with vulnerable LINE app
2. Attacker server to host phishing content
3. Basic understanding of URL encoding and Unicode (e.g., IDNA normalization flaws)

## Defense

Defensive measures and detection strategies:

- Implement strict URL normalization and validation in WebViews to reject invalid Unicode domains
- Use secure browser engines with timely address bar updates synced to navigation completion
- Educate users on verifying domains beyond visual appearance (e.g., via certificate checks)

## Objectives

1. Generate a deceptive URL that bypasses client-side checks
2. Prepare for redirect chaining to malicious content
3. Deceive the app's UI rendering

## Instructions

### Step 1: Identify Target Domain Homoglyphs

**Context**: Select Unicode characters that visually mimic a legitimate domain like "line.me" to create confusion.

No specific command; manually construct using tools like online Unicode encoders.

> Example: Replace 'l' with U+0263 (small letter l with stroke) in the domain.

### Step 2: Assemble the Malicious URL

**Context**: Build the full URL with the Unicode domain pointing to an invalid or redirecting hostname.

No command; example URL structure: `http://xn--[punycode-of-unicode-domain].attacker.com/phishing`

> This triggers normalization issues in the LINE WebView, where the app decodes and displays the spoofed name.

### Step 3: Test URL in Controlled Environment

**Context**: Verify the URL causes navigation issues without full load.

Distribute via LINE chat and observe WebView behavior.

> Expected: Partial navigation with domain spoofing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[unicode-phishing]]
- [[url-spoofing]]
