---
tags:
  - ssrf
  - protocol-testing
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: e842c9ba-9bd1-4891-b8c3-fa8f1b2e9dfa
created_at: '2025-12-14T03:46:14.362Z'
updated_at: '2025-12-14T03:46:14.362Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Test Supported Protocols in SVG xlink:href

## Summary

Iteratively tests URI schemes in the SVG to determine which protocols the parser supports for external fetches, revealing HTTP and FTP as viable for SSRF.

## Description

The SVG parser only processes certain schemes; testing against W3C list shows limitations, scoping SSRF to HTTP/FTP and excluding others like file:// or gopher://.

## Requirements

1. List of URI schemes (e.g., from W3C documentation)
2. Modified SVG payloads for each protocol
3. Attacker server to log protocol-specific requests

## Defense

Defensive measures and detection strategies:

- Configure parser to deny all external schemes
- Whitelist only internal resources
- Log protocol usage in image processing

## Objectives

1. Identify fetchable protocols
2. Limit SSRF scope
3. Optimize payloads

## Instructions

### Step 1: Modify SVG for Protocol

**Context**: Change the href to test scheme.

Edit SVG: <image xlink:href="ftp://attacker-server/test" />

> Repeat for http://, https://, file://, etc.

### Step 2: Upload and Observe

**Context**: Submit each variant and check logs.

Upload as in prior procedure; only http:// and ftp:// trigger logs.

> Others fail silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[protocol]]
