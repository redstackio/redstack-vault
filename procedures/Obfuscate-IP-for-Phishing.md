---
id: proc-obfuscate-ip-phishing-uber
tags:
  - phishing
  - ip-obfuscation
  - uber
type: procedure
tools:
  - '[[tools/IP-Address-Converter]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-obfuscated-ip-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:26.908Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Obfuscate-IP-for-Phishing

## Summary

This procedure converts an IP address to decimal form for obfuscation, then uses it in the Uber open redirect to create hard-to-detect phishing links that redirect to malicious sites while appearing legitimate.

## Description

To evade basic filters, convert IPs like 216.58.217.206 (Google) to 3627735502 using an online tool, then embed in http://uber.com//3627735502/calendar. This enhances phishing by hiding the true destination. Targets web users; requires no auth, but tool access needed.

## Requirements

1. Access to IP converter tool
2. Target IP for the malicious site
3. Browser/curl for link testing

## Defense

Defensive measures and detection strategies:

- Decode and validate numeric IPs in URLs at the application layer
- Implement referrer checks and CSP to block unexpected redirects
- Train users on suspicious Uber links and monitor click patterns

## Objectives

1. Obfuscate redirect targets to bypass detection
2. Craft realistic phishing URLs
3. Increase success rate of user deception

## Instructions

### Step 1: Convert IP to Decimal

**Context**: Use the tool to transform dotted IP to a single number.

No command; visit [[tools/IP-Address-Converter]] and input 216.58.217.206 to get 3627735502.

> Output: Decimal value for obfuscation.

### Step 2: Test Obfuscated Redirect

**Context**: Embed decimal in URL and verify redirection.

**Command** ([[commands/curl-obfuscated-ip-redirect]]):
```bash
curl -L -I "http://uber.com//3627735502/calendar"
```

> Redirects to Google Calendar, masking the IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques


## Commands Used

- [[commands/curl-obfuscated-ip-redirect]]

## Tools Used

- [[tools/IP-Address-Converter]]

## Tags

- phishing
- ip-obfuscation
