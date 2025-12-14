---
id: p-bypass-url-length-limit
tags:
  - bypass
  - length-limit
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.973Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass URL Path Length Limitation

## Summary

This procedure circumvents the character length restriction in the Glassdoor URL path by modifying the SRCH_KE parameter's numeric value.

## Description

The URL includes a comma-separated value like ,13 indicating length; increasing it to ,50 or higher allows longer payloads. This is a parameter manipulation technique on the web platform, enabling full XSS injection without truncation.

## Requirements

1. Base URL with length limit observed
2. Understanding of URL parameters
3. Browser for modification

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all URL parameters server-side
- Reject unusually high values in search parameters

## Objectives

1. Extend allowable input length
2. Enable full payload delivery
3. Maintain reflection functionality

## Instructions

### Step 1: Modify Parameter Value

**Context**: Edit the numeric value after the comma in SRCH_KE0,13 to a higher number.

Change to:

```url
...SRCH_KE0,50.htm?
```

> Reload the modified URL. Expected output: Longer paths accepted without error or truncation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- [[bypass]]
- [[length-limit]]
