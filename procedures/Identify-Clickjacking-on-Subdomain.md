---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - clickjacking
  - headers
  - ui-redressing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:04.849Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Clickjacking-on-Subdomain

## Summary

This procedure detects clickjacking vulnerabilities by checking for the absence of the X-Frame-Options HTTP header on a target subdomain, allowing the site to be embedded in iframes for UI redressing attacks.

## Description

Clickjacking involves tricking users into clicking hidden elements by framing a legitimate site invisibly. On irclogs.wordpress.org, the lack of X-Frame-Options enables this. The procedure uses browser tools to inspect headers and test iframe embedding. Outcomes include confirmation of vulnerability and assessment of impact (low for read-only sites). Requires no special access.

## Requirements

1. Target URL (e.g., https://irclogs.wordpress.org).
2. Modern web browser with dev tools.
3. Basic HTML knowledge for iframe testing.

## Defense

Defensive measures and detection strategies:

- Enforce X-Frame-Options: DENY or SAMEORIGIN in server configs.
- Monitor for unusual iframe embedding attempts via logs.

## Objectives

1. Verify missing X-Frame-Options header.
2. Confirm site can be framed.
3. Assess potential for UI redressing.

## Instructions

### Step 1: Inspect HTTP Headers

**Context**: Check response headers for frame protection.

Navigate to the target in browser, open dev tools (F12), go to Network tab, reload page.

> Look for X-Frame-Options in response headers. Expected output: Absence of the header confirms vulnerability.

### Step 2: Test Iframe Embedding

**Context**: Attempt to load the site in an iframe to validate framming.

Create a simple HTML file: <html><body><iframe src="https://irclogs.wordpress.org" width="100%" height="500"></iframe></body></html> and open it locally.

> Site loads without blocking. Expected output: Full page visible in iframe.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[web-vulnerability]]
