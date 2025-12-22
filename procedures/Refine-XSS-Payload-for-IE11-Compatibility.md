---
tags:
  - xss
  - ie11
  - bypass
  - payload-refinement
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 6fcbaa26-d7f9-4e26-a6dc-67f0edce9549
created_at: '2025-12-14T03:47:13.094Z'
updated_at: '2025-12-14T03:47:13.094Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Refine-XSS-Payload-for-IE11-Compatibility

## Summary

This procedure refines the XSS payload for Internet Explorer 11 by incorporating null bytes and a hash-based JavaScript URI to bypass the browser's built-in XSS filter, exploiting IE's lenient handling of unencoded query parameters.

## Description

IE11 does not strictly URL-encode query parameters in certain contexts, allowing payloads with special characters like '/' and null bytes (%00) to evade filters. The refined payload '</script><script/%00%00v%00%00>document.location.href=location.hash.slice(1)</script>#javascript:alert(1)' closes the tag, uses null bytes to break parsing, and executes via the hash fragment. This targets legacy browser support in environments where users might still use IE11, enhancing the attack's reach for client-side exploitation in ad-serving scenarios.

## Requirements

1. Knowledge of IE11's XSS filter behaviors and URL parsing quirks
2. Access to an IE11 instance for testing (virtualized if needed)
3. Base payload from prior steps

## Defense

Defensive measures and detection strategies:

- Encourage browser upgrades and disable legacy support like IE11
- Implement strict CSP with 'unsafe-inline' blocked and nonce usage
- Scan for payloads with %00 or hash-based JS URIs in traffic analysis

## Objectives

1. Evade IE11's XSS protections using null bytes and hash execution
2. Ensure cross-browser compatibility for the exploit
3. Prepare a deployable URL for victim targeting

## Instructions

### Step 1: Incorporate Null Bytes and Tag Breakage

**Context**: Modify the script tag opening to include %00%00 for parsing disruption in IE.

Manually edit: <script/%00%00v%00%00> to confuse the filter while preserving functionality.

> Expected: Payload that renders as a valid script tag in IE11.

### Step 2: Add Hash-Based Execution

**Context**: Append #javascript:alert(1) to trigger via document.location.href=location.hash.slice(1).

Construct full URL: https://revive-instance/www/delivery/afr.php?refresh=10000&</script><script/%00%00v%00%00>document.location.href=location.hash.slice(1)</script>#javascript:alert(1)

> Expected: URL that, when loaded, executes the JS from the hash without direct injection detection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ie11]]
- [[bypass]]
