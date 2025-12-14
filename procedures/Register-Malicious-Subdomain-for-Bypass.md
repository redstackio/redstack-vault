---
id: proc-subdomain-bypass-registration
tags:
  - subdomain-bypass
  - dns
  - recon
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
updated_at: '2025-12-14T17:23:50.069Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register-Malicious-Subdomain-for-Bypass

## Summary

This procedure registers a subdomain that mimics Basecamp's internal domains to bypass the Electron app's regex validation for internal URLs, allowing external malicious content to be treated as trusted.

## Description

The Basecamp app uses weak regex patterns like /(launchpad\.(?:dev|test))/ to validate internal domains. By registering a subdomain like launchpad.dev.mydomain.com under a controlled domain, attackers can serve content from an external server while passing the check. This is a key prerequisite for the RCE chain, targeting the image download feature. Prerequisites include domain registration access and DNS control.

## Requirements

1. Access to a domain registrar (e.g., Namecheap, GoDaddy)
2. DNS management capabilities for the domain
3. Knowledge of target regex patterns for validation

## Defense

Defensive measures and detection strategies:

- Strengthen regex to prevent subdomain takeovers (e.g., exact domain matching)
- Implement certificate pinning or HSTS for internal domains
- Monitor for anomalous subdomains mimicking internal ones via DNS logs

## Objectives

1. Create a bypass for internal URL validation
2. Point the subdomain to attacker-controlled infrastructure
3. Enable serving of malicious payloads as 'internal'

## Instructions

### Step 1: Register and Configure Domain

**Context**: Acquire a domain and set up the subdomain to match the regex prefix.

No specific command; use registrar UI to create A record for launchpad.dev.mydomain.com pointing to your server's IP.

> Verify with nslookup launchpad.dev.mydomain.com to confirm resolution.

### Step 2: Test Regex Bypass

**Context**: Manually confirm the subdomain passes the flawed regex.

Use a regex tester or script to validate /(launchpad\.(?:dev|test))/ against launchpad.dev.mydomain.com.

> Expected: Matches the pattern, allowing bypass in the app.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-bypass]]
- [[DNS]]
