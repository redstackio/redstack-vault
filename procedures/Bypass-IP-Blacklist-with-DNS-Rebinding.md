---
tags:
  - ssrf-bypass
  - dns-rebinding
  - http-redirect
type: procedure
tools:
  - '[[tools/dnschef]]'
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
updated_at: '2025-12-14T04:39:02.333Z'
sub_techniques: []
id: e43e5af3-e303-4eb3-bca6-8cc17485217a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-IP-Blacklist-with-DNS-Rebinding

## Summary

This procedure demonstrates bypassing IP blacklisting mitigations (e.g., Phabricator patch D12136) using DNS rebinding or HTTP redirects to access forbidden internal URLs like cloud metadata.

## Description

The proposed patch blacklists private IPs before requests, but DNS rebinding allows resolution to change mid-process by serving different records on subsequent queries. HTTP redirects (302) can also chain to internal targets after initial validation. This elevates the SSRF risk beyond simple blacklisting.

## Requirements

1. Patched application with IP blacklist
2. Control over DNS for the target domain
3. Tool like dnschef for dynamic resolution

## Defense

Defensive measures and detection strategies:

- Validate final destination after redirects and DNS resolution
- Use fixed DNS resolvers or hosts file overrides
- Implement request signing or hop limits

## Objectives

1. Evade IP-based SSRF filters
2. Maintain access to internal services
3. Demonstrate mitigation inadequacy

## Instructions

### Step 1: Setup DNS Rebinding

**Context**: Configure a DNS proxy to alter records dynamically.

Use [[tools/dnschef]] patched version to serve initial public IP, then switch to 169.254.169.254.

> Run dnschef to intercept and rebind queries during the request.

### Step 2: Trigger Redirect Bypass

**Context**: Use a URL that redirects to private IP post-validation.

Input a redirecting URL (e.g., http://attacker.com/redirect-to-metadata) in SSRF.

> Server follows 302 to internal target after checking the initial allowed URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/dnschef]]

## Tags

- bypass
- rebinding
- redirect
