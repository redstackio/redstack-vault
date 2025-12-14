---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - waf-bypass
  - ascii-bypass
  - url-encoding
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:49.591Z'
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
# Bypass-WAF-with-Double-Encoded-Non-Standard-ASCII-in-URL

## Summary

This procedure exploits a WAF misconfiguration by inserting non-standard ASCII hex values (%80-%FF) between double-encoded characters in a URL, bypassing filters that only sanitize %00-%7F ranges and allowing a reflected XSS payload to reach 404 error pages on Starbucks domains.

## Description

The attack targets web application firewalls (WAFs) that inadequately handle high-range hex-encoded characters. By double-encoding quotes (%2522) and spaces (%2520), and inserting %80 (or similar %80-%FF values, excluding exceptions like %81, %8d, %8f, %90, %9d that cause Bad Request errors), the payload evades normalization and filtering. This re-enables reflected XSS on paths like /testing, impacting multiple critical domains by allowing JS execution for theft or manipulation. Prerequisites include browser access and knowledge of the target's URL structure from prior reports like 629745.

## Requirements

1. Browser like Firefox 69.0.3 for URL navigation.
2. Knowledge of target's 404-handling paths (e.g., /testing).
3. No special network access; public web targets.

## Defense

Defensive measures and detection strategies:

- Expand WAF rules to decode and block all %80-%FF ranges in URLs.
- Implement comprehensive URL normalization for all ASCII hex values.
- Monitor 404 pages for anomalous reflected parameters and JS attributes.

## Objectives

1. Bypass WAF to inject unfiltered payload into response.
2. Trigger reflection on error pages for XSS setup.
3. Enable subsequent JS execution against victims.

## Instructions

### Step 1: Craft the Malicious URL

**Context**: Construct the URL by double-encoding quotes and spaces, then inserting a non-standard ASCII hex like %80 to break WAF parsing without causing errors.

No specific command; manually build the URL in the browser address bar or via a script.

Example URL:

```url
https://www.starbucks.com.br/testing%2522%80%2520accesskey='x'%2520onclick='confirm%601%60
```

> This URL uses %2522 for double-encoded ", %80 as the bypass char, and embeds accesskey='x' onclick='confirm(1)' for XSS. Low hex (%00-%7F) would be blocked, but %80-%FF slips through.

### Step 2: Navigate to the URL

**Context**: Visit the crafted URL to invoke the 404 page and reflect the payload.

Use the browser's navigation:

```bash
# In Firefox, directly enter or bookmark the URL
```

> Browser loads the 404, reflecting the payload if bypass succeeds. Inspect page source to confirm unfiltered attributes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[waf-bypass]]
- [[xss]]
- [[web]]
