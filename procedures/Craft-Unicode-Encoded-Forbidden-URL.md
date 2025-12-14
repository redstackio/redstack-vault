---
tags:
  - unicode-bypass
  - domain-validation-bypass
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:31.631Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2054fac4-ee25-4ccb-9cfc-1ce8aa12145f
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Unicode-Encoded-Forbidden-URL

## Summary

This procedure substitutes ASCII periods in forbidden domain names with URL-encoded Unicode Ideographic Full Stop (U+3002) to evade Twitter's domain deny list validation, allowing disguised links to unsafe sites.

## Description

Twitter's link validation blocks domains like ddosecrets.com by checking for exact ASCII matches, but fails to normalize Unicode equivalents like U+3002 per RFC 3490. This procedure crafts a modified URL that browsers resolve correctly but validation misses, enabling bypass when combined with redirects. Prerequisites include a blocked domain and a URL encoder.

## Requirements

1. Access to a URL encoder (browser dev tools or online tool)
2. Knowledge of the target forbidden domain
3. Twitter account for testing

## Defense

Defensive measures and detection strategies:

- Implement Punycode normalization and Unicode equivalence checks in domain validation (e.g., treat U+3002 as .)
- Scan for URL-encoded Unicode in posted links using regex patterns like %E3%80%82
- Monitor redirect chains in logs for analytics.twitter.com and twitter.com/login parameters

## Objectives

1. Create a disguised domain that evades deny list
2. Prepare URL for embedding in open redirects
3. Ensure browser resolution to original forbidden site

## Instructions

### Step 1: Select Forbidden Domain

**Context**: Choose a domain blocked by Twitter, such as ddosecrets.com.

No command required; manually note the URL.

> Expected: Base URL identified.

### Step 2: Substitute Periods with Unicode

**Context**: Replace each '.' with Ideographic Full Stop U+3002, then URL-encode it as %E3%80%82.

Manually edit: https://ddosecrets.com becomes https://ddosecrets%E3%80%82com

> This disguises the domain; browsers like Chrome resolve U+3002 as . in IDsN.

### Step 3: Single URL Encode

**Context**: Encode the modified URL for parameter use.

Use browser URL encoder or dev tools to encode: https://ddosecrets%E3%80%82com → https%3A%2F%2Fddosecrets%25E3%2580%2582com

> Expected: Encoded string without decoding errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[unicode-bypass]]
- [[domain-validation-bypass]]
