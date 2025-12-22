---
id: proc-uuid-001
tags:
  - ssrf
  - encoding
  - url-crafting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:02.509Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-URL-with-Superscript-Characters

## Summary

This procedure crafts a URL using superscript Unicode characters that, under GBK best-fit mapping on Chinese-localized systems, convert to ASCII digits, enabling hostname confusion for SSRF attacks in curl.

## Description

On systems with Chinese language settings, curl's IDN hostname parsing applies best-fit conversion from Unicode to GBK (cp936). Superscript ¹ (U+00B9) maps to 0xB9 which best-fits to '1' (0x31), and ² (U+00B2) to '2' (0x32). Thus, '¹²7.0.0.1' parses as '127.0.0.1', bypassing validations. This targets applications using curl for requests, allowing redirection to internal hosts.

## Requirements

1. Access to Unicode/GBK mapping tables (e.g., https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit936.txt)
2. System with text editor supporting Unicode
3. Knowledge of target IP (e.g., localhost 127.0.0.1)

## Defense

Defensive measures and detection strategies:

- Disable IDN in curl or use ASCII-only host validation
- Set system locale to non-Chinese encodings
- Monitor for unusual hostname resolutions in logs

## Objectives

1. Create a visually deceptive hostname that resolves to an internal IP
2. Enable SSRF in curl-based apps
3. Demonstrate encoding-based bypass

## Instructions

### Step 1: Reference GBK Best-Fit Table

**Context**: Identify characters that map to digits.

Consult the table to confirm ¹ maps to '1' and ² to '2'.

### Step 2: Construct URL

**Context**: Build the full URL.

Use 'http://¹²7.0.0.1/' as the endpoint.

**Expected Output**: URL string 'http://¹²7.0.0.1/'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[encoding]]
