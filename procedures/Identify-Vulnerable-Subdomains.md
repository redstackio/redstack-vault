---
tags:
  - web-cache-deception
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-cache-behavior]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 053fa744-fc43-4646-99d2-c634ee127793
created_at: '2025-12-13T09:00:34.053Z'
updated_at: '2025-12-13T09:00:34.053Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable Subdomains

## Summary

This procedure involves scanning and testing subdomains of a target like kaspersky.com to identify those vulnerable to Web Cache Deception, where improper caching allows sensitive pages to be stored and retrieved by unauthorized users.

## Description

Web Cache Deception exploits misconfigured caching rules, enabling attackers to force the cache to store sensitive pages by appending cacheable extensions (e.g., .css). This is tested by analyzing HTTP headers and response behaviors on multiple subdomains. The target environment is web-based, with expected outcomes including a list of exploitable subdomains.

## Requirements

1. Access to the target's domain (e.g., kaspersky.com)
2. Command-line tools like curl for testing
3. Basic knowledge of HTTP caching headers

## Defense

Defensive measures and detection strategies:

- Implement strict cache-control headers (e.g., no-cache for sensitive pages)
- Monitor for unusual URL patterns with cacheable extensions in logs

## Objectives

1. Discover subdomains with caching misconfigurations
2. Confirm exploitability for Web Cache Deception
3. Prepare for phishing exploitation

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Gather a list of subdomains to test.

Use public sources or tools to list subdomains.

> Expected: List of potential targets.

### Step 2: Test Caching Behavior

**Context**: Check if sensitive pages can be cached improperly.

**Command** ([[commands/curl-test-cache-behavior]]):
```bash
curl -I https://subdomain.kaspersky.com/sensitive-page.css
```

> Examine Cache-Control headers; if cacheable, it's vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-test-cache-behavior]]

## Tools Used



## Tags

- web-cache-deception
- reconnaissance
