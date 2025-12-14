---
tags:
  - ssrf
  - code-review
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:53:38.300Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 1625b913-32f2-42e4-9019-ead736041212
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Review-Nextcloud-Source-Code-for-Validation-Flaws

## Summary

This procedure involves analyzing Nextcloud's source code to identify weaknesses in IP validation functions, enabling the development of SSRF bypass payloads.

## Description

In a real-world scenario, review the `ThrowIfLocalIp` function from Nextcloud server code, which uses `filter_var` for IP validation with flags `FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE` and `IpUtils::checkIp` for local ranges (e.g., 100.64.0.0/10, 192.0.0.0/24). This reveals failures to normalize advanced notations like enclosed alphanumerics or octal IPs, allowing SSRF to internal resources. Prerequisites include access to source code via reports or repositories.

## Requirements

1. Access to Nextcloud source code (e.g., from HackerOne report #1608039)
2. Basic PHP knowledge for code analysis
3. Text editor or IDE for reviewing functions

## Defense

Defensive measures and detection strategies:

- Implement code reviews with static analysis tools like PHPStan to detect validation gaps
- Monitor for anomalous internal requests via WAF logs

## Objectives

1. Identify parsing flaws in `filter_var` and `IpUtils`
2. Note bypass opportunities for non-standard IP formats
3. Inform payload crafting for SSRF testing

## Instructions

### Step 1: Locate Relevant Code

**Context**: Focus on IP validation logic to understand filter behaviors.

No specific command; manually review source files for `ThrowIfLocalIp` and `ThrowIfLocalAddress` implementations.

> Expected: Code snippets showing `filter_var($ip, FILTER_VALIDATE_IP, $flags)` and `IpUtils::checkIp($ip, $ranges)`.

### Step 2: Analyze Filter Limitations

**Context**: Test mentally or note how `filter_var` handles octal (e.g., 0177.0.0.1 not normalized to 127.0.0.1) and encoded characters.

No command; document weaknesses like lack of normalization in parse_url.

> Expected: List of vulnerable notations (octal, fullwidth Unicode).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- code-review
